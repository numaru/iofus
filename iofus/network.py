import importlib
import inspect

from iofus.binaryio import ByteArray


class MessageBuilder:
    MESSAGE_SIZE_ASYNC_THRESHOLD = 300 * 1024

    def __init__(self):
        self.raw_parser = MessageReceiver()
        self._static_header = 0
        self._splitted_packet_length = 0
        self._splitted_packet_id = 0
        self._splitted_packet = False
        self._input = ByteArray()
        self._input_buffer = ByteArray()

    def receive(self, data):
        messages = []
        buffer = ByteArray(data)
        while buffer.bytes_available > 0:
            message = self._low_receive(buffer)
            if message:
                messages.append(message)
        return messages

    def send(self, socket, message):
        byte_array = ByteArray()
        message.pack(byte_array)
        socket.sendall(byte_array.getvalue())

    def _get_message_id(self, header):
        return header >> 2

    def _read_message_length(self, header, reader):
        length_bytes_count = header & 0x03
        length = 0
        if length_bytes_count == 1:
            length = reader.read_unsigned_byte()
        if length_bytes_count == 2:
            length = reader.read_unsigned_short()
        if length_bytes_count == 3:
            length = ((reader.read_byte() & 0xFF) << 16) + \
                     ((reader.read_byte() & 0xFF) << 8) + \
                     (reader.read_byte() & 0xFF)
        return length

    def _get_unpack_mode(self, protocol_id, size):
        if size == 0:
            return 1
        mode = self.raw_parser.get_unpack_mode(protocol_id)
        if mode != 1:
            return mode
        if size > self.MESSAGE_SIZE_ASYNC_THRESHOLD:
            mode = 3
        else:
            mode = 1
        return mode

    def _compute_message(self, message, functree):
        if not functree.go_down():
            message.unpacked = True
            return
        self._async_messages.push(message)
        self._async_trees.push(functree)

    def _low_receive(self, reader):
        _loc3_ = 0
        _loc4_ = 0
        _loc5_ = 0
        if not self._splitted_packet:
            if reader.bytes_available < 2:
                return None
            _loc3_ = reader.read_unsigned_short()
            _loc4_ = self._get_message_id(_loc3_)
            if reader.bytes_available >= (_loc3_ & 0x03):
                _loc5_ = self._read_message_length(_loc3_, reader)
                if reader.bytes_available >= _loc5_:
                    if self._get_unpack_mode(_loc4_, _loc5_) == 3:
                        reader.read_bytes(self._input, len(self._input), _loc5_)
                        _loc2_ = self.raw_parser.parse_async(self._input, _loc4_,
                                                             _loc5_, self._compute_message)
                    else:
                        _loc2_ = self.raw_parser.parse(reader, _loc4_, _loc5_)
                    return _loc2_
                self._static_header = -1
                self._splitted_packet_length = _loc5_
                self._splitted_packet_id = _loc4_
                self._splitted_packet = True
                reader.read_bytes(self._input_buffer, 0, reader.bytes_available)
                return None
            self._static_header = _loc3_
            self._splitted_packet_length = _loc5_
            self._splitted_packet_id = _loc4_
            self._splitted_packet = True
            return None
        if self._static_header != -1:
            self._splitted_packet_length = self._read_message_length(self._static_header, reader)
            self._static_header = -1
        if reader.bytes_available + len(self._input_buffer) >= self._splitted_packet_length:
            reader.read_bytes(self._input_buffer, len(self._input_buffer),
                              self._splitted_packet_length - len(self._input_buffer))
            self._input_buffer.seek(0)
            if self._get_unpack_mode(self._splitted_packet_id, self._splitted_packet_length) == 3:
                _loc2_ = self.raw_parser.parse_async(self._input_buffer,
                                                     self._splitted_packet_id,
                                                     self._splitted_packet_length,
                                                     self._compute_message)
            else:
                _loc2_ = self.raw_parser.parse(self._input_buffer, self._splitted_packet_id,
                                               self._splitted_packet_length)
            self._splitted_packet = False
            self._input_buffer = ByteArray()
            return _loc2_
        reader.read_bytes(self._input_buffer, len(self._input_buffer), reader.bytes_available)
        return None

class MessageReceiver:
    MESSAGES_TYPES = {}
    UNPACK_MODES = {}

    def __init__(self):
        if not self.MESSAGES_TYPES:
            self.__classinit__()

    @classmethod
    def __classinit__(cls):
        module = importlib.import_module("iofus.dmessages")
        def predicate(c):
            return inspect.isclass(c) and c.__module__ == "iofus.dmessages"
        for name, obj in inspect.getmembers(module, predicate):
            cls.MESSAGES_TYPES[obj.protocolId] = obj
        cls.UNPACK_MODES[5743] = 3

    def parse(self, reader, protocol_id, param3):
        message_type = self.MESSAGES_TYPES.get(protocol_id)
        if not message_type:
            return None
        message = message_type()
        message.unpack(reader, param3)
        message.unpacked = True
        return message

    def parse_async(self, reader, protocol_id, param3, function):
        message_type = self.MESSAGES_TYPES.get(protocol_id)
        if not message_type:
            return None
        message = message_type()
        message.unpacked = False
        function(message, message.unpackAsync(reader, param3))
        return message

    def get_unpack_mode(self, protocol_id):
        return self.UNPACK_MODES.get(protocol_id, 1)

class ProtocolTypeManager:
    __TYPES_TYPE = {}

    @classmethod
    def __classinit__(cls):
        module = importlib.import_module("iofus.dtypes")
        def predicate(c):
            return inspect.isclass(c) and c.__module__ == "iofus.dtypes"
        for name, obj in inspect.getmembers(module, predicate):
            cls.__TYPES_TYPE[obj.protocolId] = obj

    @classmethod
    def get_instance(cls, class_type, protocol_id):
        if not cls.__TYPES_TYPE:
            cls.__classinit__()
        _loc3_ = cls.__TYPES_TYPE.get(protocol_id, None)
        if not _loc3_:
            raise RuntimeError("Type with id " + str(protocol_id) + " is unknown.")
        _loc4_ = _loc3_()
        if not isinstance(_loc4_, class_type):
            raise RuntimeError("Type " + str(protocol_id) + " is not a " + str(class_type) + ".")
        return _loc4_

class NetworkMessage:
    protocolId = 0

    def __init__(self):
        self.unpacked = False

    def serialize(self, writer):
        raise NotImplementedError()

    def deserialize(self, reader):
        raise NotImplementedError()

    def unpack(self, reader):
        self.deserialize(reader)

    def pack(self, writer):
        self.serialize(writer)
        self.write_packet(writer)

    def write_packet(self, writer, protocol_id, byte_array):
        position = writer.tell()
        packet_length = len(byte_array)
        type_length = self.compute_type_length(packet_length)
        header = self.compute_static_header(type_length)
        writer.write_short(header)
        if type_length == 1:
            writer.write_byte(packet_length)
        elif type_length == 2:
            writer.write_short(packet_length)
        elif type_length == 3:
            writer.write_byte(packet_length >> 16 & 255)
            writer.write_short(packet_length & 65535)
        writer.write_bytes(byte_array)
        writer.seek(position)

    def compute_type_length(self, length):
        if length > 65535:
            return 3
        elif length > 255:
            return 2
        elif length > 0:
            return 1
        else:
            return 0

    def compute_static_header(self, type_length):
        return self.protocolId << 2 | type_length

    def __repr__(self):
        arguments = {key: value for key, value in self.__dict__.items() if key[0] != "_"}
        del arguments["unpacked"]
        return "<{0}: {1}>".format(type(self).__name__, arguments)
