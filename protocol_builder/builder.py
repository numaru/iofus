import time

from reader import EnumReader, MessageReader
from writer import EnumWriter, MessageWriter, TypeWriter


class ClassBuilder:

    @classmethod
    def _get_inheritance_order(cls, classes, parent):
        inheritance = next((x for x in classes if x["name"] == parent["inheritance"]), None)
        if inheritance:
            return cls._get_inheritance_order(classes, inheritance) + 1
        else:
            return 1

    @classmethod
    def _low_build(cls, input_paths, output_path, reader_class, writer_class):
        start = time.time()
        file_lines = [reader_class.read_file(path) for path in input_paths]
        classes = [reader_class.parse(lines) for lines in file_lines]
        classes = sorted(classes, key=lambda x: cls._get_inheritance_order(classes, x))
        writer = writer_class()
        for _ in writer.traduct_classes(classes):
            yield time.time() - start
        writer.save_file(output_path)
        end = time.time()
        yield end - start


class EnumBuilder(ClassBuilder):

    @classmethod
    def build(cls, input_paths, output_path):
        for elapsed in cls._low_build(input_paths, output_path, EnumReader, EnumWriter):
            yield elapsed


class MessageBuilder(ClassBuilder):

    @classmethod
    def build(cls, input_paths, output_path):
        for elapsed in cls._low_build(input_paths, output_path, MessageReader, MessageWriter):
            yield elapsed


class TypeBuilder(ClassBuilder):

    @classmethod
    def build(cls, input_paths, output_path):
        for elapsed in cls._low_build(input_paths, output_path, MessageReader, TypeWriter):
            yield elapsed
