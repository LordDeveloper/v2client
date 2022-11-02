# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/vless/account.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy/vless/account.proto',
  package='v2ray.core.proxy.vless',
  syntax='proto3',
  serialized_options=b'\n\032com.v2ray.core.proxy.vlessP\001Z\032v2ray.com/core/proxy/vless\252\002\026V2Ray.Core.Proxy.Vless',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19proxy/vless/account.proto\x12\x16v2ray.core.proxy.vless\"7\n\x07\x41\x63\x63ount\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x66low\x18\x02 \x01(\t\x12\x12\n\nencryption\x18\x03 \x01(\tBS\n\x1a\x63om.v2ray.core.proxy.vlessP\x01Z\x1av2ray.com/core/proxy/vless\xaa\x02\x16V2Ray.Core.Proxy.Vlessb\x06proto3'
)




_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='v2ray.core.proxy.vless.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v2ray.core.proxy.vless.Account.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flow', full_name='v2ray.core.proxy.vless.Account.flow', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='encryption', full_name='v2ray.core.proxy.vless.Account.encryption', index=2,
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
  serialized_start=53,
  serialized_end=108,
)

DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'proxy.vless.account_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.vless.Account)
  })
_sym_db.RegisterMessage(Account)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
