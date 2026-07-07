<%page args="f, config, method_template"/>\
<%
    '''Retrieves scaling coefficients from the gRPC response, avoiding reserved fields absent in the proto.'''
    import build.helper as helper
%>\

    def ${f['interpreter_name']}(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.${f['name']},
            grpc_types.${f['name']}Request(vi=self._vi, channel_list=channel_list),
        )
        return [coefficient_info_type.CoefficientInfo(offset=x.offset, gain=x.gain) for x in response.coefficient_info]
