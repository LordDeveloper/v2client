# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/vless/encoding/addons.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy/vless/encoding/addons.proto',
  package='v2ray.core.proxy.vless.encoding',
  syntax='proto3',
  serialized_options=b'\n#com.v2ray.core.proxy.vless.encodingP\001Z3github.com/v2fly/v2ray-core/v5/proxy/vless/encoding\252\002\037V2Ray.Core.Proxy.Vless.Encoding',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!proxy/vless/encoding/addons.proto\x12\x1fv2ray.core.proxy.vless.encoding\"$\n\x06\x41\x64\x64ons\x12\x0c\n\x04\x46low\x18\x01 \x01(\t\x12\x0c\n\x04Seed\x18\x02 \x01(\x0c\x42~\n#com.v2ray.core.proxy.vless.encodingP\x01Z3github.com/v2fly/v2ray-core/v5/proxy/vless/encoding\xaa\x02\x1fV2Ray.Core.Proxy.Vless.Encodingb\x06proto3'
)




_ADDONS = _descriptor.Descriptor(
  name='Addons',
  full_name='v2ray.core.proxy.vless.encoding.Addons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Flow', full_name='v2ray.core.proxy.vless.encoding.Addons.Flow', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Seed', full_name='v2ray.core.proxy.vless.encoding.Addons.Seed', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=70,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['Addons'] = _ADDONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Addons = _reflection.GeneratedProtocolMessageType('Addons', (_message.Message,), {
  'DESCRIPTOR' : _ADDONS,
  '__module__' : 'proxy.vless.encoding.addons_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.vless.encoding.Addons)
  })
_sym_db.RegisterMessage(Addons)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
