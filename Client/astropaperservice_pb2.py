# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: astropaperservice.proto

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
  name='astropaperservice.proto',
  package='astropaper',
  syntax='proto3',
  serialized_pb=_b('\n\x17\x61stropaperservice.proto\x12\nastropaper\"$\n\x10WallpaperRequest\x12\x10\n\x08quantity\x18\x01 \x01(\x05\"!\n\x0cSetupRequest\x12\x11\n\twallpaper\x18\x01 \x01(\t\"\x19\n\x08\x41PIReply\x12\r\n\x05reply\x18\x01 \x01(\t2\xa0\x01\n\x11\x41stroPaperService\x12G\n\x0fGetNewWallpaper\x12\x1c.astropaper.WallpaperRequest\x1a\x14.astropaper.APIReply\"\x00\x12\x42\n\x0eSetupWallpaper\x12\x18.astropaper.SetupRequest\x1a\x14.astropaper.APIReply\"\x00\x62\x06proto3')
)




_WALLPAPERREQUEST = _descriptor.Descriptor(
  name='WallpaperRequest',
  full_name='astropaper.WallpaperRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantity', full_name='astropaper.WallpaperRequest.quantity', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=39,
  serialized_end=75,
)


_SETUPREQUEST = _descriptor.Descriptor(
  name='SetupRequest',
  full_name='astropaper.SetupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wallpaper', full_name='astropaper.SetupRequest.wallpaper', index=0,
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
  serialized_start=77,
  serialized_end=110,
)


_APIREPLY = _descriptor.Descriptor(
  name='APIReply',
  full_name='astropaper.APIReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='astropaper.APIReply.reply', index=0,
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
  serialized_start=112,
  serialized_end=137,
)

DESCRIPTOR.message_types_by_name['WallpaperRequest'] = _WALLPAPERREQUEST
DESCRIPTOR.message_types_by_name['SetupRequest'] = _SETUPREQUEST
DESCRIPTOR.message_types_by_name['APIReply'] = _APIREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WallpaperRequest = _reflection.GeneratedProtocolMessageType('WallpaperRequest', (_message.Message,), dict(
  DESCRIPTOR = _WALLPAPERREQUEST,
  __module__ = 'astropaperservice_pb2'
  # @@protoc_insertion_point(class_scope:astropaper.WallpaperRequest)
  ))
_sym_db.RegisterMessage(WallpaperRequest)

SetupRequest = _reflection.GeneratedProtocolMessageType('SetupRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETUPREQUEST,
  __module__ = 'astropaperservice_pb2'
  # @@protoc_insertion_point(class_scope:astropaper.SetupRequest)
  ))
_sym_db.RegisterMessage(SetupRequest)

APIReply = _reflection.GeneratedProtocolMessageType('APIReply', (_message.Message,), dict(
  DESCRIPTOR = _APIREPLY,
  __module__ = 'astropaperservice_pb2'
  # @@protoc_insertion_point(class_scope:astropaper.APIReply)
  ))
_sym_db.RegisterMessage(APIReply)



_ASTROPAPERSERVICE = _descriptor.ServiceDescriptor(
  name='AstroPaperService',
  full_name='astropaper.AstroPaperService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=140,
  serialized_end=300,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetNewWallpaper',
    full_name='astropaper.AstroPaperService.GetNewWallpaper',
    index=0,
    containing_service=None,
    input_type=_WALLPAPERREQUEST,
    output_type=_APIREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetupWallpaper',
    full_name='astropaper.AstroPaperService.SetupWallpaper',
    index=1,
    containing_service=None,
    input_type=_SETUPREQUEST,
    output_type=_APIREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ASTROPAPERSERVICE)

DESCRIPTOR.services_by_name['AstroPaperService'] = _ASTROPAPERSERVICE

# @@protoc_insertion_point(module_scope)