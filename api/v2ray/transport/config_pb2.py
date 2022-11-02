# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v2ray.transport.internet import config_pb2 as transport_dot_internet_dot_config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='transport/config.proto',
  package='v2ray.core.transport',
  syntax='proto3',
  serialized_options=b'\n\030com.v2ray.core.transportP\001Z\030v2ray.com/core/transport\252\002\024V2Ray.Core.Transport',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16transport/config.proto\x12\x14v2ray.core.transport\x1a\x1ftransport/internet/config.proto\"T\n\x06\x43onfig\x12J\n\x12transport_settings\x18\x01 \x03(\x0b\x32..v2ray.core.transport.internet.TransportConfigBM\n\x18\x63om.v2ray.core.transportP\x01Z\x18v2ray.com/core/transport\xaa\x02\x14V2Ray.Core.Transportb\x06proto3'
  ,
  dependencies=[transport_dot_internet_dot_config__pb2.DESCRIPTOR,])




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.transport.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transport_settings', full_name='v2ray.core.transport.Config.transport_settings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=81,
  serialized_end=165,
)

_CONFIG.fields_by_name['transport_settings'].message_type = transport_dot_internet_dot_config__pb2._TRANSPORTCONFIG
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'transport.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
