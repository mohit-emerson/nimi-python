<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "fetch IQ single record complex" method based on the data type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        if waveform_data_type == numpy.complex128:
            return self._fetch_iq_single_record_complex_f64(record_number, number_of_samples, waveform_data, timeout)
        elif waveform_data_type == numpy.complex64:
            return self._fetch_iq_single_record_complex_f32(record_number, number_of_samples, waveform_data, timeout)
        elif waveform_data_type == numpy.int16:
            return self._fetch_iq_single_record_complex_i16(record_number, number_of_samples, waveform_data, timeout)
        else:
            raise TypeError("Unsupported waveform_data_type. Is {}, expected {} or {} or {}".format(waveform_data_type, numpy.complex128, numpy.complex64, numpy.int16))
