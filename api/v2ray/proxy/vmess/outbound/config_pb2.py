# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/vmess/outbound/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common.protocol import server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy/vmess/outbound/config.proto',
  package='v2ray.core.proxy.vmess.outbound',
  syntax='proto3',
  serialized_options=b'\n#com.v2ray.core.proxy.vmess.outboundP\001Z#v2ray.com/core/proxy/vmess/outbound\252\002\037V2Ray.Core.Proxy.Vmess.Outbound',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!proxy/vmess/outbound/config.proto\x12\x1fv2ray.core.proxy.vmess.outbound\x1a!common/protocol/server_spec.proto\"F\n\x06\x43onfig\x12<\n\x08Receiver\x18\x01 \x03(\x0b\x32*.v2ray.core.common.protocol.ServerEndpointBn\n#com.v2ray.core.proxy.vmess.outboundP\x01Z#v2ray.com/core/proxy/vmess/outbound\xaa\x02\x1fV2Ray.Core.Proxy.Vmess.Outboundb\x06proto3'
  ,
  dependencies=[common_dot_protocol_dot_server__spec__pb2.DESCRIPTOR,])




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.proxy.vmess.outbound.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Receiver', full_name='v2ray.core.proxy.vmess.outbound.Config.Receiver', index=0,
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
  serialized_start=105,
  serialized_end=175,
)

_CONFIG.fields_by_name['Receiver'].message_type = common_dot_protocol_dot_server__spec__pb2._SERVERENDPOINT
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'proxy.vmess.outbound.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.vmess.outbound.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
