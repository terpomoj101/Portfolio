# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import stringComparision_pb2 as stringComparision__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in stringComparision_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class StringComparisionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StringComparision = channel.unary_unary(
                '/grpcProject.protos.StringComparision/StringComparision',
                request_serializer=stringComparision__pb2.EntryString.SerializeToString,
                response_deserializer=stringComparision__pb2.ResponseString.FromString,
                _registered_method=True)


class StringComparisionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StringComparision(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StringComparisionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StringComparision': grpc.unary_unary_rpc_method_handler(
                    servicer.StringComparision,
                    request_deserializer=stringComparision__pb2.EntryString.FromString,
                    response_serializer=stringComparision__pb2.ResponseString.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpcProject.protos.StringComparision', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('grpcProject.protos.StringComparision', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class StringComparision(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StringComparision(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpcProject.protos.StringComparision/StringComparision',
            stringComparision__pb2.EntryString.SerializeToString,
            stringComparision__pb2.ResponseString.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
