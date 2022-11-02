# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/observatory/multiobservatory/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common.taggedfeatures import skeleton_pb2 as common_dot_taggedfeatures_dot_skeleton__pb2
from api.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/observatory/multiobservatory/config.proto',
  package='v2ray.core.app.observatory.multiobservatory',
  syntax='proto3',
  serialized_options=b'\n/com.v2ray.core.app.observatory.multiObservatoryP\001Z?github.com/v2fly/v2ray-core/v5/app/observatory/multiobservatory\252\002+V2Ray.Core.App.Observatory.MultiObservatory',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-app/observatory/multiobservatory/config.proto\x12+v2ray.core.app.observatory.multiobservatory\x1a$common/taggedfeatures/skeleton.proto\x1a common/protoext/extensions.proto\"h\n\x06\x43onfig\x12\x39\n\x07holders\x18\x01 \x01(\x0b\x32(.v2ray.core.common.taggedfeatures.Config:#\x82\xb5\x18\t\n\x07service\x82\xb5\x18\x12\x12\x10multiobservatoryB\xa2\x01\n/com.v2ray.core.app.observatory.multiObservatoryP\x01Z?github.com/v2fly/v2ray-core/v5/app/observatory/multiobservatory\xaa\x02+V2Ray.Core.App.Observatory.MultiObservatoryb\x06proto3'
  ,
  dependencies=[common_dot_taggedfeatures_dot_skeleton__pb2.DESCRIPTOR,common_dot_protoext_dot_extensions__pb2.DESCRIPTOR,])




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.app.observatory.multiobservatory.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='holders', full_name='v2ray.core.app.observatory.multiobservatory.Config.holders', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\202\265\030\t\n\007service\202\265\030\022\022\020multiobservatory',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=270,
)

_CONFIG.fields_by_name['holders'].message_type = common_dot_taggedfeatures_dot_skeleton__pb2._CONFIG
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.observatory.multiobservatory.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.observatory.multiobservatory.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
_CONFIG._options = None
# @@protoc_insertion_point(module_scope)
