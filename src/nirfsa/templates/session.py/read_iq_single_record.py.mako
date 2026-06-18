<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "read IQ single record" method based on the data type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}, reallocation_policy=enums.ReallocationPolicy.TO_GROW):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        if str(type(iq_data_array)).find("'numpy.ndarray'") != -1:
            if iq_data_array.dtype == numpy.complex128:
                expected_buffer_size = self.number_of_samples
                if len(iq_data_array) < expected_buffer_size:
                    if reallocation_policy == enums.ReallocationPolicy.TO_GROW:
                        iq_data_array.resize(expected_buffer_size, refcheck=False)
                    elif reallocation_policy == enums.ReallocationPolicy.DO_NOT_REALLOCATE:
                        raise ValueError("The length of iq_data_array is less than expected_buffer_size. ReallocationPolicy is set to DO_NOT_REALLOCATE.")

                wfm_info_struct = self._read_iq_single_record_complex_f64(channel_list, iq_data_array, timeout)
                if wfm_info_struct.actual_samples < expected_buffer_size:
                    iq_data_array.resize(wfm_info_struct.actual_samples, refcheck=False)
                return wfm_info_struct
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {}".format(iq_data_array.dtype, numpy.complex128))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array of {}".format(numpy.complex128))
