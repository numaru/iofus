import ctypes
import io
import struct


def _lrshift8(value, n):
    return (value % 0x0100) >> n

def _lrshift32(value, n):
    return (value % 0x0100000000) >> n

class ByteArray(io.BytesIO):

    def __len__(self):
        return len(self.getvalue())

    @property
    def bytes_available(self):
        position_a = self.tell()
        self.seek(0, 2)
        position_b = self.tell()
        self.seek(position_a)
        return position_b - position_a

    def read_boolean(self):
        self._unpack("?")

    def read_byte(self):
        return self._unpack("b")

    def read_bytes(self, byte_array, offset=0, length=1):
        buffer = self._unpack(str(length) + "s", length)
        byte_array.seek(offset)
        byte_array.write(buffer)

    def read_double(self):
        return self._unpack("d", 8)

    def read_float(self):
        return self._unpack("f", 4)

    def read_int(self):
        return self._unpack("i", 4)

    def read_short(self):
        return self._unpack("h", 2)

    def read_unsigned_byte(self):
        return self._unpack("B")

    def read_unsigned_int(self):
        return self._unpack("I", 4)

    def read_unsigned_short(self):
        return self._unpack("H", 2)

    def read_utf(self):
        length = self.read_unsigned_short()
        raw = self._unpack(str(length) + "s", length)
        return raw.decode("utf8")

    def read_var_int(self):
        ret = 0
        size = 0
        while size < 32:
            byte = self.read_byte()
            has_next = (byte & 0x80) == 0x80
            if size > 0:
                ret = ret + ((byte & 0x7F) << size)
            else:
                ret = ret + (byte & 0x7F)
            size = size + 7
            if not has_next:
                return ctypes.c_int32(ret).value
        raise RuntimeError("Too much data")

    def read_var_uh_int(self):
        return ctypes.c_uint32(self.read_var_int()).value

    def read_var_short(self):
        ret = 0
        size = 0
        while size < 16:
            byte = self.read_byte()
            has_next = (byte & 0x80) == 0x80
            if size > 0:
                ret = ret + ((byte & 0x7F) << size)
            else:
                ret = ret + (byte & 0x7F)
            size = size + 7
            if not has_next:
                if ret > 32767:
                    ret = ret - 65536
                return ctypes.c_int16(ret).value
        raise RuntimeError("Too much data")

    def read_var_uh_short(self):
        return ctypes.c_uint16(self.read_var_short()).value

    def read_var_long(self):
        return ctypes.c_int64(self.read_var_uh_long()).value

    def read_var_uh_long(self):
        _loc3_ = 0
        _loc2_low = 0
        _loc2_high = 0
        _loc4_ = 0
        while True:
            _loc3_ = self.read_unsigned_byte()
            if _loc4_ == 28:
                break
            if _loc3_ >= 128:
                _loc2_low = _loc2_low | (_loc3_ & 127) << _loc4_
                _loc4_ = _loc4_ + 7
                continue
            _loc2_low = _loc2_low | _loc3_ << _loc4_
            return ctypes.c_uint64(_loc2_high * 4294967296 + _loc2_low).value
        if _loc3_ >= 128:
            _loc3_ = _loc3_ & 127
            _loc2_low = _loc2_low | _loc3_ << _loc4_
            _loc2_high = _lrshift32(_loc3_, 4)
            _loc4_ = 3
            while True:
                _loc3_ = self.read_unsigned_byte()
                if _loc4_ < 32:
                    if _loc3_ >= 128:
                        _loc2_high = _loc2_high | (_loc3_ & 127) << _loc4_
                    else:
                        break
                _loc4_ = _loc4_ + 7
            _loc2_high = _loc2_high | (_loc3_ << _loc4_)
            return ctypes.c_uint64(_loc2_high * 4294967296 + _loc2_low).value
        _loc2_low = _loc2_low | (_loc3_ << _loc4_)
        _loc2_high = _lrshift32(_loc3_, 4)
        return ctypes.c_uint64(_loc2_high * 4294967296 + _loc2_low).value

    def write_boolean(self, value):
        self._pack("?", value)

    def write_byte(self, value):
        self._pack("b", value)

    def write_bytes(self, byte_array, offset=0, length=0):
        byte_array.seek(offset)
        buffer = byte_array.read(-1 if length == 0 else length)
        self.write(buffer)

    def write_double(self, value):
        self._pack("d", value)

    def write_float(self, value):
        self._pack("f", value)

    def write_int(self, value):
        self._pack("i", value)

    def write_short(self, value):
        self._pack("h", value)

    def write_unsigned_byte(self, value):
        self._pack("B", value)

    def write_unsigned_int(self, value):
        self._pack("I", value)

    def write_unsigned_short(self, value):
        self._pack("H", value)

    def write_utf(self, string):
        raw = string.encode("utf8")
        length = len(raw)
        self.write_unsigned_short(length)
        self._pack(str(length) + "s", raw)

    def write_var_int(self, value):
        byte = 0
        out = ByteArray()
        if value >= 0 and value <= 0x7F:
            out.write_byte(value)
            self.write_bytes(out)
            return
        remaining = value
        buffer_array = ByteArray()
        while remaining != 0:
            buffer_array.write_byte(remaining & 0x7F)
            buffer_array.seek(len(buffer_array) - 1)
            byte = buffer_array.read_byte()
            remaining = _lrshift32(remaining, 7)
            if remaining > 0:
                byte = ctypes.c_int8(byte | 0x80).value
            out.write_byte(byte)
        self.write_bytes(out)

    def write_var_short(self, value):
        byte = 0
        if value > 32767 or value < -32768:
            raise RuntimeError("Forbidden value")
        out = ByteArray()
        if value >= 0 and value <= 0x7F:
            out.write_byte(value)
            self.write_bytes(out)
            return
        remaining = value & 65535
        buffer_array = ByteArray()
        while remaining != 0:
            buffer_array.write_byte(remaining & 0x7F)
            buffer_array.seek(len(buffer_array) - 1)
            byte = buffer_array.read_byte()
            remaining = _lrshift32(remaining, 7)
            if remaining > 0:
                byte = ctypes.c_int8(byte | 0x80).value
            out.write_byte(byte)
        self.write_bytes(out)

    def _unpack(self, fmt, size=1):
        buffer = self.read(size)
        fmt = ">" + fmt
        return struct.unpack(fmt, buffer)[0]

    def _pack(self, fmt, buffer):
        fmt = ">" + fmt
        return self.write(struct.pack(fmt, buffer))

class BooleanByteWrapper:

    @staticmethod
    def set_flag(byte, offset, flag):
        if offset == 0:
            if flag:
                byte = byte | 1
            else:
                byte = byte & 255 - 1
        elif offset == 1:
            if flag:
                byte = byte | 2
            else:
                byte = byte & 255 - 2
        elif offset == 2:
            if flag:
                byte = byte | 4
            else:
                byte = byte & 255 - 4
        elif offset == 3:
            if flag:
                byte = byte | 8
            else:
                byte = byte & 255 - 8
        elif offset == 4:
            if flag:
                byte = byte | 16
            else:
                byte = byte & 255 - 16
        elif offset == 5:
            if flag:
                byte = byte | 32
            else:
                byte = byte & 255 - 32
        elif offset == 6:
            if flag:
                byte = byte | 64
            else:
                byte = byte & 255 - 64
        elif offset == 7:
            if flag:
                byte = byte | 128
            else:
                byte = byte & 255 - 128
        else:
            raise RuntimeError("Bytebox overflow.")
        return byte

    @staticmethod
    def get_flag(byte, offset):
        if offset == 0:
            return (byte & 1) != 0
        elif offset == 1:
            return (byte & 2) != 0
        elif offset == 2:
            return (byte & 4) != 0
        elif offset == 3:
            return (byte & 8) != 0
        elif offset == 4:
            return (byte & 16) != 0
        elif offset == 5:
            return (byte & 32) != 0
        elif offset == 6:
            return (byte & 64) != 0
        elif offset == 7:
            return (byte & 128) != 0
        else:
            raise RuntimeError("Bytebox overflow.")

class FuncTree:

    def __init__(self, parent=None, function=None):
        self._parent = parent
        self._function = function
        self._children = []
        self._input = None
        self._current = None
        self._index = 0

    @property
    def children(self):
        return self._children

    def set_root(self, param1):
        self._input = param1
        self._current = self

    def add_child(self, param1):
        _loc2_ = FuncTree(self, param1)
        self._children.append(_loc2_)
        return _loc2_

    def next(self):
        self._current._function(self._input)
        if self.go_down():
            return True
        return self.go_up()

    def go_up(self):
        while True:
            self._current = self._current._parent
            if self._current._index != len(self._current._children):
                break
            if self._current._parent == None:
                return False
        self._current._index += 1
        self._current = self._current._children[self._current._index - 1]
        return True

    def go_down(self):
        if self._current._children == None:
            return False
        if self._current._index == len(self._current._children):
            return False
        self._current._index += 1
        self._current = self._current._children[self._current._index - 1]
        return True
