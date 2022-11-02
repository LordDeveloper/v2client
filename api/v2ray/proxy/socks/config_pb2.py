# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/socks/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common.net import address_pb2 as common_dot_net_dot_address__pb2
from api.common.protocol import server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy/socks/config.proto',
  package='v2ray.core.proxy.socks',
  syntax='proto3',
  serialized_options=b'\n\032com.v2ray.core.proxy.socksP\001Z\032v2ray.com/core/proxy/socks\252\002\026V2Ray.Core.Proxy.Socks',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18proxy/socks/config.proto\x12\x16v2ray.core.proxy.socks\x1a\x18\x63ommon/net/address.proto\x1a!common/protocol/server_spec.proto\"-\n\x07\x41\x63\x63ount\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\xac\x02\n\x0cServerConfig\x12\x33\n\tauth_type\x18\x01 \x01(\x0e\x32 .v2ray.core.proxy.socks.AuthType\x12\x44\n\x08\x61\x63\x63ounts\x18\x02 \x03(\x0b\x32\x32.v2ray.core.proxy.socks.ServerConfig.AccountsEntry\x12\x32\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12\x13\n\x0budp_enabled\x18\x04 \x01(\x08\x12\x13\n\x07timeout\x18\x05 \x01(\rB\x02\x18\x01\x12\x12\n\nuser_level\x18\x06 \x01(\r\x1a/\n\rAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"J\n\x0c\x43lientConfig\x12:\n\x06server\x18\x01 \x03(\x0b\x32*.v2ray.core.common.protocol.ServerEndpoint*%\n\x08\x41uthType\x12\x0b\n\x07NO_AUTH\x10\x00\x12\x0c\n\x08PASSWORD\x10\x01\x42S\n\x1a\x63om.v2ray.core.proxy.socksP\x01Z\x1av2ray.com/core/proxy/socks\xaa\x02\x16V2Ray.Core.Proxy.Socksb\x06proto3'
  ,
  dependencies=[common_dot_net_dot_address__pb2.DESCRIPTOR,common_dot_protocol_dot_server__spec__pb2.DESCRIPTOR,])

_AUTHTYPE = _descriptor.EnumDescriptor(
  name='AuthType',
  full_name='v2ray.core.proxy.socks.AuthType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_AUTH', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PASSWORD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=539,
  serialized_end=576,
)
_sym_db.RegisterEnumDescriptor(_AUTHTYPE)

AuthType = enum_type_wrapper.EnumTypeWrapper(_AUTHTYPE)
NO_AUTH = 0
PASSWORD = 1



_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='v2ray.core.proxy.socks.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='v2ray.core.proxy.socks.Account.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='v2ray.core.proxy.socks.Account.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=113,
  serialized_end=158,
)


_SERVERCONFIG_ACCOUNTSENTRY = _descriptor.Descriptor(
  name='AccountsEntry',
  full_name='v2ray.core.proxy.socks.ServerConfig.AccountsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v2ray.core.proxy.socks.ServerConfig.AccountsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='v2ray.core.proxy.socks.ServerConfig.AccountsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=414,
  serialized_end=461,
)

_SERVERCONFIG = _descriptor.Descriptor(
  name='ServerConfig',
  full_name='v2ray.core.proxy.socks.ServerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_type', full_name='v2ray.core.proxy.socks.ServerConfig.auth_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accounts', full_name='v2ray.core.proxy.socks.ServerConfig.accounts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='v2ray.core.proxy.socks.ServerConfig.address', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='udp_enabled', full_name='v2ray.core.proxy.socks.ServerConfig.udp_enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='v2ray.core.proxy.socks.ServerConfig.timeout', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_level', full_name='v2ray.core.proxy.socks.ServerConfig.user_level', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SERVERCONFIG_ACCOUNTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=461,
)


_CLIENTCONFIG = _descriptor.Descriptor(
  name='ClientConfig',
  full_name='v2ray.core.proxy.socks.ClientConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server', full_name='v2ray.core.proxy.socks.ClientConfig.server', index=0,
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
  serialized_start=463,
  serialized_end=537,
)

_SERVERCONFIG_ACCOUNTSENTRY.containing_type = _SERVERCONFIG
_SERVERCONFIG.fields_by_name['auth_type'].enum_type = _AUTHTYPE
_SERVERCONFIG.fields_by_name['accounts'].message_type = _SERVERCONFIG_ACCOUNTSENTRY
_SERVERCONFIG.fields_by_name['address'].message_type = common_dot_net_dot_address__pb2._IPORDOMAIN
_CLIENTCONFIG.fields_by_name['server'].message_type = common_dot_protocol_dot_server__spec__pb2._SERVERENDPOINT
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['ServerConfig'] = _SERVERCONFIG
DESCRIPTOR.message_types_by_name['ClientConfig'] = _CLIENTCONFIG
DESCRIPTOR.enum_types_by_name['AuthType'] = _AUTHTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'proxy.socks.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.socks.Account)
  })
_sym_db.RegisterMessage(Account)

ServerConfig = _reflection.GeneratedProtocolMessageType('ServerConfig', (_message.Message,), {

  'AccountsEntry' : _reflection.GeneratedProtocolMessageType('AccountsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERVERCONFIG_ACCOUNTSENTRY,
    '__module__' : 'proxy.socks.config_pb2'
    # @@protoc_insertion_point(class_scope:v2ray.core.proxy.socks.ServerConfig.AccountsEntry)
    })
  ,
  'DESCRIPTOR' : _SERVERCONFIG,
  '__module__' : 'proxy.socks.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.socks.ServerConfig)
  })
_sym_db.RegisterMessage(ServerConfig)
_sym_db.RegisterMessage(ServerConfig.AccountsEntry)

ClientConfig = _reflection.GeneratedProtocolMessageType('ClientConfig', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTCONFIG,
  '__module__' : 'proxy.socks.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.socks.ClientConfig)
  })
_sym_db.RegisterMessage(ClientConfig)


DESCRIPTOR._options = None
_SERVERCONFIG_ACCOUNTSENTRY._options = None
_SERVERCONFIG.fields_by_name['timeout']._options = None
# @@protoc_insertion_point(module_scope)
