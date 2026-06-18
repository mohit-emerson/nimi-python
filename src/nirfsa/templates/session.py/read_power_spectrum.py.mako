<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "read power spectrum" method based on the data type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}, reallocation_policy=enums.ReallocationPolicy.TO_GROW):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        if str(type(power_spectrum_data_array)).find("'numpy.ndarray'") != -1:
            expected_buffer_size = self.number_of_spectral_lines
            if len(power_spectrum_data_array) < expected_buffer_size:
                if reallocation_policy == enums.ReallocationPolicy.TO_GROW:
                    power_spectrum_data_array.resize(expected_buffer_size, refcheck=False)
                elif reallocation_policy == enums.ReallocationPolicy.DO_NOT_REALLOCATE:
                    raise ValueError("The length of power_spectrum_data_array is less than expected_buffer_size. ReallocationPolicy is set to DO_NOT_REALLOCATE.")

            if power_spectrum_data_array.dtype == numpy.float64:
                spectrum_info_struct = self._read_power_spectrum_f64(channel_list, power_spectrum_data_array, timeout)
                if spectrum_info_struct.number_of_spectral_lines < expected_buffer_size:
                    power_spectrum_data_array.resize(spectrum_info_struct.number_of_spectral_lines, refcheck=False)
                return spectrum_info_struct
            elif power_spectrum_data_array.dtype == numpy.float32:
                spectrum_info_struct = self._read_power_spectrum_f32(channel_list, power_spectrum_data_array, timeout)
                if spectrum_info_struct.number_of_spectral_lines < expected_buffer_size:
                    power_spectrum_data_array.resize(spectrum_info_struct.number_of_spectral_lines, refcheck=False)
                return spectrum_info_struct
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {} or {}".format(power_spectrum_data_array.dtype, numpy.float64, numpy.float32))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array of {} or {}".format(numpy.float64, numpy.float32))
