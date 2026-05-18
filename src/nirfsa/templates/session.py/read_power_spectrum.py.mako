<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "read power spectrum" method based on the data type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        if str(type(power_spectrum_data_array)).find("'numpy.ndarray'") != -1:
            if power_spectrum_data_array.dtype == numpy.float64:
                return self._read_power_spectrum_f64(channel_list, power_spectrum_data_array, timeout)
            elif power_spectrum_data_array.dtype == numpy.float32:
                return self._read_power_spectrum_f32(channel_list, power_spectrum_data_array, timeout)
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {} or {}".format(power_spectrum_data_array.dtype, numpy.float64, numpy.float32))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array of {} or {}".format(numpy.float64, numpy.float32))
