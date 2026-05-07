# -*- coding: utf-8 -*-
# This file is generated from NI-RFSA API metadata version 26.5.0d9999
config = {
    'api_version': '26.5.0d9999',
    'c_function_prefix': 'niRFSA_',
    'close_function': 'Close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'acquisition'
    },
    'custom_types': [
        {
            'ctypes_type': 'struct_niRFSA_wfmInfo',
            'file_name': 'waveform_info',
            'grpc_name': 'WaveformInfo',
            'python_name': 'WaveformInfo'
        },
        {
            'ctypes_type': 'struct_niRFSA_spectrumInfo',
            'file_name': 'spectrum_info_type',
            'grpc_name': 'SpectrumInfoT',
            'python_name': 'SpectrumInfoT'
        }
    ],
    'driver_name': 'NI-RFSA',
    'enum_whitelist_prefix': [
        'RANGE_',
        'CLOCK_RATE_'
    ],
    'enum_whitelist_suffix': [
        '_TOWARDS_DUT'
    ],
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiRFSA',
    'init_function': 'InitWithOptions',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfsa',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFSA.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFSA_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'nirfsa',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'ports'
        },
        {
            'prefix': 'LO',
            'python_name': 'los'
        },
        {
            'prefix': '',
            'python_name': 'device_temperatures'
        },
        {
            'prefix': '',
            'python_name': 'channels'
        }
    ],
    'session_class_description': 'An NI-RFSA session to the NI-RFSA driver',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
