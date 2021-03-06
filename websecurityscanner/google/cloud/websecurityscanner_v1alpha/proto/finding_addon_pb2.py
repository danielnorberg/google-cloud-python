# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner_v1alpha/proto/finding_addon.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/websecurityscanner_v1alpha/proto/finding_addon.proto",
    package="google.cloud.websecurityscanner.v1alpha",
    syntax="proto3",
    serialized_options=_b(
        "\n+com.google.cloud.websecurityscanner.v1alphaB\021FindingAddonProtoP\001ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscanner"
    ),
    serialized_pb=_b(
        '\nAgoogle/cloud/websecurityscanner_v1alpha/proto/finding_addon.proto\x12\'google.cloud.websecurityscanner.v1alpha\x1a\x1cgoogle/api/annotations.proto"Q\n\x0fOutdatedLibrary\x12\x14\n\x0clibrary_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x17\n\x0flearn_more_urls\x18\x03 \x03(\t"?\n\x11ViolatingResource\x12\x14\n\x0c\x63ontent_type\x18\x01 \x01(\t\x12\x14\n\x0cresource_url\x18\x02 \x01(\t"/\n\x14VulnerableParameters\x12\x17\n\x0fparameter_names\x18\x01 \x03(\t"2\n\x03Xss\x12\x14\n\x0cstack_traces\x18\x01 \x03(\t\x12\x15\n\rerror_message\x18\x02 \x01(\tB\x9d\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x11\x46indingAddonProtoP\x01ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscannerb\x06proto3'
    ),
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)


_OUTDATEDLIBRARY = _descriptor.Descriptor(
    name="OutdatedLibrary",
    full_name="google.cloud.websecurityscanner.v1alpha.OutdatedLibrary",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="library_name",
            full_name="google.cloud.websecurityscanner.v1alpha.OutdatedLibrary.library_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="google.cloud.websecurityscanner.v1alpha.OutdatedLibrary.version",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="learn_more_urls",
            full_name="google.cloud.websecurityscanner.v1alpha.OutdatedLibrary.learn_more_urls",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=140,
    serialized_end=221,
)


_VIOLATINGRESOURCE = _descriptor.Descriptor(
    name="ViolatingResource",
    full_name="google.cloud.websecurityscanner.v1alpha.ViolatingResource",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="content_type",
            full_name="google.cloud.websecurityscanner.v1alpha.ViolatingResource.content_type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="resource_url",
            full_name="google.cloud.websecurityscanner.v1alpha.ViolatingResource.resource_url",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=223,
    serialized_end=286,
)


_VULNERABLEPARAMETERS = _descriptor.Descriptor(
    name="VulnerableParameters",
    full_name="google.cloud.websecurityscanner.v1alpha.VulnerableParameters",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parameter_names",
            full_name="google.cloud.websecurityscanner.v1alpha.VulnerableParameters.parameter_names",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=288,
    serialized_end=335,
)


_XSS = _descriptor.Descriptor(
    name="Xss",
    full_name="google.cloud.websecurityscanner.v1alpha.Xss",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="stack_traces",
            full_name="google.cloud.websecurityscanner.v1alpha.Xss.stack_traces",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="error_message",
            full_name="google.cloud.websecurityscanner.v1alpha.Xss.error_message",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=337,
    serialized_end=387,
)

DESCRIPTOR.message_types_by_name["OutdatedLibrary"] = _OUTDATEDLIBRARY
DESCRIPTOR.message_types_by_name["ViolatingResource"] = _VIOLATINGRESOURCE
DESCRIPTOR.message_types_by_name["VulnerableParameters"] = _VULNERABLEPARAMETERS
DESCRIPTOR.message_types_by_name["Xss"] = _XSS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OutdatedLibrary = _reflection.GeneratedProtocolMessageType(
    "OutdatedLibrary",
    (_message.Message,),
    dict(
        DESCRIPTOR=_OUTDATEDLIBRARY,
        __module__="google.cloud.websecurityscanner_v1alpha.proto.finding_addon_pb2",
        __doc__="""Information reported for an outdated library.
  
  
  Attributes:
      library_name:
          The name of the outdated library.
      version:
          The version number.
      learn_more_urls:
          URLs to learn more information about the vulnerabilities in
          the library.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.OutdatedLibrary)
    ),
)
_sym_db.RegisterMessage(OutdatedLibrary)

ViolatingResource = _reflection.GeneratedProtocolMessageType(
    "ViolatingResource",
    (_message.Message,),
    dict(
        DESCRIPTOR=_VIOLATINGRESOURCE,
        __module__="google.cloud.websecurityscanner_v1alpha.proto.finding_addon_pb2",
        __doc__="""Information regarding any resource causing the vulnerability such as
  JavaScript sources, image, audio files, etc.
  
  
  Attributes:
      content_type:
          The MIME type of this resource.
      resource_url:
          URL of this violating resource.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.ViolatingResource)
    ),
)
_sym_db.RegisterMessage(ViolatingResource)

VulnerableParameters = _reflection.GeneratedProtocolMessageType(
    "VulnerableParameters",
    (_message.Message,),
    dict(
        DESCRIPTOR=_VULNERABLEPARAMETERS,
        __module__="google.cloud.websecurityscanner_v1alpha.proto.finding_addon_pb2",
        __doc__="""Information about vulnerable request parameters.
  
  
  Attributes:
      parameter_names:
          The vulnerable parameter names.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.VulnerableParameters)
    ),
)
_sym_db.RegisterMessage(VulnerableParameters)

Xss = _reflection.GeneratedProtocolMessageType(
    "Xss",
    (_message.Message,),
    dict(
        DESCRIPTOR=_XSS,
        __module__="google.cloud.websecurityscanner_v1alpha.proto.finding_addon_pb2",
        __doc__="""Information reported for an XSS.
  
  
  Attributes:
      stack_traces:
          Stack traces leading to the point where the XSS occurred.
      error_message:
          An error message generated by a javascript breakage.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.Xss)
    ),
)
_sym_db.RegisterMessage(Xss)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
