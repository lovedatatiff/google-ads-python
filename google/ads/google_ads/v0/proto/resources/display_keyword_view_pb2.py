# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/resources/display_keyword_view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/resources/display_keyword_view.proto',
  package='google.ads.googleads.v0.resources',
  syntax='proto3',
  serialized_pb=_b('\nBgoogle/ads/googleads_v0/proto/resources/display_keyword_view.proto\x12!google.ads.googleads.v0.resources\"+\n\x12\x44isplayKeywordView\x12\x15\n\rresource_name\x18\x01 \x01(\tB\xdc\x01\n%com.google.ads.googleads.v0.resourcesB\x17\x44isplayKeywordViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V0.Resources\xca\x02!Google\\Ads\\GoogleAds\\V0\\Resourcesb\x06proto3')
)




_DISPLAYKEYWORDVIEW = _descriptor.Descriptor(
  name='DisplayKeywordView',
  full_name='google.ads.googleads.v0.resources.DisplayKeywordView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.resources.DisplayKeywordView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['DisplayKeywordView'] = _DISPLAYKEYWORDVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DisplayKeywordView = _reflection.GeneratedProtocolMessageType('DisplayKeywordView', (_message.Message,), dict(
  DESCRIPTOR = _DISPLAYKEYWORDVIEW,
  __module__ = 'google.ads.googleads_v0.proto.resources.display_keyword_view_pb2'
  ,
  __doc__ = """A display keyword view.
  
  
  Attributes:
      resource_name:
          The resource name of the display keyword view. Display Keyword
          view resource names have the form:  ``customers/{customer_id}/
          displayKeywordViews/{ad_group_id}_{criterion_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.resources.DisplayKeywordView)
  ))
_sym_db.RegisterMessage(DisplayKeywordView)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%com.google.ads.googleads.v0.resourcesB\027DisplayKeywordViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V0.Resources\312\002!Google\\Ads\\GoogleAds\\V0\\Resources'))
# @@protoc_insertion_point(module_scope)
