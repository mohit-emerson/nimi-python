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
        if spectrum_data_type == numpy.float64:
            return self._read_power_spectrum_f64(timeout)
        elif spectrum_data_type == numpy.float32:
            return self._read_power_spectrum_f32(timeout)
        else:
            raise TypeError("Unsupported spectrum_data_type. Is {}, expected {} or {}".format(spectrum_data_type, numpy.float64, numpy.float32))
