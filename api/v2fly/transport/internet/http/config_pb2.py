# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/http/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from transport.internet.headers.http import config_pb2 as transport_dot_internet_dot_headers_dot_http_dot_config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='transport/internet/http/config.proto',
  package='v2ray.core.transport.internet.http',
  syntax='proto3',
  serialized_options=b'\n&com.v2ray.core.transport.internet.httpP\001Z6github.com/v2fly/v2ray-core/v5/transport/internet/http\252\002\"V2Ray.Core.Transport.Internet.Http',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$transport/internet/http/config.proto\x12\"v2ray.core.transport.internet.http\x1a,transport/internet/headers/http/config.proto\"x\n\x06\x43onfig\x12\x0c\n\x04host\x18\x01 \x03(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0e\n\x06method\x18\x03 \x01(\t\x12\x42\n\x06header\x18\x04 \x03(\x0b\x32\x32.v2ray.core.transport.internet.headers.http.HeaderB\x87\x01\n&com.v2ray.core.transport.internet.httpP\x01Z6github.com/v2fly/v2ray-core/v5/transport/internet/http\xaa\x02\"V2Ray.Core.Transport.Internet.Httpb\x06proto3'
  ,
  dependencies=[transport_dot_internet_dot_headers_dot_http_dot_config__pb2.DESCRIPTOR,])




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.transport.internet.http.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='v2ray.core.transport.internet.http.Config.host', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='v2ray.core.transport.internet.http.Config.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='method', full_name='v2ray.core.transport.internet.http.Config.method', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='header', full_name='v2ray.core.transport.internet.http.Config.header', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=122,
  serialized_end=242,
)

_CONFIG.fields_by_name['header'].message_type = transport_dot_internet_dot_headers_dot_http_dot_config__pb2._HEADER
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'transport.internet.http.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.http.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
