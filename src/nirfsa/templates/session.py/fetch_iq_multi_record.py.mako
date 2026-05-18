<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "fetch IQ multi record" method based on the data type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        if str(type(iq_data_arrays)).find("'numpy.ndarray'") != -1:
            if iq_data_arrays.ndim != 2:
                raise ValueError("iq_data_arrays must be a 2D numpy array (number_of_records x number_of_samples), but got {}D array".format(iq_data_arrays.ndim))
            if iq_data_arrays.dtype == numpy.complex128:
                return self._fetch_iq_multi_record_complex_f64(channel_list, starting_record, number_of_records, number_of_samples, iq_data_arrays, timeout)
            elif iq_data_arrays.dtype == numpy.complex64:
                return self._fetch_iq_multi_record_complex_f32(channel_list, starting_record, number_of_records, number_of_samples, iq_data_arrays, timeout)
            elif iq_data_arrays.dtype == numpy.int16:
                return self._fetch_iq_multi_record_complex_i16(channel_list, starting_record, number_of_records, number_of_samples, iq_data_arrays, timeout)
            else:
                raise TypeError("Unsupported datatype. Is {}, expected {} or {} or {}".format(iq_data_arrays.dtype, numpy.complex128, numpy.complex64, numpy.int16))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array of {} or {} or {}".format(numpy.complex128, numpy.complex64, numpy.int16))
