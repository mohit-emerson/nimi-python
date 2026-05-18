<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "fetch IQ single record" method based on the data type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        if str(type(iq_data_array)).find("'numpy.ndarray'") != -1:
            if iq_data_array.dtype == numpy.complex128:
                return self._fetch_iq_single_record_complex_f64(channel_list, record_number, number_of_samples, iq_data_array, timeout)
            elif iq_data_array.dtype == numpy.complex64:
                return self._fetch_iq_single_record_complex_f32(channel_list, record_number, number_of_samples, iq_data_array, timeout)
            elif iq_data_array.dtype == numpy.int16:
                return self._fetch_iq_single_record_complex_i16(channel_list, record_number, number_of_samples, iq_data_array, timeout)
            else:
                raise TypeError("Unsupported datatype. Is {}, expected {} or {} or {}".format(iq_data_array.dtype, numpy.complex128, numpy.complex64, numpy.int16))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array of {} or {} or {}".format(numpy.complex128, numpy.complex64, numpy.int16))
