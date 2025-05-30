# coding=utf-8
# Copyright 2025 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature_neighborhood_tensor_opts.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='feature_neighborhood_tensor_opts.proto',
  package='neighborhood',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&feature_neighborhood_tensor_opts.proto\x12\x0cneighborhood\"\xed\x01\n\x0fPaddedBatchOpts\x12\x37\n\x08pad_type\x18\x01 \x01(\x0e\x32%.neighborhood.PaddedBatchOpts.PadType\x12\x0f\n\x07pad_dim\x18\x02 \x01(\x05\x12\x11\n\tfixed_len\x18\x03 \x01(\x05\x12\x11\n\tpad_value\x18\x04 \x01(\x02\x12\x13\n\x0b\x66ixate_size\x18\x05 \x03(\x05\"U\n\x07PadType\x12\x17\n\x13PADTYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bPAD_MAX_LEN\x10\x01\x12\x11\n\rPAD_FIXED_LEN\x10\x02\x12\r\n\tFIXED_LEN\x10\x03\"\xcc\x03\n\x1d\x46\x65\x61tureNeighborhoodTensorOpts\x12L\n\x05input\x18\x01 \x01(\x0b\x32=.neighborhood.FeatureNeighborhoodTensorOpts.SymbolsAndMarkers\x12M\n\x06output\x18\x02 \x01(\x0b\x32=.neighborhood.FeatureNeighborhoodTensorOpts.SymbolsAndMarkers\x12\x12\n\nappend_eos\x18\x03 \x01(\x08\x12\x18\n\x10max_spelling_len\x18\x04 \x01(\x05\x12\x1d\n\x15max_pronunciation_len\x18\x05 \x01(\x05\x12\x15\n\rmax_neighbors\x18\x06 \x01(\x05\x12\x31\n\nbatch_opts\x18\x07 \x01(\x0b\x32\x1d.neighborhood.PaddedBatchOpts\x12\x1d\n\x15split_output_on_space\x18\x08 \x01(\x08\x1aX\n\x11SymbolsAndMarkers\x12\x19\n\x11start_of_sentence\x18\x01 \x01(\t\x12\x17\n\x0f\x65nd_of_sentence\x18\x02 \x01(\t\x12\x0f\n\x07symbols\x18\x03 \x01(\t\"g\n\x19\x46\x65\x61tureNeighborhoodOpOpts\x12J\n\x15\x66\x65\x61ture_neighborhoods\x18\x01 \x03(\x0b\x32+.neighborhood.FeatureNeighborhoodTensorOptsb\x06proto3'
)



_PADDEDBATCHOPTS_PADTYPE = _descriptor.EnumDescriptor(
  name='PadType',
  full_name='neighborhood.PaddedBatchOpts.PadType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PADTYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAD_MAX_LEN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAD_FIXED_LEN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIXED_LEN', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=209,
  serialized_end=294,
)
_sym_db.RegisterEnumDescriptor(_PADDEDBATCHOPTS_PADTYPE)


_PADDEDBATCHOPTS = _descriptor.Descriptor(
  name='PaddedBatchOpts',
  full_name='neighborhood.PaddedBatchOpts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pad_type', full_name='neighborhood.PaddedBatchOpts.pad_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pad_dim', full_name='neighborhood.PaddedBatchOpts.pad_dim', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fixed_len', full_name='neighborhood.PaddedBatchOpts.fixed_len', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pad_value', full_name='neighborhood.PaddedBatchOpts.pad_value', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fixate_size', full_name='neighborhood.PaddedBatchOpts.fixate_size', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PADDEDBATCHOPTS_PADTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=294,
)


_FEATURENEIGHBORHOODTENSOROPTS_SYMBOLSANDMARKERS = _descriptor.Descriptor(
  name='SymbolsAndMarkers',
  full_name='neighborhood.FeatureNeighborhoodTensorOpts.SymbolsAndMarkers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_of_sentence', full_name='neighborhood.FeatureNeighborhoodTensorOpts.SymbolsAndMarkers.start_of_sentence', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_of_sentence', full_name='neighborhood.FeatureNeighborhoodTensorOpts.SymbolsAndMarkers.end_of_sentence', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symbols', full_name='neighborhood.FeatureNeighborhoodTensorOpts.SymbolsAndMarkers.symbols', index=2,
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
  serialized_start=669,
  serialized_end=757,
)

_FEATURENEIGHBORHOODTENSOROPTS = _descriptor.Descriptor(
  name='FeatureNeighborhoodTensorOpts',
  full_name='neighborhood.FeatureNeighborhoodTensorOpts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='neighborhood.FeatureNeighborhoodTensorOpts.input', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output', full_name='neighborhood.FeatureNeighborhoodTensorOpts.output', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='append_eos', full_name='neighborhood.FeatureNeighborhoodTensorOpts.append_eos', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_spelling_len', full_name='neighborhood.FeatureNeighborhoodTensorOpts.max_spelling_len', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_pronunciation_len', full_name='neighborhood.FeatureNeighborhoodTensorOpts.max_pronunciation_len', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_neighbors', full_name='neighborhood.FeatureNeighborhoodTensorOpts.max_neighbors', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_opts', full_name='neighborhood.FeatureNeighborhoodTensorOpts.batch_opts', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='split_output_on_space', full_name='neighborhood.FeatureNeighborhoodTensorOpts.split_output_on_space', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FEATURENEIGHBORHOODTENSOROPTS_SYMBOLSANDMARKERS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=757,
)


_FEATURENEIGHBORHOODOPOPTS = _descriptor.Descriptor(
  name='FeatureNeighborhoodOpOpts',
  full_name='neighborhood.FeatureNeighborhoodOpOpts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_neighborhoods', full_name='neighborhood.FeatureNeighborhoodOpOpts.feature_neighborhoods', index=0,
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
  serialized_start=759,
  serialized_end=862,
)

_PADDEDBATCHOPTS.fields_by_name['pad_type'].enum_type = _PADDEDBATCHOPTS_PADTYPE
_PADDEDBATCHOPTS_PADTYPE.containing_type = _PADDEDBATCHOPTS
_FEATURENEIGHBORHOODTENSOROPTS_SYMBOLSANDMARKERS.containing_type = _FEATURENEIGHBORHOODTENSOROPTS
_FEATURENEIGHBORHOODTENSOROPTS.fields_by_name['input'].message_type = _FEATURENEIGHBORHOODTENSOROPTS_SYMBOLSANDMARKERS
_FEATURENEIGHBORHOODTENSOROPTS.fields_by_name['output'].message_type = _FEATURENEIGHBORHOODTENSOROPTS_SYMBOLSANDMARKERS
_FEATURENEIGHBORHOODTENSOROPTS.fields_by_name['batch_opts'].message_type = _PADDEDBATCHOPTS
_FEATURENEIGHBORHOODOPOPTS.fields_by_name['feature_neighborhoods'].message_type = _FEATURENEIGHBORHOODTENSOROPTS
DESCRIPTOR.message_types_by_name['PaddedBatchOpts'] = _PADDEDBATCHOPTS
DESCRIPTOR.message_types_by_name['FeatureNeighborhoodTensorOpts'] = _FEATURENEIGHBORHOODTENSOROPTS
DESCRIPTOR.message_types_by_name['FeatureNeighborhoodOpOpts'] = _FEATURENEIGHBORHOODOPOPTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PaddedBatchOpts = _reflection.GeneratedProtocolMessageType('PaddedBatchOpts', (_message.Message,), {
  'DESCRIPTOR' : _PADDEDBATCHOPTS,
  '__module__' : 'feature_neighborhood_tensor_opts_pb2'
  # @@protoc_insertion_point(class_scope:neighborhood.PaddedBatchOpts)
  })
_sym_db.RegisterMessage(PaddedBatchOpts)

FeatureNeighborhoodTensorOpts = _reflection.GeneratedProtocolMessageType('FeatureNeighborhoodTensorOpts', (_message.Message,), {

  'SymbolsAndMarkers' : _reflection.GeneratedProtocolMessageType('SymbolsAndMarkers', (_message.Message,), {
    'DESCRIPTOR' : _FEATURENEIGHBORHOODTENSOROPTS_SYMBOLSANDMARKERS,
    '__module__' : 'feature_neighborhood_tensor_opts_pb2'
    # @@protoc_insertion_point(class_scope:neighborhood.FeatureNeighborhoodTensorOpts.SymbolsAndMarkers)
    })
  ,
  'DESCRIPTOR' : _FEATURENEIGHBORHOODTENSOROPTS,
  '__module__' : 'feature_neighborhood_tensor_opts_pb2'
  # @@protoc_insertion_point(class_scope:neighborhood.FeatureNeighborhoodTensorOpts)
  })
_sym_db.RegisterMessage(FeatureNeighborhoodTensorOpts)
_sym_db.RegisterMessage(FeatureNeighborhoodTensorOpts.SymbolsAndMarkers)

FeatureNeighborhoodOpOpts = _reflection.GeneratedProtocolMessageType('FeatureNeighborhoodOpOpts', (_message.Message,), {
  'DESCRIPTOR' : _FEATURENEIGHBORHOODOPOPTS,
  '__module__' : 'feature_neighborhood_tensor_opts_pb2'
  # @@protoc_insertion_point(class_scope:neighborhood.FeatureNeighborhoodOpOpts)
  })
_sym_db.RegisterMessage(FeatureNeighborhoodOpOpts)


# @@protoc_insertion_point(module_scope)
