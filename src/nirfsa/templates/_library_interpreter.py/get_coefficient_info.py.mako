<%page args="f, config, method_template"/>\
<%
    '''Gets coefficients from the driver. Queries the number of coefficient sets, retrieves the coefficient data into a pre-allocated buffer.'''
    import build.helper as helper
    c_function_name = config['c_function_prefix'] + f['name']
%>\

    def ${f['interpreter_name']}(self, channel_list):
        # First call with arraySize=0 to get number of coefficient sets
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        array_size_ctype = _visatype.ViInt32(0)  # case S150
        coefficient_info_ctype = None  # case B580
        number_of_coefficient_sets_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.${c_function_name}(vi_ctype, channel_list_ctype, array_size_ctype, coefficient_info_ctype, None if number_of_coefficient_sets_ctype is None else (ctypes.pointer(number_of_coefficient_sets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        # Second call to get actual data
        array_size = number_of_coefficient_sets_ctype.value
        array_size_ctype = _visatype.ViInt32(array_size)  # case S150
        coefficient_info_ctype = (_complextype.niRFSA_coefficientInfo * array_size)()  # case B590
        error_code = self._library.${c_function_name}(vi_ctype, channel_list_ctype, array_size_ctype, coefficient_info_ctype, None if number_of_coefficient_sets_ctype is None else (ctypes.pointer(number_of_coefficient_sets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [{'offset': c.offset, 'gain': c.gain} for c in coefficient_info_ctype]
