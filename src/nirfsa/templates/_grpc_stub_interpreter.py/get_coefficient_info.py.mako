<%page args="f, config, method_template"/>\
<%
    '''Retrieves coefficients from the gRPC call response and converts them to a list of dicts.'''
    import build.helper as helper
%>\

    def ${f['interpreter_name']}(self, channel_list):
        response = self._invoke(
            self._client.${f['name']},
            grpc_types.${f['name']}Request(vi=self._vi, channel_list=channel_list),
        )
        return [{'offset': c.offset, 'gain': c.gain} for c in response.coefficient_info]
