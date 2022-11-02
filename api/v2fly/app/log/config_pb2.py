# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/log/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common.log import log_pb2 as common_dot_log_dot_log__pb2
from api.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/log/config.proto',
  package='v2ray.core.app.log',
  syntax='proto3',
  serialized_options=b'\n\026com.v2ray.core.app.logP\001Z&github.com/v2fly/v2ray-core/v5/app/log\252\002\022V2Ray.Core.App.Log',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x61pp/log/config.proto\x12\x12v2ray.core.app.log\x1a\x14\x63ommon/log/log.proto\x1a common/protoext/extensions.proto\"{\n\x10LogSpecification\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.v2ray.core.app.log.LogType\x12.\n\x05level\x18\x02 \x01(\x0e\x32\x1f.v2ray.core.common.log.Severity\x12\x0c\n\x04path\x18\x03 \x01(\t\"\xa9\x01\n\x06\x43onfig\x12\x33\n\x05\x65rror\x18\x06 \x01(\x0b\x32$.v2ray.core.app.log.LogSpecification\x12\x34\n\x06\x61\x63\x63\x65ss\x18\x07 \x01(\x0b\x32$.v2ray.core.app.log.LogSpecification:\x16\x82\xb5\x18\t\n\x07service\x82\xb5\x18\x05\x12\x03logJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06*5\n\x07LogType\x12\x08\n\x04None\x10\x00\x12\x0b\n\x07\x43onsole\x10\x01\x12\x08\n\x04\x46ile\x10\x02\x12\t\n\x05\x45vent\x10\x03\x42W\n\x16\x63om.v2ray.core.app.logP\x01Z&github.com/v2fly/v2ray-core/v5/app/log\xaa\x02\x12V2Ray.Core.App.Logb\x06proto3'
  ,
  dependencies=[common_dot_log_dot_log__pb2.DESCRIPTOR,common_dot_protoext_dot_extensions__pb2.DESCRIPTOR,])

_LOGTYPE = _descriptor.EnumDescriptor(
  name='LogType',
  full_name='v2ray.core.app.log.LogType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='None', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Console', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='File', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Event', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=397,
  serialized_end=450,
)
_sym_db.RegisterEnumDescriptor(_LOGTYPE)

LogType = enum_type_wrapper.EnumTypeWrapper(_LOGTYPE)
globals()['None'] = 0
Console = 1
File = 2
Event = 3



_LOGSPECIFICATION = _descriptor.Descriptor(
  name='LogSpecification',
  full_name='v2ray.core.app.log.LogSpecification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='v2ray.core.app.log.LogSpecification.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='v2ray.core.app.log.LogSpecification.level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='v2ray.core.app.log.LogSpecification.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=223,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.app.log.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='v2ray.core.app.log.Config.error', index=0,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access', full_name='v2ray.core.app.log.Config.access', index=1,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\202\265\030\t\n\007service\202\265\030\005\022\003log',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=395,
)

_LOGSPECIFICATION.fields_by_name['type'].enum_type = _LOGTYPE
_LOGSPECIFICATION.fields_by_name['level'].enum_type = common_dot_log_dot_log__pb2._SEVERITY
_CONFIG.fields_by_name['error'].message_type = _LOGSPECIFICATION
_CONFIG.fields_by_name['access'].message_type = _LOGSPECIFICATION
DESCRIPTOR.message_types_by_name['LogSpecification'] = _LOGSPECIFICATION
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.enum_types_by_name['LogType'] = _LOGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogSpecification = _reflection.GeneratedProtocolMessageType('LogSpecification', (_message.Message,), {
  'DESCRIPTOR' : _LOGSPECIFICATION,
  '__module__' : 'app.log.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.log.LogSpecification)
  })
_sym_db.RegisterMessage(LogSpecification)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.log.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.log.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
_CONFIG._options = None
# @@protoc_insertion_point(module_scope)
