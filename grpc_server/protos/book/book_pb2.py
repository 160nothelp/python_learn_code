# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbook.proto\"\xb2\x01\n\x04\x42ook\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x04type\x18\x02 \x01(\x0e\x32\t.BookType\x12\x1d\n\x04tags\x18\x03 \x03(\x0b\x32\x0f.Book.TagsEntry\x12\x12\n\x08username\x18\x04 \x01(\tH\x00\x12\x12\n\x08realname\x18\x05 \x01(\tH\x00\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x42\x0f\n\rauthor_one_of\"\x1f\n\x0f\x42ookListRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\"(\n\x10\x42ookListResponse\x12\x14\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x05.Book*\x1f\n\x08\x42ookType\x12\t\n\x05STORY\x10\x00\x12\x08\n\x04LOVE\x10\x01\x32>\n\x0b\x42ookService\x12/\n\x08\x42ookList\x12\x10.BookListRequest\x1a\x11.BookListResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'book_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BOOK_TAGSENTRY']._loaded_options = None
  _globals['_BOOK_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_BOOKTYPE']._serialized_start=270
  _globals['_BOOKTYPE']._serialized_end=301
  _globals['_BOOK']._serialized_start=15
  _globals['_BOOK']._serialized_end=193
  _globals['_BOOK_TAGSENTRY']._serialized_start=133
  _globals['_BOOK_TAGSENTRY']._serialized_end=176
  _globals['_BOOKLISTREQUEST']._serialized_start=195
  _globals['_BOOKLISTREQUEST']._serialized_end=226
  _globals['_BOOKLISTRESPONSE']._serialized_start=228
  _globals['_BOOKLISTRESPONSE']._serialized_end=268
  _globals['_BOOKSERVICE']._serialized_start=303
  _globals['_BOOKSERVICE']._serialized_end=365
# @@protoc_insertion_point(module_scope)
