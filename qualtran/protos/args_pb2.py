# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qualtran/protos/args.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aqualtran/protos/args.proto\x12\x08qualtran\"<\n\nIntOrSympy\x12\x11\n\x07int_val\x18\x01 \x01(\x03H\x00\x12\x14\n\nsympy_expr\x18\x02 \x01(\tH\x00\x42\x05\n\x03val\"5\n\x07NDArray\x12\r\n\x05shape\x18\x01 \x03(\x05\x12\r\n\x05\x64type\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\xc5\x01\n\x07\x42loqArg\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x07int_val\x18\x02 \x01(\x03H\x00\x12\x13\n\tfloat_val\x18\x03 \x01(\x01H\x00\x12\x14\n\nstring_val\x18\x04 \x01(\tH\x00\x12\x14\n\nsympy_expr\x18\x05 \x01(\tH\x00\x12$\n\x07ndarray\x18\x06 \x01(\x0b\x32\x11.qualtran.NDArrayH\x00\x12\x11\n\x07subbloq\x18\x07 \x01(\x05H\x00\x12\x18\n\x0e\x63irq_json_gzip\x18\x08 \x01(\x0cH\x00\x42\x05\n\x03valb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qualtran.protos.args_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_INTORSYMPY']._serialized_start=40
  _globals['_INTORSYMPY']._serialized_end=100
  _globals['_NDARRAY']._serialized_start=102
  _globals['_NDARRAY']._serialized_end=155
  _globals['_BLOQARG']._serialized_start=158
  _globals['_BLOQARG']._serialized_end=355
# @@protoc_insertion_point(module_scope)