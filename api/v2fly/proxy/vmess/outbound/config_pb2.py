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
from api.common.net import address_pb2 as common_dot_net_dot_address__pb2
from api.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy/vmess/outbound/config.proto',
  package='v2ray.core.proxy.vmess.outbound',
  syntax='proto3',
  serialized_options=b'\n#com.v2ray.core.proxy.vmess.outboundP\001Z3github.com/v2fly/v2ray-core/v5/proxy/vmess/outbound\252\002\037V2Ray.Core.Proxy.Vmess.Outbound',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!proxy/vmess/outbound/config.proto\x12\x1fv2ray.core.proxy.vmess.outbound\x1a!common/protocol/server_spec.proto\x1a\x18\x63ommon/net/address.proto\x1a common/protoext/extensions.proto\"F\n\x06\x43onfig\x12<\n\x08Receiver\x18\x01 \x03(\x0b\x32*.v2ray.core.common.protocol.ServerEndpoint\"}\n\x10SimplifiedConfig\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x0c\n\x04uuid\x18\x03 \x01(\t:\x19\x82\xb5\x18\n\n\x08outbound\x82\xb5\x18\x07\x12\x05vmessB~\n#com.v2ray.core.proxy.vmess.outboundP\x01Z3github.com/v2fly/v2ray-core/v5/proxy/vmess/outbound\xaa\x02\x1fV2Ray.Core.Proxy.Vmess.Outboundb\x06proto3'
  ,
  dependencies=[common_dot_protocol_dot_server__spec__pb2.DESCRIPTOR,common_dot_net_dot_address__pb2.DESCRIPTOR,common_dot_protoext_dot_extensions__pb2.DESCRIPTOR,])




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
  serialized_start=165,
  serialized_end=235,
)


_SIMPLIFIEDCONFIG = _descriptor.Descriptor(
  name='SimplifiedConfig',
  full_name='v2ray.core.proxy.vmess.outbound.SimplifiedConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='v2ray.core.proxy.vmess.outbound.SimplifiedConfig.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='v2ray.core.proxy.vmess.outbound.SimplifiedConfig.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='v2ray.core.proxy.vmess.outbound.SimplifiedConfig.uuid', index=2,
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
  serialized_options=b'\202\265\030\n\n\010outbound\202\265\030\007\022\005vmess',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=362,
)

_CONFIG.fields_by_name['Receiver'].message_type = common_dot_protocol_dot_server__spec__pb2._SERVERENDPOINT
_SIMPLIFIEDCONFIG.fields_by_name['address'].message_type = common_dot_net_dot_address__pb2._IPORDOMAIN
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['SimplifiedConfig'] = _SIMPLIFIEDCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'proxy.vmess.outbound.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.vmess.outbound.Config)
  })
_sym_db.RegisterMessage(Config)

SimplifiedConfig = _reflection.GeneratedProtocolMessageType('SimplifiedConfig', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLIFIEDCONFIG,
  '__module__' : 'proxy.vmess.outbound.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.vmess.outbound.SimplifiedConfig)
  })
_sym_db.RegisterMessage(SimplifiedConfig)


DESCRIPTOR._options = None
_SIMPLIFIEDCONFIG._options = None
# @@protoc_insertion_point(module_scope)
