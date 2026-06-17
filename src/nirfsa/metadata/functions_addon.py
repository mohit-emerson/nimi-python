# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    'GetError': {
        'codegen_method': 'private',
        'is_error_handling': True,
    },
    'FetchIqSingleRecordComplexF32': {
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'fetch_iq_numpy_read_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_read_method',
            }
        ],
    },
    'FetchIqSingleRecordComplexF64': {
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'fetch_iq_numpy_read_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_read_method',
            }
        ],
    },
    'FetchIqSingleRecordComplexI16': {
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'fetch_iq_numpy_read_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_read_method',
            }
        ],
    },
    'FetchIqMultiRecordComplexF32': {
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'fetch_iq_numpy_read_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_read_method',
            }
        ],
    },
    'FetchIqMultiRecordComplexF64': {
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'fetch_iq_numpy_read_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_read_method',
            }
        ],
    },
    'FetchIqMultiRecordComplexI16': {
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
