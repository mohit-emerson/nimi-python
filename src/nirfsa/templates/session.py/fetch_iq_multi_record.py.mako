<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "fetch IQ multi record" method based on the data type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}, reallocation_policy=enums.ReallocationPolicy.TO_GROW):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        if str(type(iq_data_arrays)).find("'numpy.ndarray'") != -1:
            if iq_data_arrays.ndim != 2:
                raise ValueError("iq_data_arrays must be a 2D numpy array (number_of_records x number_of_samples), but got {}D array".format(iq_data_arrays.ndim))
            if iq_data_arrays.shape[0] < number_of_records:
                raise ValueError("iq_data_arrays must have at least {} rows (number_of_records), but has {}".format(number_of_records, iq_data_arrays.shape[0]))
            if iq_data_arrays.dtype == numpy.int16:
                expected_buffer_size = 2 * number_of_samples
            else:
                expected_buffer_size = number_of_samples

            if iq_data_arrays.shape[1] < expected_buffer_size:
                if reallocation_policy == enums.ReallocationPolicy.TO_GROW:
                    iq_data_arrays.resize((iq_data_arrays.shape[0], expected_buffer_size), refcheck=False)
                elif reallocation_policy == enums.ReallocationPolicy.DO_NOT_REALLOCATE:
                    raise ValueError("The width of iq_data_arrays is less than expected_buffer_size. ReallocationPolicy is set to DO_NOT_REALLOCATE.")

            if iq_data_arrays.dtype == numpy.complex128:
                wfm_info_struct = self._fetch_iq_multi_record_complex_f64(channel_list, starting_record, number_of_records, iq_data_arrays, timeout)
                if wfm_info_struct.actual_samples < number_of_samples:
                    iq_data_arrays.resize((iq_data_arrays.shape[0], wfm_info_struct.actual_samples), refcheck=False)
                return wfm_info_struct
            elif iq_data_arrays.dtype == numpy.complex64:
                wfm_info_struct = self._fetch_iq_multi_record_complex_f32(channel_list, starting_record, number_of_records, iq_data_arrays, timeout)
                if wfm_info_struct.actual_samples < number_of_samples:
                    iq_data_arrays.resize((iq_data_arrays.shape[0], wfm_info_struct.actual_samples), refcheck=False)
                return wfm_info_struct
            elif iq_data_arrays.dtype == numpy.int16:
                wfm_info_struct = self._fetch_iq_multi_record_complex_i16(channel_list, starting_record, number_of_records, iq_data_arrays, timeout)
                if wfm_info_struct.actual_samples < number_of_samples:
                    iq_data_arrays.resize((iq_data_arrays.shape[0], 2 * wfm_info_struct.actual_samples), refcheck=False)
                return wfm_info_struct
            else:
                raise TypeError("Unsupported datatype. Is {}, expected {} or {} or {}".format(iq_data_arrays.dtype, numpy.complex128, numpy.complex64, numpy.int16))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array of {} or {} or {}".format(numpy.complex128, numpy.complex64, numpy.int16))
