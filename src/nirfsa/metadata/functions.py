# -*- coding: utf-8 -*-
# This file is generated from NI-RFSA API metadata version 26.5.0d9999
functions = {
    'Abort': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Stops an acquisition previously started with the nirfsa_Initiate function or the nirfsa_ReadPowerSpectrumF64 function. \n                \n                You can also use the nirfsa_Abort function to stop a self-calibration. Calling this function is optional, unless you want to stop an acquisition before it is complete or you are continuously acquiring data.\n\n                You can stop the following kinds of acquisitions:\n\n                - Triggered spectrum acquisitions that have not yet been triggered\n                - Multispan acquisitions in progress\n                - Average spectrum acquisitions in progress\n                - Single-record spectrum acquisitions in progress\n                - Streaming in progress\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CalAdjustCalTonePower': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the calibration tone power during calibration tone amplitude calibration. \n                \n                You must call the nirfsa_Initiate function before calling this function.\n\n                **Supported Devices**: PXIe-5693'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify 0 as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the calibration tone power, in dBm, for the current device setting.'
                },
                'name': 'measurement',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CalAdjustDeviceGain': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Records measured gain information that is gathered during the Reference Level Calibration step and IF Attenuation Calibration step.\n\n                This function internally queries the attributes you set, and you must commit all attributes appropriate for your device calibration procedure prior to calling this function. Refer to ni.com/manuals for the most recent version of the calibration procedure for your device.\n\n                Call this function immediately after a measurement is made and while the device under test (DUT) is still in the same state as it was during the measurement.\n\n                **Supported Devices**: PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify 0 as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the RF frequency, in Hz, of the measurement taken.'
                },
                'name': 'frequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the gain measurement, in dB.'
                },
                'name': 'gain',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CalAdjustDownconverterGain': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Records measured gain information that is gathered during the Reference Level Calibration step and IF Attenuation Calibration step.\n\n                This function internally queries the attributes you set, and you must set and commit the following attributes prior to calling this function.\n\n                - NIRFSA_ATTR_CAL_RF_ELECTRONIC_ATTENUATION_INDEX (This attribute is required only when the NIRFSA_ATTR_CAL_RF_PATH_SELECTION attribute is set to NIRFSA_VAL_EXT_CAL_RF_BAND_1.)\n                - NIRFSA_ATTR_CAL_RF_MECHANICAL_ATTENUATION_INDEX\n                - NIRFSA_ATTR_CAL_IF_ATTENUATION_TABLE_SELECTION\n                - NIRFSA_ATTR_CAL_IF_ATTENUATION_INDEX\n                - NIRFSA_ATTR_CAL_IF_FILTER_SELECTION\n                - NIRFSA_ATTR_CHANNEL_COUPLING\n                - NIRFSA_ATTR_RF_PREAMP_ENABLED\n\n                Call this function immediately after a measurement is made and while the device under test (DUT) is still in the same state as it was during the measurement.\n\n                **Supported Devices**: PXIe-5603/5605/5606'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitExtCal function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the RF frequency, in Hz, of the measurement taken.'
                },
                'name': 'frequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the gain measurement, in dB.'
                },
                'name': 'gain',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CalAdjustIfAttenuationCalibration': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the IF attenuation settings.\n\n                **Supported Devices**: PXIe-5601, PXIe-5694'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the IF filter used by the downconverter.\n\n                        |Value                                     |Description                                             |\n                        |:------------------------------------|:--------------------------------------------|\n                        | NIRFSA_VAL_187_5_MHZ_NARROW (1400)  | Uses the 187.5 MHz wide bandwidth filter.   |\n                        | NIRFSA_VAL_187_5_MHZ_NARROW (1401) | Uses the 187.5 MHz narrow bandwidth filter. |\n                        | NIRFSA_VAL_53_MHZ (1402)            | Uses the 53 MHz filter.                     |\n                        | NIRFSA_VAL_BYPASS (1403)            | Bypasses the IF filter.                     |'
                },
                'name': 'ifFilter',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of attenuators to use during the IF attenuation adjustment.'
                },
                'name': 'numberOfAttenuators',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the IF attenuator settings for the measurement. The first element in the array corresponds with IF1, the next element corresponds to IF2, and so on.'
                },
                'name': 'attenuatorSettings',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the relevant measurement taken for the current configuration.'
                },
                'name': 'measurement',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CalAdjustIfResponseCalibration': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the IF response settings.\n\n                **Supported Devices**: PXIe-5601, PXIe-5694'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the IF filter used by the downconverter.\n\n                        |Value                                     |Description                                           |\n                        |:------------------------------------|:------------------------------------------|\n                        | NIRFSA_VAL_187_5_MHZ_NARROW (1400)   | Uses the 187.5 MHz wide bandwidth path.   |\n                        | NIRFSA_VAL_187_5_MHZ_NARROW (1401) | Uses the 187.5 MHz narrow bandwidth path. |\n                        | NIRFSA_VAL_53_MHZ (1402)            | Uses the 53 MHz path.                     |\n                        | NIRFSA_VAL_BYPASS (1403)            | Bypasses the IF path.                     |'
                },
                'name': 'ifFilter',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the RF frequency, in Hz, used during the IF response adjustment.'
                },
                'name': 'rfFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the bandwidth, in Hz, to use for the IF response adjustment.'
                },
                'name': 'bandWidth',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of measurements to make.'
                },
                'name': 'numberOfMeasurements',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the relevant measurements taken for each IF filter configuration, in dB.'
                },
                'name': 'measurements',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CalAdjustLoExportCalibration': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'LO export calibration measures the PXIe-5603/5605 LO output power level.\n\n                The LO output power measurements are taken from the PXIe-5653 module. In MIMO applications, when the LO is exported from one PXIe-5603/5605 module to another subsequent PXIe-5603/5605, an output power signal of approximately +7 dBm is expected on each LO connector (LO1, LO2, and LO3). This function records the LO attenuation that results in an output power of +7 dBm (or greater) on the three LO output terminals.\n\n                The PXIe-5665/5668 uses three LOs, but only LO1 is variable in frequency. This function accepts an array of frequencies and attenuations; however, for LO2 and LO3, this array must have only one element because these two LO sources operate only at one frequency. LO1 can have multiple values for specific frequencies.\n\n                **Supported Devices**: PXIe-5603/5605/5606'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitExtCal function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the LO source to use for the LO export calibration.\n\n                        |Value                                   |Description                                                                    |\n                        |:----------------------------------|:-------------------------------------------------------------------|\n                        | NIRFSA_VAL_EXT_CAL_LO1  (2200) | Selects LO1, which is the 3.2 GHz to 8.3 GHz variable signal path. |\n                        | NIRFSA_VAL_EXT_CAL_LO2 (2201) | Selects LO2, which is the 4 GHz signal path.                       |\n                        | NIRFSA_VAL_EXT_CAL_LO3  (2202) | Selects LO3, which is the 800 MHz signal path.                     |'
                },
                'name': 'loNumber',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the length of the **frequencies** and **NIRFSA_ATTR_LO_ATTENUATION** arrays.'
                },
                'name': 'numberOfFrequencyPoints',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies frequencies for the LO output power measurement. The length of this array equals the **NIRFSA_ATTR_NUMBER_OF_FREQUENCY_POINTS** parameter.'
                },
                'name': 'frequencyPoints',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the attenuation value of the corresponding frequency point that results in a +7 dBm output signal on the respective LO OUT connector. The length of this array equals the **NIRFSA_ATTR_NUMBER_OF_FREQUENCY_POINTS** parameter.'
                },
                'name': 'loAttenuation',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CalAdjustRefLevelCalibration': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Writes the reference level calibration data settings to the driver.\n\n                **Supported Devices**: PXIe-5601'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether the reference level calibration data being used is the default configuration data or the mechanical relay disabled configuration data.\n\n                        |Value                                                          |Description                                                                                                                                                           |\n                        |:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|\n                        | NIRFSA_VAL_EXT_CAL_DEFAULT (1800)                        | The data is the default configuration data.                                                                                                               |\n                        | NIRFSA_VAL_EXT_CAL_MECHANICAL_ATTENUATOR_DISABLED (1801) | The data is the configuration data when the mechanical relay is disabled. Use this option to save uncalibrated measurements for more advanced operations. |'
                },
                'name': 'referenceLevelDataType',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the RF band used during the reference level calibration.\n\n                        |Value                      |Description                             |\n                        |:---------------------|:----------------------------|\n                        | NIRFSA_VAL_EXT_CAL_RF_BAND_1 | The RF band 1 path is used. |\n                        | NIRFSA_VAL_EXT_CAL_RF_BAND_2| The RF band 2 path is used. |\n                        | NIRFSA_VAL_EXT_CAL_RF_BAND_3 | The RF band 3 path is used. |\n                        | NIRFSA_VAL_EXT_CAL_RF_BAND_4 | The RF band 4 path is used. |'
                },
                'name': 'rfBand',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which attenuation table you are using. Valid values are 0 and 1.'
                },
                'name': 'attenuatorTableNumber',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the frequency for the reference level adjustment.'
                },
                'name': 'frequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the relevant measurement taken for the current configuration.'
                },
                'name': 'measurement',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CalSetTemperature': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Writes the calibration temperature to the driver.\n\n                **Supported Devices**: PXIe-5601'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the calibration temperature, in degrees Celsius.'
                },
                'name': 'temperature',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ChangeExtCalPassword': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Changes the password that is required to initialize an external calibration session.\n\n                **Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the old (current) external calibration password.\n\n                        The maximum length of the password varies by device.'
                },
                'name': 'oldPassword',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the new (desired) external calibration password.\n\n                        The maximum length of the password varies by device.'
                },
                'name': 'newPassword',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CheckAcquisitionStatus': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Checks the status of the acquisition. \n                \n                Use this function to check for any errors that may occur during signal acquisition or to check whether the device has completed the acquisition operation.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/hardware-state-diagram.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns signal acquisition status.\n\n                        |Value          |Description                                     |\n                        |:---------|:------------------------------------|\n                        | VI_TRUE  | Signal acquisition is complete.     |\n                        | VI_FALSE | Signal acquisition is not complete. |'
                },
                'name': 'isDone',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ClearError': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Clears the error information associated with the session. \n                \n                If you pass VI_NULL for the NIRFSA_ATTR_VI parameter, this function clears the error information for the current execution thread.\n\n                ----\n                **Note**\n                The nirfsa_GetError function clears the error information after it is retrieved. A call to the nirfsa_ClearError function is necessary only when a call to the nirfsa_GetError function is not used to retrieve error information.\n\n                ----\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5840'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ClearSelfCalibrateRange': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Clears the data obtained from the nirfsa_SelfCalibrateRange function.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'Close': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Closes the session to the device.\n\n                If you close a session that has Soft Front Panel (SFP) session access enabled, any application connected to the shared device session is no longer usable. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about using SFP session access.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'grpc_name': 'Close',
        'included_in_proto': True,
        'is_error_handling': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': '_close',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'CloseCalibrationStep': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Closes the current calibration step.\n\n                **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CloseExtCal': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Closes an NI-RFSA external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM.\n\n                **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies how to use the calibration values from this session as the session is closed.\n\n                        |Value                           |Description                                                                         |\n                        |:--------------------------|:------------------------------------------------------------------------|\n                        | NIRFSA_VAL_EXT_CAL_ABORT  | The old calibration constants are kept, and the new ones are discarded. |\n                        | NIRFSA_VAL_EXT_CAL_COMMIT | The new calibration constants are stored in the EEPROM.                 |'
                },
                'name': 'action',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CloseExternalAlignment': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Closes an NI-RFSA external alignment session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM.\n\n                **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitializeExternalAlignment function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies how to use the alignment values from this session as the session is closed.\n\n                        |Value                           |Description                                                                       |\n                        |:--------------------------|:----------------------------------------------------------------------|\n                        | NIRFSA_VAL_EXT_CAL_ABORT  | The old alignment constants are kept, and the new ones are discarded. |\n                        |  NIRFSA_VAL_EXT_CAL_COMMIT| The new alignment constants are stored in the EEPROM.                 |'
                },
                'name': 'action',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CloseExternalAlignmentStep': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Closes an EEPROM-specific external alignment step.\n\n                **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitializeExternalAlignment function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'Commit': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Commits settings to hardware. \n                \n                Calling this function is optional. Settings are automatically committed to hardware when you call the nirfsa_Initiate function, the nirfsa_ReadIqSingleRecordComplexF64 function, or the nirfsa_ReadPowerSpectrumF64 function.\n\n                ----\n                **Note**\n                This function does not wait for settling time, unlike the nirfsa_Initiate function.\n\n                ----\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/hardware-state-diagram.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureAcquisitionType': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures whether the session acquires I/Q data or computes a power spectrum over the specified frequency range.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Configures the type of acquisition.\n\n                        | Value                    | Description                                                                       |\n                        |:--------------------|:-----------------------------------------------------------------------|\n                        | NIRFSA_VAL_IQ       | Configures the driver for I/Q acquisitions. This value is the default. |\n                        | NIRFSA_VAL_SPECTRUM | Configures the driver for spectrum acquisitions.                       |'
                },
                'name': 'acquisitionType',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDeembeddingTableInterpolationLinear': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Selects the linear interpolation method. \n                \n                If the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the format of parameters to interpolate.\n\n                        %enum_table{format}'
                },
                'name': 'format',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDeembeddingTableInterpolationNearest': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Selects the nearest interpolation method. \n                \n                NI-RFSA uses the parameters of the table nearest to the carrier frequency for de-embedding.\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDeembeddingTableInterpolationSpline': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Selects the spline interpolation method. \n                \n                If the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDigitalEdgeAdvanceTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for a digital edge Advance Trigger. \n                \n                The Advance Trigger indicates where a new record begins.\n\n                ----\n                **Note**\n                 This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n                ----\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the source of the digital edge for the Advance Trigger.\n\n                        | Value                                           | Description                                                                                                                                                                                                                |\n                        |:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n                        | NIRFSA_VAL_PFI0_STR ('PFI0')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                            |\n                        | NIRFSA_VAL_PFI1_STR ('PFI1')               | The trigger is received on PFI 1.                                                                                                                                                                              |\n                        | NIRFSA_VAL_PXI_TRIG0_STR ('PXI_Trig0')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG1_STR ('PXI_Trig1')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG2_STR ('PXI_Trig2')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG3_STR ('PXI_Trig3')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG4_STR ('PXI_Trig4')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG5_STR ('PXI_Trig5')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG6_STR ('PXI_Trig6')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG7_STR ('PXI_Trig7')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_STAR_STR ('PXI_STAR')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                             |\n                        | NIRFSA_VAL_PXIE_DSTARB_STR ('PXIE_DSTARB') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |\n                        | NIRFSA_VAL_TIMER_EVENT_STR ('TimerEvent')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |\n                        | NIRFSA_VAL_DIO_PFI0_STR ('PFI0')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI1_STR('PFI1')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI2_STR ('PFI2')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI3_STR ('PFI3')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI4_STR ('PFI4')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI5_STR ('PFI5')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI6_STR ('PFI6')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI7_STR ('PFI7')               | The trigger is received on PFI 7 of the DIO Terminal. |"
                },
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the trigger edge to detect. The default value is NIRFSA_VAL_RISING_EDGE.\n\n                        | Value                              | Description                                |\n                        |:------------------------------|:--------------------------------|\n                        | NIRFSA_VAL_RISING_EDGE (900)  | NI-RFSA detects a rising edge.  |\n                        | NIRFSA_VAL_FALLING_EDGE (901) | NI-RFSA detects a falling edge. |'
                },
                'name': 'edge',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDigitalEdgeRefTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for a digital edge Reference Trigger to mark a reference point within the record.\n\n                You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.\n\n                ----\n                **Note**\n                 The PXIe-5644/5645/5646 does not support the NI-TClk API.\n\n                ----\n\n                ----\n                **Note**\n                 This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n                ----\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the source of the digital edge for the Reference trigger.\n\n                        |Value                                            |Description                                                                                                                                                                                                                               |\n                        |:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n                        | NIRFSA_VAL_PFI0_STR ('PFI0')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                                           |\n                        | NIRFSA_VAL_PFI1_STR ('PFI1')               | The trigger is received on PFI 1.                                                                                                                                                                                             |\n                        | NIRFSA_VAL_PXI_TRIG0_STR ('PXI_Trig0')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                                |\n                        | NIRFSA_VAL_PXI_TRIG1_STR ('PXI_Trig1')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                                |\n                        | NIRFSA_VAL_PXI_TRIG2_STR ('PXI_Trig2')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                                |\n                        | NIRFSA_VAL_PXI_TRIG3_STR ('PXI_Trig3')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                                |\n                        | NIRFSA_VAL_PXI_TRIG4_STR ('PXI_Trig4')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                                |\n                        | NIRFSA_VAL_PXI_TRIG5_STR ('PXI_Trig5')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                                |\n                        | NIRFSA_VAL_PXI_TRIG6_STR ('PXI_Trig6')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                                |\n                        | NIRFSA_VAL_PXI_TRIG7_STR ('PXI_Trig7')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                                |\n                        | NIRFSA_VAL_PXI_STAR_STR ('PXI_STAR')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                                            |\n                        | NIRFSA_VAL_PXIE_DSTARB_STR ('PXIE_DSTARB') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |\n                        | NIRFSA_VAL_TIMER_EVENT_STR ('TimerEvent')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |\n                        | NIRFSA_VAL_DIO_PFI0_STR ('PFI0')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI1_STR('PFI1')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI2_STR ('PFI2')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI3_STR ('PFI3')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI4_STR ('PFI4')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI5_STR ('PFI5')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI6_STR ('PFI6')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI7_STR ('PFI7')               | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                          |"
                },
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the trigger edge to detect. The default value is NIRFSA_VAL_RISING_EDGE.\n\n                        |Value                               |Description                                 |\n                        |:------------------------------|:--------------------------------|\n                        | NIRFSA_VAL_RISING_EDGE (900)  | NI-RFSA detects a rising edge.  |\n                        | NIRFSA_VAL_FALLING_EDGE (901) | NI-RFSA detects a falling edge. |'
                },
                'name': 'edge',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.'
                },
                'name': 'pretriggerSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for a digital edge Start Trigger at the beginning of the acquisition.\n\n                You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.\n\n                ----\n                **Note**\n                 The PXIe-5644/5645/5646 does not support the NI-TClk API.\n\n                ----\n\n                ----\n                **Note**\n                 This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n                ----\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the source of the digital edge for the Start Trigger.\n\n                        | Value                                           | Description                                                                                                                                                                                                               |\n                        |:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n                        | NIRFSA_VAL_PFI0_STR ('PFI0')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                            |\n                        | NIRFSA_VAL_PFI1_STR ('PFI1')               | The trigger is received on PFI 1.                                                                                                                                                                              |\n                        | NIRFSA_VAL_PXI_TRIG0_STR ('PXI_Trig0')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG1_STR ('PXI_Trig1')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG2_STR ('PXI_Trig2')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG3_STR ('PXI_Trig3')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG4_STR ('PXI_Trig4')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG5_STR ('PXI_Trig5')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG6_STR ('PXI_Trig6')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_TRIG7_STR ('PXI_Trig7')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                 |\n                        | NIRFSA_VAL_PXI_STAR_STR ('PXI_STAR')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                             |\n                        | NIRFSA_VAL_PXIE_DSTARB_STR ('PXIE_DSTARB') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |\n                        | NIRFSA_VAL_TIMER_EVENT_STR ('TimerEvent')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |\n                        | NIRFSA_VAL_DIO_PFI0_STR ('PFI1')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI1_STR('PFI2')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI2_STR ('PFI3')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI3_STR ('PFI4')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI4_STR ('PFI5')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI5_STR ('PFI6')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI6_STR ('PFI7')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI7_STR ('PFI8')               | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                          |"
                },
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the trigger edge to detect. The default value is NIRFSA_VAL_RISING_EDGE.\n\n                        | Value                              | Description                                |\n                        |:------------------------------|:--------------------------------|\n                        | NIRFSA_VAL_RISING_EDGE (900)  | NI-RFSA detects a rising edge.  |\n                        | NIRFSA_VAL_FALLING_EDGE (901) | NI-RFSA detects a falling edge. |'
                },
                'name': 'edge',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureIqCarrierFrequency': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the `carrier frequency <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/fund-carrierwave.html>`_ of the RF vector signal analyzer hardware for an I/Q acquisition. \n                \n                The carrier frequency is the center frequency of the I/Q acquisition.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Carrier Wave <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/fund-carrierwave.html>`_\n\n                `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the carrier frequency, in hertz (Hz), of the RF signal to acquire. \n                        \n                        The RF vector signal analyzer tunes to this frequency. NI-RFSA may coerce this value based on hardware settings and downconversion settings.\n\n                        NI-RFSA sets the NIRFSA_ATTR_IQ_CARRIER_FREQUENCY attribute to this value. Refer to the specifications document that shipped with your device for allowable frequency settings.'
                },
                'name': 'carrierFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureIqPowerEdgeRefTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.\n\n                To trigger on burst signals, add a minimum quiet time, configured with the NIRFSA_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME attribute, to ensure the trigger does not occur in the middle of a burst if the acquisition starts while a burst is being generated. The quiet time should be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.\n\n                You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.\n\n                ----\n                **Note**\n                 This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n                ----\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source of the RF signal for the power edge Reference trigger. The only supported value is "0".'
                },
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the threshold, in dBm, above or below which the device triggers.'
                },
                'name': 'level',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether the device detects a positive or negative slope on the trigger signal. The default value is NIRFSA_VAL_RISING_SLOPE.\n\n                        | Value                                | Description                                                |\n                        |:--------------------------------|:-------------------------------------------------|\n                        | NIRFSA_VAL_RISING_SLOPE (1000)  | NI-RFSA detects a rising edge (positive slope).  |\n                        | NIRFSA_VAL_FALLING_SLOPE (1001) | NI-RFSA detects a falling edge (negative slope). |'
                },
                'name': 'slope',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.'
                },
                'name': 'pretriggerSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureIqRate': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the I/Q rate for the acquisition. \n                \n                The value is expressed in samples per second (S/s).\n\n                For the PXIe-5663/5663E/5665/5667/5668, when you set the NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE attribute to NIRFSA_VAL_ONBOARD_CLOCK_STR, the digitizer bandwidth is greater than or equal to the coerced **NIRFSA_ATTR_IQ_RATE** times 0.8. Actual signal bandwidth is limited for all supported devices by the anti-aliasing filter. Further device-specific limitations are as follows.\n\n                ----\n                **Note**\n                For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect your measurements. Refer to the NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED attribute for more information about dithering.\n\n                ----\n\n                - **PXI-5661** You should not need to configure an **NIRFSA_ATTR_IQ_RATE** higher than 25 megasamples per second (MS/s) because the PXI-5600 RF downconverter bandwidth is 20 MHz. If you configure a higher I/Q rate, you may see aliasing effects at negative frequencies because the IF frequency of the PXI-5600 RF downconverter is 15 MHz.\n                - **PXIe-5663/5663E** Maximum allowed instantaneous bandwidth depends on the I/Q carrier frequency you use. Refer to the `PXIe-5601 RF downconverter overview <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/overview.3.html>`_  for more information about instantaneous bandwidth.\n                - **PXIe-5665** Actual signal bandwidth is limited by the preselector and the combination of the chosen IF filter and anti-aliasing filter. Maximum allowed instantaneous bandwidth is independent of the downconverter center frequency for frequencies less than 3.6 GHz. At frequencies greater than 3.6 GHz, if your device supports the preselector (YIG-tuned filter) and you have enabled it for your application, the maximum allowed instantaneous bandwidth is limited to the instantaneous bandwidth of the preselector. Refer to the *NI PXIe-5665 Specifications* for more information about instantaneous bandwidth limits.\n                - **PXIe-5667** Actual signal bandwidth is limited by the preselector and the combination of the chosen IF filter and anti-aliasing filter. Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the *NI PXIe-5667 Specifications* for more information about instantaneous bandwidth limits.\n                - **PXIe-5668** Actual signal bandwidth is limited by the FPGA image that is downloaded upon opening the session to the PXIe-5624 digitizer. Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the *PXIe-5668 Specifications* for more information about instantaneous bandwidth limits.\n                - **PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842** Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the specifications document for your device for more information about instantaneous bandwidth limits.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the I/Q rate for the acquisition. The value is expressed in samples per second (S/s).'
                },
                'name': 'iqRate',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureNumberOfRecords': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the number of records in a finite acquisition or configures the device to continuously acquire records. \n                \n                You can only configure the device to acquire multiple records if you set the **NIRFSA_ATTR_NUMBER_OF_RECORDS_IS_FINITE** parameter to VI_TRUE.\n\n                If you configure the device to continuously acquire samples, it continues acquiring data until you call the nirfsa_Abort function to abort the acquisition. The device stores data in onboard memory in a circular fashion. After the device fills the memory, it starts overwriting previously acquired data from the beginning of the memory buffer. Retrieve the samples as they are being acquired, using one of the niRFSA fetch I/Q functions, to avoid overwriting data before you retrieve it.\n\n                To acquire more records than will fit into the device memory without continuously acquiring records, set the **NIRFSA_ATTR_NUMBER_OF_RECORDS_IS_FINITE** parameter in this function to VI_TRUE and the NIRFSA_ATTR_ALLOW_MORE_RECORDS_THAN_MEMORY attribute to VI_TRUE.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether to configure the device to acquire a finite number of records or to acquire records continuously. The default is VI_TRUE.\n\n                        | Value         | Description                                                                                                                                                                                                                |\n                        |:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n                        | VI_TRUE  | The device acquires a finite number of records.                                                                                                                                                                 |\n                        | VI_FALSE | The NI-RFSA device acquires records continuously until you call the nirfsa_Abort function to abort the acquisition. |'
                },
                'name': 'numberOfRecordsIsFinite',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of records to acquire if **NIRFSA_ATTR_NUMBER_OF_RECORDS_IS_FINITE** is set to VI_TRUE.'
                },
                'name': 'numberOfRecords',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureNumberOfSamples': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the number of samples in a finite acquisition or configures the device to continuously acquire samples.\n\n                If you configure the device for finite acquisition, it acquires the specified number of samples and then stops the acquisition. You can configure the device to acquire multiple records using the nirfsa_ConfigureNumberOfRecords function. Each record contains the number of samples specified in this function.\n\n                If you configure the device to continuously acquire samples, it continues acquiring data until you call the nirfsa_Abort function to abort the acquisition. The device stores data in onboard memory in a circular fashion. After the device fills the memory, it starts overwriting previously acquired data from the beginning of the memory buffer. Retrieve the samples as they are being acquired, using one of the niRFSA fetch I/Q functions, to avoid overwriting data before you retrieve it.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether to configure the device to acquire a finite number of samples or to acquire samples continuously. The default is VI_TRUE.\n\n                        | Value         | Description                                                                                                                                                                                                        |\n                        |:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n                        | VI_TRUE  | The device acquires a finite number of samples.                                                                                                                                                         |\n                        | VI_FALSE | The device acquires samples continuously until you call the nirfsa_Abort function to abort the acquisition. |'
                },
                'name': 'numberOfSamplesIsFinite',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples per record if **NIRFSA_ATTR_NUMBER_OF_SAMPLES_IS_FINITE** is set to VI_TRUE.'
                },
                'name': 'samplesPerRecord',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigurePxiChassisClk10': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. \n                \n                This option can be configured only when the PXI-5600 is installed in the Star Trigger Controller Slot, also known as the System Timing Slot, of the PXI chassis.\n\n                **Supported Devices**: PXI-5600 (external digitizer mode), PXI-5661\n\n                **Related Topics**\n\n                `System Reference Clock <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/system-reference-clock.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. This option can only be configured when the PXI-5600 is in Slot 2 of the PXI chassis.\n\n                        | Value                                              | Description                                                                                                                                                                                                                                                |\n                        |:----------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n                        | NIRFSA_VAL_NONE_STR ('None')                  | The device does not drive the PXI 10 MHz backplane Reference Clock.                                                                                                                                                                             |\n                        | NIRFSA_VAL_ONBOARD_CLOCK_STR ('OnboardClock') | The device drives the PXI 10 MHz backplane Reference Clock with the PXI-5600 onboard clock. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O connector on the PXI-5600 front panel to use this option.                           |\n                        | NIRFSA_VAL_REF_IN_STR ('RefIn')               | The device drives the PXI 10 MHz backplane Reference Clock with the reference source attached to the PXI-5600 REF IN connector. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O on the PXI-5600 front panel to use this option. |"
                },
                'name': 'pxiClk10Source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureRefClock': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the NI-RFSA device Reference Clock.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `PXI-5661 Reference Clock <https://www.ni.com/docs/en-US/bundle/pxi-5661-feature/page/reference-clock.html>`_\n\n                `PXIe-5663 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/timing-configurations.html>`_\n\n                `PXIe-5665 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/timing-configurations.html>`_\n\n                `PXIe-5667 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/timing-configurations.html>`_\n\n                `PXIe-5668 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/timing-configurations.html>`_\n\n                `PXIe-5830 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/timing-configurations.html>`_\n\n                `PXIe-5831 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/timing-configurations.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'specifies the source of the Reference Clock signal.\n                        | Clock Source          | Description |\n                        |-----------------------|-------------|\n                        | **Onboard Clock (default)** | Uses the onboard Reference Clock as the clock source. <br/>**PXIe-5830/5831/5832**-<br>- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT. <br>- PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br/>**PXIe-5831 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. <br/>**PXIe-5841 with PXIe-5655**-<br>- Lock to PXIe-5655 onboard clock. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. <br/>**PXIe-5842**-<br>- Lock to PXIe-5655 onboard clock. Use cables as shown in the Getting Started Guide. |\n                        | **RefIn** | Uses the signal at the front panel REF IN connector. <br/>**PXIe-5830/5831/5832**-<br>- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT; lock external signal to PXIe-3621 REF IN. <br>- PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT; lock external signal to PXIe-3622 REF IN. <br>- PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT; lock external signal to PXIe-3623 REF IN. <br/>**PXIe-5831 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. <br>- Lock external signal to PXIe-5653 REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. <br>- Lock external signal to PXIe-5653 REF IN. <br/>**PXIe-5841 with PXIe-5655**-<br>- Lock to signal at REF IN on PXIe-5655. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. <br/>**PXIe-5842**-<br>- Lock to signal at REF IN on PXIe-5655. Use cables as shown in the Getting Started Guide. |\n                        | **PXI Clock** | Uses the PXI_CLK signal present on the PXI backplane. |\n                        | **PXI_ClkMaster** | Valid only for PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653. <br/>**PXIe-5831 with PXIe-5653**-<br>- NI-RFSG configures PXIe-5653 to export Reference Clock. <br>- Configures PXIe-5820 and PXIe-3622 to use PXI_Clk. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- NI-RFSG configures PXIe-5653 to export Reference Clock. <br>- Configures PXIe-5820 and PXIe-3623 to use PXI_Clk. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. |'
                },
                'name': 'clockSource',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. This parameter is only valid when the **ref clock source** parameter is set to **RefIn**. The default value is Auto (-1.0), which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. Refer to the Reference Clock Rate property for possible values.'
                },
                'name': 'refClockRate',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureReferenceLevel': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the reference level. \n                \n                The reference level represents the maximum expected power of an input RF signal.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Improving Your Measurements <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/measurement_guidelines.html>`_\n\n                `Programming Attenuation-Related Properties and Attributes Using NI-RFSA <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/programming-attenuation.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the expected total power, in dBm, of the RF input signal.'
                },
                'name': 'referenceLevel',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureResolutionBandwidth': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the resolution bandwidth of a spectrum acquisition. \n                \n                The resolution bandwidth controls the width of the frequency bins in the power spectrum computed by NI-RFSA. A larger value for resolution bandwidth means the frequency bins are wider, so you get fewer bins, or spectral lines.\n\n                By default, the resolution bandwidth value corresponds to the 3 decibels (dB) bandwidth of the window type NI-RFSA uses to compute the spectrum. To directly specify the frequency bin width, set the NIRFSA_ATTR_RESOLUTION_BANDWIDTH_TYPE attribute to NIRFSA_VAL_RBW_BIN_WIDTH\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Resolution Bandwidth <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/resolution-bandwidth.html>`_\n\n                `Improving Your Measurements <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/measurement_guidelines.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the resolution bandwidth of a spectrum acquisition. The value is expressed in hertz (Hz). Configure the type of resolution bandwidth with the NIRFSA_ATTR_RESOLUTION_BANDWIDTH_TYPE attribute.'
                },
                'name': 'resolutionBandwidth',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureSoftwareEdgeAdvanceTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for a software Advance Trigger. \n                \n                The Advance Trigger indicates where a new record begins. The device waits until you call the nirfsa_SendSoftwareEdgeTrigger function to assert the trigger.\n\n                ----\n                **Note**\n                 This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n                ----\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureSoftwareEdgeRefTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for a software Reference Trigger to mark a reference point within the record. \n                \n                The device waits until you call the nirfsa_SendSoftwareEdgeTrigger function to assert the trigger.\n\n                You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.\n\n                ----\n                **Note**\n                 The PXIe-5644/5645/5646 does not support the NI-TClk API.\n\n                ----\n\n                ----\n                **Note**\n                 This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n                ----\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.'
                },
                'name': 'pretriggerSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureSoftwareEdgeStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to wait for a software Start Trigger at the beginning of the acquisition. \n                \n                The device waits until you call the nirfsa_SendSoftwareEdgeTrigger function to assert the trigger.\n\n                You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.\n\n                ----\n                **Note**\n                 The PXIe-5644/5645/5646 does not support the NI-TClk API.\n\n                ----\n\n                ----\n                **Note**\n                 This function is not supported if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function or if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM.\n\n                ----\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureSpectrumFrequencyCenterSpan': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the span and center frequency of the spectrum read by NI-RFSA. \n                \n                A spectrum acquisition consists of data surrounding the center frequency.\n\n                ----\n                **Note**\n                If you configure the spectrum span to a value larger than the instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you requested.\n\n                ----\n\n                ----\n                **Note**\n                 For the PXIe-5663/5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the bandwidths that correspond to each span are different (10 MHz and 20 MHz, respectively).\n\n                ----\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the center frequency in a spectrum acquisition. The value is expressed in hertz (Hz). The NI-RFSA device you use determines the valid range. Refer to your device specifications document for more information about frequency range.'
                },
                'name': 'centerFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the span of a spectrum acquisition. The value is expressed in hertz (Hz).\n\n                        ----\n                        \n                        *Note* For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect your measurements. Refer to the NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED attribute for more information about dithering.\n\n                        ----'
                },
                'name': 'span',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ConfigureSpectrumFrequencyStartStop': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the start and stop frequencies of a spectrum read by NI-RFSA.\n\n                ----\n                **Note**\n                If you configure the spectrum span (**NIRFSA_ATTR_STOP_FREQUENCY**  **NIRFSA_ATTR_START_FREQUENCY**) to a value larger than the instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you request.\n\n                ----\n\n                ----\n                **Note**\n                 For the PXIe-5663/5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the bandwidths that correspond to each span are different (10 MHz and 20 MHz, respectively).\n\n                ----\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the lower limit of a span of frequencies. This value is expressed in hertz (Hz).'
                },
                'name': 'startFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the upper limit of a span of frequencies. This value is expressed in hertz (Hz).'
                },
                'name': 'stopFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CreateConfigurationList': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Creates an empty configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_. \n                \n                After a configuration list is created, enable the list using the **setAsActiveList** parameter. Call the nirfsa_CreateConfigurationListStep function to add steps to the active configuration list.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters\n\n                **Related Topics**\n\n                `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the configuration list. This string may not contain spaces, special characters, or punctuation marks.'
                },
                'name': 'listName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of configuration list attributes to set.'
                },
                'name': 'numberOfListAttributes',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the attributes that you intend to change between configuration list steps. Calling the nirfsa_CreateConfigurationList function allocates space for each of the configuration list attributes. When you use an NI-RFSG Set attribute function to set one of the attributes in the configuration list, that attribute is set for one of the configuration list steps. Use the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP attribute to specify which configuration list step to configure.\n\n                        You can include the following attributes in your configuration list based on your device:\n\n                        | Attribute                                                                                              | PXIe-5663E | PXIe-5665 | PXIe-5667 | PXIe-5644/5646 | PXIe-5645 | PXIe-5820 | PXIe-5830/5831/5832 | PXIe-5840/5841 | PXIe-5841 with PXIe-5655 | PXIe-5842 |\n                        |:-------------------------------------------------------------------------------------------------------|:-----------|:----------|:----------|:----------------|:----------|:----------|:----------------------|:---------------|:--------------------------|:-----------|\n                        | NIRFSA_ATTR_CHANNEL_COUPLING                                                                           |            |           | Supported |                |           |           |                      |                |                            |            |\n                        | NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH                                                             | Supported  | Supported | Supported |                |           | Supported |                      | Supported      |                            | Supported  |\n                        | NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY                                                             |            |           |           |                | Supported | Supported |                      | Supported      | Supported                  | Supported  |\n                        | NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET                                                      |            |           |           |                |           | Supported |                      |                |                            |            |\n                        | NIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED                                                        | Supported  | Supported |           |                |           |           |                      | Supported      | Supported                  | Supported  |\n                        | NIRFSA_ATTR_EXTERNAL_GAIN                                                                              |            |           |           |                |           |           |                      | Supported      | Supported                  | Supported  |\n                        | NIRFSA_ATTR_FREQUENCY_SETTLING                                                                         | Supported  | Supported | Supported | Supported       | Supported | Supported | Supported            | Supported      |                            |            |\n                        | NIRFSA_ATTR_IF_FILTER_BANDWIDTH                                                                        |            |           | Supported | Supported       | Supported | Supported | Supported            |                |                            | Supported  |\n                        | NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL                                                                      |            | Supported |           |                |           |           |                      | Supported      |                            |            |\n                        | NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET                                                               |            | Supported |           |                |           |           |                      | Supported      |                            |            |\n                        | NIRFSA_ATTR_IQ_CARRIER_FREQUENCY                                                                       |            | Supported |           |                |           |           |                      | Supported      |                            |            |\n                        | NIRFSA_ATTR_IQ_IN_PORT_CARRIER_FREQUENCY                                                               |            | Supported |           |                |           |           |                      | Supported      |                            |            |\n                        | NIRFSA_ATTR_IQ_IN_PORT_VERTICAL_RANGE                                                                  |            |           |           |                |           |           |                      |                | Supported                  | Supported  |\n                        | NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_LEVEL                                                            |            |           |           |                | Supported | Supported |                      |                |                            |            |\n                        | NIRFSA_ATTR_LO_SOURCE                                                                                  | Supported  | Supported | Supported | Supported       |           |           | Supported            | Supported      | Supported                  | Supported  |\n                        | NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL                                                                                | Supported  | Supported | Supported |                | Supported | Supported | Supported            |                | Supported                  | Supported  |\n                        | NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED                                                               |            |           |           |                |           |           | Supported            | Supported      | Supported                  | Supported  |\n                        | NIRFSA_ATTR_MECHANICAL_ATTENUATION                                                                     |            |           |           |                | Supported | Supported | Supported            |                |                            |            |\n                        | NIRFSA_ATTR_MECHANICAL_ATTENUATOR_ENABLED                                                              |            |           |           |                |           |           |                      |                | Supported                  |            |\n                        | NIRFSA_ATTR_MINIMUM_ACPR                                                                                  |            |           |           |                |           |           |                      |                | Supported                  |            |\n                        | NIRFSA_ATTR_NOTCH_FILTER_ENABLED                                                                       |            |           |           |                |           |           |                      | Supported      |                            | Supported  |\n                        | NIRFSA_ATTR_NUMBER_OF_SAMPLES                                                                          | Supported  | Supported | Supported |                | Supported | Supported | Supported            | Supported      | Supported                  | Supported  |\n                        | NIRFSA_ATTR_OSP_DATA_SCALING_FACTOR                                                                     | Supported  | Supported |           |                |           |           | Supported            |                |                            | Supported  |\n                        | NIRFSA_ATTR_REFERENCE_LEVEL                                                                            |            |           |           |                |           |           |                      |                |                            | Supported  |\n                        | NIRFSA_ATTR_ATTENUATION                                                                                |            |           |           |                |           |           |                      |                |                            | Supported  |\n                        | NIRFSA_ATTR_RF_OUT_LO_EXPORT_ENABLED                                                                   |            |           |           |                |           |           |                      |                | Supported                  | Supported  |\n                        | NIRFSA_ATTR_RF_PREAMP_ENABLED                                                                          |            |           |           |                |           |           |                      |                | Supported                  | Supported  |\n                        | NIRFSA_ATTR_RF_PRESELECTOR_FILTER                                                                      |            |           |           |                |           |           |                      |                | Supported                  | Supported  |\n                        | NIRFSA_ATTR_SELECTED_PORTS                                                                              |            |           |           |                |           |           |                      |                | Supported                  | Supported  |\n                        | NIRFSA_ATTR_TIMER_EVENT_INTERVAL                                                                       |            |           |           |                |           |           |                      |                | Supported                  | Supported  |'
                },
                'name': 'listAttributeIDs',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Sets this list as the active configuration list when this parameter is set to VI_TRUE.'
                },
                'name': 'setAsActiveList',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CreateConfigurationListStep': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Creates a new configuration list step in the configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_ specified by the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST attribute. \n                \n                When you create a configuration list step, a new instance of each attribute specified by the configuration list attributes is created. Configuration list attributes are specified when a configuration list is created.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters\n\n                **Related Topics**\n\n                `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Sets this step as the active step for the active configuration list. The default value for this parameter is VI_TRUE.\n\n                        If you set this parameter to VI_FALSE, you can select the active configuration list step using the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP attribute.'
                },
                'name': 'setAsActiveStep',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CreateDeembeddingSparameterTableArray': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Creates an s-parameter de-embedding table for the port from the input data.\n\n                If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_\n\n                `S-parameters <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html#GUID-0AD828DE-398A-45C6-ABBA-4208DEB7DE1B__GUID-67A69775-E4DB-4FA2-84FE-C05977ED4184>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the frequencies for the NIRFSA_ATTR_SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.'
                },
                'name': 'frequencies',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'frequenciesSize'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the frequency array.'
                },
                'name': 'frequenciesSize',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'array_dimensions': 3,
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.'
                },
                'name': 'sparameterTable',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'sparameterTableSize'
                },
                'type': 'NIComplexNumber[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the S-parameter table array.'
                },
                'name': 'sparameterTableSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of DUT ports.'
                },
                'name': 'numberOfPorts',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the orientation of the data in the S2P file relative to the port on the DUT port.\n\n                        %enum_table{sparameter orientation}'
                },
                'name': 'sparameterOrientation',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'CreateDeembeddingSparameterTableS2PFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Creates an S-parameter de-embedding table for the port based on the specified S2P file.\n\n                If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_\n\n                `S-parameters <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html#GUID-0AD828DE-398A-45C6-ABBA-4208DEB7DE1B__GUID-67A69775-E4DB-4FA2-84FE-C05977ED4184>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the path to the S2P file that contains de-embedding information for the specified port.'
                },
                'name': 's2pFilePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the orientation of the data in the S2P file relative to the port on the DUT port.\n\n                       %enum_table{sparameter orientation}'
                },
                'name': 'sparameterOrientation',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'DeleteAllDeembeddingTables': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Deletes all configured de-embedding tables for the session.\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'DeleteConfigurationList': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Deletes a previously created configuration list and all the configuration list steps in the `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_ configuration list. \n                \n                When a configuration list step is deleted, all the instances of the attributes associated with the configuration list step are also removed. When you delete the active configuration list, NI-RFSA automatically resets the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST attribute to "" (empty string), which indicates no list is active, and the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP attribute to 0.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters\n\n                **Related Topics**\n\n                `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the configuration list. This string may not contain spaces, special characters, or punctuation marks.'
                },
                'name': 'listName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'DeleteDeembeddingTable': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Deletes the selected de-embedding table for a given port.\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'Disable': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'DisableAdvanceTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to not use an Advance Trigger. \n                \n                This function is necessary only if you configured an Advance Trigger in the past and now want to disable it.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'DisableRefTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to not wait for a Reference Trigger to mark a reference point within a record. \n                \n                This function is necessary only if you previously configured a Reference trigger in the past and now want to disable it.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'DisableStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device to not wait for a Start Trigger at the beginning of the acquisition. \n                \n                This function is necessary only if you previously configured a Start Trigger in the past and now want to disable it.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'EnableSessionAccess': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables or disables SFP session access for the specified instrument.\n\n                SFP session access allows the NI-RFSA Soft Front Panel (SFP) to access a device with an existing open session and can help you debug your code. To enable session access, pass VI_TRUE to the **enabled** parameter. To disable session access, pass VI_FALSE to the **enabled** parameter.\n\n                Refer to `Configuring SFP Session Access using LabWindows/CVI or C <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/configuring_session_access_labwindows.html>`_ for more information about SFP session access.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842/5860\n\n                ----\n                **Note**\n                NI-RFSA does not support NI-TClk when driver session debugging is enabled.\n\n                ----'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Enables or disables SFP session access for the specified device.\n\n                        | Value         | Description                         |\n                        |:---------|:-------------------------|\n                        | VI_TRUE  | Enables session access.  |\n                        | VI_FALSE | Disables session access. |'
                },
                'name': 'enable',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ErrorMessage': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Converts a status code returned by an NI-RFSA function into a user-readable string.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5840'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ViSession handle that you obtain from nirfsa_Init or nirfsa_InitWithOptions. The handle identifies a particular instrument session.\n\n                        You can pass VI_NULL for this parameter. Passing VI_NULL is useful when nirfsa_Init or nirfsa_InitWithOptions fails.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Passes the **status** parameter that is returned from any NI-RFSA function.'
                },
                'name': 'statusCode',
                'type': 'ViStatus',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Returns the user-readable message string that corresponds to the status code you specify.\n\n                        You must pass a ViChar array with at least 256 bytes to this parameter.'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ErrorQuery': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Reads an error code and a message from the instrument error queue.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ViSession handle that you obtain from nirfsa_Init or nirfsa_InitWithOptions. The handle identifies a particular instrument session.\n\n                        You can pass VI_NULL for this parameter. Passing VI_NULL is useful when nirfsa_Init or nirfsa_InitWithOptions fails.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Passes the **status** parameter that is returned from any NI-RFSA function.'
                },
                'name': 'errorCode',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the user-readable message string that corresponds to the error code.\n\n                        You must pass a ViChar array with at least 256 bytes to this parameter.'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ExportSignal': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Routes signals (triggers, clocks, and events) to the specified output terminal.\n\n                If you export a signal with this function and [commit](rfsacref.chm/cviniRFSA_Commit.html) the session, the signal is routed to the output terminal you specify. If you then reconfigure the signal to have a different output terminal, the previous output terminal is tri-stated when the session is next committed. If you set the **NIRFSA_ATTR_OUTPUT_TERMINAL** parameter to NIRFSA_VAL_DO_NOT_EXPORT_STR and commit, the previous output terminal is tristated.\n\n                Any signals, except for those exported over PXI trigger lines, that are exported within a session persist after the session closes to prevent signal glitches between sessions. PXI trigger lines are always set to tristate when a session is closed. If you wish to have the output terminal tristated when the session closes, change the **NIRFSA_ATTR_OUTPUT_TERMINAL** for the exported signal to NIRFSA_VAL_DO_NOT_EXPORT_STR, and commit the session again before closing it.\n\n                You can also tristate all PFI lines by setting the **resetDevice** parameter in the nirfsa_Init function to VI_TRUE or by using the nirfsa_Reset function.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the type of signal to route.\n\n                        %enum_table{signal}'
                },
                'name': 'signal',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the user-defined signal to route. Specify the signal you have implemented using FPGA extensions.'
                },
                'name': 'signalIdentifier',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "Specifies the terminal where the signal will be exported. You can also choose not to export any signal. For the PXIe-5841 with PXIe-5655, the signal is exported to the terminal on the PXIe-5841.\n\n                        | Value                             | Description                                                                                                                                                                                                                                |\n                        |:-----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n                        | NIRFSA_VAL_DO_NOT_EXPORT_STR | The signal is not exported.                                                                                                                                                                                                     |\n                        | NIRFSA_VAL_CLK_OUT_STR       | The signal is exported to the CLK OUT connector on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                       |\n                        | NIRFSA_VAL_REF_OUT_STR       | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |\n                        | NIRFSA_VAL_REF_OUT2_STR          | The signal is exported to the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                                  |\n                        | NIRFSA_VAL_PFI0_STR          | The signal is exported to the PFI 0 connector.                                                                                                                                                                                  |\n                        | NIRFSA_VAL_PFI1_STR          | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.                                                                                                                                                    |\n                        | NIRFSA_VAL_PXI_TRIG0_STR     | The signal is exported to the PXI trigger line 0.                                                                                                                                                                               |\n                        | NIRFSA_VAL_PXI_TRIG1_STR     | The signal is exported to the PXI trigger line 1.                                                                                                                                                                               |\n                        | NIRFSA_VAL_PXI_TRIG2_STR     | The signal is exported to the PXI trigger line 2.                                                                                                                                                                               |\n                        | NIRFSA_VAL_PXI_TRIG3_STR     | The signal is exported to the PXI trigger line 3.                                                                                                                                                                               |\n                        | NIRFSA_VAL_PXI_TRIG4_STR     | The signal is exported to the PXI trigger line 4.                                                                                                                                                                               |\n                        | NIRFSA_VAL_PXI_TRIG5_STR     | The signal is exported to the PXI trigger line 5.                                                                                                                                                                               |\n                        | NIRFSA_VAL_PXI_TRIG6_STR     | The signal is exported to the PXI trigger line 6.                                                                                                                                                                               |\n                        | NIRFSA_VAL_PXI_TRIG7_STR     | The signal is exported to the PXI trigger line 7.                                                                                                                                                                               |\n                        | NIRFSA_VAL_PXI_STAR_STR      | The signal is exported to the PXI star trigger line.                                                                                                                                                                            |\n                        | NIRFSA_VAL_PXIE_DSTARC_STR   | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                                          |\n                        | NIRFSA_VAL_DIO_PFI0_STR ('PFI0') | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                                           |\n                        | NIRFSA_VAL_DIO_PFI1_STR ('PFI1') | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                                           |\n                        | NIRFSA_VAL_DIO_PFI2_STR ('PFI2') | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                                           |\n                        | NIRFSA_VAL_DIO_PFI3_STR ('PFI3') | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                                           |\n                        | NIRFSA_VAL_DIO_PFI4_STR ('PFI4') | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                                           |\n                        | NIRFSA_VAL_DIO_PFI5_STR ('PFI5') | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                                           |\n                        | NIRFSA_VAL_DIO_PFI6_STR ('PFI6') | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                                           |\n                        | NIRFSA_VAL_DIO_PFI7_STR ('PFI7') | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                                           |"
                },
                'name': 'outputTerminal',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ExtCalStoreBaselineForSelfCalibration': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the external calibration step to run and stores the associated constants in the device memory so that they can be compared with the computed constants at run time. \n                \n                A password is required to run the function.\n\n                **Supported Devices**: PXIe-5603/5605/5606, PXIe-5665/5668'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitExtCal function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the password for the calibration session. The initial password is factory configured to NI. NIRFSA_ATTR_PASSWORD can be a maximum of ten alphanumeric characters.'
                },
                'name': 'password',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the step for which constants are computed.\n\n                        %enum_table{self calibration step}'
                },
                'name': 'selfCalibrationStep',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ExternalAlignmentAdjustPreselector': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Stores the preselector alignment coefficients that NI-RFSA uses to compute the preselector-tuning DAC value whenever the preselector is enabled. \n                \n                These coefficients are based on the desired center frequency for the preselector.\n\n                **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitializeExternalAlignment function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the length for the NIRFSA_ATTR_COEFFICIENTS array.'
                },
                'name': 'numberOfCoefficients',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the coefficients in the polynomial used to map the preselector center frequency to a preselector-tuning DAC value. Enter the coefficients in the array in order of highest order coefficient first (index 0) down to lowest order coefficient last.'
                },
                'name': 'coefficients',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfCoefficients'
                },
                'type': 'ViReal64[]',
                'use_array': True,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIqMultiRecordComplexF32': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Fetches I/Q data from multiple records in an acquisition. \n                \n                A fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\n                This function is not necessary if you use the nirfsa_ReadIqSingleRecordComplexF64 function because the nirfsa_ReadIqSingleRecordComplexF64 function performs the fetch as part of the function.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.'
                },
                'name': 'startingRecord',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of records to fetch.'
                },
                'name': 'numberOfRecords',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples per record.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n                        **PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n                        ----\n                        \n                        For all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n                        ----'
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the acquired waveform for each record fetched. The waveforms are written sequentially in the array. Allocate an array at least as large as **NIRFSA_ATTR_NUMBER_OF_SAMPLES** times **NIRFSA_ATTR_NUMBER_OF_RECORDS** for this parameter.'
                },
                'name': 'data',
                'type': 'NIComplexNumberF32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read. Each element of this array corresponds to a record.\n\n                        The following list provides more information about each of these properties:\n\n                        - **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n                        ----\n                        \n                        The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5840/5841/5842/5860.\n\n                        ----\n\n                        - **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n                        ----\n                        \n                        The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n                        ----\n\n                        - **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n                        - **actual samples read** Returns an integer representing the number of samples in the waveform.The actual number of samples for each record can vary if the NIRFSA ATTR NUMBER OF SAMPLES attribute changes per step during RF list mode.\n                        - **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n                        - **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.'
                },
                'name': 'wfmInfo',
                'type': 'struct niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIqMultiRecordComplexF64': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Fetches I/Q data from multiple records in an acquisition. \n                \n                A fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\n                This function is not necessary if you use the nirfsa_ReadIqSingleRecordComplexF64 function because the nirfsa_ReadIqSingleRecordComplexF64 function performs the fetch as part of the function.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.'
                },
                'name': 'startingRecord',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of records to fetch.'
                },
                'name': 'numberOfRecords',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples per record.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n                        **PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n                        ----\n                        \n                        For all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n                        ----'
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the acquired waveform for each record fetched. The waveforms are written sequentially in the array. Allocate an array at least as large as **NIRFSA_ATTR_NUMBER_OF_SAMPLES** times **NIRFSA_ATTR_NUMBER_OF_RECORDS** for this parameter.'
                },
                'name': 'data',
                'type': 'NIComplexNumber',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read. Each element of this array corresponds to a record.\n\n                        The following list provides more information about each of these properties:\n\n                        - **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n                        ----\n                        \n                        The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5840/5841/5842/5860.\n\n                        ----\n\n                        - **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n                        ----\n                        \n                        The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n                        ----\n\n                        - **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n                        - **actual samples read** Returns an integer representing the number of samples in the waveform.The actual number of samples for each record can vary if the NIRFSA ATTR NUMBER OF SAMPLES attribute changes per step during RF list mode.\n                        - **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n                        - **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.'
                },
                'name': 'wfmInfo',
                'type': 'struct niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIqMultiRecordComplexI16': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Fetches binary I/Q data from multiple records in an acquisition. \n                \n                Fetching transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\n                This function is not necessary if you use the nirfsa_ReadIqSingleRecordComplexF64 function because the nirfsa_ReadIqSingleRecordComplexF64 function performs the fetch as part of the function.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.'
                },
                'name': 'startingRecord',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of records to fetch.'
                },
                'name': 'numberOfRecords',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples per record.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n                        **PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n                        ----\n                        \n                        For all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n                        ----'
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the acquired waveform for each record fetched. The waveforms are written sequentially in the array. Allocate an array at least as large as **numberOfSamples** times **NIRFSA_ATTR_NUMBER_OF_RECORDS** for this parameter.'
                },
                'name': 'data',
                'type': 'NIComplexI16',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read. Each element of this array corresponds to a record.\n\n                        The following list provides more information about each of these properties:\n\n                        - **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n                        ----\n                        \n                        The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.\n\n                        ----\n\n                        - **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n                        ----\n                        \n                        The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n                        ----\n\n                        - **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n                        - **actual samples read** Returns an integer representing the number of samples in the waveform.The actual number of samples for each record can vary if the NIRFSA ATTR NUMBER OF SAMPLES attribute changes per step during RF list mode.\n                        - **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n                        - **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.'
                },
                'name': 'wfmInfo',
                'type': 'struct niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIqSingleRecordComplexF32': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Fetches I/Q data from a single record in an acquisition. \n                \n                The fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\n                This function is not necessary if you use the nirfsa_ReadIqSingleRecordComplexF64 function because the nirfsa_ReadIqSingleRecordComplexF64 function performs the fetch as part of the function.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the record to retrieve. Record numbers are zero-based.'
                },
                'name': 'recordNumber',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to fetch. The value must specify the array size of the NIRFSA_ATTR_DATA parameter.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n                        **PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n                        ----\n                        \n                        For all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n                        ----'
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the acquired waveform. Allocate an NIComplexNumberF32 array at least as large as **NIRFSA_ATTR_NUMBER_OF_SAMPLES**.'
                },
                'name': 'data',
                'type': 'NIComplexNumberF32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read.\n\n                        The following list provides more information about each of these properties:\n\n                        - **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n                        ----\n                        \n                        The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.\n\n                        ----\n\n                        - **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n                        ----\n                        \n                        The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n                        ----\n\n                        - **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n                        - **actual samples read** Returns an integer representing the number of samples in the waveform.\n                        - **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n                        - **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.'
                },
                'name': 'wfmInfo',
                'type': 'struct niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIqSingleRecordComplexF64': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Fetches I/Q data from a single record in an acquisition. \n                \n                The fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\n                This function is not necessary if you use the nirfsa_ReadIqSingleRecordComplexF64 function because the nirfsa_ReadIqSingleRecordComplexF64 function performs the fetch as part of the function.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the record to retrieve. Record numbers are zero-based.'
                },
                'name': 'recordNumber',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to fetch. The value must specify the array size of the NIRFSA_ATTR_DATA parameter.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n                        **PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n                        ----\n                        \n                        For all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n                        ----'
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the acquired waveform. Allocate an NIComplexNumber array at least as large as **NIRFSA_ATTR_NUMBER_OF_SAMPLES**.'
                },
                'name': 'data',
                'type': 'NIComplexNumber',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read.\n\n                        The following list provides more information about each of these properties:\n\n                        - **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n                        ----\n                        \n                        The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.\n\n                        ----\n\n                        - **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n                        ----\n                        \n                        The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n                        ----\n\n                        - **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n                        - **actual samples read** Returns an integer representing the number of samples in the waveform.\n                        - **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n                        - **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.'
                },
                'name': 'wfmInfo',
                'type': 'struct niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'FetchIqSingleRecordComplexI16': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Fetches binary I/Q data from a single record in an acquisition. \n                \n                The fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.\n\n                This function is not necessary if you use the nirfsa_ReadIqSingleRecordComplexF64 function because the nirfsa_ReadIqSingleRecordComplexF64 function performs the fetch as part of the function.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the record to retrieve. Record numbers are zero-based.'
                },
                'name': 'recordNumber',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to fetch. The value must specify the array size of the NIRFSA_ATTR_DATA parameter.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.\n\n                        **PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.\n\n                        ----\n                        \n                        For all supported devices, a value of  specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data.\n\n                        ----'
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the acquired waveform. Allocate an NIComplexI16 array at least as large as **NIRFSA_ATTR_NUMBER_OF_SAMPLES**.'
                },
                'name': 'data',
                'type': 'NIComplexI16',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read.\n\n                        The following list provides more information about each of these properties:\n\n                        - **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n                        ----\n                        \n                        The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.\n\n                        ----\n\n                        - **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n                        ----\n                        \n                        The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n                        ----\n\n                        - **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n                        - **actual samples read** Returns an integer representing the number of samples in the waveform.\n                        - **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n                        - **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.'
                },
                'name': 'wfmInfo',
                'type': 'struct niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Queries the value of a ViBoolean attribute.\n\n                You can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViBoolean variable.'
                },
                'name': 'value',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetAttributeViInt32': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Queries the value of a ViInt32 attribute.\n\n                You can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViInt32 variable.'
                },
                'name': 'value',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetAttributeViInt64': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Queries the value of a ViInt64 attribute.\n\n                You can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViInt64 variable.'
                },
                'name': 'value',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetAttributeViReal64': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Queries the value of a ViReal64 attribute.\n\n                You can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViReal64 variable.'
                },
                'name': 'value',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetAttributeViSession': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Queries the value of a ViSession attribute.\n\n                You can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViSession variable.'
                },
                'name': 'value',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetAttributeViString': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Queries the value of a ViString attribute.\n\n                You can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.\n\n                You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **NIRFSA_ATTR_BUF_SIZE** parameter. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **NIRFSA_ATTR_BUF_SIZE** parameter, the function copies buffer size  1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.\n\n                If you want to call this function just to get the required buffer size, you can pass 0 for **NIRFSA_ATTR_BUF_SIZE** and VI_NULL for the **attributeValue** buffer.\n\n                **Supported Devices:** PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar buffer you specify for the attribute value parameter.\n\n                        If you pass 0, you can pass VI_NULL for the attribute value buffer parameter.'
                },
                'name': 'bufSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The buffer in which the function returns the current value of the attribute. The buffer must be of type ViChar and have at least as many bytes as indicated in **NIRFSA_ATTR_BUF_SIZE**.\n\n                        If you specify 0 for the **NIRFSA_ATTR_BUF_SIZE** parameter, you can pass VI_NULL for this parameter.'
                },
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetCalUserDefinedInfo': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns user-defined information from the onboard EEPROM.\n\n                **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init, nirfsa_InitWithOptions, or nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a string containing the user-defined information.'
                },
                'name': 'info',
                'size': {
                    'mechanism': 'fixed',
                    'value': 22
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetCalUserDefinedInfoMaxSize': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the number of characters of user-defined information that can be stored in the device onboard EEPROM.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init, nirfsa_InitWithOptions, or nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of characters of user-defined information that can be stored in the device onboard EEPROM. The maximum size of the user-defined information array is 21 characters.'
                },
                'name': 'infoSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetDeembeddingSparameters': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the S-parameters used for de-embedding a measurement on the selected port. \n                \n                This includes interpolation of the parameters based on the configured carrier frequency. This function returns an empty array if no de-embedding is done.\n\n                If you want to call this function just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860',
            'note': 'The port orientation for the returned S-parameters is normalized to NIRFSA_VAL_PORT2_TOWARDS_DUT.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'get_deembedding_sparameter',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'array_dimensions': 2,
                'complex_array_representation': 'complex_number_array',
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22.'
                },
                'name': 'sparameters',
                'numpy': True,
                'type': 'NIComplexNumber[]',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array that is returned by the NIRFSA_ATTR_SPARAMETERS output.'
                },
                'name': 'sparametersArraySize',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of S-parameters.'
                },
                'name': 'numberOfSparameters',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of S-parameter ports. The **sparameter** array is always *n* x *n*, where span *n* is the number of ports.'
                },
                'name': 'numberOfPorts',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDeviceResponse': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the requested response type, based on current NI-RFSA settings. \n                \n                The PXI-5661 and PXIe-5663/5663E/5665/5667/5668 automatically corrects for the IF and RF response when you set the NIRFSA_ATTR_DIGITAL_IF_EQUALIZATION_ENABLED attribute to VI_TRUE. If you are using external digitizer mode, you can use information returned from this function to correct your measurement.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the IF, RF, or combined (IF and RF) response of the downconverter or NI-RFSA device that NI-RFSA returns. The default value is NIRFSA_VAL_DOWNCONVERTER_IF_RESPONSE.\n\n                        %enum_table{response type}'
                },
                'name': 'responseType',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array you specify for the NIRFSA_ATTR_FREQUENCIES, **NIRFSA_ATTR_MAGNITUDE_RESPONSE**, and **NIRFSA_ATTR_PHASE_RESPONSE** parameters.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array containing the frequencies, in hertz (Hz), that correspond to the response data.\n\n                        Pass VI_NULL if you do not want to use this parameter.'
                },
                'name': 'frequencies',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array containing the magnitude of the requested response, in decibels (dB). The magnitude response is normalized to the center frequency at each frequency in the NIRFSA_ATTR_FREQUENCIES array.\n\n                        Pass VI_NULL if you do not want to use this parameter.'
                },
                'name': 'magnitudeResponse',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array containing the phase of the requested response, in radians. The phase response is normalized to the center frequency at each frequency entry in the NIRFSA_ATTR_FREQUENCIES array.\n\n                        Pass VI_NULL if you do not want to use this parameter. This array may contain zeros if the device does not contain a stored phase response in its calibration data.'
                },
                'name': 'phaseResponse',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the required number of elements in the NIRFSA_ATTR_FREQUENCIES array and the response arrays. If **NIRFSA_ATTR_BUFFER_SIZE** is 0, this parameter returns the expected array size. The expected array size depends on which NI-RFSA device you use (PXI-5661, PXIe-5663/5663E/5665) and on the current settings (PXIe-5663/5663E/5665 only).'
                },
                'name': 'numberOfFrequencies',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetError': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Retrieves and then clears the IVI error information for the session or the current execution thread.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5840',
            'note': 'If the **NIRFSA_ATTR_ERROR_DESCRIPTION_BUFFER_SIZE** parameter is 0, this function does not clear the error information. By passing 0 to **NIRFSA_ATTR_ERROR_DESCRIPTION_BUFFER_SIZE**, you can determine the buffer size required to read the entire error description string. You can then call this function again with a sufficiently large buffer. If you specify a valid IVI session for the NIRFSA_ATTR_VI parameter, this function retrieves and then clears the error information for the session. If you pass VI_NULL for NIRFSA_ATTR_VI, this function retrieves and then clears the error information for the current execution thread. If NIRFSA_ATTR_VI is an invalid session, this function does nothing and returns an error. Normally, the error information describes the first error that occurred since you last called this function or the nirfsa_ClearError function.'
        },
        'included_in_proto': True,
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the error code for the session or execution thread. If you pass 0 for the **NIRFSA_ATTR_ERROR_DESCRIPTION_BUFFER_SIZE** parameter, you can pass VI_NULL for this parameter.'
                },
                'name': 'errorCode',
                'type': 'ViStatus',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': '256',
                'direction': 'in',
                'documentation': {
                    'description': 'Passes the number of bytes in the ViChar array you specify in **description**.\n\n                        If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies **NIRFSA_ATTR_ERROR_DESCRIPTION_BUFFER_SIZE**  1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.\n\n                        If you pass 0, you can pass VI_NULL for the **NIRFSA_ATTR_ERROR_DESCRIPTION** parameter.'
                },
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the error description for the IVI session or execution thread. If there is no description, this function returns an empty string.\n\n                        The buffer must contain at least as many elements as the value you specify with the **NIRFSA_ATTR_ERROR_DESCRIPTION_BUFFER_SIZE** parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies **NIRFSA_ATTR_ERROR_DESCRIPTION_BUFFER_SIZE**  1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer, in the **status** return value, that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.\n\n                        If you pass 0, you can pass VI_NULL for the this parameter.'
                },
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetExtCalLastDateAndTime': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the date and time of the last successful external calibration. \n                \n                The time returned is 24-hour local time, and the date is returned as integer values. For example, if the device was calibrated at 2:30 PM on December 31, 2010, this function returns 14 for the NIRFSA_ATTR_HOUR parameter, 30 for the NIRFSA_ATTR_MINUTE parameter, 12 for the NIRFSA_ATTR_MONTH parameter, 31 for the NIRFSA_ATTR_DAY parameter, and 2010 for the NIRFSA_ATTR_YEAR parameter.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init, nirfsa_InitWithOptions, or nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the year of the last external calibration.'
                },
                'name': 'year',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the month of the last external calibration.'
                },
                'name': 'month',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the day of the last external calibration.'
                },
                'name': 'day',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the hour of the last external calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the minute of the last external calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetExtCalLastTemp': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the temperature of the last successful external calibration. \n                \n                The temperature is returned in degrees Celsius.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init, nirfsa_InitWithOptions, or nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the temperature, in degrees Celsius, of the last external calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetExtCalRecommendedInterval': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the recommended interval between external calibrations, in months.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init, nirfsa_InitWithOptions, or nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the recommended maximum interval between external calibrations, in months.'
                },
                'name': 'months',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetFetchBacklog': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the number of points acquired that have not yet been fetched.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the record from which to read the backlog. Record numbers are zero-based.'
                },
                'name': 'recordNumber',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of samples available to read for the requested record.'
                },
                'name': 'backlog',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetFrequencyResponse': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the requested response type, based on current NI-RFSA settings. The PXI-5661 and PXIe-5663/5663E/5665/5667/5668 automatically corrects the IF and RF response when you set the Digital IF Equalization Enabled property to TRUE. If you are using external digitizer mode, you can use information returned from this VI to correct your measurement.\n\n                Refer to the *Factory Calibration* topic for your device for more information about frequency-response calibration.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array you specify for the NIRFSA_ATTR_FREQUENCIES, **NIRFSA_ATTR_MAGNITUDE_RESPONSE**, and **NIRFSA_ATTR_PHASE_RESPONSE** parameters.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array containing the frequencies, in hertz (Hz), that correspond to the response data.\n\n                        Pass VI_NULL if you do not want to use this parameter.'
                },
                'name': 'frequencies',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array containing the magnitude of the requested response, in decibels (dB). The magnitude response is normalized to the center frequency at each frequency in the NIRFSA_ATTR_FREQUENCIES array.\n\n                        Pass VI_NULL if you do not want to use this parameter.'
                },
                'name': 'magnitudeResponse',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array containing the phase of the requested response, in radians. The phase response is normalized to the center frequency at each frequency entry in the NIRFSA_ATTR_FREQUENCIES array.\n\n                        Pass VI_NULL if you do not want to use this parameter. This array may contain zeros if the device does not contain a stored phase response in its calibration data.'
                },
                'name': 'phaseResponse',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the required number of elements in the NIRFSA_ATTR_FREQUENCIES array and the response arrays. If **NIRFSA_ATTR_BUFFER_SIZE** is 0, this parameter returns the expected array size. The expected array size depends on which NI-RFSA device you use (PXI-5661, PXIe-5663/5663E/5665) and on the current settings (PXIe-5663/5663E/5665 only).'
                },
                'name': 'numberOfFrequencies',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetGainReferenceCalBaseline': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the gain reference calibration constants.\n\n                **Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5668'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitExtCal function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the buffer size.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the gain reference calibration constants.'
                },
                'name': 'gainReferenceCalConstants',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the number of elements in the **NIRFSA_ATTR_GAIN_REFERENCE_CAL_CONSTANTS** array.'
                },
                'name': 'numberOfGainReferenceCalConstants',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetNormalizationCoefficients': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'get_coefficient_info',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'name': 'coefficientInfo',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'niRFSA_coefficientInfo[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'name': 'numberOfCoefficientSets',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetNumberOfSpectralLines': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the number of spectral lines that NI-RFSA computes with the current power spectrum configuration.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the NIRFSA_ATTR_NUMBER_OF_SPECTRAL_LINES attribute.'
                },
                'name': 'numberOfSpectralLines',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetRelayName': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the name of a relay for your device. \n                \n                When you call this function and pass a VI_NULL pointer to the NIRFSA_ATTR_NAME parameter, **NIRFSA_ATTR_BUFFER_SIZE** is populated with the size of name including the terminating NULL byte. When you call this function and specify a value for **NIRFSA_ATTR_BUFFER_SIZE** that is greater than or equal to the name of relay, the NIRFSA_ATTR_NAME parameter returns the appropriate value.\n\n                **Supported Devices**: PXIe-5603/5605/5606.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the index of the relay.'
                },
                'name': 'index',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the relay name, when used as an input. You can select VI_NULL or a pointer to a ViInt32 array. VI_NULL is the default. When **NIRFSA_ATTR_BUFFER_SIZE** is greater than or equal to the number of relays, NIRFSA_ATTR_NAME returns the relay name.'
                },
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'When a VI_NULL pointer is passed in for the name, **NIRFSA_ATTR_BUFFER_SIZE** is populated with the size of the NIRFSA_ATTR_NAME.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetRelayOperationsCount': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns an array consisting of all the relay counts for your device. \n                \n                When you call this function and pass a VI_NULL pointer to the **NIRFSA_ATTR_OPERATIONS_COUNT** parameter, **NIRFSA_ATTR_BUFFER_SIZE** is populated with the number of relays on the device. When you call this function and specify a value for **NIRFSA_ATTR_BUFFER_SIZE** that is greater than or equal to the number of relays, the **NIRFSA_ATTR_OPERATIONS_COUNT** parameter returns the appropriate value.\n\n                **Supported Devices**: PXIe-5603/5605/5606, PXIe-5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the operations count array, when used as an input. You can select VI_NULL or a pointer to a ViInt32 array. VI_NULL is the default. When **NIRFSA_ATTR_BUFFER_SIZE** is greater than or equal to the number of relays, **NIRFSA_ATTR_OPERATIONS_COUNT** returns the number of relay operations.'
                },
                'name': 'operationsCount',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViInt32[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Functions as an input or an output. **NIRFSA_ATTR_BUFFER_SIZE** receives or returns the number of relays that are on the device.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetScalingCoefficients': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns coefficients you can use to convert unscaled data to scaled I/Q data.\n\n                Acquired data may be unscaled when sent by a peer-to-peer stream or fetched as unscaled data. Use this function to obtain nirfsa_GetScalingCoefficients structures in the **NIRFSA_ATTR_COEFFICIENT_INFO** array that provide gain and offset values you can use to scale this data into the actual I/Q values. The **NIRFSA_ATTR_COEFFICIENT_INFO** array returns one element for each channel specified in the **NIRFSA_ATTR_CHANNEL_LIST** parameter. The element order matches the order specified by the **NIRFSA_ATTR_CHANNEL_LIST** parameter. To get the actual I/Q values, scale the unscaled data from an acquisition by multiplying it by the gain value of the appropriate **NIRFSA_ATTR_COEFFICIENT_INFO** element then adding the offset from the same element.\n\n                ----\n                **Note**\n                The coefficients are calculated by NI-RFSA for the current configuration of the device, so they are only valid for acquisitions obtained with the same device configuration.\n\n                ----\n\n                To get the required size of the array, call this function with **NIRFSA_ATTR_ARRAY_SIZE** set to 0 and NULL for the **NIRFSA_ATTR_COEFFICIENT_INFO** array. This function returns the required size in the **NIRFSA_ATTR_NUMBER_OF_COEFFICIENT_SETS** parameter.\n\n                **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'get_coefficient_info',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array you specify for the **NIRFSA_ATTR_COEFFICIENT_INFO** parameter.'
                },
                'name': 'arraySize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the array for storing the coefficient info.\n\n                        - **offset** is the number that should be added to the data from a peer-to-peer stream after the gain has been applied if you want to scale unscaled data.\n                        - **gain** returns the multiplier that you should use to scale data obtained from a peer-to-peer stream.'
                },
                'name': 'coefficientInfo',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'niRFSA_coefficientInfo[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of valid coefficient sets.'
                },
                'name': 'numberOfCoefficientSets',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetSelfCalLastDateAndTime': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the date and time of the last successful self-calibration. \n                \n                The time returned is 24-hour local time, and the date is returned as integer values. For example, if the device was calibrated at 2:30 PM on December 31, 2010, this function returns 14 for the NIRFSA_ATTR_HOUR parameter, 30 for the NIRFSA_ATTR_MINUTE parameter, 12 for the NIRFSA_ATTR_MONTH parameter, 31 for the NIRFSA_ATTR_DAY parameter, and 2010 for the NIRFSA_ATTR_YEAR parameter.\n\n                ----\n                **Note**\n                For the PXIe-5644/5645/5646, you must select NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION for the **NIRFSA_ATTR_SELF_CALIBRATION_STEP** parameter.\n\n                ----\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the self-calibration step to query for the last successful self-calibration date and time data.\n\n                        %enum_table{self calibration step}'
                },
                'name': 'selfCalibrationStep',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the year of the last external calibration.'
                },
                'name': 'year',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the month of the last external calibration.'
                },
                'name': 'month',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the day of the last external calibration.'
                },
                'name': 'day',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the year of the last external calibration. It is expressed as an integer.'
                },
                'name': 'hour',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the minute of the last external calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetSelfCalLastTemp': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the temperature, in degrees Celsius, at the last successful self-calibration.\n\n                ----\n                **Note**\n                For the PXIe-5644/5645/5646, you must select NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION for the **selfCalibrationStep** parameter.\n\n                ----\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the self-calibration step to query for the last successful self-calibration date and time data.\n\n                        %enum_table{self calibration step}'
                },
                'name': 'selfCalibrationStep',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.'
                },
                'name': 'temp',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetSpectralInfoForSmt': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns information about the power spectrum NI-RFSA computes.\n\n                ----\n                **Note**\n                The NI Spectral Measurements Toolkit (SMT) requires this information.\n\n                ----\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns returns properties of the computed spectrum such as spectrum type, spectrum scale (linear or logarithmic), the window type the function used to compute the spectrum, window size, and FFT size. Pass this parameter to subsequent functions that contain the **NIRFSA_ATTR_SPECTRUM_INFO** parameter.'
                },
                'name': 'spectrumInfo',
                'type': 'struct niRFSA_spectrumInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetStreamEndpointHandle': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a writer endpoint handle that you can use with NI-P2P to configure a peer-to-peer stream with the digitizer as an endpoint.\n\n                **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Configuring An Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_\n\n                [Peer-to-Peer Streaming](nirfsa.chm/p2p-streaming.html)\n\n                [Configuring a Peer-to-Peer Stream](nirfsa.chm/configuring-p2p-stream.html)'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the stream resources you want to use.'
                },
                'name': 'streamEndpoint',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the writer endpoint handle which you use with NI-P2P to create a stream with the digitizer as an endpoint.'
                },
                'name': 'writerHandle',
                'type': 'ViUInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetTerminalName': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the fully qualified name of the signal being queried. \n                \n                Signals can be triggers, clocks, or events.\n\n                You can pass the **NIRFSA_ATTR_TERMINAL_NAME** parameter that is returned to the **source** parameter of a configure trigger function.\n\n                **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the signal for which you want to query the terminal.\n\n                       %enum_table{signal}'
                },
                'name': 'signal',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a particular instance of a trigger. NI-RFSA does not support this parameter.'
                },
                'name': 'signalIdentifier',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Passes the number of bytes in the ViChar buffer that you allocate for the **NIRFSA_ATTR_TERMINAL_NAME** parameter.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the fully qualified name of the signal being queried.'
                },
                'name': 'terminalName',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'GetUserData': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'name': 'identifier',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViInt8[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'name': 'actualDataSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'Init': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Creates a new session for the device. This function sends initialization commands to reset all hardware modules to a known state necessary for NI-RFSA operation.\n\n                To create a new session, pass the downconverter resource name for the RF vector signal analyzer to the **resource name** parameter.\n\n                You can access the device session this function creates using the NI-RFSA Soft Front Panel (SFP). Accessing the device session with the SFP can help you debug your code. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about accessing your session with the SFP.\n\n                ----\n                **Note**\n                Before initializing your device, you must first associate the modules that comprise your device in MAX. After associating the modules, pass the resource name of the device to this function to initialize all the modules. Refer to `Associating NI-RFSA Modules <https://www.ni.com/docs/en-US/bundle/ni-rfsa-max/page/maxrfsa/mi_rf_associating.html>`_ for information about MAX association.\n\n                ----\n\n                ----\n                **Note**\n                For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending *ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.\n\n                ----\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the resource name of the device to initialize.\n\n                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.\n\n                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.'
                },
                'name': 'resourceName',
                'type': 'ViRsrc',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether NI-RFSA performs an ID query. When you perform an ID query, NI-RFSA verifies the device you initialize is supported.\n\n                        | Value              | Description                                                |\n                        |:--------------|:------------------------------------------------|\n                        | VI_TRUE (Yes) | Perform an ID query. This value is the default. |\n                        | VI_FALSE (No) | Do not perform an ID query.                     |'
                },
                'name': 'idQuery',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether the NI-RFSA device is reset during the initialization procedure.\n\n                        | Value              | Description                                                    |\n                        |:--------------|:----------------------------------------------------|\n                        | VI_TRUE (Yes) | The device is reset.                                |\n                        | VI_FALSE (No) | The device is not reset. This value is the default. |'
                },
                'name': 'reset',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Identifies your instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'InitExtCal': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Creates and initializes a special NI-RFSA external calibration session. \n                \n                The ViSession returned is an NI-RFSA session that you can use to configure the device using normal attributes and functions. However, NI-RFSA sets flags that allow you to program an external calibration procedure using the calibration attributes and functions.\n\n                **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the resource name of the device to initialize.\n\n                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI ** topic of the *Measurement & Automation Explorer Help*.\n\n                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.'
                },
                'name': 'resourceName',
                'type': 'ViRsrc',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the password for the calibration session. The initial password is factory configured to NI. NIRFSA_ATTR_PASSWORD can have a maximum of ten alphanumeric characters.'
                },
                'name': 'password',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Sets the initial value of certain options for the session.\n\n                        The following options are used in this parameter.\n\n                        - calAction:create Use this option when starting a calibration step for the first time.\n                        - calAction:append Use this option when appending data to existing calibration data.'
                },
                'name': 'optionString',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Identifies your instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'InitWithOptions': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Creates a new session for the device. \n                \n                This function sets the initial value of certain attributes and sends initialization commands to reset all hardware modules to a known state necessary for NI-RFSA operation.\n\n                To create a new session, pass the downconverter resource name for the RF vector signal analyzer to the **resource name** parameter.\n\n                You can access the device session this VI creates using the NI-RFSA Soft Front Panel (SFP). Accessing the device session with the SFP can help you debug your code. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about accessing your session with the SFP.\n\n                ----\n                **Note**\n                Before initializing your device, you must first associate the modules that comprise your device in MAX. After associating the modules, pass the resource name of the device to this function to initialize all the modules. Refer to `Associating NI-RFSA Modules <https://www.ni.com/docs/en-US/bundle/ni-rfsa-max/page/maxrfsa/mi_rf_associating.html>`_ for information about MAX association.\n\n                ----\n\n                ----\n                **Note**\n                For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending *ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.\n\n                ----\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the resource name of the device to initialize.\n\n                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.\n\n                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.'
                },
                'name': 'resourceName',
                'type': 'ViRsrc',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether NI-RFSA performs an ID query. When you perform an ID query, NI-RFSA verifies the device you initialize is supported.\n\n                        | Value               |  Description                                               |\n                        |:--------------|:------------------------------------------------|\n                        | VI_TRUE (Yes) | Perform an ID query. This value is the default. |\n                        | VI_FALSE (No) | Do not perform an ID query.                     |'
                },
                'name': 'idQuery',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether the NI-RFSA device is reset during the initialization procedure.\n\n                        | Value              |  Description                                                   |\n                        |:--------------|:----------------------------------------------------|\n                        | VI_TRUE (Yes) | The device is reset.                                |\n                        | VI_FALSE (No) | The device is not reset. This value is the default. |'
                },
                'name': 'reset',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Sets the initial value of certain attributes for the session. The attributes shown in the following table are used in this parameter.\n\n                        | Name             | Attribute                                                                                                                                  |\n                        |:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------|\n                        | RangeCheck       | NIRFSA_ATTR_RANGE_CHECK                         |\n                        | QueryInstrStatus | NIRFSA_ATTR_QUERY_INSTRUMENT_STATUS |\n                        | Cache            | NIRFSA_ATTR_CACHE                                     |\n                        | RecordCoercions  | NIRFSA_ATTR_RECORD_COERCIONS               |\n                        | DriverSetup      | NIRFSA_ATTR_DRIVER_SETUP                       |\n                        | Simulate         | NIRFSA_ATTR_SIMULATE                               |\n\n                        The format of this string is *AttributeName=Value*, where *AttributeName* is the name of the attribute and *Value* is the value to which the attribute will be set. For example, you can simulate the PXIe-5663 using the following strings:\n\n                        *Simulate=1, DriverSetup=Model:5663\\E*.\n\n                        *Simulate=1, DriverSetup=Model:5601*; *Digitizer:5622; LO:5652; LOBoardType:PXIe*.\n\n                        To set multiple attributes, separate their assignments with a comma.\n\n                        Refer to `Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_ for more information about the driver setup string.\n\n                        Note: To simulate a device using the PXIe-5622 25 MHz digitizer, set the *Digitizer* field to 5622_25MHz_DDC and the *Simulate* field to 1. You can set the *Digitizer* field to 5622_25MHz_DDC only when using the PXIe-5665.'
                },
                'name': 'optionString',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Identifies your instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'InitializeCalibrationStep': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Initializes an EEPROM-specific calibration step.\n\n                **Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the calibration step to initialize.\n\n                       %enum_table{self calibration step}'
                },
                'name': 'calibrationStep',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'InitializeExternalAlignment': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Creates and initializes a special NI-RFSA external alignment session.\n\n                The ViSession returned is an NI-RFSA session that you can use to configure the device using normal attributes and functions. However, NI-RFSA sets flags that allow you to program an external alignment procedure using the external alignment attributes and functions.\n\n                **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the resource name of the device to initialize.\n                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.\n\n                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.'
                },
                'name': 'resourceName',
                'type': 'ViRsrc',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Sets the initial value of certain attributes for the session. The attributes shown in the following table are used in this parameter.\n\n                        | Name             | Attribute                                                                                                                                        |\n                        |:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|\n                        | RangeCheck       | NIRFSA_ATTR_RANGE_CHECK                         |\n                        | QueryInstrStatus | NIRFSA_ATTR_QUERY_INSTRUMENT_STATUS |\n                        | Cache            | NIRFSA_ATTR_CACHE                                     |\n                        | RecordCoercions  | NIRFSA_ATTR_RECORD_COERCIONS               |\n                        | DriverSetup      | NIRFSA_ATTR_DRIVER_SETUP                       |\n                        | Simulate         | NIRFSA_ATTR_SIMULATE                               |\n\n                        The format of this string is "*AttributeName=Value*", where *AttributeName* is the name of the attribute and *Value* is the value to which the attribute will be set. To set multiple attributes, separate their assignments with a comma.'
                },
                'name': 'optionString',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Identifies your instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'InitializeExternalAlignmentStep': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Initializes an EEPROM-specific external alignment step.\n\n                **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_InitializeExternalAlignment function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which external alignment step you want to initialize.\n\n                        | Value                                     | Description                                                                                                                                            |\n                        |:-------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|\n                        | EXT ALIGNMENT PRESELECTOR | Initiates preselector alignment. This step generates coefficients to align the preselector across the frequency range of 3.6 GHz to 14 GHz. |'
                },
                'name': 'externalAlignmentStep',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Commits settings to hardware, waits for hardware settling, and starts an acquisition. \n                \n                You can use this function in conjunction with one of the niRFSA fetch I/Q functions to retrieve acquired I/Q data, or you can use the nirfsa_ReadIqSingleRecordComplexF64 function to both initiate the acquisition and retrieve I/Q data at one time.\n\n                ----\n                **Note**\n                If you are using external digitizer mode, this function commits settings and waits for settling, but it does not start an acquisition. Notice that using the nirfsa_Commit function on its own commits settings to hardware, but the device does not wait for hardware settling.\n\n                ----\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_\n\n                `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_\n\n                `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/hardware-state-diagram.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'InvalidateAllAttributes': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'IsSelfCalValid': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Indicates which calibration steps contain valid calibration data. \n                \n                To omit steps with valid calibration data from self-calibration, you can pass the **NIRFSA_ATTR_VALID_STEPS** parameter to the **stepsToOmit** parameter of the nirfsa_SelfCalibrate function.\n\n                **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns VI_TRUE if all the calibration data is valid and VI_FALSE if any of the calibration data is invalid.'
                },
                'name': 'selfCalValid',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns valid steps.\n\n                        ----\n                        If two or more calibration steps are valid, this parameter returns a bitwise-OR combination of the calibration steps. For example, if both NIRFSA_VAL_SELF_CAL_IF_FLATNESS and NIRFSA_VAL_SELF_CAL_LO_SELF_CAL steps are valid, NI-RFSA returns the following string:\n\n                        NIRFSA_VAL_SELF_CAL_IF_FLATNESS |\n\n                        NIRFSA_VAL_SELF_CAL_LO_SELF_CAL\n\n                        ----\n\n                        %enum_table{self calibration step}'
                },
                'name': 'validSteps',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'LoadConfigurationsFromFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nLoads the configurations from the specified file to the NI-RFSA driver session.\n\nThe VI does an implicit reset before loading the configurations from the file.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsa_Init function or the nirfsa_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the absolute path of the file from which the NI-RFSA loads the configurations.'
                },
                'name': 'filePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Obtains a multithread lock on the instrument session. \n                \n                Before doing so, this function waits until all other execution threads have released their locks on the instrument session.\n\n                Other threads might have obtained a lock on this session in the following ways:\n\n                - Your application already called this function.\n                - A call to NI-RFSA locked the session.\n\n                After the call to this function returns successfully, no other threads can access the instrument session until you call the nirfsa_UnlockSession function. Use the nirfsa_LockSession function and the nirfsa_UnlockSession function around a sequence of calls to NI-RFSA functions if you require that the NI-RFSA device retain its settings through the end of the sequence.\n\n                You can safely make nested calls to the nirfsa_LockSession function within the same thread. To completely unlock the session, balance each call to the nirfsa_LockSession function with a call to the nirfsa_UnlockSession function. If, however, you use **NIRFSA_ATTR_CALLER_HAS_LOCK** in all calls to the nirfsa_LockSession function and the nirfsa_UnlockSession function within a function, the IVI Library locks the session only once within the function regardless of the number of calls you make to the nirfsa_LockSession function. Locking the session only once allows you to call the nirfsa_UnlockSession function just once at the end of the function.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Keeps track of whether you obtain a lock and therefore need to unlock the session in complex functions. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to this function or the nirfsa_UnlockSession function in the same function.\n\n                        This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.\n\n                        The nirfsa_LockSession function and the nirfsa_UnlockSession function each inspect the current value and take the actions shown in the following table.\n\n                        | Function             | Boolean Value | Action                                                                                               |\n                        |:---------------------|:--------------|:-----------------------------------------------------------------------------------------------------|\n                        | nirfsa_LockSession   | VI_TRUE       | The nirfsa_LockSession function does not lock the session again.                                     |\n                        |                      | VI_FALSE      | The nirfsa_LockSession function obtains the lock and sets the value of the parameter to VI_TRUE.     |\n                        | nirfsa_UnlockSession | VI_FALSE      | The nirfsa_UnlockSession function does not attempt to unlock the session.                            |\n                        |                      | VI_TRUE       | The nirfsa_UnlockSession function releases the lock and sets the value of the parameter to VI_FALSE. |\n\n                        Thus, you can call the nirfsa_UnlockSession function at the end of your function regardless of whether you actually have the lock.'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'PerformThermalCorrection': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Corrects for temperature variations while acquiring the same signal for an extended period of time in a continuous acquisition.\n\n                NI-RFSA internally acquires the temperature every time you initiate an acquisition. If you are performing a continuous acquisition, National Instruments recommends calling this function once every 10 minutes in a stable temperature environment to periodically update temperature calibration. If the ambient temperature varies, call this function more frequently.\n\n                ----\n                **Note**\n                You cannot call this function if your device is operating in `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_.\n\n                ----\n\n                Refer to the *Thermal Management* section for your device for more information about typical operating temperatures.\n\n                **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ReadIqSingleRecordComplexF64': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Initiates an acquisition and fetches a single I/Q data record. \n                \n                Do not use this function if you have configured the device to continuously acquire data samples or to acquire multiple records.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies in seconds the time allotted for the function to complete before returning a timeout error. A value of  specifies the function waits until all data is available.'
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the acquired waveform. Allocate an NIComplexNumber array at least as large as the number of samples configured in the nirfsa_ConfigureNumberOfSamples function.'
                },
                'name': 'data',
                'type': 'NIComplexNumber',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array for the NIRFSA_ATTR_DATA parameter. The array needs to be at least as large as the number of samples configured in the nirfsa_ConfigureNumberOfSamples function.'
                },
                'name': 'dataArraySize',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read.\n\n                        The following list provides more information about each of these properties:\n\n                        - **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.\n\n                        ----\n                        \n                        The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.\n\n                        ----\n\n                        - **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.\n\n                        ----\n                        \n                        \n                        The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.\n\n                        ----\n\n                        - **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.\n                        - **actual samples read** Returns an integer representing the number of samples in the waveform.\n                        - **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.\n                        - **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.'
                },
                'name': 'wfmInfo',
                'type': 'struct niRFSA_wfmInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ReadPowerSpectrumF32': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Initiates a spectrum acquisition and returns power spectrum data.\n\n                ----\n                **Note**\n                 Under certain configurations, negative infinity is returned from this VI. If the Reference Level is very high and if the Signal Bandwidth is comparatively less, the ADC returns zero, which equates to negative infinity in dBm. This is expected behavior.\n\n                ----\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the time, in seconds, allotted for the function to complete before returning a timeout error. A value of specifies the function waits until all data is available.'
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns power spectrum data. Allocate an array as large as **NIRFSA_ATTR_DATA_ARRAY_SIZE**.'
                },
                'name': 'powerSpectrumData',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'dataArraySize'
                },
                'type': 'ViReal32[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array that is returned by the **NIRFSA_ATTR_POWER_SPECTRUM_DATA** parameter. Use the nirfsa_GetNumberOfSpectralLines function to obtain the array size to allocate. The array must be at least as large as the number of spectral lines that NI-RFSA computes for the power spectrum.'
                },
                'name': 'dataArraySize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns additional information about the **NIRFSA_ATTR_POWER_SPECTRUM_DATA** array. This information includes the frequency, in hertz (Hz), corresponding to the first element in the array, the frequency increment, in Hz, between adjacent array elements, and the number of spectral lines the function returned.'
                },
                'name': 'spectrumInfo',
                'type': 'struct niRFSA_spectrumInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ReadPowerSpectrumF64': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Initiates a spectrum acquisition and returns power spectrum data.\n\n                ----\n                **Note**\n                 Under certain configurations, negative infinity is returned from this VI. If the Reference Level is very high and if the Signal Bandwidth is comparatively less, the ADC returns zero, which equates to negative infinity in dBm. This is expected behavior.\n\n                ----\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies which channels to apply settings. Specify an empty string as the value of this parameter.'
                },
                'name': 'channelList',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the time, in seconds, allotted for the function to complete before returning a timeout error. A value of specifies the function waits until all data is available.'
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns power spectrum data. Allocate an array as large as **NIRFSA_ATTR_DATA_ARRAY_SIZE**.'
                },
                'name': 'powerSpectrumData',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'dataArraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array that is returned by the **NIRFSA_ATTR_POWER_SPECTRUM_DATA** parameter. Use the nirfsa_GetNumberOfSpectralLines function to obtain the array size to allocate. The array must be at least as large as the number of spectral lines that NI-RFSA computes for the power spectrum.'
                },
                'name': 'dataArraySize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns additional information about the **NIRFSA_ATTR_POWER_SPECTRUM_DATA** array. This information includes the frequency, in hertz (Hz), corresponding to the first element in the array, the frequency increment, in Hz, between adjacent array elements, and the number of spectral lines the function returned.'
                },
                'name': 'spectrumInfo',
                'type': 'struct niRFSA_spectrumInfo',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'Reset': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Resets all properties to default values, deletes all de-embedding tables, and stops the export of all external signals and events.\n\n                For the PXI-5600, this function does not reset the PXI Clock signal that is driven by devices installed in the Trigger Controller Slot, also known as the System Timing Slot.\n\n                This function resets all configured routes for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 in NI-RFSA and NI-RFSG. To avoid resetting routes on the device that are in use by NI-RFSG sessions, NI recommends using the nirfsa_ResetWithOptions function, with **stepsToOmit** set to NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_\n\n                `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ResetAttribute': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Resets the attribute to its default value.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to reset the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ResetDevice': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Performs a hard reset on the device. \n                \n                A hard reset consists of the following actions:\n\n                - Signal acquisition is stopped.\n                - All routes are released.\n                - External bidirectional terminals are tristated.\n                - FPGAs are reset.\n                - Hardware is configured to its default state.\n                - All session attributes are reset to their default states.\n\n                During a device reset, routes of signals between this and other devices are released, regardless of which device created the route. For example, a trigger signal exported to a PXI trigger line that is used by another device is no longer exported.\n\n                On the PXI-5600, if you are driving the PXI_CLK10 line, you continue to drive the clock even after a device reset. To stop driving the PXI_CLK10 line, use the nirfsa_ConfigurePxiChassisClk10 function and set the **pxiClk10Source** parameter to NIRFSA_VAL_NONE_STR or set the NIRFSA_ATTR_PXI_CHASSIS_CLK10_SOURCE attribute to NIRFSA_VAL_NONE_STR.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ResetWithDefaults': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'ResetWithOptions': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes.\n\n                For the PXI-5600, this function does not reset the PXI Clock signal that is driven by devices installed in the Star Trigger Controller Slot, also known as the System Timing Slot.\n\n                By default, this function resets all properties to their default values, deletes all de-embedding tables, aborts generation, clears all routes, and resets session properties to initial values. You can specify steps to omit using the steps to omit parameter. For example, if you specify NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES for the **NIRFSA_ATTR_STEPS_TO_OMIT** parameter, this function does not release signal routes during the reset process.\n\n                When routes of signals between two devices are released, they are released regardless of which device created the route.\n\n                To avoid resetting routes on PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSG sessions, NI recommends using this function instead of nirfsa_Reset, with **NIRFSA_ATTR_STEPS_TO_OMIT** set to NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_\n\n                `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a list of steps to skip during the reset process. The default value is NIRFSA_VAL_RESET_WITH_OPTIONS_NONE, which specifies that no step is omitted during reset.\n\n                        %enum_table{steps to omit}\n\n                        \n                        Note:NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES is not supported in external calibration or alignment sessions.\n\n                    \n                        Note:NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES is not supported for the PXI-5600/5661.'
                },
                'name': 'stepsToOmit',
                'type': 'ViUInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'RevisionQuery': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the revision numbers of the NI-RFSA instrument driver.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the instrument driver software revision numbers in the form of a string. The value of the NIRFSA_ATTR_SPECIFIC_DRIVER_REVISION attribute is returned.\n\n                        You must pass a ViChar array with 256 bytes or more to this parameter.'
                },
                'name': 'driverRev',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the instrument firmware revision numbers in the form of a string. The value of the NIRFSA_ATTR_INSTRUMENT_FIRMWARE_REVISION attribute is returned.\n\n                        You must pass a ViChar array with 256 bytes or more to this parameter.'
                },
                'name': 'instrRev',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SaveConfigurationsToFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSaves the configurations of the session to the specified file.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsa_Init function or the nirfsa_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the absolute path of the file to which the NI-RFSA saves the configurations.'
                },
                'name': 'filePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCal': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SelfCalibrate': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Self-calibrates the NI-RFSA device and associated modules that support self-calibration. \n                \n                If self-calibration is performed successfully, the new calibration constants are stored immediately in the self-calibration area of the module EEPROM. Refer to the specifications document for your device for more information about how often to self-calibrate.\n\n                For best results, NI recommends that you perform a complete self-calibration without omitting any steps. However, if the nirfsa_IsSelfCalValid function indicates that the calibration data for a specific step is still valid, you can omit that step for faster execution.\n\n                **Open NI-RFSG Session for the PXIe-5820/5830/5831/5832/5840/5841/5842/5860**\n\n                If there is an existing NI-RFSG session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this function runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSG Commit or niRFSG Initiate. For the existing open session to use the new self-calibration data, the session will need to be closed and reopened.\n\n                 **PXIe-5860**\n\n                 While this VI is running on one channel, if there are any existing NI-RFSG or NI-RFSA sessions open on the other channel, they may remain open but cannot be used for operations that access the hardware, for example niRFSG Commit or niRFSG Initiate or niRFSA Commit or niRFSA Initiate. For the existing open session to use the new self-calibration data, the session will need to be closed and reopened.\n\n                 **PXIe-5841 with PXIe-5655**\n\n                The PXIe-5841 maintains separate self-calibration data for both the PXIe-5841 standalone and when associated with the PXIe-5655. Use this function once for each intended configuration.\n\n                **IF Flatness Step Time**\n\n                - The IF Flatness step can take approximately 15 minutes to complete on the PXIe-5665 (3.6 GHz) and approximately 25 minutes to complete on the PXIe-5665 (14 GHz).\n                - The IF Flatness step can take approximately 1 minute to complete on the PXIe-5667 (3.6 GHz) and approximately 1.5 minutes to complete on the PXIe-5667 (7 GHz).\n                - The IF Flatness step can take approximately 15 minutes to complete on the PXIe-5668.\n\n                **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `PXI-5661 Calibration <https://www.ni.com/docs/en-US/bundle/pxi-5661-feature/page/self-calibration.html>`_\n\n                `PXIe-5663/5663E Calibration <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/self-calibration.html>`_\n\n                `PXIe-5665 Self-Calibration <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/self-calibration.html>`_\n\n                `PXIe-5667 Self-Calibration <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/self-calibration.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which calibration steps to skip as part of the self-calibration process. A value of 0 specifies all supported calibration steps are performed.\n\n                        ----\n                        \n                        To omit two or more calibration steps, specify a bitwise-OR combination of the following constants. For example, if you wanted to omit NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY and NIRFSA_VAL_SELF_CAL_LO_SELF_CAL, you would pass the following string to the nirfsa_SelfCalibrate function: NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY | NIRFSA_VAL_SELF_CAL_LO_SELF_CAL\n\n                        ----\n\n                        | Value                                          |  Description                                                                                                                                                                                                                     |\n                        |:------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n                        | NIRFSA_VAL_RESET_WITH_OPTIONS_NONE             | No step is omitted during self-calibration.                                                                                                                                                                           |\n                        | NIRFSA_VAL_SELF_CAL_PRESELECTOR_ALIGNMENT | Not used by this function.                                                                                                                                                                                            |\n                        | NIRFSA_VAL_SELF_CAL_GAIN_REFERENCE        | Not used by this function.                                                                                                                                                                                            |\n                        | NIRFSA_VAL_SELF_CAL_IF_FLATNESS           | Not used by this function.                                                                                                                                                                                            |\n                        | NIRFSA_VAL_SELF_CAL_DIGITIZER_SELF_CAL    | Not used by this function.                                                                                                                                                                                            |\n                        | NIRFSA_VAL_SELF_CAL_LO_SELF_CAL           | Omits the Local Oscillator (LO) Self Cal step. If you omit this step and the nirfsa_IsSelfCalValid function indicates the calibration data for this step is invalid, the LO phase-locked loop (PLL) may fail to lock. |\n                        | NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY    | Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy of the device is not adjusted.                                                                                                        |\n                        | NIRFSA_VAL_SELF_CAL_RESIDUAL_LO_POWER     | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.                                                                                                           |\n                        |NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION      | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image Performance is not adjusted.                                                                                                     |\n                        | NIRFSA_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT | Omits the Synthesizer Alignment step. If you omit this step, the LO PLL is not adjusted. This step is not valid for the PXIe-5820.                                                                                    |\n                        | NIRFSA_VAL_SELF_CAL_DC_OFFSET             | Omits the DC Offset step. This step applies only to the PXIe-5820.                                                                                                                                                    |'
                },
                'name': 'stepsToOmit',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SelfCalibrateRange': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Self-calibrates all configurations within the specified frequency and reference level limits.\n\n                Self-calibration range data is valid until you restart the system or call the nirfsa_ClearSelfCalibrateRange function.\n\n                NI recommends that no external signals are present on the RF In port while the calibration is taking place.\n\n                ----\n                **Note**\n                This function does not update self-calibration date and temperature.\n\n                ----\n\n                For best results, NI recommends that you perform a complete self-calibration without omitting any steps. However, if certain aspects of performance are less important for your application, you can omit that step for faster execution.\n\n                ----\n                **Note**\n                If there is an existing NI-RFSG session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this function runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSG Commit or niRFSG Initiate.\n\n                ----\n\n                ----\n                **Note**\n                If there is an existing NI-RFSG session open for the same PXIe-5644/5645/5646, it may remain open but cannot be used while this function runs.\n\n                ----\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which calibration steps to skip as part of the self-calibration process. A value of 0 specifies all supported calibration steps are performed.\n\n                        ----\n                        \n                        To omit two or more calibration steps, specify a bitwise-OR combination of the following constants. For example, if you wanted to omit NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY and NIRFSA_VAL_SELF_CAL_LO_SELF_CAL, you would pass the following string to the nirfsa_SelfCalibrate function: NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY | NIRFSA_VAL_SELF_CAL_LO_SELF_CAL\n\n                        ----\n\n                        | Value                                          |  Description                                                                                                                                                                                                                     |\n                        |:------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n                        | NIRFSA_VAL_RESET_WITH_OPTIONS_NONE             | No step is omitted during self-calibration.                                                                                                                                                                           |\n                        | NIRFSA_VAL_SELF_CAL_PRESELECTOR_ALIGNMENT | Not used by this function.                                                                                                                                                                                            |\n                        | NIRFSA_VAL_SELF_CAL_GAIN_REFERENCE        | Not used by this function.                                                                                                                                                                                            |\n                        | NIRFSA_VAL_SELF_CAL_IF_FLATNESS           | Not used by this function.                                                                                                                                                                                            |\n                        | NIRFSA_VAL_SELF_CAL_DIGITIZER_SELF_CAL    | Not used by this function.                                                                                                                                                                                            |\n                        | NIRFSA_VAL_SELF_CAL_LO_SELF_CAL           | Omits the Local Oscillator (LO) Self Cal step. If you omit this step and the nirfsa_IsSelfCalValid function indicates the calibration data for this step is invalid, the LO phase-locked loop (PLL) may fail to lock. |\n                        | NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY    | Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy of the device is not adjusted.                                                                                                        |\n                        | NIRFSA_VAL_SELF_CAL_RESIDUAL_LO_POWER     | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.                                                                                                           |\n                        |NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION      | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image Performance is not adjusted.                                                                                                     |\n                        | NIRFSA_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT | Omits the Synthesizer Alignment step. If you omit this step, the LO PLL is not adjusted. This step is not valid for the PXIe-5820.                                                                                    |\n                        | NIRFSA_VAL_SELF_CAL_DC_OFFSET             | Omits the DC Offset step. This step applies only to the PXIe-5820.                                                                                                                                                    |'
                },
                'name': 'stepsToOmit',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the minimum RF frequency in Hz.'
                },
                'name': 'minFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum RF frequency in Hz.'
                },
                'name': 'maxFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the minimum reference level in dBm.'
                },
                'name': 'minReferenceLevel',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum reference level in dBm.'
                },
                'name': 'maxReferenceLevel',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SelfTest': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Performs a self-test on the NI-RFSA device and returns the test result. \n                \n                This function performs a simple series of tests verifying that the NI-RFSA device is powered on and responding.\n\n                ----\n                **Note**\n                This function calls the nirfsa_Reset function, which resets the software state.\n\n                ----\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Running a Self-Test on an NI-RFSA Device <https://www.ni.com/docs/en-US/bundle/ni-rfsa-max/page/maxrfsa/mi_rf_self_test.html>`_'
        },
        'grpc_name': 'SelfTest',
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value from the device self-test. A value of 0 means success. All other values indicate failure.\n\n                        You must pass a ViChar array with 1024 bytes or more to this parameter. Only the first 1024 bytes of the array are used.'
                },
                'name': 'testResult',
                'type': 'ViInt16',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the self-test response string from the NI-RFSA device.'
                },
                'name': 'testMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SendSoftwareEdgeTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Sends a trigger to the device when you use a software version of a supported trigger and the device is waiting for the trigger to be sent. \n                \n                You can also use this function to override a hardware trigger.\n\n                This function returns an error in the following situations:\n\n                - You configure an invalid trigger.\n                - You set the **acquisitionType** to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function.\n                - You have not previously called the nirfsa_Initiate function.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Software Trigger <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/software-edge-trigger.html>`_\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the software signal to send.\n\n                        %enum_table{trigger}'
                },
                'name': 'trigger',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a particular instance of a trigger. NI-RFSA does not currently support this parameter.'
                },
                'name': 'triggerIdentifier',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Sets the value of a ViBoolean attribute.\n\n                Use this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.\n\n                NI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n                        ----\n                        \n                        Some of the values might not be valid depending on the current state of the instrument session.\n\n                        ----'
                },
                'name': 'value',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetAttributeViInt32': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Sets the value of a ViInt32 attribute.\n\n                Use this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.\n\n                NI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel-based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n                        ----\n                        \n                        Some of the values might not be valid depending on the current state of the instrument session.\n\n                        ----'
                },
                'grpc_enum': 'NiRFSAInt32AttributeValues',
                'grpc_mapped_enum': 'NiRFSAInt32AttributeValuesMapped',
                'name': 'value',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetAttributeViInt64': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Sets the value of a ViInt64 attribute.\n\n                Use this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.\n\n                NI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n                        ----\n                        \n                        Some of the values might not be valid depending on the current state of the instrument session.\n\n                        ----'
                },
                'grpc_name': 'value_raw',
                'name': 'value',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetAttributeViReal64': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Sets the value of a ViReal64 attribute.\n\n                Use this low-level function to set the values of inherent IVI attributes, and instrument-specific attributes.\n\n                NI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread-locking for you.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n                        ----\n                        \n                        Some of the values might not be valid depending on the current state of the instrument session.\n\n                        ----'
                },
                'grpc_enum': 'NiRFSAReal64AttributeValues',
                'name': 'value',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetAttributeViSession': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Sets the value of a ViSession attribute.\n\n                Use this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.\n\n                NI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n                        ----\n                        \n                        Some of the values might not be valid depending on the current state of the instrument session.\n\n                        ----'
                },
                'name': 'value',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetAttributeViString': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Sets the value of a ViString attribute.\n\n                Use this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.\n\n                NI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n                        ----\n                        \n                        Some of the values might not be valid depending on the current state of the instrument session.\n\n                        ----'
                },
                'grpc_mapped_enum': 'NiRFSAStringAttributeValuesMapped',
                'name': 'value',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetCalUserDefinedInfo': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Writes user-defined information into the onboard EEPROM. \n                \n                This should be called in its own session or else the data may be overwritten by a commit.\n\n                **Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init, nirfsa_InitWithOptions, or nirfsa_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a string containing the user-defined information. This string can be up to 21 characters long.'
                },
                'name': 'info',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'SetUserData': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'name': 'identifier',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'bufferSize'
                },
                'type': 'ViInt8[]',
                'use_array': True,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'UnlockSession': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Releases a lock obtained on an NI-RFSA device session by calling the nirfsa_LockSession function. \n                \n                Refer to the nirfsa_LockSession function for additional information on session locks.\n\n                **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. NIRFSA_ATTR_VI is obtained from the nirfsa_Init or nirfsa_InitWithOptions function.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Keeps track of whether you obtain a lock and therefore need to unlock the session in complex functions. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to this function or the nirfsa_UnlockSession function in the same function.\n\n                        This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.\n\n                        The nirfsa_LockSession function and the nirfsa_UnlockSession function each inspect the current value and take the actions shown in the following table.\n\n                        | Function             | Boolean Value | Action                                                                                               |\n                        |:---------------------|:--------------|:-----------------------------------------------------------------------------------------------------|\n                        | nirfsa_LockSession   | VI_TRUE       | The nirfsa_LockSession function does not lock the session again.                                     |\n                        |                      | VI_FALSE      | The nirfsa_LockSession function obtains the lock and sets the value of the parameter to VI_TRUE.     |\n                        | nirfsa_UnlockSession | VI_FALSE      | The nirfsa_UnlockSession function does not attempt to unlock the session.                            |\n                        |                      | VI_TRUE       | The nirfsa_UnlockSession function releases the lock and sets the value of the parameter to VI_FALSE. |\n\n                        Thus, you can call the nirfsa_UnlockSession function at the end of your function regardless of whether you actually have the lock.'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': True
    },
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'TBD'
        },
        'grpc_name': 'FancySelfTest',
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    }
}
