import re

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
    (r'setRoot', "set_root"),
    (r'addChild', "add_child"),
    (r'goUp', "go_up"),
    (r'goDown', "go_down"),
]

def python_subs(line):
    for replacement in REPLACEMENTS:
        line = re.sub(replacement[0], replacement[1], line)
    return line

class ClassReader:
    CONST_PATTERN = r'public\s+static\s+const\s+(\w+):u?int\s+=\s+(\d+);'
    CLASS_INFO_PATTERN = r'public\s+class\s+(\w+)(?:\s+extends\s(\w+))?'
    INCLUDE_PATTERN = r'import\s+com\.ankamagames\.dofus\.network\.([\w.]+)'

    @classmethod
    def _parse_class_info(cls, lines):
        for line in lines:
            match = re.search(cls.CLASS_INFO_PATTERN, line)
            if match:
                return match.group(1), match.group(2)
        raise RuntimeError("Could not find class and inheritance")

    @classmethod
    def _parse_includes(cls, lines):
        includes = []
        for line in lines:
            match = re.search(cls.INCLUDE_PATTERN, line)
            if match:
                includes.append(match.group(1))
        return includes

    @classmethod
    def _parse_class_attributes(cls, lines):
        attributes = []
        for line in lines:
            match = re.search(cls.CONST_PATTERN, line)
            if match:
                attribute = (match.group(1), match.group(2))
                attributes.append(attribute)
        return attributes

    @staticmethod
    def read_file(path):
        with open(path) as file_:
            return file_.read().splitlines()

    @classmethod
    def parse(cls, lines):
        name, inheritance = cls._parse_class_info(lines)
        return {"name": name, "inheritance": inheritance}

class EnumReader(ClassReader):

    @classmethod
    def parse(cls, lines):
        class_ = super().parse(lines)
        class_["class_attributes"] = cls._parse_class_attributes(lines)
        class_["inheritance"] = "IntEnum"
        return class_

class MessageReader(ClassReader):
    VARIABLE_PATTERN = r'(public|private|protected)\s+var\s+([\w\d_]+):([\w\d\.<>\*]+)[ = ]*([^\s=;]*);'
    VECTOR_PATTERN = r'(Vector).<([\w\d]+)>'
    METHOD_PATTERN = r'(?:override\s+)?(?:public|private|protected)\s+function\s+([\w\d_]+)\(([^)]*)\)'
    PARAM_PATTERN = r'([\w\d_]+):([\w\d\.<>\*]+)(?:\s+=\s+([^,\s)]+))?'

    @classmethod
    def _build_variable(cls, scope, name, type_, value):
        variable = {}
        variable["scope"] = scope
        variable["name"] = name
        variable["type"] = type_
        variable["value"] = value
        match = re.search(cls.VECTOR_PATTERN, variable["type"])
        if match:
            variable["is_array"] = True
            variable["type"] = match.group(2)
            variable["value"] = "[]"
        else:
            variable["is_array"] = False
        return variable

    @classmethod
    def _build_method(cls, name, params):
        method = {}
        method["name"] = name
        method["params"] = []
        for match in re.findall(cls.PARAM_PATTERN, params):
            variable = cls._build_variable(0, match[0], match[1], match[2])
            method["params"].append(variable)
        method["content"] = []
        return method

    @classmethod
    def _parse_attributes(cls, lines):
        attributes = []
        for line in lines:
            match = re.search(cls.VARIABLE_PATTERN, line)
            if match:
                attribute = cls._build_variable(
                    match.group(1),
                    match.group(2),
                    match.group(3),
                    match.group(4)
                )
                attributes.append(attribute)
        return attributes

    @classmethod
    def _parse_methods(cls, lines):
        methods = []
        for index, line in enumerate(lines):
            match = re.search(cls.METHOD_PATTERN, line)
            if match:
                indent_level = 0
                method = cls._build_method(match.group(1), match.group(2))
                for method_line in lines[index+1:]:
                    method["content"].append((method_line, indent_level))
                    if "{" in method_line:
                        indent_level += 1
                    elif "}" in method_line:
                        indent_level -= 1
                    if indent_level == 0:
                        methods.append(method)
                        break
        return methods

    @classmethod
    def parse(cls, lines):
        class_ = super().parse(lines)
        class_["includes"] = cls._parse_includes(lines)
        class_["attributes"] = cls._parse_attributes(lines)
        class_["class_attributes"] = cls._parse_class_attributes(lines)
        class_["methods"] = cls._parse_methods(lines)
        return class_
