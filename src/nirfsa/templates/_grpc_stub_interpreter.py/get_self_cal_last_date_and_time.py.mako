<%page args="f, config, method_template"/>\
<%
    '''Renders get_self_cal_last_date_and_time for gRPC.
    The proto GetSelfCalLastDateAndTimeRequest field is named "self_calibration_step"
    (plain int64), not "self_calibration_step_raw", so the _raw suffix must not be used.'''
    import build.helper as helper
    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
        response = self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(vi=self._vi, self_calibration_step=self_calibration_step.value),
        )
        return response.year, response.month, response.day, response.hour, response.minute
