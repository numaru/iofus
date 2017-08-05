import re

class ClassWriter:
    HEADER = []
    REPLACEMENTS = [
        (r'this', "self"),
        (r'(null|NaN)', "None"),
        (r'(?:;|{|})', ""),
        (r'\s*\|\|\s*', " or "),
        (r'\s*&&\s*', " and "),
        (r'([\w\d_.]+).length', lambda x: "len({0})".format(x.group(1))),
        (r'.push\(', ".append("),
        (r'super.([\w\d_]+)', lambda x: "super().{0}".format(x.group(1))),
        (r'(false|true)', lambda x: x.group(1).capitalize()),
        (r'([\w\d_.]+)\+\+', lambda x: "{0} += 1".format(x.group(1))),
        (r'(while|if)\s*\((.*)\)', lambda x: "{0} {1}:".format(x.group(1), x.group(2))),
        (r'throw\s+(?:new\s+)?([\w\d_]+)', "raise RuntimeError"),
        (
            r'(\".*\")\s*\+\s*([\w\d_.\[\]\(\)]+)',
            lambda x: "{0} + str({1})".format(x.group(1), x.group(2))
        ),
        (r'var\s+([\w\d_]+):[\w\d_]+', lambda x: "{0}".format(x.group(1))),
        (
            r'\(([\w\d_\[\]\.]+)\s+as\s+([\w\_]+)\)',
            lambda x: "as_parent({0}, {1})".format(x.group(1), x.group(2))
        ),
        (r'new\s+', ""),
        (r'Vector.<[\w\d_]+>\([^)]*\)', "[]"),
        (
            r'([\w\d_]+)\[_loc\d+_\]\s*=\s*([^\s]+)',
            lambda x: "{0}.append({1})".format(x.group(1), x.group(2))
        ),
        (r'CustomDataWrapper\(([^)]+)\)', lambda x: "{0}".format(x.group(1))),
        (r'writePacket', "self.write_packet"),

        # Switch to snake_case
        (r'bytesAvailable', "bytes_available"),
        (r'getInstance', "get_instance"),
        (r'getFlag', "get_flag"),
        (r'setFlag', "set_flag"),
        (r'readBoolean', "read_boolean"),
        (r'readByte', "read_byte"),
        (r'readBytes', "read_bytes"),
        (r'readDouble', "read_double"),
        (r'readFloat', "read_float"),
        (r'readInt', "read_int"),
        (r'readShort', "read_short"),
        (r'readUnsignedByte', "read_unsigned_byte"),
        (r'readUnsignedInt', "read_unsigned_int"),
        (r'readUnsignedShort', "read_unsigned_short"),
        (r'readUTF', "read_utf"),
        (r'readVarInt', "read_var_int"),
        (r'readVarUhInt', "read_var_uh_int"),
        (r'readVarShort', "read_var_short"),
        (r'readVarUhShort', "read_var_uh_short"),
        (r'readVarLong', "read_var_long"),
        (r'readVarUhLong', "read_var_uh_long"),
        (r'writeBoolean', "write_boolean"),
        (r'writeByte', "write_byte"),
        (r'writeBytes', "write_bytes"),
        (r'writeDouble', "write_double"),
        (r'writeFloat', "write_float"),
        (r'writeInt', "write_int"),
        (r'writeShort', "write_short"),
        (r'writeUnsignedByte', "write_unsigned_byte"),
        (r'writeUnsignedInt', "write_unsigned_int"),
        (r'writeUnsignedShort', "write_unsigned_short"),
        (r'writeUTF', "write_utf"),
        (r'writeVarInt', "write_var_int"),
        (r'writeVarShort', "write_var_short"),
        (r'writeVarLong', "write_var_long"),
        (r'setRoot', "set_root"),
        (r'addChild', "add_child"),
        (r'goUp', "go_up"),
        (r'goDown', "go_down"),
    ]

    def __init__(self):
        self._ident_level = 0
        self._ident_char = " "
        self._ident_number = 4
        self._carriage_char = "\n"
        self.content = ""

    def indent(self):
        self._ident_level += 1

    def unindent(self):
        if self._ident_level == 0:
            return
        self._ident_level -= 1

    def skip_line(self, number=1):
        self.content += self._carriage_char * number

    def write_line(self, line):
        self.content += "{0}{1}{2}".format(
            self._ident_char * self._ident_number * self._ident_level,
            line,
            self._carriage_char
        )

    def traduct_classes(self, classes):
        for line in self.HEADER:
            self.write_line(line)
        self.skip_line(2)
        for class_ in classes:
            self.traduct_class(class_)
            self.skip_line(2)
            yield

    def traduct_class(self, class_):
        inheritance = class_["inheritance"] if class_["inheritance"] else ""
        self.write_line("class {0}({1}):".format(
            class_["name"],
            inheritance
        ))

    def save_file(self, path):
        with open(path, "w") as file_:
            file_.write(self.content)

    @classmethod
    def correct(cls, line):
        for replacement in cls.REPLACEMENTS:
            line = re.sub(replacement[0], replacement[1], line)
        return str(line)


class EnumWriter(ClassWriter):
    HEADER = ["from enum import IntEnum"]

    def __init__(self):
        super().__init__()

    def traduct_class(self, class_data):
        super().traduct_class(class_data)
        self.indent()
        for attribute in class_data.get("class_attributes", []):
            name = attribute[0]
            value = attribute[1]
            self.write_line("{0} = {1}".format(name, value))
        self.unindent()


class MessageWriter(ClassWriter):
    HEADER = [
        "from iofus.binaryio import BooleanByteWrapper, ByteArray, FuncTree",
        "from iofus.denums import *",
        "from iofus.dtypes import *",
        "from iofus.network import NetworkMessage, ProtocolTypeManager"
    ]

    def __init__(self):
        super().__init__()

    def traduct_class(self, class_):
        super().traduct_class(class_)
        self.indent()
        for attribute in class_.get("class_attributes", []):
            name = attribute[0]
            value = attribute[1]
            self.write_line("{0} = {1}".format(name, value))
        self.traduct_constructor(class_)
        for method in class_["methods"]:
            if method["name"] != class_["name"]:
                self.skip_line()
                self.traduct_method(method)
        self.unindent()

    def traduct_constructor(self, class_):
        if class_.get("attributes"):
            self.skip_line()
            self.write_line("def __init__(self):")
            self.indent()
            self.write_line("super().__init__()")
            for attribute in class_["attributes"]:
                name = attribute["name"]
                type_ = attribute["type"]
                value = self.correct(attribute["value"])
                if value == "":
                    value = type_ + "()"
                self.write_line("self.{0} = {1}".format(name, value))
            self.unindent()

    def traduct_method(self, method):
        param_string = ""
        for param in method["params"]:
            param_string += ", "
            param_string += param["name"]
            if param["value"]:
                param_string += "=" + self.correct(param["value"])
        self.write_line("def {0}(self{1}):".format(method["name"], param_string))
        if len(method["content"]) < 3:
            self.indent()
            self.write_line("pass")
            self.unindent()
        else:
            for _, (line, indent_level) in enumerate(method["content"]):
                line = self.correct(line)
                if not line.isspace():
                    self.write_line(" " * indent_level * 4 + line.strip())


class TypeWriter(MessageWriter):
    HEADER = [
        "from iofus.binaryio import BooleanByteWrapper, ByteArray, FuncTree",
        "from iofus.denums import *",
        "from iofus.network import ProtocolTypeManager"
    ]
