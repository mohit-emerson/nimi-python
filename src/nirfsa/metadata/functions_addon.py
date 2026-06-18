# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    'GetError': {
        'codegen_method': 'private',
        'is_error_handling': True,
    },
    'FetchIQSingleRecordComplexF32': {
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'fetch_iq_numpy_read_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_read_method',
            }
        ],
    },
    'FetchIQSingleRecordComplexF64': {
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'fetch_iq_numpy_read_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_read_method',
            }
        ],
    },
    'FetchIQSingleRecordComplexI16': {
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'fetch_iq_numpy_read_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_read_method',
            }
        ],
    },
    'FetchIQMultiRecordComplexF32': {
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'fetch_iq_numpy_read_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_read_method',
            }
        ],
    },
    'FetchIQMultiRecordComplexF64': {
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'fetch_iq_numpy_read_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_read_method',
            }
        ],
    },
    'FetchIQMultiRecordComplexI16': {
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'fetch_iq_numpy_read_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_read_method',
            }
        ],
    },
}
functions_additional_fetch_array_measurement = {
}

functions_additional_fetch_array_measurement_stats = {
}
