# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/dns/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common.net import destination_pb2 as common_dot_net_dot_destination__pb2
from api.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy/dns/config.proto',
  package='v2ray.core.proxy.dns',
  syntax='proto3',
  serialized_options=b'\n\030com.v2ray.core.proxy.dnsP\001Z(github.com/v2fly/v2ray-core/v5/proxy/dns\252\002\024V2Ray.Core.Proxy.Dns',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16proxy/dns/config.proto\x12\x14v2ray.core.proxy.dns\x1a\x1c\x63ommon/net/destination.proto\x1a common/protoext/extensions.proto\"M\n\x06\x43onfig\x12/\n\x06server\x18\x01 \x01(\x0b\x32\x1f.v2ray.core.common.net.Endpoint\x12\x12\n\nuser_level\x18\x02 \x01(\r\"+\n\x10SimplifiedConfig:\x17\x82\xb5\x18\n\n\x08outbound\x82\xb5\x18\x05\x12\x03\x64nsB]\n\x18\x63om.v2ray.core.proxy.dnsP\x01Z(github.com/v2fly/v2ray-core/v5/proxy/dns\xaa\x02\x14V2Ray.Core.Proxy.Dnsb\x06proto3'
  ,
  dependencies=[common_dot_net_dot_destination__pb2.DESCRIPTOR,common_dot_protoext_dot_extensions__pb2.DESCRIPTOR,])




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.proxy.dns.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server', full_name='v2ray.core.proxy.dns.Config.server', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_level', full_name='v2ray.core.proxy.dns.Config.user_level', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=112,
  serialized_end=189,
)


_SIMPLIFIEDCONFIG = _descriptor.Descriptor(
  name='SimplifiedConfig',
  full_name='v2ray.core.proxy.dns.SimplifiedConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\202\265\030\n\n\010outbound\202\265\030\005\022\003dns',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=234,
)

_CONFIG.fields_by_name['server'].message_type = common_dot_net_dot_destination__pb2._ENDPOINT
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['SimplifiedConfig'] = _SIMPLIFIEDCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'proxy.dns.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.dns.Config)
  })
_sym_db.RegisterMessage(Config)

SimplifiedConfig = _reflection.GeneratedProtocolMessageType('SimplifiedConfig', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLIFIEDCONFIG,
  '__module__' : 'proxy.dns.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.dns.SimplifiedConfig)
  })
_sym_db.RegisterMessage(SimplifiedConfig)


DESCRIPTOR._options = None
_SIMPLIFIEDCONFIG._options = None
# @@protoc_insertion_point(module_scope)
