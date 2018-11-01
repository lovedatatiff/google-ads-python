# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/income_range_type.proto

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
  name='google/ads/googleads_v0/proto/enums/income_range_type.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n;google/ads/googleads_v0/proto/enums/income_range_type.proto\x12\x1dgoogle.ads.googleads.v0.enums\"\x83\x02\n\x13IncomeRangeTypeEnum\"\xeb\x01\n\x0fIncomeRangeType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x17\n\x11INCOME_RANGE_0_50\x10\xb1\x90\x1f\x12\x18\n\x12INCOME_RANGE_50_60\x10\xb2\x90\x1f\x12\x18\n\x12INCOME_RANGE_60_70\x10\xb3\x90\x1f\x12\x18\n\x12INCOME_RANGE_70_80\x10\xb4\x90\x1f\x12\x18\n\x12INCOME_RANGE_80_90\x10\xb5\x90\x1f\x12\x18\n\x12INCOME_RANGE_90_UP\x10\xb6\x90\x1f\x12\x1f\n\x19INCOME_RANGE_UNDETERMINED\x10\xb0\x90\x1f\x42\xc5\x01\n!com.google.ads.googleads.v0.enumsB\x14IncomeRangeTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_INCOMERANGETYPEENUM_INCOMERANGETYPE = _descriptor.EnumDescriptor(
  name='IncomeRangeType',
  full_name='google.ads.googleads.v0.enums.IncomeRangeTypeEnum.IncomeRangeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_0_50', index=2, number=510001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_50_60', index=3, number=510002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_60_70', index=4, number=510003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_70_80', index=5, number=510004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_80_90', index=6, number=510005,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_90_UP', index=7, number=510006,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_UNDETERMINED', index=8, number=510000,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=119,
  serialized_end=354,
)
_sym_db.RegisterEnumDescriptor(_INCOMERANGETYPEENUM_INCOMERANGETYPE)


_INCOMERANGETYPEENUM = _descriptor.Descriptor(
  name='IncomeRangeTypeEnum',
  full_name='google.ads.googleads.v0.enums.IncomeRangeTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INCOMERANGETYPEENUM_INCOMERANGETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=354,
)

_INCOMERANGETYPEENUM_INCOMERANGETYPE.containing_type = _INCOMERANGETYPEENUM
DESCRIPTOR.message_types_by_name['IncomeRangeTypeEnum'] = _INCOMERANGETYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IncomeRangeTypeEnum = _reflection.GeneratedProtocolMessageType('IncomeRangeTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _INCOMERANGETYPEENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.income_range_type_pb2'
  ,
  __doc__ = """Container for enum describing the type of demographic income ranges.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.IncomeRangeTypeEnum)
  ))
_sym_db.RegisterMessage(IncomeRangeTypeEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\024IncomeRangeTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
