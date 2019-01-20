# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: connect.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='connect.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rconnect.proto\"\x17\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x17\n\x08ReplyInt\x12\x0b\n\x03per\x18\x01 \x01(\x05\x32+\n\x07\x43onnect\x12 \n\x07persent\x12\x08.Request\x1a\t.ReplyInt\"\x00\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Request.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=17,
  serialized_end=40,
)


_REPLYINT = _descriptor.Descriptor(
  name='ReplyInt',
  full_name='ReplyInt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='per', full_name='ReplyInt.per', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=42,
  serialized_end=65,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['ReplyInt'] = _REPLYINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'connect_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

ReplyInt = _reflection.GeneratedProtocolMessageType('ReplyInt', (_message.Message,), dict(
  DESCRIPTOR = _REPLYINT,
  __module__ = 'connect_pb2'
  # @@protoc_insertion_point(class_scope:ReplyInt)
  ))
_sym_db.RegisterMessage(ReplyInt)



_CONNECT = _descriptor.ServiceDescriptor(
  name='Connect',
  full_name='Connect',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=67,
  serialized_end=110,
  methods=[
  _descriptor.MethodDescriptor(
    name='persent',
    full_name='Connect.persent',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_REPLYINT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONNECT)

DESCRIPTOR.services_by_name['Connect'] = _CONNECT

# @@protoc_insertion_point(module_scope)
