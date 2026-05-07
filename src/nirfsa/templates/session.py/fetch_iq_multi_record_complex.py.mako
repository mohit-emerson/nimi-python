<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "fetch IQ multi record complex" method based on the data type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        if data_type == numpy.complex128:
            return self._fetch_iq_multi_record_complex_f64(starting_record, number_of_records, number_of_samples, data, timeout)
        elif data_type == numpy.complex64:
            return self._fetch_iq_multi_record_complex_f32(starting_record, number_of_records, number_of_samples, data, timeout)
        elif data_type == numpy.int16:
            return self._fetch_iq_multi_record_complex_i16(starting_record, number_of_records, number_of_samples, data, timeout)
        else:
            raise TypeError("Unsupported data_type. Is {}, expected {} or {} or {}".format(data_type, numpy.complex128, numpy.complex64, numpy.int16))
