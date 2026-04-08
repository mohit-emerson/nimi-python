# -*- coding: utf-8 -*-
# This file is generated from NI-RFSA API metadata version 26.5.0d9999
attributes = {
    1050002: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to validate attribute values and function parameters. \n\nIf enabled, NI-RFSA validates the parameter values that you pass to NI-RFSA functions. Range checking parameters is very useful for debugging. After you validate your program, you can set this attribute to VI_FALSE to disable range checking and maximize performance.\n\n----\n**Note**\nUse the nirfsa_InitWithOptions function to override this value.\n\n----\n\n**Defined Values:**\n\n| Value         | Description                                                                    |\n|:---------|:--------------------------------------------------------------------|\n| VI_TRUE  | NI-RFSA validates attribute values and function parameters.         |\n| VI_FALSE | NI-RFSA does not validate attribute values and function parameters. |\n\n**Default Value**: VI_TRUE\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Range Check',
        'name': 'RANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050003: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether NI-RFSA queries the NI-RFSA device status after each operation. \n\nQuerying the device status is useful for debugging. After you validate your program, you can set this attribute to VI_FALSE to disable status checking and maximize performance.\n\nNI-RFSA can choose to ignore status checking for particular attributes regardless of the setting of this attribute.\n\n----\n**Note**\nUse the nirfsa_InitWithOptions function to override this value.\n\n----\n\n**Defined Values:**\n\n| Value         | Description                                                               |\n|:---------|:---------------------------------------------------------------|\n| VI_TRUE  | NI-RFSA queries the device status after each operation.        |\n| VI_FALSE | NI-RFSA does not query the device status after each operation. |\n\n**Default Value**: VI_FALSE\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Query Instrument Status',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'type': 'ViBoolean'
    },
    1050004: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to cache the value of attributes.\n\nIf you set this attribute to VI_TRUE, NI-RFSA tracks the current NI-RFSA device settings and avoids sending redundant commands to the device.\n\nNI-RFSA can always cache or never cache particular attributes, regardless of the setting of this attribute.\n\nUse the nirfsa_InitWithOptions function to override the default value.\n\n**Defined Values:**\n\n|Value          | Description                      |\n|:---------|:---------------------|\n| VI_TRUE  | Caching is enabled.  |\n| VI_FALSE | Caching is disabled. |\n\n**Default Value**: VI_TRUE\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Cache',
        'name': 'CACHE',
        'type': 'ViBoolean'
    },
    1050005: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether NI-RFSA simulates I/O operations. This attribute is useful for debugging applications without using hardware. After a session is opened, you cannot change the simulation state. Use the nirfsa_InitWithOptions function to enable simulation.\n\n----\n**Note**\nPXI-5600/5661 support setting this attribute to VI_FALSE only.\n\n----\n\n**Defined Values:**\n\n| Value         | Description                                                           |\n|:---------|:-----------------------------------------------------------|\n| VI_TRUE  | NI-RFSA simulates NI-RFSA I/O operations.                  |\n| VI_FALSE | NI-RFSA does not support simulated NI-RFSA I/O operations. |\n\n**Default Value**: VI_FALSE\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode); PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050006: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type attributes.\n\n----\n**Note**\nThis attribute is currently not supported.\n\n----\n\n**Defined Values:**\n\n| Value         | Description                                                            |\n|:---------|:------------------------------------------------------------|\n| VI_TRUE  | The IVI engine keeps a list of the value coercions.         |\n| VI_FALSE | The IVI engine does not keep a list of the value coercions. |\n\n**Default Value**: VI_FALSE\n\n**Supported Devices**: None'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Record Value Coercions',
        'name': 'RECORD_COERCIONS',
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'The Driver Setup string returns the initial values for properties that are specific to NI-RFSA.\n\nThe Driver Setup string uses the following format:\n\nDriverSetup= <i>Tag</i>:<i>Value</i>\n\n*Tag* is the name of the Driver Setup string attribute. *Value* is the value set to the attribute. If multiple attributes are set, their assignments are separated with a semicolon.\n\nThis attribute only returns the Driver Setup string that has already been defined. Refer to `Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_ for more information about configuring the Driver Setup string. Refer to the nirfsa_InitWithOptions function for additional information about using the **option string** parameter.\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Driver Setup',
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050021: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to perform interchangeability checking and retrieve interchangeability warnings.\n\n----\n**Note**\nInterchangeability check is unsupported.\n\n----\n\n**Defined Values:**\n\n| Value         | Description                                                                           |\n|:---------|:---------------------------------------------------------------------------|\n| VI_TRUE  | NI-RFSA performs interchangeability-checking and retrieves warnings.       |\n| VI_FALSE | NI-RFSA does not perform interchangeability-checking or retrieve warnings. |\n\n**Default Value**: VI_FALSE\n\n**Supported Devices**: None'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Interchange Check',
        'name': 'INTERCHANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050302: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the prefix for NI-RFSA. The name of each user-callable function in NI-RFSA starts with this prefix. \n\nThis attribute returns\n\nniRFSA.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Prefix',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'type': 'ViString'
    },
    1050304: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Indicates the resource name NI-RFSA uses to identify the physical device. \n\nIf you initialize NI-RFSA with a logical name, this attribute contains the resource name that corresponds to the entry in the IVI Configuration Utility.\n\nIf you initialize NI-RFSA with the resource name, this attribute contains that value.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Contains the logical name you specified when opening the current IVI session. \n\nYou may pass a logical name to the nirfsa_Init function or the nirfsa_InitWithOptions function. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a driver session section in the IVI Configuration file. The driver session section specifies a physical device and initial user options.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a comma-separated list of supported devices.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050510: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the firmware revision information for the NI-RFSA downconverter for the composite device you are currently using.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n----\n**Note**\nPXIe-5820/5830/5831/5832/5840/5841/5842/5860 devices will return "No revision information available." To retrieve the firmware revision, use MAX, Hardware Configuration Utility, or NI System Configuration API.\n\n----'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the name of the manufacturer for the NI-RFSA device you are currently using.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the model number or name of the NI-RFSA device that you are currently using.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the name of the vendor that supplies NI-RFSA. \n\nThis attribute returns\n\nNational Instruments.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains a brief description of NI-RFSA. \n\nThis attribute returns\n\nRF Signal Analyzer Instrument Driver.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050551: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains additional version information about NI-RFSA. \n\nFor example, NI-RFSA can return\n\nDriver: NI-RFSA 2.6, Compiler: MSVC 7.10, Components: IVI Engine 4.00, VISA-Spec 4.00 as the value of this attribute.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150001: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the session to either acquire I/Q data or to compute a power spectrum over the specified frequency range.\n\n**Defined Values:**\n\n%enum_table{acquisition type}\n\n**Default Value**: NIRFSA_VAL_IQ\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureAcquisitionType'
        },
        'enum': 'AcquisitionType',
        'lv_property': 'Acquisition Type',
        'name': 'ACQUISITION_TYPE',
        'type': 'ViInt32'
    },
    1150002: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the center frequency in a spectrum acquisition. \n\nThe value is expressed in hertz (Hz). An acquisition consists of a span of data surrounding the center frequency.\n\n----\n**Note**\nUse this attribute to tune the downconverter when using external digitizer mode.\n\n----\n\n**Units**: hertz (Hz)\n\n**Default Values**:\n\n**PXIe-5694**: 193.6 MHz\n\n**PXIe-5820**: 0 Hz\n\n**PXIe-5830/5831/5832**: 6.5 GHz\n\n**All other devices**: 1 GHz\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Acquisition:Spectrum:Center Frequency',
        'name': 'CENTER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150003: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the frequency range of the computed spectrum in hertz (Hz). \n\nFor example, if you specify a center frequency of 1 GHz and a span of 100 MHz, the spectrum ranges from 950 MHz to 1,050 MHz after zoom processing. This value may be coerced based on hardware settings and RF downconverter specifications.\n\nNI-RFSA performs multispan acquisitions by dividing the total requested span into equally sized subspans based on the device instantaneous bandwidth at the range of frequencies you specify. NI-RFSA combines these subspans to yield a multispan acquisition. You can use the NIRFSA_ATTR_FFT_WIDTH attribute to improve amplitude accuracy and avoid unwanted effects such as filter roll-off and spurs across the span you select.\n\n----\n**Note**\nIf you configure the spectrum span to a value larger than the hardware instantaneous bandwidth, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you requested.\n\n----\n\n----\n**Note**\nFor the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect measurements. Refer to the NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED attribute for more information about dithering.\n\n----\n\n**PXIe-5663/5663E**: NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the instantaneous bandwidth for frequencies above 120 MHz is different than instantaneous bandwidth for frequencies less than 120 MHz, which are 20 MHz and 10 MHz respectively.\n\n**PXIe-5665 (14 GHz)/5667 (7 GHz)**: If you enable the downconverter preselector filter, the device instantaneous bandwidth is only a typical specification.\n\n**Default Value**: 10 MHz\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureSpectrumFrequencyCenterSpan'
        },
        'lv_property': 'Acquisition:Spectrum:Span',
        'name': 'SPECTRUM_SPAN',
        'type': 'ViReal64'
    },
    1150004: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the reference level, in dBm. \n\nThe reference level represents the maximum expected power of an RF input signal.\n\n----\n**Note**\nFor the PXIe-5645, this attribute is ignored if you are using the I/Q ports.\n\n----\n\nRefer to the NIRFSA_ATTR_EXTERNAL_GAIN attribute for more information about how configuring an external gain and a reference level affect attenuation.\n\n**Default Value**: 0\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Improving Your Measurements <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/measurement_guidelines.html>`_\n\n`Programming Attenuation-Related Properties and Attributes Using NI-RFSA <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/programming-attenuation.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureReferenceLevel'
        },
        'lv_property': 'Vertical:Reference Level (dBm)',
        'name': 'REFERENCE_LEVEL',
        'type': 'ViReal64'
    },
    1150005: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the nominal attenuation setting, in dB, for all attenuators before the first mixer in the RF signal chain.\n\nIf you do not set this attribute, NI-RFSA automatically chooses an attenuation setting based on the reference level you configure. The valid values for this attribute depend on the device configuration.\n\n**PXI-5600/5661**: You can change the attenuation value to modify the amount of noise and distortion. Higher attenuation levels increase the noise level while decreasing distortion; lower attenuation levels decrease the noise level while increasing distortion.\n\n**PXIe-5601/5663/5663E**: You can change the attenuation value and the value of the NIRFSA_ATTR_IF_ATTENUATION attribute to modify the amount of noise and distortion. Higher attenuation levels increase the noise level while decreasing distortion; lower attenuation levels decrease the noise level while increasing distortion.\n\n**PXIe-5603/5605/5606/5665/5668**: You can set multiple attributes to modify the attenuation values for the device. Refer to `PXIe-5665 RF Attenuation and Signal Levels <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/attenuation-and-signal-levels.html>`_ for more information about configuring attenuation.\n\n**PXIe-5667**: This attribute specifies the nominal attenuation setting for all attenuators before the first RF mixer in the input signal path. This attribute is read-only when the NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED attribute is set to NIRFSA_VAL_DISABLED.\n\n**PXIe-5693**: This attribute is read-only and returns the nominal RF attenuation of the PXIe-5693.\n\n**Units**: dB\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693'
        },
        'lv_property': 'Vertical:Advanced:RF Attenuation (dB)',
        'name': 'ATTENUATION',
        'type': 'ViReal64'
    },
    1150006: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the mixer level, in dBm. \n\nThe mixer level represents the attenuation value to apply to the input RF signal as it reaches the first mixer in the signal chain. If you do not set this attribute, NI-RFSA automatically selects an optimal mixer level value based on the reference level. The valid values for this attribute depend on your device configuration.\n\nIf you set the NIRFSA_ATTR_MIXER_LEVEL and NIRFSA_ATTR_MIXER_LEVEL_OFFSET attributes at the same time, NI-RFSA returns an error.\n\n**PXIe-5601/5663/5663E**: This attribute is read-only.\n\n**PXIe-5667**: This attribute is read-only when the NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED attribute is set to NIRFSA_VAL_DISABLED.\n\n**Units**: dBm\n\n**Default Values**:\n\n**PXI-5600/5661**: -30\n\n**PXIe-5603/5605/5665/5667/5668**: -10\n\n**All other devices**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668'
        },
        'lv_property': 'Vertical:Mixer Level (dBm)',
        'name': 'MIXER_LEVEL',
        'type': 'ViReal64'
    },
    1150007: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the I/Q rate for the acquisition. \n\nThe value is expressed in samples per second (S/s).\n\nRefer to the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute for more information about device specific instantaneous bandwidth limits. You can also refer to the *NI PXIe-5665 Specifications* for more information about instantaneous bandwidth device specifications.\n\n----\n**Note**\nFor the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. At I/Q rates above 50 MS/s, the dither noise can affect phase coherency performance and leak into the lower frequencies and the upper frequencies of the IF passband. Refer to the NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED attribute for more information about dithering.\n\nFor the PXIe-5663/5663E/5665/5667, when you set the NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE attribute to NIRFSA_VAL_ONBOARD_CLOCK_STR, the downconverter instantaneous bandwidth is greater than or equal to the coerced I/Q rate times 0.8. For the PXIe-5665, the actual signal bandwidth is further limited by the combination of the chosen IF filter and anti-aliasing filter.\n\n----\n\n**PXI-5661**: You should not need to configure an I/Q rate higher than 25 megasamples per second (MS/s) because the PXI-5600 RF downconverter bandwidth is 20 MHz. If you configure a higher I/Q rate, you may see aliasing effects at negative frequencies because the IF frequency of the PXI-5600 is 15 MHz.\n\n**PXIe-5663/5663E**: Your maximum allowed instantaneous bandwidth depends on the I/Q carrier frequency you use. Refer to the `PXIe-5601 RF downconverter overview <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/overview.3.html>`_ for more information about instantaneous bandwidth.\n\n**PXIe-5665**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency if you have enabled the preselector (YIG-tuned filter).\n\n**PXIe-5667**: Your maximum allowed instantaneous bandwidth depends on the selected [RF preselector filter](NIRFSA_ATTR_RF_PRESELECTOR_FILTER.html) and whether the preselector on the [RF downconverter](NIRFSA_ATTR_PRESELECTOR_ENABLED.html) is enabled.\n\n**PXIe-5668**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use and whether or not you enable the highpass filter or preselector (YIG-tuned filter).\n\n**Units**: S/s\n\n**Default Values:**\n\n**PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality**: 5 GS/s only.\n\n**All Other Devices**: 1 MS/s\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureIqRate'
        },
        'lv_property': 'Acquisition:IQ:IQ Rate (S/s)',
        'name': 'IQ_RATE',
        'type': 'ViReal64'
    },
    1150008: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the device acquires a finite number of samples or acquires continuously.\n\n**Defined Values:**\n\n| Value         |  Description                                                     |\n|:---------|:------------------------------------------------------|\n| VI_TRUE  | Acquire a finite number of samples.                   |\n| VI_FALSE | Acquire continuously until you abort the acquisition. |\n\n**Default Value**: VI_TRUE\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureNumberOfSamples'
        },
        'lv_property': 'Acquisition:IQ:Number Of Samples Is Finite',
        'name': 'NUMBER_OF_SAMPLES_IS_FINITE',
        'type': 'ViBoolean'
    },
    1150009: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the number of samples to acquire. \n\nThis attribute is valid only if the NIRFSA_ATTR_NUMBER_OF_SAMPLES_IS_FINITE attribute is set to VI_TRUE.\n\n**Default Value**: 1,000\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureNumberOfSamples'
        },
        'lv_property': 'Acquisition:IQ:Number Of Samples',
        'name': 'NUMBER_OF_SAMPLES',
        'type': 'ViInt64'
    },
    1150010: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the device stops after acquiring the specified number of records or acquires records continuously.\n\n**Defined Values:**\n\n|Value          | Description                                                              |\n|:---------|:--------------------------------------------------------------|\n| VI_TRUE  | Acquire a finite number of records.                           |\n| VI_FALSE | Acquire records continuously until you abort the acquisition. |\n\n**Default Value**: VI_TRUE\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureNumberOfRecords'
        },
        'lv_property': 'Acquisition:IQ:Number Of Records Is Finite',
        'name': 'NUMBER_OF_RECORDS_IS_FINITE',
        'type': 'ViBoolean'
    },
    1150011: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the number of records to acquire if the NIRFSA_ATTR_NUMBER_OF_RECORDS_IS_FINITE attribute is set to VI_TRUE.\n\n**Default Value**: 1\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureNumberOfRecords'
        },
        'lv_property': 'Acquisition:IQ:Number Of Records',
        'name': 'NUMBER_OF_RECORDS',
        'type': 'ViInt64'
    },
    1150012: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the units of the power spectrum.\n\n**Defined Values:**\n\n%enum_table{spectrum units}\n\n**Default Value**: NIRFSA_VAL_DBM\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'enum': 'SpectrumUnits',
        'lv_property': 'Acquisition:Spectrum:Power Spectrum Units',
        'name': 'POWER_SPECTRUM_UNITS',
        'type': 'ViInt32'
    },
    1150013: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the resolution along the x-axis of the spectrum. \n\nNI-RFSA uses the resolution bandwidth value to determine the acquisition size. If specified, the NIRFSA_ATTR_NUMBER_OF_SPECTRAL_LINES attribute value overrides this value.\n\n**Units**: hertz (Hz)\n\n**Default Value**: 100 kHz\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureResolutionBandwidth'
        },
        'lv_property': 'Acquisition:Spectrum:Resolution Bandwidth (Hz)',
        'name': 'RESOLUTION_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150014: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies how the NIRFSA_ATTR_RESOLUTION_BANDWIDTH attribute is expressed.\n\n**Defined Values:**\n\n%enum_table{spectrum resolution bandwidth type}\n\n**Default Value**: NIRFSA_VAL_RBW_3DB\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'enum': 'SpectrumResolutionBandwidthType',
        'lv_property': 'Acquisition:Spectrum:Resolution Bandwidth Type',
        'name': 'RESOLUTION_BANDWIDTH_TYPE',
        'type': 'ViInt32'
    },
    1150015: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the number of acquisitions to average. \n\nThe averaging process returns the final result after the number of averages is complete.\n\n**Default Value**: 10\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Acquisition:Spectrum:Number Of Averages',
        'name': 'SPECTRUM_NUMBER_OF_AVERAGES',
        'type': 'ViInt32'
    },
    1150016: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the averaging mode for the spectrum acquisition.\n\n**Defined Values:**\n\n%enum_table{spectrum averaging mode}\n\n**Default Value**: NIRFSA_VAL_NO_AVERAGING\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'enum': 'SpectrumAveragingMode',
        'lv_property': 'Acquisition:Spectrum:Averaging Mode',
        'name': 'SPECTRUM_AVERAGING_MODE',
        'type': 'ViInt32'
    },
    1150017: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the time-domain window type.\n\n**Defined Values:**\n\n%enum_table{spectrum ff twindow type}\n\n**Default Values**:\n\n**PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: NIRFSA_VAL_7_TERM_BLACKMAN_HARRIS\n\n**PXIe-5667**: NIRFSA_VAL_4_TERM_BLACKMAN_HARRIS\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Resolution Bandwidth <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/resolution-bandwidth.html>`_'
        },
        'enum': 'SpectrumFfTwindowType',
        'lv_property': 'Acquisition:Spectrum:FFT Window Type',
        'name': 'FFT_WINDOW_TYPE',
        'type': 'ViInt32'
    },
    1150018: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the number of spectral lines expected with the current power spectrum configuration. \n\nIf you do not configure this attribute, NI-RFSA selects an appropriate value based on the NIRFSA_ATTR_RESOLUTION_BANDWIDTH attribute. If you configure this attribute, NI-RFSA coerces the NIRFSA_ATTR_RESOLUTION_BANDWIDTH value based on the number of spectral lines requested and the value of the NIRFSA_ATTR_SPECTRUM_SPAN attribute.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Acquisition:Spectrum:Number Of Spectral Lines',
        'name': 'NUMBER_OF_SPECTRAL_LINES',
        'type': 'ViInt32'
    },
    1150019: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the Reference Clock source.\n\n----\n**Note**\nFor the PXIe-5694, if your application requires an external LO source, set this attribute to NIRFSA_VAL_NONE_STR.\n\n----\n\n**Defined Values:**\n\n%enum_table{ref clock src}\n\n**Default Values**:\n\n**PXIe-5694**: NIRFSA_VAL_REF_IN_STR\n\n**All other devices**: NIRFSA_VAL_ONBOARD_CLOCK_STR\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureRefClock'
        },
        'enum': 'RefClockSrc',
        'lv_property': 'Clocking:Ref Clock Source',
        'name': 'REF_CLOCK_SOURCE',
        'type': 'ViString'
    },
    1150020: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector. \n\nThis attribute is only valid when the NIRFSA_ATTR_REF_CLOCK_SOURCE attribute is set to NIRFSA_VAL_CLK_IN_STR,NIRFSA_VAL_REF_IN_STR , or NIRFSA_VAL_REF_IN_2_STR.\n\n**Valid Values**:\n\n**PXIe-5644/5645/5646, PXIe-5601/5663/5663E, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841**: 10 MHz\n\n**PXIe-5603/5605/5665/5667/5668**: 5 MHz to 100 MHz, in increments of 1 MHz\n\n**PXIe-5841 with PXIe-5655, PXIe-5842**: 10 MHz, 100 MHz, 270 MHz, and 3.84 MHz  *y*, where *y* is 4, 8, 16, 24, 25, or 32.\n\n**PXIe-5860**: 10 MHz, 100 MHz\n\n**Default Value**: 10 MHz\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureRefClock'
        },
        'lv_property': 'Clocking:Ref Clock Rate',
        'name': 'REF_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1150021: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the source of the Sample Clock timebase, which is the timebase used to control waveform sampling.\n\n**Defined Values:**\n\n%enum_table{digitizer samp clk timebase src}\n\n**Default Value**: NIRFSA_VAL_ONBOARD_CLOCK_STR\n\n**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668'
        },
        'enum': 'DigitizerSampClkTimebaseSrc',
        'lv_property': 'Clocking:Digitizer Sample Clock Timebase Source',
        'name': 'DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE',
        'type': 'ViString'
    },
    1150022: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the frequency, in hertz (Hz), of the external clock used as the timebase source if you set the NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE attribute to an external source, such as NIRFSA_VAL_CLK_IN_STR, NIRFSA_VAL_LO_REF_CLK_STR, or NIRFSA_VAL_DOWNCONVERTER_LO2_OUT_STR\n\n**PXI-5661**If this attribute is set to a value less than 60 MHz, signals at frequencies just above the 20 MHz passband of the downconverter may be aliased back into the passband. This aliasing occurs because the IF frequency of the downconverter is 15 MHz, and the upper end of the passband is 25 MHz. At sampling rates below 60 MHz, the Nyquist frequency is close to the end of the passband and creates aliases that are not filtered effectively by the downconverter.\n\n**Units**: hertz (Hz)\n\n**Valid and Default Values**:\n\n| Device                    | Valid Values            | Default Value |\n|:--------------------------|:------------------------|:--------------|\n| PXI-5661                  | Any frequency 226552.5 MHz | 100 MHz       |\n| PXIe-5663/5663E/5665/5667 | 150 MHz                 | 150 MHz       |\n| PXIe-5668                 | 2 GHz                   | 2 GHz         |\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668'
        },
        'lv_property': 'Clocking:Digitizer Sample Clock Timebase Rate',
        'name': 'DIGITIZER_SAMPLE_CLOCK_TIMEBASE_RATE',
        'type': 'ViReal64'
    },
    1150023: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. \n\nThis option can be configured only when the PXI-5600 is installed in Slot 2 of the PXI chassis.\n\n**Defined Values:**\n\n%enum_table{pxi chassis clk10 src}\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600 (external digitizer mode), PXI-5661\n\n**Related Topics**\n\n[System Reference Clock](nirfsa.chm/system-reference-clock.html)\n\n**High-Level Functions**:\n\n- nirfsa_ConfigurePxiChassisClk10'
        },
        'enum': 'PxiChassisClk10Src',
        'lv_property': 'Clocking:PXI Chassis Clk10 Source',
        'name': 'PXI_CHASSIS_CLK10_SOURCE',
        'type': 'ViString'
    },
    1150024: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether you want the Start Trigger to be a digital edge or software trigger.\n\n----\n**Note**\nSet this attribute to NIRFSA_VAL_NONE if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM or if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the [cviniRFSA_ConfigureAcquisitionType](cviniRFSA_ConfigureAcquisitionType.html) function.\n\n----\n\n**Defined Values:**\n\n%enum_table{start trig type}\n\n**Default Value**: NIRFSA_VAL_NONE\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'enum': 'StartTrigType',
        'lv_property': 'Triggers:Start:Type',
        'name': 'START_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150025: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the source terminal for the Start Trigger.\n\nThis attribute is used only when the NIRFSA_ATTR_START_TRIGGER_TYPE attribute is set to NIRFSA_VAL_DIGITAL_EDGE.\n\n**Defined Values**:\n\n%enum_table{output term}\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureDigitalEdgeStartTrigger'
        },
        'lv_property': 'Triggers:Start:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150026: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the active edge for the Start Trigger.\n\nThis attribute is used only when the NIRFSA_ATTR_START_TRIGGER_TYPE attribute is set to NIRFSA_VAL_DIGITAL_EDGE.\n\n**Defined and Valid Values:**\n\n| Value                         | Description                                           | Valid For                           |\n|:------------------------------|:------------------------------------------------------|:------------------------------------|\n| NIRFSA_VAL_RISING_EDGE (900)  | The trigger asserts on the rising edge of the signal. | PXI-5661, PXIe-5663/5663E/5665/5668 |\n| NIRFSA_VAL_FALLING_EDGE (901) | The trigger asserts on the falling edge of the signal | PXIe-5668                           |\n\n**Default Value**: NIRFSA_VAL_RISING_EDGE\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureDigitalEdgeStartTrigger'
        },
        'enum': 'StartTrigDigEdgeEdge',
        'lv_property': 'Triggers:Start:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150027: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for the exported Start Trigger.\n\n**Defined Values:**\n\n%enum_table{export output term}\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ExportSignal'
        },
        'enum': 'ExportOutputTerm',
        'lv_property': 'Triggers:Start:Export:Output Terminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150028: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether you want the Reference Trigger to be a digital edge, I/Q power edge, or software trigger.\n\n**Defined Values:**\n\n%enum_table{ref trig type}\n\n**Default Value**: NIRFSA_VAL_NONE\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'enum': 'RefTrigType',
        'lv_property': 'Triggers:Ref:Type',
        'name': 'REF_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150029: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the source terminal for the digital edge Reference Trigger.\n\nThis attribute is used only when the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute is set to NIRFSA_VAL_DIGITAL_EDGE.\n\n**Defined Values:**\n\n%enum_table{output term}\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'lv_property': 'Triggers:Ref:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_REF_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150030: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the active edge for the Reference Trigger.\n\nThis attribute is used only when the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute is set to NIRFSA_VAL_DIGITAL_EDGE.\n\n**Defined Values:**\n\n%enum_table{ref trig dig edge edge}\n\n**Default Value**: NIRFSA_VAL_RISING_EDGE\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureDigitalEdgeRefTrigger'
        },
        'enum': 'RefTrigDigEdgeEdge',
        'lv_property': 'Triggers:Ref:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_REF_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150032: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for the exported Reference Trigger.\n\n**Defined Values:**\n\n%enum_table{export output term}\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ExportSignal'
        },
        'enum': 'ExportOutputTerm',
        'lv_property': 'Triggers:Ref:Export:Output Terminal',
        'name': 'EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150033: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the minimum time, in seconds, that must elapse after the Start Trigger is received before the device recognizes a Reference Trigger.\n\n**Units:** seconds\n\n**Default Value**: 0\n\n**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Triggers:Ref:Advanced:Start To Ref Trigger Holdoff (s)',
        'name': 'START_TO_REF_TRIGGER_HOLDOFF',
        'type': 'ViReal64'
    },
    1150034: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the minimum time, in seconds, that must elapse between Reference Triggers of two records. \n\nThe device does not recognize the Reference Trigger of the next record before this minimum time elapses.\n\n**Units:**: seconds\n\n**Default Value**: 0\n\n**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Triggers:Ref:Advanced:Ref To Ref Trigger Holdoff (s)',
        'name': 'REF_TO_REF_TRIGGER_HOLDOFF',
        'type': 'ViReal64'
    },
    1150035: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the number of pretrigger samples the samples acquired before the Reference Trigger is received to be acquired per record.\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureDigitalEdgeRefTrigger\n- nirfsa_ConfigureSoftwareEdgeRefTrigger\n- nirfsa_ConfigureIqPowerEdgeRefTrigger'
        },
        'lv_property': 'Triggers:Ref:Pretrigger Samples',
        'name': 'REF_TRIGGER_PRETRIGGER_SAMPLES',
        'type': 'ViInt64'
    },
    1150036: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether you want the Advance Trigger to be a digital edge or software trigger.\n\n----\n**Note**\nSet this attribute to NIRFSA_VAL_NONE if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM or if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function.\n\n----\n\n**Defined Values:**\n\n%enum_table{advance trig type}\n\n**Default Value**: NIRFSA_VAL_NONE\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'enum': 'AdvanceTrigType',
        'lv_property': 'Triggers:Advance:Type',
        'name': 'ADVANCE_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150037: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the source terminal for the Advance Trigger.\n\nThis attribute is used only when the NIRFSA_ATTR_ADVANCE_TRIGGER_TYPE attribute is set to NIRFSA_VAL_DIGITAL_EDGE.\n\n**Defined Values:**\n\n%enum_table{output term}\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureDigitalEdgeRefTrigger'
        },
        'lv_property': 'Triggers:Advance:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_ADVANCE_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150038: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for the exported Advance Trigger.\n\n**Defined Values:**\n\n%enum_table{export output term}\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ExportSignal'
        },
        'enum': 'ExportOutputTerm',
        'lv_property': 'Triggers:Advance:Export:Output Terminal',
        'name': 'EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150039: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether you want the Arm Reference Trigger to be a digital edge or software trigger.\n\n----\n**Note**\nThe PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841 only support NIRFSA_VAL_NONE.\n\n----\n\n----\n**Note**\nSet this attribute to NIRFSA_VAL_NONE if you set the NIRFSA_ATTR_ACQUISITION_TYPE attribute to NIRFSA_VAL_SPECTRUM or if you set the **acquisitionType** parameter to NIRFSA_VAL_SPECTRUM using the nirfsa_ConfigureAcquisitionType function.\n\n----\n\n**Defined Values:**\n\n%enum_table{arm ref trig type}\n\n**Default Value**: NIRFSA_VAL_NONE\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'enum': 'ArmRefTrigType',
        'lv_property': 'Triggers:Arm Ref:Type',
        'name': 'ARM_REF_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150040: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the source terminal for the digital edge Arm Reference Trigger.\n\nThis attribute is used only when the NIRFSA_ATTR_ARM_REF_TRIGGER_TYPE attribute is set to NIRFSA_VAL_DIGITAL_EDGE.\n\n**Defined Values:**\n\n%enum_table{output term}\n\n**Default Value**: "" (empty string)\n\n----\n**Note**\nThe PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841 devices only support "" (empty string).\n\nThe trigger is received on PFI0 from the front panel DIO terminal.\n\nThe trigger is received on PFI1 from the front panel DIO terminal.\n\nThe trigger is received on PFI2 from the front panel DIO terminal.\n\nThe trigger is received on PFI3 from the front panel DIO terminal.\n\nThe trigger is received on PFI4 from the front panel DIO terminal.\n\nThe trigger is received on PFI5 from the front panel DIO terminal.\n\nThe trigger is received on PFI6 from the front panel DIO terminal.\n\nThe trigger is received on PFI7 from the front panel DIO terminal.\n\n----\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_'
        },
        'lv_property': 'Triggers:Arm Ref:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_ARM_REF_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150041: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for the Ready for Start Event.\n\n| Value                                           | Description                                                                                                                                                                   |\n|:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| NIRFSA_VAL_DO_NOT_EXPORT_STR ("")          | The signal is not exported.                                                                                                                                        |\n| NIRFSA_VAL_CLK_OUT_STR ("ClkOut")          | The signal is exported to the CLK OUT connector on the PXIe-5622/5624 front panel.                                                                                 |\n| NIRFSA_VAL_REF_OUT_STR ("RefOut")          | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652 and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841. |\n| NIRFSA_VAL_REF_OUT2_STR ("RefOut2")        | The signal is exported to the REF OUT2 terminal on the LO. This connector exists only on the PXIe-5652.                                                            |\n| NIRFSA_VAL_PFI0_STR ("PFI0")               | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.                                    |\n| NIRFSA_VAL_PFI1_STR ("PFI1")               | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.                                                                                       |\n| NIRFSA_VAL_PXI_TRIG0_STR ("PXI_Trig0")     | The signal is exported to the PXI trigger line 0.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG1_STR ("PXI_Trig1")     | The signal is exported to the PXI trigger line 1.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG2_STR ("PXI_Trig2")     | The signal is exported to the PXI trigger line 2.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG3_STR ("PXI_Trig3")     | The signal is exported to the PXI trigger line 3.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG4_STR ("PXI_Trig4")     | The signal is exported to the PXI trigger line 4.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG5_STR ("PXI_Trig5")     | The signal is exported to the PXI trigger line 5.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG6_STR ("PXI_Trig6")     | The signal is exported to the PXI trigger line 6.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG7_STR ("PXI_Trig7")     | The signal is exported to the PXI trigger line 7.                                                                                                                  |\n| NIRFSA_VAL_PXI_STAR_STR ("PXI_Star")       | The signal is exported to the PXI star trigger line.                                                                                                               |\n| NIRFSA_VAL_PXIE_DSTARC_STR ("PXIe_DStarC") | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                      |\n| NIRFSA_VAL_DIO_PFI0_STR ("DIO/PFI0")           | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI1_STR("DIO/PFI1")           | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI2_STR ("DIO/PFI2")           | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI3_STR ("DIO/PFI3")           | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI4_STR ("DIO/PFI4")           | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI5_STR ("DIO/PFI5")           | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI6_STR ("DIO/PFI6")           | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI7_STR ("DIO/PFI7")           | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                 |\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ExportSignal'
        },
        'enum': 'ExportOutputTerm',
        'lv_property': 'Events:Ready For Start:Output Terminal',
        'name': 'EXPORTED_READY_FOR_START_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150042: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for the Ready for Advance Event.\n\n| Value                                           | Description                                                                                                                                                                   |\n|:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| NIRFSA_VAL_DO_NOT_EXPORT_STR ("")          | The signal is not exported.                                                                                                                                        |\n| NIRFSA_VAL_CLK_OUT_STR ("ClkOut")          | The signal is exported to the CLK OUT connector on the PXIe-5622/5624 front panel.                                                                                 |\n| NIRFSA_VAL_REF_OUT_STR ("RefOut")          | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652 and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841. |\n| NIRFSA_VAL_REF_OUT2_STR ("RefOut2")        | The signal is exported to the REF OUT2 terminal on the LO. This connector exists on only the PXIe-5652.                                                            |\n| NIRFSA_VAL_PFI0_STR ("PFI0")               | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.                                    |\n| NIRFSA_VAL_PFI1_STR ("PFI1")               | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.                                                                                       |\n| NIRFSA_VAL_PXI_TRIG0_STR ("PXI_Trig0")     | The signal is exported to the PXI trigger line 0.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG1_STR ("PXI_Trig1")     | The signal is exported to the PXI trigger line 1.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG2_STR ("PXI_Trig2")     | The signal is exported to the PXI trigger line 2.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG3_STR ("PXI_Trig3")     | The signal is exported to the PXI trigger line 3.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG4_STR ("PXI_Trig4")     | The signal is exported to the PXI trigger line 4.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG5_STR ("PXI_Trig5")     | The signal is exported to the PXI trigger line 5.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG6_STR ("PXI_Trig6")     | The signal is exported to the PXI trigger line 6.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG7_STR ("PXI_Trig7")     | The signal is exported to the PXI trigger line 7.                                                                                                                  |\n| NIRFSA_VAL_PXI_STAR_STR ("PXI_Star")       | The signal is exported to the PXI star trigger line.                                                                                                               |\n| NIRFSA_VAL_PXIE_DSTARC_STR ("PXIe_DStarC") | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                      |\n| NIRFSA_VAL_DIO_PFI0_STR ("DIO/PFI0")           | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI1_STR("DIO/PFI1")           | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI2_STR ("DIO/PFI2")           | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI3_STR ("DIO/PFI3")           | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI4_STR ("DIO/PFI4")           | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI5_STR ("DIO/PFI5")           | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI6_STR ("DIO/PFI6")           | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI7_STR ("DIO/PFI7")           | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                 |\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ExportSignal'
        },
        'enum': 'ExportOutputTerm',
        'lv_property': 'Events:Ready For Advance:Output Terminal',
        'name': 'EXPORTED_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150043: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for the Ready for Reference Event.\n\n| Value                                           | Description                                                                                                                                                                   |\n|:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| NIRFSA_VAL_DO_NOT_EXPORT_STR ("")          | The signal is not exported.                                                                                                                                        |\n| NIRFSA_VAL_CLK_OUT_STR ("ClkOut")          | The signal is exported to the CLK OUT connector on the PXIe-5622/5624 front panel.                                                                                 |\n| NIRFSA_VAL_REF_OUT_STR ("RefOut")          | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652 and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841. |\n| NIRFSA_VAL_REF_OUT2_STR ("RefOut2")        | The signal is exported to the REF OUT2 terminal on the LO. This connector exists on only the PXIe-5652.                                                            |\n| NIRFSA_VAL_PFI0_STR ("PFI0")               | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.                                    |\n| NIRFSA_VAL_PFI1_STR ("PFI1")               | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.                                                                                       |\n| NIRFSA_VAL_PXI_TRIG0_STR ("PXI_Trig0")     | The signal is exported to the PXI trigger line 0.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG1_STR ("PXI_Trig1")     | The signal is exported to the PXI trigger line 1.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG2_STR ("PXI_Trig2")     | The signal is exported to the PXI trigger line 2.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG3_STR ("PXI_Trig3")     | The signal is exported to the PXI trigger line 3.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG4_STR ("PXI_Trig4")     | The signal is exported to the PXI trigger line 4.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG5_STR ("PXI_Trig5")     | The signal is exported to the PXI trigger line 5.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG6_STR ("PXI_Trig6")     | The signal is exported to the PXI trigger line 6.                                                                                                                  |\n| NIRFSA_VAL_PXI_TRIG7_STR ("PXI_Trig7")     | The signal is exported to the PXI trigger line 7.                                                                                                                  |\n| NIRFSA_VAL_PXI_STAR_STR ("PXI_Star")       | The signal is exported to the PXI star trigger line.                                                                                                               |\n| NIRFSA_VAL_PXIE_DSTARC_STR ("PXIe_DStarC") | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                      |\n| NIRFSA_VAL_DIO_PFI0_STR ("DIO/PFI0")           | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI1_STR("DIO/PFI1")           | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI2_STR ("DIO/PFI2")           | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI3_STR ("DIO/PFI3")           | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI4_STR ("DIO/PFI4")           | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI5_STR ("DIO/PFI5")           | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI6_STR ("DIO/PFI6")           | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                 |\n| NIRFSA_VAL_DIO_PFI7_STR ("DIO/PFI7")           | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                 |\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ExportSignal'
        },
        'enum': 'ExportOutputTerm',
        'lv_property': 'Events:Ready For Ref:Output Terminal',
        'name': 'EXPORTED_READY_FOR_REF_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150044: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for the End of Record Event.\n\n**Defined Values:**\n\n%enum_table{export output term}\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_\n\n`Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_\n\n`Signal Routing <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/signal-routing.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ExportSignal'
        },
        'enum': 'ExportOutputTerm',
        'lv_property': 'Events:End Of Record:Output Terminal',
        'name': 'EXPORTED_END_OF_RECORD_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150045: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the reference location within the acquired record from which to begin fetching.\n\n**Defined Values:**\n\n%enum_table{fetch relative to}\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'enum': 'FetchRelativeTo',
        'lv_property': 'Acquisition:Fetch:Fetch Relative To',
        'name': 'FETCH_RELATIVE_TO',
        'type': 'ViInt32'
    },
    1150046: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the offset relative to the position specified by the NIRFSA_ATTR_FETCH_RELATIVE_TO attribute from which to start fetching data. \n\nOffset can be a positive or negative value.\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Acquisition:Fetch:Fetch Offset',
        'name': 'FETCH_OFFSET',
        'type': 'ViInt64'
    },
    1150047: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the number of records the RF vector signal analyzer has acquired.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Acquisition:Fetch:Records Done',
        'name': 'RECORDS_DONE',
        'type': 'ViInt64'
    },
    1150048: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables use of the digital equalization filter for the RF downconverter.\n\n**PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: The only valid value for this attribute is VI_TRUE.\n\n----\n**Note**\nFor PXIe-5665/5667 devices, digital IF equalization is supported only with a 150 MHz clock. You cannot set this attribute to VI_TRUE if the NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE attribute is set to NIRFSA_VAL_LO_REF_CLK_STR.\n\n----\n\n----\n**Note**\nFor the PXIe-5665 (14 GHz)/5667 (7 GHz)/5668, the preselector is not part of the IF filter path, so NI-RFSA does not equalize the preselector distortions.\n\n----\n\n**Defined Values:**\n\n|Value          | Description                                                          |\n|:---------|:----------------------------------------------------------|\n| VI_TRUE  | Enables digital IF equalization on the RF downconverter.  |\n| VI_FALSE | Disables digital IF equalization on the RF downconverter. |\n\n**Default Value**: VI_TRUE, if the device configuration is supported.\n\n**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841'
        },
        'lv_property': 'Signal Path:Digital IF Equalization Enabled',
        'name': 'DIGITAL_IF_EQUALIZATION_ENABLED',
        'type': 'ViBoolean'
    },
    1150049: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the size of the window used in the fast Fourier transform (FFT), in terms of the number of samples in the window.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Acquisition:Spectrum:FFT Window Size',
        'name': 'FFT_WINDOW_SIZE',
        'type': 'ViInt32'
    },
    1150050: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the size of the fast Fourier transform (FFT).\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Acquisition:Spectrum:FFT Size',
        'name': 'FFT_SIZE',
        'type': 'ViInt32'
    },
    1150051: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the current temperature, in degrees Celsius, of the module.\n\n**PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860**: If you query this attribute during RF list mode, list steps may take longer to complete during list execution.\n\n**PXIe-5830/5831/5832**: To use this attribute, you must first set the channelName parameter of the nirfsa_SetAttributeViReal64 function to using the appropriate string for your instrument configuration. Setting the nirfsa_SetAttributeViReal64 attribute is not required for the PXIe-3621/3622. Refer to the following table to determine which strings are valid for your configuration.\n\n| Hardware Module               |         TRX Port Type          | Active Channel String     |\n|:------------------------------|:------------------------------:|:--------------------------|\n| PXIe-3621/3622/5842           |            -                    | if or "" (empty string)   |\n| PXIe-5820                     |            -                    | fpga                      |\n| PXIe-5860                     |            -                    | 5860 or "" (empty string) |\n| First connected mmRH-5582     |     DIRECT TRX PORTS Only      | rf0                       |\n| First connected mmRH-5582     |   SWITCHED TRX PORTS [0-7]   | rf0switch0                |\n| First connected mmRH-5582     |   SWITCHED TRX PORTS [8-15]   | rf0switch1                |\n| Second connected mmRH-5582    |     DIRECT TRX PORTS Only      | rf1                       |\n| Second connected mmRH-5582    |   SWITCHED TRX PORTS [0-7]   | rf1switch0                |\n| Second connected mmRH-5582    |   SWITCHED TRX PORTS [8-15]   | rf1switch1                |\n| First connected RMM-5544/5546 |             -                   | rmm0                      |\n| Second connected RMM-5544/5546 |            -                   | rmm1                      |\n\n**Units**: degrees Celcius\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:Device Temperature (Degrees C)',
        'name': 'DEVICE_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150053: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the serial number of the RF downconverter module.\n\n----\n**Note**\nFor the PXIe-5644/5645/5646 and PXIe-5820/5840/5841, this attribute returns the serial number of the VST module. For the PXIe-5830/5831/5832, this attribute returns the serial number of the PXIe-3621/3622.\n\n----\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:Serial Number',
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    1150054: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for the Done Event.\n\n**Defined Values:**\n\n%enum_table{export output term}\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ExportSignal'
        },
        'enum': 'ExportOutputTerm',
        'lv_property': 'Events:Done:Output Terminal',
        'name': 'EXPORTED_DONE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150055: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the channel from which the device monitors the trigger. \n\nNI-RFSA currently supports only 0 as the value of this attribute.\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureIqPowerEdgeRefTrigger'
        },
        'lv_property': 'Triggers:Ref:IQ Power Edge:Source',
        'name': 'IQ_POWER_EDGE_REF_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150056: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the power level, in dBm, at which the device triggers. \n\nThe device asserts the trigger when the signal crosses the level specified by the value of this attribute, taking into consideration the specified slope. If you are using external gain, refer to the NIRFSA_ATTR_EXTERNAL_GAIN attribute for more information about how this attribute affects the I/Q power edge trigger level.\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureIqPowerEdgeRefTrigger'
        },
        'lv_property': 'Triggers:Ref:IQ Power Edge:Level',
        'name': 'IQ_POWER_EDGE_REF_TRIGGER_LEVEL',
        'type': 'ViReal64'
    },
    1150057: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the device asserts the trigger when the signal power is rising or falling. \n\nWhen you set the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute to NIRFSA_VAL_IQ_POWER_EDGE, the device asserts the trigger when the signal power exceeds the specified level with the slope you specify.\n\n**Defined Values:**\n\n%enum_table{ref trig iq pwr edge slope}\n\n**Default Value**: NIRFSA_VAL_RISING_SLOPE\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureIqPowerEdgeRefTrigger'
        },
        'enum': 'RefTrigIqPwrEdgeSlope',
        'lv_property': 'Triggers:Ref:IQ Power Edge:Slope',
        'name': 'IQ_POWER_EDGE_REF_TRIGGER_SLOPE',
        'type': 'ViInt32'
    },
    1150058: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies a time duration, in seconds, for which the signal must be quiet before the device arms the trigger. \n\nThe signal is quiet when it is below the trigger level if the trigger slope, specified by the NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_SLOPE attribute, is set to NIRFSA_VAL_RISING_SLOPE or when it is above the trigger level if the trigger slope is set to NIRFSA_VAL_FALLING_SLOPE.\n\nBy default, this value is set to 0, which means the device does not wait for a quiet time before arming the trigger. This attribute is useful to trigger the acquisition on signals containing repeated bursts, but for which each burst may have large changes in signal power within itself. By configuring the minimum quiet time to the time between bursts, you can ensure that the trigger occurs at the beginning of a burst rather than at the signal power change within a burst.\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Triggers:Ref:Minimum Quiet Time',
        'name': 'REF_TRIGGER_MINIMUM_QUIET_TIME',
        'type': 'ViReal64'
    },
    1150059: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the expected carrier frequency of the incoming signal for demodulation. \n\nThe NI-RFSA device tunes to this frequency. NI-RFSA may coerce this value based on hardware settings and the RF downconverter specifications.\n\n----\n**Note**\nFor the PXIe-5645, this attribute is ignored if you are using the I/Q ports.\n\n----\n\n**Units**: hertz (Hz)\n\n**Default Values**:\n\n**PXIe-5644/5645/5646, PXIe-5840/5841/5860, PXIe-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options)**: 1 GHz\n\n**PXIe-5842 (4 GHz bandwidth option) using the Standard personality**: 1 GHz\n\n**PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality**: 6.5 GHz\n\n**PXIe-5820**: 0 Hz\n\n**PXIe-5830/5831/5832**: 6.5 GHz\n\n**All other devices**: 100 MHz\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Carrier Wave <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/fund-carrierwave.html>`_\n\n`I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_ConfigureIqCarrierFrequency'
        },
        'lv_property': 'Acquisition:IQ:IQ Carrier Frequency',
        'name': 'IQ_CARRIER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150060: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the trigger delay time, in seconds. \n\nThe trigger delay time is the length of time the IF digitizer waits after it receives the trigger before it asserts the Reference Event.\n\n**Units:**: seconds\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Triggers:Ref:Advanced:Ref Trigger Delay (s)',
        'name': 'REF_TRIGGER_DELAY',
        'type': 'ViReal64'
    },
    1150061: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Indicates the minimum time between temperature sensor readings in seconds. \n\nWhen you call the nirfsa_ReadPowerSpectrumF64 function, the nirfsa_ReadIqSingleRecordComplexF64 function, or the nirfsa_Initiate function, NI-RFSA checks whether at least the amount of time specified by this attribute has elapsed before reading the hardware temperature.\n\n----\n**Note**\nNI-RFSA ignores this attribute if you call the nirfsa_PerformThermalCorrection function or read the NIRFSA_ATTR_DOWNCONVERTER_GAIN attribute.\n\n----\n\n**Default Value**: 30 seconds\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:Temperature Read Interval',
        'name': 'TEMPERATURE_READ_INTERVAL',
        'type': 'ViReal64'
    },
    1150065: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the net signal gain for the NI-RFSA device at the current NI-RFSA settings and temperature. \n\nNI-RFSA scales the acquired I/Q and spectrum data from the digitizer using the value of this attribute.\n\nFor a vector signal analyzer (VSA), the system is defined as the RF downconverter and all interfaces between the RF IN connector on the RF downconverter front panel and the IF IN connector on the digitizer front panel. For a spectrum monitoring receiver, the system is defined as the RF preselector, RF downconverter, and IF conditioning modules including all interfaces between the RF IN connector on the RF preselector module front panel and the IF IN connector on the digitizer front panel.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Vertical:Downconverter Gain (dB)',
        'name': 'DOWNCONVERTER_GAIN',
        'type': 'ViReal64'
    },
    1150067: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the loop bandwidth of the RF downconverter tuning PLLs. \n\nTo set this attribute, the NI-RFSA device must be in the Configuration state.\n\n**PXI-5600/5661** : For signal bandwidths greater than 10 MHz, NIRFSA_VAL_WIDE is the only value supported for this attribute.\n\n**PXIe-5601/5663/5663E** : The PXIe-5601 does not support the NIRFSA_VAL_MEDIUM value. This attribute is not supported if you are using an external LO.\n\n**PXIe-5830/5831/5832/5840/5841/5842** : The PXIe-5840/5841/5842 supports only NIRFSA_VAL_MEDIUM for this attribute. This attribute is not supported if you are using an external LO.\n\nTo use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsa_SetAttributeViInt32 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n**Defined Values:**\n\n%enum_table{downconverter loop bandwidth}\n\n**Default Values**:\n\n**PXI-5600** : NIRFSA_VAL_WIDE\n\n**PXIe-5601** : NIRFSA_VAL_NARROW\n\n**PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842** : NIRFSA_VAL_MEDIUM\n\n**Supported Devices**: PXI-5600, PXIe-5601 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E, PXIe-5830/5831/5832/5840/5841/5842'
        },
        'enum': 'DownconverterLoopBandwidth',
        'lv_property': 'Signal Path:Advanced:Downconverter Loop Bandwidth',
        'name': 'DOWNCONVERTER_LOOP_BANDWIDTH',
        'type': 'ViInt32'
    },
    1150068: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the LO signal frequency for the configured center frequency.\n\nIf you are using the NI RF vector signal analyzer with an external LO, use this attribute to specify the LO frequency that the external LO source passes into the LO IN or LO1 IN connector on the RF downconverter front panel. If you are using an external LO, reading the value of this attribute after configuring the rest of the parameters returns the LO frequency needed by the device.\n\nSet this attribute to the actual LO frequency because NI-RFSA corrects for any difference between expected and actual LO frequencies.\n\nTo use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsa_SetAttributeViReal64 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n**Default Values**:\n\n**PXIe-5694**: 215 MHz\n\n**All other devices**: 0\n\n**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`PXIe-5830 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-configuration.html>`_\n\n`PXIe-5831/5832 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-configuration.html>`_\n\n`PXIe-5841 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-configuration.html>`_'
        },
        'lv_property': 'Signal Path:LO Frequency',
        'name': 'LO_FREQUENCY',
        'type': 'ViReal64'
    },
    1150069: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the LO injection side.\n\n**PXIe-5601/5663/5663E**: For frequencies below 517.5 MHz or above 6.4125 GHz, the LO injection side is fixed and NI-RFSA returns an error if you specify the incorrect value. If you do not configure this attribute, NI-RFSA selects the default LO injection side based on the downconverter center frequency. Reset this attribute to return to automatic behavior.\n\n**PXIe-5603/5605/5665 (3.6 GHz)/5667 (3.6 GHz)**: Setting this attribute to NIRFSA_VAL_LO_INJECTION_LOW_SIDE is not supported for this device.\n\n**PXIe-5605/5665 (14 GHz)/5667 (7 GHz)**: Setting this attribute to NIRFSA_VAL_LO_INJECTION_LOW_SIDE is supported for this device for frequencies greater than 4 GHz, but this configuration is not calibrated, and device specifications are not guaranteed.\n\n**PXIe-5606/5668**: Setting this attribute to NIRFSA_VAL_LO_INJECTION_LOW_SIDE is supported for certain frequencies in high band, varying by final IF frequency. This configuration is not calibrated and device specifications are not guaranteed.\n\n**Defined Values:**\n\n%enum_table{lo injection}\n\n**Default Values**:\n\n**PXIe-5601 (external digitizer mode), PXIe-5663/5663E (frequencies < 3.0 GHz)**: NIRFSA_VAL_LO_INJECTION_HIGH_SIDE\n\n**PXIe-5601 (external digitizer mode), PXIe-5663/5663E (frequencies  3.0 GHz)**: NIRFSA_VAL_LO_INJECTION_LOW_SIDE\n\n**PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668**: NIRFSA_VAL_LO_INJECTION_HIGH_SIDE\n\n**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668'
        },
        'enum': 'LoInjection',
        'lv_property': 'Signal Path:Advanced:LO Injection Side',
        'name': 'LO_INJECTION_SIDE',
        'type': 'ViInt32'
    },
    1150070: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the vertical range of the digitizer.\n\nThe vertical range is defined as the absolute value of the input range for a channel. The default vertical range works for all device configurations, but you can use this attribute to optimize performance if you know that the signal level at the digitizer input terminal is low.\n\n----\n**Note**\nFor most applications, NI-RFSA selects an appropriate value for this attribute.\n\n----\n\nThis value is expressed in volts. For example, to acquire a sine wave that spans between 20130.5 V and +0.5 V, set this attribute to 1.0.\n\n**PXIe-5840/5841/5842/5860**: This attribute is read-only.\n\n**Default Value**: 1.0\n\n**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5840/5841/5842/5860'
        },
        'lv_property': 'Vertical:Digitizer Vertical Range',
        'name': 'DIGITIZER_VERTICAL_RANGE',
        'type': 'ViReal64'
    },
    1150071: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether fractional resampling is enabled on the digitizer. \n\nFractional resampling allows the digitizer to achieve very fine resolution on the I/Q rate value. Setting this attribute to VI_FALSE improves spectral performance.\n\n**PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: The only valid value for this attribute is VI_TRUE.\n\n**PXIe-5668**: When using a 400 MHz FPGA image, the only valid value for this attribute is VI_TRUE. When using a 800 MHz FPGA image, the only valid value for this attribute is VI_FALSE. Refer to `NI-RFSA Instrument Driver FPGA Extensions <https://www.ni.com/docs/en-US/bundle/ni-rf-vst/page/rfsa-rfsg-instrument-driver-fpga-extensions.html>`_ for more information about FPGA images.\n\n**Defined Values:**\n\n| Value         | Description                                |\n|:---------|:--------------------------------|\n| VI_TRUE  | Enables fractional resampling.  |\n| VI_FALSE | Disables fractional resampling. |\n\n**Default Value**: VI_TRUE\n\n**Supported Devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Signal Path:Fractional Resample Enabled',
        'name': 'ENABLE_FRACTIONAL_RESAMPLING',
        'type': 'ViBoolean'
    },
    1150072: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies a comma-separated list of the terminals at which to export the Reference Clock.\n\n**Defined Values:**\n\n%enum_table{ref clk exported term}\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_ExportSignal'
        },
        'enum': 'RefClkExportedTerm',
        'lv_property': 'Clocking:Ref Clock Exported Terminal',
        'name': 'EXPORTED_REF_CLOCK_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150074: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the device attenuation to a value that has the actual calibrated IF attenuation closest to the desired value.\n\n**Valid Values**: 0 to 30\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5601/5603/5605 (external digitizer mode), PXIe-5663/5663E/5665/5667, PXIe-5693'
        },
        'lv_property': 'Signal Path:Advanced:NI 5663:IF Attenuation (dB)',
        'name': 'IF_ATTENUATION',
        'type': 'ViReal64'
    },
    1150075: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the desired IF filter path, regardless of the RF band chosen by NI-RFSA.\n\n**Defined Values:**\n\n%enum_table{i ffilter}\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5601'
        },
        'enum': 'IFfilter',
        'lv_property': 'Signal Path:Advanced:NI 5663:IF Filter',
        'name': 'IF_FILTER',
        'type': 'ViInt32'
    },
    1150076: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the value of the RF attenuation from a table of valid configurations. \n\nThis attribute is valid only during a calibration session and when you set the NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED attribute to NIRFSA_VAL_DISABLED.\n\n**Valid Values**: 0 to 64\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5693'
        },
        'lv_property': 'Factory Calibration:NI 5693:RF Attenuation Index',
        'name': 'RF_ATTENUATION_INDEX',
        'type': 'ViInt32'
    },
    1150077: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies which RF attenuator table to use.\n\n**Valid Values**: 0 to 1\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E'
        },
        'lv_property': 'Signal Path:Advanced:NI 5663:RF Attenuation Table',
        'name': 'RF_ATTENUATION_TABLE',
        'type': 'ViInt32'
    },
    1150078: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the IF1 attenuation, in dB. The device IF1 attenuator is set to this nominal value. \n\nUse this attribute, along with the NIRFSA_ATTR_IF2_ATTEN_VALUE attribute, when you set the NIRFSA_ATTR_IF_FILTER attribute to NIRFSA_VAL_BYPASS.\n\n**Valid Values**: 0 to 15\n\n**Units**: dB\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E'
        },
        'lv_property': 'Signal Path:Advanced:NI 5663:IF1 Attenuation (dB)',
        'name': 'IF1_ATTEN_VALUE',
        'type': 'ViReal64'
    },
    1150079: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the IF2 attenuation, in dB. The device IF2 attenuator is set to this nominal value. \n\nUse this attribute, along with the NIRFSA_ATTR_IF1_ATTEN_VALUE attribute, when you set the NIRFSA_ATTR_IF_FILTER attribute to NIRFSA_VAL_BYPASS.\n\n**Valid Values**: 0 to 15\n\n**Units**: dB\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E'
        },
        'lv_property': 'Signal Path:Advanced:NI 5663:IF2 Attenuation (dB)',
        'name': 'IF2_ATTEN_VALUE',
        'type': 'ViReal64'
    },
    1150080: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether dithering is enabled on the digitizer.\n\nDithering adds band-limited noise in the analog signal path to help reduce the quantization effects of the A/D converter and improve spectral performance. On the PXIe-5622, this out-of-band noise is added at low frequencies up to approximately 12 MHz. On the PXIe-5624, this out-of-band noise is added at low frequencies up to approximately 50 MHz.\n\n**PXIe-5663/5663E/5665/5667**: When you enable dithering, the maximum signal level is reduced by up to 3 dB. This signal level reduction is accounted for in the nominal input ranges of the PXIe-5622. Therefore, you can overrange the input by up to 3 dB with dither disabled. For example, the +4 dBm input range can handle signal levels up to +7 dBm with dither disabled. For wider bandwidth acquisitions, such as 40 MHz, disable dithering to eliminate residual leakage of the dither signal into the lower frequencies of the IF passband, which starts at 12.5 MHz and ends at 62.5 MHz. This leakage can slightly raise the noise floor in the lower frequencies, thus degrading the performance in high-sensitivity applications. When taking spectral measurements, this leakage can also appear as a wide, low-amplitude signal near 12.5 MHz and 62.5 MHz. The width and amplitude of the signal depends on your resolution bandwidth and the type of time-domain window you apply to your FFT.\n\n**PXIe-5668**: When you enable dithering, the maximum signal level is reduced by up to 2 dB. For the PXIe-5624, the maximum input power with dither off is 8 dBm and the maximum input power with dither on is 6 dBm. When acquiring an 800 MHz bandwidth signal, the I/Q data contains the dither even if the dither signal is not in the displayed spectrum. The dither can affect actions like power level triggering.\n\n----\n**Note**\nFor the PXIe-5668, disabling dithering can negatively affect absolute amplitude accuracy.\n\n----\n\n**Defined Values:**\n\n%enum_table{enable attr vals}\n\n----\n**Note**\nFor the PXIe-5820/5830/5831/5832/5840/5841/5842, only NIRFSA_VAL_ENABLED is supported.\n\n----\n\n**Default Value**: NIRFSA_VAL_ENABLED\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Signal Path:Digitizer Dither Enabled',
        'name': 'DIGITIZER_DITHER_ENABLED',
        'type': 'ViInt32'
    },
    1150081: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the mechanical attenuator is enabled. \n\nSet this attribute to NIRFSA_VAL_ENABLED to allow NI-RFSA to use the mechanical attenuator.\n\nDisabling this attenuator can improve device performance. Refer to `PXIe-5663/5663E Programming Attenuation <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/programming-attenuation.html>`_ for more information about the attenuators.\n\n**Defined Values:**\n\n%enum_table{enable attr vals}\n\n**Default Value**: NIRFSA_VAL_ENABLED\n\n**Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Vertical:Advanced:NI 5663:Mechanical Attenuator Enabled',
        'name': 'MECHANICAL_ATTENUATOR_ENABLED',
        'type': 'ViInt32'
    },
    1150082: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables in-band retuning and specifies the current frequency, in hertz (Hz), of the RF downconverter. \n\nIf you set this attribute, any measurements outside the instantaneous bandwidth of the device are invalid. To disable in-band retuning, reset the attribute or call the nirfsa_ResetDevice function.\n\nAfter you set this attribute, the downconverter is locked to that frequency until the value is changed or the attribute is reset. Locking the downconverter to a fixed value allows frequencies within the instantaneous bandwidth of the downconverter to be measured with minimal overhead, decreasing tuning time.\n\n**Valid Values**: Any supported tuning frequency of the device\n\n**PXIe-5820**: The only valid value for this attribute is 0 Hz.\n\n**Default Value**:\n\n**PXIe-5694**: The default value for the PXIe-5694 is 193.6 MHz unless you set the NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED attribute to  NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED, in which case the default value is 187.5 MHz.\n\n**All other devices**: The carrier frequency or spectrum center frequency. NI-RFSA sets this attribute to the default value based on the value of the NIRFSA_ATTR_ACQUISITION_TYPE attribute.\n\n**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Acquisition:Advanced:Downconverter Center Frequency',
        'name': 'DOWNCONVERTER_CENTER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150083: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the RF path to use during calibration.\n\nThis attribute is valid only during a calibration session. When you set this attribute, NI-RFSA does not select the RF path based on the downconverter center frequency.\n\nThe following table lists the RF bands used by the supported devices.\n\n| Device                                               | RF Band   | Frequency Range      |\n|:-----------------------------------------------------|:----------|:---------------------|\n| PXIe-5603                                            | RF band 1 | 20 Hz to 3.6 GHz     |\n| PXIe-5605 (low band signal path)                     | RF band 1 | 20 Hz to 3.6 GHz     |\n| PXIe-5605 (high band signal path)                    | RF band 2 | 3.6 GHz to 14 GHz    |\n| PXIe-5606 (low band signal path)                     | RF band 1 | 20 Hz to 3.6 GHz     |\n| PXIe-5606 (high band signal path)                    | RF band 2 | 3.6 GHz to 26.5 GHz  |\n| PXIe-5606 (low band signal path, 320 MHz IF filter)  | RF band 1 | 20 Hz to 3.41 GHz    |\n| PXIe-5606 (high band signal path, 320 MHz IF filter) | RF band 2 | 3.41 GHz to 26.5 GHz |\n\n**Defined and Valid Values:**\n\n| Value                                  | Description                 | Valid For                |\n|:---------------------------------------|:----------------------------|:-------------------------|\n| NIRFSA_VAL_EXT_CAL_RF_BAND_1 (1700)    | Specifies to use RF band 1. | PXIe-5601/5603/5605/5606 |\n| NIRFSA_VAL_EXT_CAL_RF_BAND_2 (1701)    | Specifies to use RF band 2. | PXIe-5601/5605/5606      |\n| NIRFSA_VAL_EXT_CAL_RF_BAND_3 (1702)    | Specifies to use RF band 3. | PXIe-5601                |\n| NIRFSA_VAL_EXT_CAL_RF_BAND_4 (1703)    | Specifies to use RF band 4. | PXIe-5601                |\n\n**Default Values**:\n\n**PXIe-5603/5605 (low band)/5606**: NIRFSA_VAL_EXT_CAL_RF_BAND_1\n\n**PXIe-5601/5605 (high band)**: NIRFSA_VAL_EXT_CAL_RF_BAND_2\n\n**Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5698'
        },
        'enum': 'RfPathSel',
        'lv_property': 'Factory Calibration:NI 5665/5668R:RF Path Selection',
        'name': 'CAL_RF_PATH_SELECTION',
        'type': 'ViInt32'
    },
    1150085: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the digitizer onboard memory size, in bytes.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:Memory Size',
        'name': 'MEMORY_SIZE',
        'type': 'ViInt64'
    },
    1150086: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the center frequency of the IF output signal that corresponds to the configured RF center frequency.\n\nThe downconverter translates the RF input frequency to the IF output frequency by mixing it with the LO signal. The nominal values for the IF output frequency are shown in the following table.\n\n| Downconverter | Nominal IF Output Frequency |\n|:--------------|:---------------------------|\n| PXI-5600 | 15 MHz |\n| PXIe-5601 | 53 MHz or 187.5 MHz |\n| PXIe-5603 | 187.5 MHz or 199 MHz |\n| PXIe-5605 | 187.5 MHz, 190 MHz, or 199 MHz |  \n| PXIe-5606 | 187.5 MHz, 190 MHz, 199 MHz, 507.5 MHz, or 730 MHz |\n| PXIe-5694 | - signal_conditioning_enabled set to SIGNAL_CONDITIONING_ENABLED and if_conditioning_down_conversion_enabled set to disabled: 193.6 MHz<br>- if_conditioning_down_conversion_enabled set to enabled: 21.4 MHz<br>- signal_conditioning_enabled set to SIGNAL_CONDITIONING_BYPASSED: 162.5 MHz to 212.5 MHz |\n\nThe coarse nature of the LO settings can cause the downconverter to be unable to tune to the exact LO frequency that would produce the nominal IF output frequency. Any coercion in the actual LO frequency results in the IF output frequency being slightly off from the nominal value.\n\nAdditionally, if you use the NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY and NIRFSA_ATTR_LO_FREQUENCY attributes to program the downconverter, the IF output frequency could vary from the nominal value. NI-RFSA adjusts the acquired spectrum or I/Q data for the difference between nominal and actual IF output frequency. If you use an external digitizer with a RF downconverter, use this attribute to specify the actual IF output frequency.\n\n**Default Value**: N/A\n\n**Supported Devices**:PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694'
        },
        'lv_property': 'Acquisition:Advanced:IF Output Frequency',
        'name': 'IF_OUTPUT_FREQUENCY',
        'type': 'ViReal64'
    },
    1150087: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the delay duration units and interpretation for LO settling. \n\nSpecify the actual settling value using the NIRFSA_ATTR_FREQUENCY_SETTLING attribute. This attribute is not supported if you are using an external LO.\n\n**Defined Values:**\n\n%enum_table{frequency settling units}\n\n**Default Value**: NIRFSA_VAL_FSU_PPM\n\n**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842'
        },
        'enum': 'FrequencySettlingUnits',
        'lv_property': 'Signal Path:Advanced:Frequency Settling Units',
        'name': 'FREQUENCY_SETTLING_UNITS',
        'type': 'ViInt32'
    },
    1150088: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the value used for local oscillator (LO) frequency settling. \n\nThe units and interpretation for this scalar value are specified using the NIRFSA_ATTR_FREQUENCY_SETTLING_UNITS attribute. This attribute is not supported if you are using an external LO.\n\nThe valid values for this attribute depend on the NIRFSA_ATTR_FREQUENCY_SETTLING_UNITS attribute.\n\n| Device | NIRFSA_VAL_FSU_SECONDS_AFTER_LOCK | NIRFSA_VAL_FSU_SECONDS_AFTER_IO | %enum_value{frequency settling units.fsu \nppm} |\n|:-------|:----------------------------------|:--------------------------------|:------------------|\n| PXIe-5663/5663E | 2 microseconds<sup>1</sup> to 80 milliseconds, resolution of approximately 2 microseconds | 0 microseconds to 80 milliseconds<sup>2</sup>, resolution of 1 microsecond | 1.0, 0.1, 0.01 |\n| PXIe-5665/5667/5668 | 4 microseconds to 80 milliseconds, resolution of approximately 4 microseconds | 0 microseconds to 80 milliseconds<sup>2</sup>, resolution of 1 microsecond | 1.0, 0.1, 0.01, 0.001 |\n| PXIe-5644/5645/5646 | 1 microsecond<sup>1</sup> to 65 milliseconds, resolution of 1 microsecond | 1 microsecond<sup>1</sup> to 65 milliseconds, resolution of 1 microsecond | 1.0, 0.1, 0.01 |\n| PXIe-5830/5831/5832/5840/5841/5842 | 1 microsecond<sup>1</sup> to 10 seconds, resolution of 1 microsecond | 0 microseconds to 10 seconds, resolution of 1 microsecond | 1.0 to 0.01 |\n| PXIe-5831/5832 with PXIe-5653 (using PXIe-3622 LO)<sup>3</sup> | 1 microsecond<sup>1</sup> to 10 seconds, resolution of 1 microsecond | 0 microseconds to 10 seconds, resolution of 1 microsecond | 1.0 to 0.01 |\n| PXIe-5831/5832 with PXIe-5653 (using PXIe-5653 LO)<sup>3</sup> | 4 microseconds to 80 milliseconds, resolution of approximately 4 microseconds | 0 microseconds to 80 milliseconds, resolution of 1 microsecond | 1.0 to 0.01 |\n\n**Notes:**\n1. If the frequency settling units attribute is set to NIRFSA_VAL_FSU_SECONDS_AFTER_LOCK and the downconverter loop bandwidth attribute is set to narrow, NI recommends a minimum settling time of 128 microseconds to ensure that the phase-locked loop (PLL) lock stabilizes. If the downconverter loop bandwidth is set to wide, NI recommends a minimum settling time of 16 microseconds.\n2. When in RF list mode, the valid values for NIRFSA_VAL_FSU_SECONDS_AFTER_IO are 0 microseconds to 50 milliseconds.\n3. The valid values for this configuration depend on the module used as the LO source. Refer to the lo source attribute for more information.\n\n**Default Value**: 0.1\n\n**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Signal Path:Advanced:Frequency Settling',
        'name': 'FREQUENCY_SETTLING',
        'type': 'ViReal64'
    },
    1150089: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the current temperature, in degrees Celsius, of the LO module.\n\n**PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode) PXI-5661, PXIe-5663/5663E/5665/5667/5668** This attribute is not supported if you are using an external LO.\n\n**PXIe-5840/5841/5842**: If you query this attribute during RF list mode, list steps may take longer to complete during list execution.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode) PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5840/5841/5842'
        },
        'lv_property': 'Device Characteristics:LO Temperature (Degrees C)',
        'name': 'LO_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150090: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the current temperature, in degrees Celsius, of the digitizer module.\n\n**PXIe-5820/5840/5841/5842**: If you query this attribute during RF list mode, list steps may take longer to complete during list execution.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842'
        },
        'lv_property': 'Device Characteristics:Digitizer Temperature (Degrees C)',
        'name': 'DIGITIZER_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150091: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the revision of the RF downconverter module.\n\n----\n**Note**\nFor the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5840/5841, this attribute returns the revision of the VST module. For the PXIe-5830/5831/5832, this attribute returns the revision of the PXIe-3621/3622\n\n----\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:Module Revision',
        'name': 'MODULE_REVISION',
        'type': 'ViString'
    },
    1150092: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_ to make active for configuration or initiation.\n\nActivating a list makes all attributes in the list reflect the value of the attributes that correspond to the set specified by the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST and the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP attributes.\n\nSet this attribute to an empty string to disable RF list mode.\n\n**Default Value**: "" (empty string) for devices that support RF list mode. For all other devices, the default value is N/A.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters\n\n**Related Topics**\n\n`RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_CreateConfigurationList'
        },
        'lv_property': 'Configuration List:Active List',
        'name': 'ACTIVE_CONFIGURATION_LIST',
        'type': 'ViString'
    },
    1150093: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the step in the configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_ to make active for configuration or initiation.\n\nActivating a list makes all attributes in the list reflect the value of the attributes that correspond to the set specified by the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST and the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP attributes.\n\n**Default Value**: 0 for devices that support RF list mode. For all other devices, the default value is N/A.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters\n\n**Related Topics**\n\n`RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_CreateConfigurationListStep'
        },
        'lv_property': 'Configuration List:Active Step',
        'name': 'ACTIVE_CONFIGURATION_LIST_STEP',
        'type': 'ViInt64'
    },
    1150094: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the gain, in dB, of a switch (or cable) connected before the RF IN connector of an NI-RFSA system. \n\nWhen you set this attribute, NI-RFSA calculates appropriate attenuator settings based on the value of this attribute and the value of the NIRFSA_ATTR_REFERENCE_LEVEL attribute. In this case, NI-RFSA interprets the reference level as the maximum expected power level of the signal at the input of the external gain device. For more information about attenuation, refer to the *Attenuation and Signal Levels* topic for your device in the *NI RF Vector Signal Analyzers Help*.\n\n----\n**Note**\nFor the PXIe-5820, this attribute specifies the gain, in dB, of a switch (or cable) connected before the IQ IN connector.\n\n----\n\n----\n**Note**\nFor the PXIe-5645, this attribute is ignored if you are using the I/Q ports.\n\n----\n\nWith this attribute set, NI-RFSA reads the NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_LEVEL attribute value as the power level at the input of the external gain device at which the NI-RFSA device should trigger.\n\nNegative values indicate attenuation.\n\n**Valid Values**: INF to +INF\n\n**Units**: dB\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Vertical:Advanced:External Gain (dB)',
        'name': 'EXTERNAL_GAIN',
        'type': 'ViReal64'
    },
    1150095: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the list trigger source.\n\nThe default value is the NIRFSA_VAL_END_OF_RECORD_EVENT. When the value is NIRFSA_VAL_END_OF_RECORD_EVENT, this will signal the instrument to reconfigure from configuration N to configuration N + 1 after the End Of Record Event, and before the Ready For Advance Event. If you configure this attribute to any other value, the instrument reconfiguration will occur whenever the specified trigger is asserted, which may be decoupled from the acquisition state machine. Therefore, if you trigger a reconfiguration during a record acquisition, you may see transient data in the record, which should be discarded by the application. NI recommends you to use this attribute only in case of streaming.'
        },
        'lv_property': 'Triggers:Configuration List Step:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150096: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the time, in seconds, that the timer counts before generating a Timer Event.\n\nAfter the timer reaches zero, it automatically restarts.\n\n----\n**Note**\nFor the PXIe-5820/5830/5831/5832/5840/5841/5842 and the PXIe-5842 with S-parameters, this attribute must be set for the timer to start. If you do not set this attribute, the timer is disabled.\n\n----\n\n**Units**: seconds\n\n**Default Value**: 0.01\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters'
        },
        'lv_property': 'Configuration List:Timer Event Interval',
        'name': 'TIMER_EVENT_INTERVAL',
        'type': 'ViReal64'
    },
    1150097: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether peer-to-peer streaming is enabled for the active stream endpoint.\n\nThis attribute is `endpoint based <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/configuring-peer-to-peer-endpoint-ni-rfsa.html>`_.\n\n**Defined Values:**\n\n| Value                | Description                    |\n|:----------------|:--------------------|\n| VI_TRUE (1900)  | Enables streaming.  |\n| VI_FALSE (1901) | Disables streaming. |\n\n**Default Value**: VI_FALSE\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Peer-to-Peer:Enabled',
        'name': 'P2P_ENABLED',
        'type': 'ViBoolean'
    },
    1150098: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the number of peer-to-peer streams supported by the device.\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Peer-to-Peer:FIFO Endpoint Count',
        'name': 'P2P_FIFO_ENDPOINT_COUNT',
        'type': 'ViInt64'
    },
    1150099: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the number of complex samples transferred through the peer-to-peer stream endpoint since the endpoint was last reset.\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Peer-to-Peer:Samples Transferred',
        'name': 'P2P_SAMPLES_TRANSFERRED',
        'type': 'ViInt64'
    },
    1150100: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the current number of complex samples available in the peer-to-peer endpoint.\n\n----\n**Note**\nThe complex samples are composed of two 16-bit words with the I data as the LSB.\n\n----\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Peer-to-Peer:Samples in P2P Endpoint',
        'name': 'P2P_SAMPLES_AVAILABLE_IN_ENDPOINT',
        'type': 'ViInt64'
    },
    1150101: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the largest number of complex samples available in the peer-to-peer endpoint since this attribute was last read.\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Peer-to-Peer:Most Samples in P2P Endpoint',
        'name': 'P2P_MOST_SAMPLES_AVAILABLE_IN_ENDPOINT',
        'type': 'ViInt64'
    },
    1150102: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the size, in samples, of the peer-to-peer endpoint.\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Peer-to-Peer:Endpoint Size',
        'name': 'P2P_ENDPOINT_SIZE',
        'type': 'ViInt64'
    },
    1150103: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Indicates whether the endpoint has overflowed. \n\nAn overflow condition occurs when data is written to the endpoint faster than it can be streamed from it. During an overflow, data in the endpoint begins to be overwritten. Reset the device or close the session to reset the overflow condition.\n\n**Defined Values:**\n\n| Value         | Description                                               |\n|:---------|:-----------------------------------------------|\n| VI_TRUE  | The endpoint has overflowed.                   |\n| VI_FALSE | You can write additional data to the endpoint. |\n\n**Default Value**: VI_FALSE\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Peer-to-Peer:Endpoint Overflow',
        'name': 'P2P_ENDPOINT_OVERFLOW',
        'type': 'ViBoolean'
    },
    1150104: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the maximum bandwidth that the device can consume.\n\n----\n**Note**\nThe NI device limits itself to transfer fewer bytes per second on the PCI Express bus than the value you specify for this attribute.\n\n----\n\n**Default Value**: N/A\n\n**Supported Devices:**: PXI-5661, PXIe-5663/5663E/5665'
        },
        'lv_property': 'Acquisition:Fetch:Data Transfer:Data Transfer Maximum Bandwidth',
        'name': 'DATA_TRANSFER_MAXIMUM_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150105: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the maximum number of samples to transfer at one time from the device to host memory.\n\nIncreasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may increase the amount of page-locked memory required from the system.\n\n**Default Values**:\n\n**PXIe-5668**: 0x2,000,000\n\n**All Other Devices**: 0x400,000\n\n**Supported Devices:**: PXI-5661, PXIe-5663/5663E/5665/5667/5668'
        },
        'lv_property': 'Acquisition:Fetch:Data Transfer:Data Transfer Block Size',
        'name': 'DATA_TRANSFER_BLOCK_SIZE',
        'type': 'ViInt32'
    },
    1150106: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the offset to apply to the initial I and Q phases.\n\n**Valid Values**: 0 to 180\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Acquisition:IQ:Phase Offset',
        'name': 'PHASE_OFFSET',
        'type': 'ViReal64'
    },
    1150107: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether a limit is placed on the number of records and the size of the records by the size of the device onboard memory. \n\nWhen a peer-to-peer stream is enabled and onboard memory is disabled, any fetch calls result in an error.\n\n**Default Value**: VI_FALSE\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Peer-to-Peer:Onboard Memory Enabled',
        'name': 'P2P_ONBOARD_MEMORY_ENABLED',
        'type': 'ViBoolean'
    },
    1150109: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the IF attenuation index from a table of valid settings. \n\nTo select a correct attenuation table, set this attribute in conjunction with the NIRFSA_ATTR_CAL_IF_FILTER_SELECTION attribute. This attribute is valid only during a calibration session.\n\n**Valid Values**: 0 to 25\n\n**Default Value**: 0\n\n**Supported Devices:** PXIe-5694'
        },
        'lv_property': 'Factory Calibration:NI 5665/5668R:IF Attenuation Table Index',
        'name': 'CAL_IF_ATTENUATION_INDEX',
        'type': 'ViInt32'
    },
    1150110: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Selects the value of RF electronic attenuation from a table of valid configurations.\n\nThis attribute is valid only during a calibration session and when you set the NIRFSA_ATTR_CAL_RF_PATH_SELECTION attribute to NIRFSA_VAL_EXT_CAL_RF_BAND_1.\n\n**Default Value**: N/A\n\n**Supported Devices:** PXIe-5603/5605/5606'
        },
        'lv_property': 'Factory Calibration:NI 5665/5668R:RF Electronic Attenuation Table Index',
        'name': 'CAL_RF_ELECTRONIC_ATTENUATION_INDEX',
        'type': 'ViInt32'
    },
    1150111: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Selects the value of the RF mechanical attenuation configuration from a table of valid configurations.\n\nThis attribute is valid only during a calibration session.\n\n**Default Values**:\n\n**PXIe-5603/5605**: 3\n\n**PXIe-5606**: 2\n\n**Supported Devices:** PXIe-5603/5605/5606'
        },
        'lv_property': 'Factory Calibration:NI 5665/5668R:RF Mechanical Attenuation Table Index',
        'name': 'CAL_RF_MECHANICAL_ATTENUATION_INDEX',
        'type': 'ViInt32'
    },
    1150112: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the IF filter path during calibration.\n\nThe attribute is valid only during a calibration session.\n\n**Defined Values:**\n\n%enum_table{i ffilter sel}\n\n**Default Value**: NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_4\n\n**Supported Devices**: PXIe-5694'
        },
        'enum': 'IFfilterSel',
        'lv_property': 'Factory Calibration:NI 5665/5668R:IF Filter Selection',
        'name': 'CAL_IF_FILTER_SELECTION',
        'type': 'ViInt32'
    },
    1150113: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Selects the LO signal path used during calibration.\n\nDuring noncalibration sessions, NI-RFSA implicitly derives the LO signal path from the center frequency. During calibration sessions, you must explicitly specify the LO signal path. This attribute is valid only during a calibration session.\n\n**Defined Values:**\n\n%enum_table{lo path sel}\n\n**Default Value**: NIRFSA_VAL_EXT_CAL_LO_PATH_1\n\n**Supported Devices**: PXIe-5603/5605/5606'
        },
        'enum': 'LoPathSel',
        'lv_property': 'Factory Calibration:NI 5665/5668R:LO Path Selection',
        'name': 'CAL_LO_PATH_SELECTION',
        'type': 'ViInt32'
    },
    1150114: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the LO1 attenuation, in dB, during a calibration session.\n\nThis attribute is valid only during a calibration session.\n\n**Valid Values and Default Values**:\n\n| Device         | Valid Values | Default Value |\n|:---------------|:-------------|:--------------|\n| PXIe-5603/5605 | 0 to 15.5    | 15.5          |\n| PXIe-5606      | 0 to 31      | 31            |\n\n**Supported Devices**: PXIe-5603/5605/5606'
        },
        'lv_property': 'Factory Calibration:NI 5665/5668R:LO1 Attenuation',
        'name': 'CAL_LO1_ATTENUATION',
        'type': 'ViReal64'
    },
    1150115: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the LO2 attenuation, in dB, during a calibration session.\n\nThis attribute is valid only during a calibration session.\n\n**Valid Values and Default Values**:\n\n| Device         | Valid Values | Default Value |\n|:---------------|:-------------|:--------------|\n| PXIe-5603/5605 | 0 to 15.5    | 15.5          |\n| PXIe-5606      | 0 to 31      | 31            |\n\n**Supported Devices**: PXIe-5603/5605/5606'
        },
        'lv_property': 'Factory Calibration:NI 5665/5668R:LO2 Attenuation',
        'name': 'CAL_LO2_ATTENUATION',
        'type': 'ViReal64'
    },
    1150116: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the LO3 attenuation, in dB, during a calibration session. This attribute is valid only during a calibration session.\n\n**Valid Values and Default Values**:\n\n| Device         | Valid Values | Default Value |\n|:---------------|:-------------|:--------------|\n| PXIe-5603/5605 | 0 to 15.5    | 15.5          |\n| PXIe-5606      | 0 to 31      | 31            |\n\n**Supported Devices**: PXIe-5603/5605/5606'
        },
        'lv_property': 'Factory Calibration:NI 5665/5668R:LO3 Attenuation',
        'name': 'CAL_LO3_ATTENUATION',
        'type': 'ViReal64'
    },
    1150117: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the fully qualified signal name as a string.\n\n**Default Values**:\n\n**PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>ReadyForStartEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\n**PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>ReadyForStartEvent</i>, where *ModuleName* is the name of your device in MAX.\n\n**PXIe-5860**: /<i>ModuleName/<i>ai</i>/<i>ChannelNumber</i>/<i>ReadyForStartEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n**All other devices**: /<i>DigitizerName</i>/<i>ReadyForStartEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_GetTerminalName'
        },
        'lv_property': 'Events:Ready For Start:Terminal Name',
        'name': 'READY_FOR_START_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150118: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the fully qualified signal name as a string.\n\n**Default Values**:\n\n**PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>ReadyForAdvanceEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\n**PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>ReadyForAdvanceEvent</i>, where *ModuleName* is the name of your device in MAX.\n\n**PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>ReadyForAdvanceEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n**All other devices**: /<i>DigitizerName</i>ReadyForAdvanceEvent, where *DigitizerName* is the name associated with your digitizer module in MAX.\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_GetTerminalName'
        },
        'lv_property': 'Events:Ready For Advance:Terminal Name',
        'name': 'READY_FOR_ADVANCE_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150119: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the fully qualified signal name as a string.\n\n**PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>ReadyForReferenceEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\n**PXIe-5820/5840/5841/5842**: /<i>ModuleName/<i>ai/0/<i>ReadyForReferenceEvent</i>, where *ModuleName* is the name of your device in MAX.\n\n**PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>ReadyForReferenceEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n**All other devices**: /<i>DigitizerName</i>/<i>ReadyForReferenceEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_GetTerminalName'
        },
        'lv_property': 'Events:Ready For Ref:Terminal Name',
        'name': 'READY_FOR_REF_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150120: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the fully qualified signal name as a string.\n\n**Default Values**:\n\n**PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>EndOfRecordEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\n**PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>EndOfRecordEvent</i>, where *ModuleName* is the name of your device in MAX.\n\n**PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>EndOfRecordEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n**All other devices**: /<i>DigitizerName</i>/<i>EndOfRecordEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_GetTerminalName'
        },
        'lv_property': 'Events:End Of Record:Terminal Name',
        'name': 'END_OF_RECORD_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150121: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the fully qualified signal name as a string.\n\n**Default Values**:\n\n**PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>DoneEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\n**PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>DoneEvent</i>, where *ModuleName* is the name of your device in MAX.\n\n**PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>DoneEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n**All other devices**: /<i>DigitizerName</i>/<i>DoneEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_GetTerminalName'
        },
        'lv_property': 'Events:Done:Terminal Name',
        'name': 'DONE_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150122: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the fully qualified signal name as a string.\n\n**Default Values**:\n\n**PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>StartTrigger</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\n**PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>StartTrigger</i>, where *ModuleName* is the name of your device in MAX.\n\n**PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>StartTrigger</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n**All other devices**: /<i>DigitizerName</i>/StartTrigger</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_GetTerminalName'
        },
        'lv_property': 'Triggers:Start:Terminal Name',
        'name': 'START_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150123: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the fully qualified signal name as a string.\n\n**Default Values**:\n\n**PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>RefTrigger</i>, where *BasebandModule* is the name of your baseband module of your device in MAX.\n\n**PXIe-5820/5840/5841/5842**: /<i>ModuleName/<i>ai</i>/0/<i>RefTrigger</i>, where *ModuleName* is the name of your device in MAX.\n\n**PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>RefTrigger</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n**All other devices**: /<i>DigitizerName</i>/<i>RefTrigger</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsa_GetTerminalName'
        },
        'lv_property': 'Triggers:Ref:Terminal Name',
        'name': 'REF_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150124: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the fully qualified signal name as a string.\n\n**Default Values**:\n\n**PXIe-5830/5831/5832**:  /<i>BasebandModule</i>/<i>ai</i>/0/<i>AdvanceTrigger</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\n**PXIe-5820/5840/5841/5842**: /<i>ModuleNameai</i>/0/<i>AdvanceTrigger</i>, where *ModuleName* is the name of your device in MAX.\n\n**PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>AdvanceTrigger</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n**All other devices**: /<i>DigitizerName</i>/<i>AdvanceTrigger</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_\n\n**High-Level Functions**:\n\n- nirfsa_GetTerminalName'
        },
        'lv_property': 'Triggers:Advance:Terminal Name',
        'name': 'ADVANCE_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150125: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': "Specifies the instantaneous bandwidth of the device in hertz (Hz).\n\nThe instantaneous bandwidth is the effective real-time bandwidth of the signal path for your configuration.\n\nSpecify the maximum instantaneous bandwidth needed for your measurement. NI-RFSA coerces the actual IF filter to use based on other measurement constraints such as the NIRFSA_ATTR_IF_FILTER_BANDWIDTH attribute and the NIRFSA_ATTR_DIGITAL_IF_EQUALIZATION_ENABLED attribute.\n\nTo change the value that NI-RFSA uses for the maximum size of multispan acquisition subspans, use the NIRFSA_ATTR_FFT_WIDTH attribute.\n\n----\n**Note**\nIf your application uses the PXIe-5622 IF digitizer, your maximum device instantaneous bandwidth is constrained to 50 MHz or 25 MHz, depending on the digitizer option you purchased. If your application uses the PXIe-5624 digitizer, your maximum device instantaneous bandwidth is constrained by the hardware option you purchased and your FPGA image.\n\n----\n\n**PXI-5661**: The PXI-5600 RF downconverter instantaneous bandwidth is 20 MHz.\n\n**PXIe-5663/5663E**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the `PXIe-5601 RF Signal Downconverter Overview <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/overview.3.html>`_ for more information about instantaneous bandwidth.\n\n----\n**Note**\nFor the PXIe-5663/5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the instantaneous bandwidth for frequencies above 120 MHz is different than the instantaneous bandwidth for frequencies less than 120 MHz, which are 20 MHz and 10 MHz respectively.\n\n----\n\n**PXIe-5665**: Your maximum allowed instantaneous bandwidth is independent of the downconverter center frequency. Refer to the *NI PXIe-5665 Specifications* for more information about instantaneous bandwidth.\n\n**PXIe-5665 (14 GHz), PXIe-5668**: If you have enabled the preselector for the PXIe-5605/5606, the device instantaneous bandwidth value is only a typical specification. For multispan acquisitions, NI-RFSA uses this typical specification as the maximum size for the acquisition subspans.\n\n----\n**Note**\nWhen used with an external digitizer, the PXIe-5603 and the low band signal path of the PXIe-5605 provide a nominal 80 MHz bandwidth at   dB. At frequencies greater than 3.6 GHz, the PXIe-5605 provides a typical bandwidth of 47 MHz at   dB with the preselector (YIG-tuned filter) enabled.\n\n----\n\n----\n**Note**\nFor PXIe-5606 devices, the 765 MHz IF filter is available only at center frequencies above 3.6 GHz.\n\n----\n\n**PXIe-5693**: This attribute is read-only for the PXIe-5693. The value for the device instantaneous bandwidth depends on the value for the RF preselector filter.\n\n**PXIe-5694/PXIe-5667**: If your application uses the PXIe-5694 as part of an PXIe-5667 spectrum monitoring receiver or the PXIe-5694 as a stand-alone device, NI-RFSA determines the appropriate IF filter to use based on the value that you set for this attribute.\n\n----\n**Note**\n\n----\n\n**PXIe-5644/5645/5646**: This attribute is read-only for the PXIe-5644/5645/5646. Refer to the specifications document for your device for more information about instantaneous bandwidth.\n\n**PXIe-5840/5841/5860**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the *PXIe-5840/5841/5860 Specifications* for more information about instantaneous bandwidth. Set this attribute to select different device instantaneous bandwidths for a given downconverter center frequency. The device instantaneous bandwidth that you select is greater than or equal to the requested instantaneous bandwidth. If this attribute is not set, NI-RFSA uses the maximum allowed instantaneous bandwidth.\n\n**PXIe-5842**: Your maximum allowed instantaneous bandwidth depends on the device's hardware options, configured device personality, and the downconverter center frequency you use. Refer to the *PXIe-5842 Specifications* for more information about instantaneous bandwidth. Set this attribute to select different device instantaneous bandwidths for a given downconverter center frequency. The device instantaneous bandwidth that you select is greater than or equal to the requested instantaneous bandwidth. If this attribute is not set, NI-RFSA uses the maximum allowed instantaneous bandwidth.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-selection.html>`_\n\n`PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-selection.html>`_\n\n`PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-selection.html>`_"
        },
        'lv_property': 'Acquisition:Device Instantaneous Bandwidth (Hz)',
        'name': 'DEVICE_INSTANTANEOUS_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150126: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the configuration list step that is currently programmed to the hardware.\n\nThe list is zero-indexed. You can query this attribute only when a list is executed.\n\n**PXIe-5663E/5665/5667**: This attribute can be read only when a configuration list is running.\n\n**PXIe-5644/5645/5646**: This attribute always returns 0 when the configuration list is not running.\n\n**PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters**: If a configuration list is not running, this attribute returns the last step of a configuration list that is programmed to the hardware. If the device was last initiated without an active configuration list, this attribute returns 0.\n\n**Default Value**: N/A\n\n**Supported Devices:**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters\n\n**Related Topics**\n\n`RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_'
        },
        'lv_property': 'Configuration List:Step In Progress',
        'name': 'CONFIGURATION_LIST_STEP_IN_PROGRESS',
        'type': 'ViInt64'
    },
    1150127: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the number of dB by which to adjust the device mixer level. \n\nThe default value is 0, which specifies device settings that are the best compromise between distortion and noise. Specifying a positive value for this attribute configures the device for moderate distortion and low noise, and specifying a negative value results in low distortion and higher noise.\n\nYou cannot set the NIRFSA_ATTR_MIXER_LEVEL and NIRFSA_ATTR_MIXER_LEVEL_OFFSET attributes at the same time.\n\n**PXIe-5667**: This attribute is read-only when the NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED attribute is set to NIRFSA_VAL_DISABLED.\n\n**Units**: dB\n\n**Default Value**: 0\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668'
        },
        'lv_property': 'Vertical:Mixer Level Offset (dB)',
        'name': 'MIXER_LEVEL_OFFSET',
        'type': 'ViReal64'
    },
    1150128: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the level of mechanical attenuation for the RF path, in dB.\n\n**PXIe-5667**: This attribute is read-only when the NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED attribute is set to NIRFSA_VAL_DISABLED.\n\n**PXIe-5668with PXIe-5698**: This attribute is read-only when the NIRFSA_ATTR_RF_PREAMP_ENABLED attribute is set to NIRFSA_VAL_RF_PREAMP_ENABLED.\n\n**Units**: dB\n\n**Valid Values:**\n\n**PXIe-5601/5663/5663E**: 0, 16\n\n**PXIe-5603/5665 (3.6 GHz)**: 0, 10, 20, 30\n\n**PXIe-5605/5665 (14 GHz), PXIe-5606/5668**: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75\n\n**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 0, 10, 20, 30\n\n**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**: 0\n\n**PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75\n\n**PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector filter path**: 0\n\n**PXIe-5668 with PXIe-5698 with the** NIRFSA_ATTR_RF_PREAMP_ENABLED attribute set to NIRFSA_VAL_RF_PREAMP_ENABLED: 5\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668'
        },
        'lv_property': 'Vertical:Advanced:Mechanical Attenuation (dB)',
        'name': 'MECHANICAL_ATTENUATION',
        'type': 'ViReal64'
    },
    1150129: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the RF preamplifier is enabled in the system.\n\n**PXIe-5667, PXIe-5644/5645/5646, PXIe-5830/5831/5840/5841/5842**: The  NIRFSA_VAL_RF_PREAMP_AUTOMATIC value enables the RF preamplifier based on the value of the NIRFSA_ATTR_REFERENCE_LEVEL attribute and the center frequency. Except on the PXIe-5830/5831/5832, NI-RFSA coerces this attribute from NIRFSA_VAL_RF_PREAMP_AUTOMATIC to the selected value.\n\n----\n**Note**\nFor the PXIe-5840/5841, the automatically selected value may not be optimal for all measurements. At some reference levels, NIRFSA_VAL_RF_PREAMP_ENABLED may improve the noise floor while NIRFSA_VAL_RF_PREAMP_DISABLED may improve distortion.\n\n----\n\n**PXIe-5667**: The NIRFSA_VAL_RF_PREAMP_AUTOMATIC value is supported only when the NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED attribute is set to NIRFSA_VAL_RF_PREAMP_DISABLED. If the reference level is greater than -25 dBm, NI-RFSA disables the preamplifier. If the reference level is less than or equal to -25 dBm, NI-RFSA sets the NIRFSA_ATTR_RF_PREAMP_ENABLED attribute to NIRFSA_VAL_RF_PREAMP_ENABLED_WHEN_IN_SIGNAL_PATH.\n\n**PXIe-5668 with PXIe-5698**: If you set this attribute to NIRFSA_ATTR_RF_PREAMP_ENABLED, only the preamplifier on the PXIe-5698 is used, and the preamplifier on the PXIe-5668 remains disabled.\n\n**Defined Values:**\n\n%enum_table{enable rf preamp}\n\n**Default Value**:\n\n**PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842**: NIRFSA_VAL_RF_PREAMP_AUTOMATIC\n\n**All other devices**: NIRFSA_VAL_RF_PREAMP_DISABLED\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5698, PXIe-5830/5831/5832/5840/5841/5842'
        },
        'enum': 'EnableRfPreamp',
        'lv_property': 'Vertical:Advanced:Preamp Enabled',
        'name': 'RF_PREAMP_ENABLED',
        'type': 'ViInt32'
    },
    1150130: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the level of the IF signal leaving the system, in dBm. \n\nUse this attribute to increase or decrease the nominal IF signal output level to achieve better measurement results.\n\nIf you set the NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL and NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET attributes at the same time, NI-RFSA returns an error.\n\n----\n**Note**\nIf you set the NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL attribute to a value less than 201310 dBm, the IF output power level may be higher than the value you request. Read the value of this attribute to determine the configured IF output power level.\n\n----\n\n----\n**Note**\nThe value of this attribute is limited by the amount of IF attenuation that the downconverter can apply, the NIRFSA_ATTR_REFERENCE_LEVEL attribute, the NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY attribute, and the NIRFSA_ATTR_CENTER_FREQUENCY attribute or NIRFSA_ATTR_IQ_CARRIER_FREQUENCY attribute, depending on your acquisition type.\n\n----\n\n**Units**: dBm\n\n**Default Value**:\n\n**PXIe-5667**: -2 dBm\n\n**PXIe-5668**: -1 dBm\n\n**All other devices**:   dBm\n\n**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694'
        },
        'lv_property': 'Vertical:IF Output Power Level (dBm)',
        'name': 'IF_OUTPUT_POWER_LEVEL',
        'type': 'ViReal64'
    },
    1150131: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the number of dB by which to adjust the default IF output power level. \n\nThis attribute does not depend on absolute IF output power levels, so you can use it to adjust the IF output power level on all NI-RFSA devices without knowing the exact default value. Use this attribute to increase or decrease the nominal output level to achieve better measurement results. The default value for the offset is 0 dB.\n\nIf you set the NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL and NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET attributes at the same time, NI-RFSA returns an error.\n\n**Units**: dB\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668'
        },
        'lv_property': 'Vertical:IF Output Power Level Offset (dB)',
        'name': 'IF_OUTPUT_POWER_LEVEL_OFFSET',
        'type': 'ViReal64'
    },
    1150132: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the tunable preselector is enabled on the downconverter.\n\n----\n**Note**\nAll devices support setting this attribute to NIRFSA_VAL_PRESELECTOR_DISABLED or NIRFSA_VAL_PRESELECTOR_ENABLED_WHEN_IN_SIGNAL_PATH. Only devices with a preselector support setting this attribute to NIRFSA_VAL_PRESELECTOR_ENABLED.\n\n----\n\n**Defined Values:**\n\n%enum_table{enable preselector}\n\n**Default Value**: NIRFSA_VAL_PRESELECTOR_DISABLED if the device has no preselector. NIRFSA_VAL_PRESELECTOR_ENABLED_WHEN_IN_SIGNAL_PATH if the device has a preselector.\n\n**Supported Devices:** PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'enum': 'EnablePreselector',
        'lv_property': 'Signal Path:Advanced:Downconverter Preselector Enabled',
        'name': 'DOWNCONVERTER_PRESELECTOR_ENABLED',
        'type': 'ViInt32'
    },
    1150134: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to enable the LO OUT terminals on the installed devices.\n\n**PXIe-5601**: The only valid value for this attribute is VI_TRUE.\n\n**PXIe-5603/5605/5606**: If you want to daisy-chain multiple devices together using the same LO source, set this attribute to TRUE to export the LO input signals on the LO1 IN, LO2 IN, and LO3 IN terminals to LO1 OUT, LO2 OUT, and LO3 OUT, respectively.\n\n**PXIe-5694**: You can enable this attribute only if you set the NIRFSA_ATTR_LO_SOURCE attribute to NIRFSA_VAL_LO_IN_STR, or if you set the NIRFSA_ATTR_LO_SOURCE attribute to NIRFSA_VAL_ONBOARD_STR and the NIRFSA_ATTR_IF_CONDITIONING_DOWN_CONVERSION_ENABLED attribute to NIRFSA_VAL_ENABLED.\n\n**PXIe-5830/5831**: To use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsa_SetAttributeViBoolean function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).\n\n----\n**Note**\nIf you are sharing an LO for the PXIe-5830/5831/5832 between an NI-RFSA and NI-RFSG session, ensure both sessions use the same shared setting.\n\n----\n\n**Defined Values:**\n\n| Value         |  Description                              |\n|:---------|:-------------------------------|\n| VI_TRUE  | Enables the LO OUT terminals.  |\n| VI_FALSE | Disables the LO OUT terminals. |\n\n**Default Values**:\n\n**PXIe-5601, PXIe-5663/5663E**: VI_TRUE\n\n**PXIe-5603/5605/5606, PXIe-5644/5645/5646, PXIe-5665/5667/5668, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842**: VI_FALSE\n\n**Supported Devices**: PXIe-5601/5603/5605 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Signal Path:LO Export Enabled',
        'name': 'LO_EXPORT_ENABLED',
        'type': 'ViBoolean'
    },
    1150135: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Adjusts the dynamics of the current driving the YIG main coil.\n\n----\n**Note**\nSetting this attribute to NIRFSA_VAL_LO_YIG_MAIN_COIL_DRIVE_FAST allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise. This attribute is not supported if you are using an external LO.\n\n----\n\n**Defined Values:**\n\n%enum_table{lo yig main coil drive}\n\n**Default Value**: NIRFSA_VAL_LO_YIG_MAIN_COIL_DRIVE_NORMAL\n\n**Supported Devices:** PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668'
        },
        'enum': 'LoYigMainCoilDrive',
        'lv_property': 'Signal Path:Advanced:LO YIG Main Coil Drive',
        'name': 'LO_YIG_MAIN_COIL_DRIVE',
        'type': 'ViInt32'
    },
    1150136: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns whether a preselector is available on the RF downconverter module.\n\n**Defined Values:**\n\n| Value         | Description                                                  |\n|:---------|:--------------------------------------------------|\n| VI_TRUE  | A preselector is available on the downconverter.  |\n| VI_FALSE | No preselector is available on the downconverter. |\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842'
        },
        'lv_property': 'Device Characteristics:Preselector Present',
        'name': 'PRESELECTOR_PRESENT',
        'type': 'ViBoolean'
    },
    1150137: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns whether an RF preamplifier is available on the RF downconverter module.\n\n**Defined Values:**\n\n| Value         | Description                                                     |\n|:---------|:-----------------------------------------------------|\n| VI_TRUE  | The device has an enabled RF preamplifier available. |\n| VI_FALSE | The device has no RF preamplifier available.         |\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Device Characteristics:RF Preamp Present',
        'name': 'RF_PREAMP_PRESENT',
        'type': 'ViBoolean'
    },
    1150139: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the location in a signal path where an RF downconverter calibration tone is injected or whether the tone is disabled.\n\nRefer to `PXIe-5665 Theory of Operation <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/block-diagram.2.html>`_, `PXIe-5667 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/block-diagram.html>`_, or `PXIe-5668 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/block-diagram.html>`_ for more information about signal paths for your device.\n\n**Defined and Valid Values:**\n\n| Value                                          | Description                                                                                | Valid For           |\n|:-----------------------------------------------|:-------------------------------------------------------------------------------------------|:--------------------|\n|  NIRFSA_VAL_DISABLED (2700)            | Disables the calibration tone for the associated signal path.                              | PXIe-5603/5605/5606 |\n| NIRFSA_VAL_CAL_TONE_LOWBAND_RF (2701)          | Injects the calibration tone into the low band RF signal path.                             | PXIe-5603/5605/5606 |\n| NIRFSA_VAL_CAL_TONE_HIGHBAND_RF (2702)         | Injects the calibration tone into the high band RF signal path.                            | PXIe-5605/5606      |\n| NIRFSA_VAL_CAL_TONE_HIGHBAND_IF (2703)         | Injects the calibration tone into the high band IF signal path.                            | PXIe-5605           |\n| NIRFSA_VAL_CAL_TONE_LOWBAND_RF_WITHOUT_ALC (2704) | Injects the calibration tone into the low band RF signal path, bypassing the ALC.          | PXIe-5606           |\n| NIRFSA_VAL_CAL_TONE_COMB_GENERATOR (2705)      | Injects the calibration tone into the high band RF signal path through the Comb Generator. | PXIe-5606           |\n\n**Default Value**:  NIRFSA_VAL_DISABLED\n\n**Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668'
        },
        'enum': 'CalToneMode',
        'lv_property': 'Self Calibration:NI 5665/5667/5668R:Downconverter Cal Tone Mode',
        'name': 'DOWNCONVERTER_CAL_TONE_MODE',
        'type': 'ViInt32'
    },
    1150140: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the frequency of the RF downconverter calibration tone, in hertz (Hz).\n\n**Valid Values**\n\n**PXIe-5603/5605**: 134 MHz to 13.2 GHz\n\n**PXIe-5606**: 34.5 MHz to 4 GHz\n\n**Default Value**: 612.5 MHz\n\n**Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668'
        },
        'lv_property': 'Self Calibration:NI 5665/5667/5668R:Downconverter Cal Tone Frequency',
        'name': 'DOWNCONVERTER_CAL_TONE_FREQUENCY',
        'type': 'ViReal64'
    },
    1150141: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the IF attenuation table to be used for external calibration.\n\nThis attribute is valid only in a calibration session.\n\n**Defined Values**:\n\n%enum_table{i fatten table sel}\n\n**Default Value**: NIRFSA_VAL_EXT_CAL_IF_ATTENUATION_TABLE_STANDARD\n\n**Supported Devices**: PXIe-5603/5605'
        },
        'enum': 'IFattenTableSel',
        'lv_property': 'Factory Calibration:NI 5665/5668R:IF Attenuation Table Selection',
        'name': 'CAL_IF_ATTENUATION_TABLE_SELECTION',
        'type': 'ViInt32'
    },
    1150142: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the minimum adjacent channel power ratio (ACPR), in dB, relative to the main channel reference level. \n\nThis attribute configures NI-RFSA to optimize downconverter gain to measure a lower-power adjacent channel, adding gain only after filtering the main channel. The gain NI-RFSA applies is always less than or equal to the ACPR value you specify.\n\n----\n**Note**\nFor the PXIe-5665 (3.6 GHz), this attribute is supported only if you set the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH, NIRFSA_ATTR_SPECTRUM_SPAN, or NIRFSA_ATTR_IF_FILTER_BANDWIDTH attribute to a value less than 300 kHz. For the PXIe-5665 (14 GHz), this attribute is supported for NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH, NIRFSA_ATTR_SPECTRUM_SPAN, or NIRFSA_ATTR_IF_FILTER_BANDWIDTH attribute values less than 300 kHz by using the 300 kHz IF filter, and it is supported for values between 300 kHz and 5 MHz by using the 5 MHz IF filter.\n\n----\n\n----\n**Note**\nNI-RFSA coerces this attribute to zero for the PXI-5600, PXIe-5601 and the PXIe-5667. For all other devices, read the coerced value of this attribute to determine the actual amount of gain applied.\n\n----\n\n----\n**Note**\nFor the PXIe-5668, this attribute alters the NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL attribute. This attribute will not affect the NIRFSA_ATTR_REFERENCE_LEVEL attribute.\n\n----\n\n**Default Value**: 0\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668'
        },
        'lv_property': 'Vertical:Advanced:Minimum Adjacent Channel Power Ratio (dB)',
        'name': 'MINIMUM_ACPR',
        'type': 'ViReal64'
    },
    1150144: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the oversampling ratio used by the digitizer onboard signal processing (OSP) when you are in spectrum acquisition mode. This attribute allows you to acquire a larger bandwidth in hardware and reduce that bandwidth in software, decreasing the possibility of hardware data path overflows.\n\n**PXIe-5644/5645/5646**: The only valid value for this attribute is 1.\n\n**Default Value**: 1.0\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Acquisition:Spectrum:Spectrum OSP Sampling Ratio',
        'name': 'SPECTRUM_OSP_SAMPLING_RATIO',
        'type': 'ViReal64'
    },
    1150146: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the internal gain self-calibration correction for the IF filter through path.\n\nThe value you specify using this attribute overrides any previously-set value.\n\n**Units**: dB\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5603/5605'
        },
        'lv_property': 'Self Calibration:NI 5665/5668R:Calibration Correction for Through Filter',
        'name': 'CALIBRATION_CORRECTION_THROUGH_FILTER',
        'type': 'ViReal64'
    },
    1150147: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the internal gain self-calibration correction for the 300 kHz IF filter path.\n\nThe value you specify using this attribute overrides any previously-set value.\n\n**Units**: dB\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5603/5605/5606'
        },
        'lv_property': 'Self Calibration:NI 5665/5668R:Calibration Correction for 300 kHz Filter',
        'name': 'CALIBRATION_CORRECTION_300_KHZ_FILTER',
        'type': 'ViReal64'
    },
    1150148: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the internal gain self-calibration correction for the 5 MHz IF filter path.\n\nThe value you specify using this attribute overrides any previously-set value.\n\n**Units**: dB\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5603/5605/5606'
        },
        'lv_property': 'Self Calibration:NI 5665/5668R:Calibration Correction for 5 MHz Filter',
        'name': 'CALIBRATION_CORRECTION_5_MHZ_FILTER',
        'type': 'ViReal64'
    },
    1150149: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter.\n\n----\n**Note**\nFor the PXIe-5605/5606/5665/5667/5668, this attribute must be set to NIRFSA_VAL_AC when the DC block is present and set to NIRFSA_VAL_DC when the DC block is not present to ensure device specifications are met and proper calibration data is used. For more information about removing or attaching the DC block, refer to the `PXIe-5665 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/block-diagram.2.html>`_, the `PXIe-5605 Front Panel and LEDs <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/pinout.4.html>`_, the `PXIe-5667 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/block-diagram.html>`_, or the `PXIe-5668 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/block-diagram.html>`_ topics in this help file.\n\n----\n\n**Valid Values**:\n\n**PXIe-5603/5665 (3.6 GHz)**: NIRFSA_VAL_AC, NIRFSA_VAL_DC\n\n**PXIe-5605/5665 (14 GHz)**: NIRFSA_VAL_AC, NIRFSA_VAL_DC\n\n**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low-frequency bypass path**: NIRFSA_VAL_AC, NIRFSA_VAL_DC\n\n**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**: NIRFSA_VAL_AC\n\n**PXIe-5667 (7 GHz)**: NIRFSA_VAL_AC\n\n**PXIe-5606/5668**: NIRFSA_VAL_AC, NIRFSA_VAL_DC\n\n**Defined Values**:\n\n%enum_table{channel coupling}\n\n**Default Value**: NIRFSA_VAL_AC\n\n**Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668'
        },
        'enum': 'ChannelCoupling',
        'lv_property': 'Vertical:Advanced:NI 5665/5667/5668R:Channel Coupling',
        'name': 'CHANNEL_COUPLING',
        'type': 'ViInt32'
    },
    1150151: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the scaling factor applied to the time-domain voltage data in the IF digitizer. \n\nUse this attribute to maximize the dynamic range of the digitizer by increasing the maximum IF power the digitizer can measure without creating OSP overflows.\n\nBecause of the device amplitude response, some wide-band signals normally attenuated by the downconverter go through the IF digitizer without causing an ADC overflow. During IF equalization, these wide-band digitizer input signals may become amplified. These amplified input signal values overflow the available numeric range used in the signal processing algorithm.\n\nYou can use this attribute when OSP calculations would generate an overflow while applying digital filters to the data. The OSP module in the digitizer multiplies the time-domain signal amplitude, in volts, by the specified attribute value before further onboard processing. Set this attribute to a value less than 1 to avoid OSP overflow for near full-scale IF signals and to use the maximum dynamic range of the digitizer. NI-RFSA compensates for the specified OSP data scaling factor to ensure that the correct scaled data, in absolute levels, is always returned regardless of the value of this attribute.\n\n**Valid Values:**: 0.25 to 1.0\n\n**Default Values:**\n\n**PXI-5661, PXIe-5663/5663E/5665 (3.6 GHz)/5667 (3.6 GHz)/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: 1.0\n\n**PXIe-5665 (14 GHz)/5667 (7 GHz)**: 0.8\n\n**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Vertical:Advanced:OSP Data Scaling Factor',
        'name': 'OSP_DATA_SCALING_FACTOR',
        'type': 'ViReal64'
    },
    1150154: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to allow the device to acquire more records than can fit in the device memory of the PXIe-5622/5624.\n\n----\n**Note**\nIf you set the attribute to FALSE and attempt to acquire more records than can fit into the PXIe-5622/5624 device memory, NI-RFSA returns an error. If this attribute is set to TRUE, NI-RFSA returns an error only in the event of an acquisition buffer overflow.\n\n----\n\n----\n**Note**\nThis attribute is always set to VI_TRUE for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841.\n\n----\n\n**Defined Values:**\n\n|Value         | Description                                                                       |\n|:---------|:-----------------------------------------------------------------------|\n| VI_TRUE  | Allows acquisition of more records than fit in device memory.          |\n| VI_FALSE | Does not allow acquisitions of more records than fit in device memory. |\n\n**Default Value**: VI_FALSE\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Acquisition:IQ:Allow More Records Than Memory',
        'name': 'ALLOW_MORE_RECORDS_THAN_MEMORY',
        'type': 'ViBoolean'
    },
    1150155: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the step size for the RF attenuation level. \n\nThe actual RF attenuation is coerced up to the next highest multiple of this step size. You can also set this value to change the step size for the device within the supported device precision and configuration.\n\n**PXI-5600**: The device configuration supports only the following attenuation step size values: 10, 20, 30, 40, and 50.\n\n**PXIe-5601**: The attenuation is calculated based on the actual calibrated value closest to the desired value, so the step size varies as the actual gain values vary between consecutive attenuation settings.\n\n**PXIe-5603**: The device configuration supports attenuation changes in 1 dB steps.\n\n**PXIe-5605**: The available attenuation step size depends on the specified center frequency. In the high band signal path (input frequencies greater than 3.6 GHz), the only available attenuation is the step attenuator that you can change in 5 dB steps. In the low band signal path (input frequencies less than or equal to 3.6 GHz), an additional 31 dB of solid-state attenuation is available in 1 dB steps. The 5 dB default value indicates that, even when in the low band signal path, NI-RFSA changes the attenuation in 5 dB steps using only the mechanical attenuator. You can use this attribute to affect when the device changes the attenuation settings. To use the solid-state attenuation in the low band signal path, change the step size to a value other than a multiple of 5 (for example, a step size of 1 dB). If you use a value other than a multiple of 5 while in the high band of the PXIe-5605, NI-RFSA returns an error.\n\n**Units**: dB\n\n**Valid Values:**\n\n**PXI-5600/5661**: 10, 20, 30, 40, and 50\n\n**PXIe-5601/5663/5663E**: 0.0 to 93.0, continuous\n\n**PXIe-5603/5665 (3.6 GHz)**: 1.0 to 74.0, in 1 dB steps\n\n**PXIe-5605/5665 (14 GHz) (low band), PXIe-5606/5668 (low band)**: 1.0 to 106.0, in 1 dB steps\n\n**PXIe-5605/5665 (14 GHz) (high band), PXIe-5606/5668 (high band)**: 5.0 to 75.0, in 5 dB steps\n\n**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 1.0 to 74.0, in 1 dB steps\n\n**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**:  1.0\n\n**PXIe-5667 (7 GHz) using the PXIe-5693 preselector low frequency bypass path**:  1.0 to 106.0 in 1 dB steps\n\n**PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector filter path**:  1.0\n\n**Default Value:**\n\n**PXI-5600/5661**: 10.0\n\n**PXIe-5601/5663/5663E**: 0.0\n\n**PXIe-5603/5665 (3.6 GHz)**: 1.0\n\n**PXIe-5605/5665 (14 GHz), PXIe-5606/5668**: 5.0\n\n**PXIe-5667**: 1.0\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668'
        },
        'lv_property': 'Vertical:Advanced:RF Attenuation Step Size (dB)',
        'name': 'RF_ATTENUATION_STEP_SIZE',
        'type': 'ViReal64'
    },
    1150157: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to enable the step gain amplifier.\n\n**Defined Values:**\n\n%enum_table{step gain enabled}\n\n**Default Value**: NIRFSA_VAL_STEP_GAIN_DISABLED\n\n**Supported Devices**: PXIe-5694'
        },
        'enum': 'StepGainEnabled',
        'lv_property': 'Vertical:Advanced:NI 5694:Step Gain Enabled',
        'name': 'STEP_GAIN_ENABLED',
        'type': 'ViInt32'
    },
    1150158: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the preselector tuning DAC value during the preselector external alignment step.\n\nThis value is valid only during a external alignment session.\n\n**Valid Values:**\n\n| Device    | Value       |\n|:----------|:------------|\n| PXIe-5605 | 0 to 16,383 |\n| PXIe-5606 | 0 to 65,535 |\n\n**Defined Values:** 0 to 15.5\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5605/5606 (external digitizer mode), PXIe-5665/5668'
        },
        'lv_property': 'External Alignment:NI 5665/5668R:Preselector Tuning DAC Value',
        'name': '5665_PRESELECTOR_TUNING_DAC_VALUE',
        'type': 'ViInt32'
    },
    1150159: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the temperature, in degrees Celsius, that NI-RFSA uses to calculate the device configuration settings.\n\n----\n**Note**\nFor most applications, you can choose not to set this attribute, so NI-RFSA uses the device temperature to calculate best attenuation settings. Set this attribute only if you want NI-RFSA to maintain the same device configuration settings from acquisition to acquisition, independent of device temperature changes.\n\n----\n\n**PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: This attribute is read-only.\n\n**Units**: degrees Celsius\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Vertical:Advanced:Device Configuration Temperature (Degrees C)',
        'name': 'DEVICE_CONFIGURATION_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150160: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether all signal conditioning is enabled on the PXIe-5694.\n\n----\n**Note**\nIf you set this attribute to NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED, NI-RFSA bypasses all signal conditioning, prevents any signal downconversion, and fixes the values for NIRFSA_ATTR_DOWNCONVERTER_GAIN attribute, the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute, and the NIRFSA_ATTR_IF_FILTER_BANDWIDTH attribute.\n\n----\n\n**Defined Values:**\n\n%enum_table{signal conditioning enabled}\n\n**Default Value**: NIRFSA_VAL_SIGNAL_CONDITIONING_ENABLED\n\n**Supported Devices**: PXIe-5694'
        },
        'enum': 'SignalConditioningEnabled',
        'lv_property': 'Signal Path:Advanced:NI 5694:Signal Conditioning Enabled',
        'name': 'SIGNAL_CONDITIONING_ENABLED',
        'type': 'ViInt32'
    },
    1150161: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether downconversion to 21.4 MHz is enabled for the IF conditioning module. \n\nThe IF output frequency is 21.4 MHz when you enable this attribute, and it is 193.6 MHz when you disable this attribute.\n\n----\n**Note**\nIf you set the NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED attribute to NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED, you cannot set the NIRFSA_ATTR_IF_CONDITIONING_DOWN_CONVERSION_ENABLED attribute to NIRFSA_VAL_ENABLED.\n\n----\n\n----\n**Note**\nFor the PXI-5661, PXIe-5663/5663E/5665, the only valid value for this attribute is NIRFSA_VAL_DISABLED.\n\n----\n\n**Defined Values:**\n\n%enum_table{enable attr vals}\n\n**Default Values**: NIRFSA_VAL_DISABLED\n\n**Supported Devices**: PXIe-5667, PXIe-5694'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Signal Path:Advanced:IF Conditioning Downconversion Enabled',
        'name': 'IF_CONDITIONING_DOWN_CONVERSION_ENABLED',
        'type': 'ViInt32'
    },
    1150162: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the LO signal source used to downconvert the RF input signal.\n\n                If no signal downconversion is required, this attribute is ignored. If this attribute is set to "" (empty string), NI-RFSA uses the internal LO source.\n\n                To use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsa_SetAttributeViString function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).\n\n                ----\n                **Note**\n                For the PXIe-5841 with PXIe-5655, RF list mode is not supported when this attribute is set to NIRFSA_VAL_LO_SOURCE_SG_SA_SHARED_STR.\n\n                ----\n\n                **Defined Values:**\n                %enum_table{lo source vals}\n\n                **Default Value**: NIRFSA_VAL_ONBOARD_STR ("Onboard")\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n                `PXIe-5830 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/lo-sharing-using-rfsa-rfsg.html>`_\n                `PXIe-5831/5832 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/lo-sharing-using-rfsa-rfsg.html>`_'
        },
        'enum': 'LoSourceVals',
        'lv_property': 'Signal Path:LO Source',
        'name': 'LO_SOURCE',
        'type': 'ViString'
    },
    1150163: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the amplitude settling accuracy in decibels.\n\nNI-RFSA waits until the RF power settles within the specified accuracy level after calling the nirfsa_Initiate function.\n\nAny specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.\n\n**Units**: dB\n\n**Default Value:** 0.5\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Vertical:Advanced:Amplitude Settling',
        'name': 'AMPLITUDE_SETTLING',
        'type': 'ViReal64'
    },
    1150164: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'This attribute is not for customer use.'
        },
        'lv_property': 'Triggers:Advanced:DDC Reference Trigger Override',
        'name': 'DDC_REF_TRIGGER_OVERRIDE',
        'type': 'ViBoolean'
    },
    1150165: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'This attribute is not for customer use.'
        },
        'lv_property': 'Configuration List:Advanced:Minimum Reconfiguration Time',
        'name': 'MINIMUM_RECONFIG_TIME',
        'type': 'ViReal64'
    },
    1150166: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the RF preselector filter to use.\n\n----\n**Note**\nYou can write to this attribute when using only the PXIe-5693 as a stand-alone device.\n\n----\n\n**Defined Values**:\n\n%enum_table{rf preselector filter}\n\n**Default Values**:\n\n**PXIe-5667, PXIe-5693**: NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_9\n\n**PXIe-5665**: NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_NONE\n\n**Supported Devices**: PXIe-5665/5667, PXIe-5693'
        },
        'enum': 'RfPreselectorFilter',
        'lv_property': 'Signal Path:Advanced:RF Preselector Filter',
        'name': 'RF_PRESELECTOR_FILTER',
        'type': 'ViInt32'
    },
    1150167: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the notch filter is enabled on the RF conditioning module.\n\n----\n**Note**\nThe PXI-5661 and PXIe-5663/5663E/5665 only support setting this attribute to NIRFSA_VAL_NOTCH_FILTER_DISABLED.\n\n----\n\n**Defined Values**:\n\n%enum_table{notch filter enabled}\n\n**Default Value**: NIRFSA_VAL_NOTCH_FILTER_DISABLED\n\n**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5693'
        },
        'enum': 'NotchFilterEnabled',
        'lv_property': 'Signal Path:Advanced:Notch Filter Enabled',
        'name': 'NOTCH_FILTER_ENABLED',
        'type': 'ViInt32'
    },
    1150168: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the step attenuator to engage in the calibration tone path.\n\n**Units**: dB\n\n**Valid Values**: 2.00, 10.00\n\n**Default Value**: 2.00 dB\n\n**Supported Devices**: PXIe-5693'
        },
        'lv_property': 'Factory Calibration:NI 5665/5668R:Cal Tone Step Attenuation',
        'name': 'CAL_TONE_STEP_ATTENUATION',
        'type': 'ViReal64'
    },
    1150169: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the FFT width of the device. \n\nThe FFT width is the effective bandwidth of the signal path during each signal acquisition.\n\n----\n**Note**\nThe maximum FFT width when using the PXIe-5622 is constrained to 50 MHz or 25 MHz, depending on the digitizer option you purchased. The maximum FFT width when using thing PXIe-5624 is constrained to 400 MHz or 765 MHz, depending on the digitizer configuration.\n\n----\n\n----\n**Note**\nYou can use the NIRFSA_ATTR_FFT_WIDTH attribute with in-band retuning. For more information about in-band retuning, refer to the NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY attribute.\n\n----\n\nNI-RFSA treats the *device instantaneous bandwidth* as the effective real-time bandwidth of the signal path. The *span* specifies the frequency range of the computed spectrum. An RF vector signal analyzer can acquire a bandwidth only within the device instantaneous bandwidth frequency. If the span you choose is greater than the device instantaneous bandwidth, NI-RFSA obtains multiple acquisitions and combines them into a single spectrum. By specifying the FFT width, you can control the specific bandwidth obtained in each signal acquisition. If you read the NIRFSA_ATTR_FFT_WIDTH attribute without setting it, NI-RFSA returns the value of the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute.\n\n**Valid Values**:\n\nThe lower limit for all FFT width supported devices using the PXIe-5622 IF digitizer is 7.325 kHz. The lower limit for all FFT width supported devices using the PXIe-5624 IF digitizer is 400 MHz or 800 MHz, depending on the FPGA image that is downloaded upon opening the session to the PXIe-5624 IF digitizer.\n\n**PXIe-5663/5663E**: The FFT width upper limit for the PXIe-5663/5663E depends on the downconverter center frequency and on the module revision of the PXIe-5601 as illustrated in the following table. Refer to the `Identifying Module Revision <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/identifying-module-revision.html>`_ topic for more information about determining which revision of the PXIe-5601 RF downconverter you have installed.\n\n| Downconverter Center Frequency                                                                                                                                                              | PXIe-5601 Instantaneous Bandwidth | FFT Width Upper Limit                                          |\n|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------|:---------------------------------------------------------------|\n| 10 MHz to <120 MHz                                                                                                                                                                         | 10 MHz                            | 10 MHz (Revision E), 20 MHz< sup >* < /sup> (Revision G or later) |\n| 120 MHz to <330 MHz                                                                                                                                                                        | 20 MHz                            | 20 MHz (Revision E), 30 MHz< sup > * < /sup> (Revision G or later) |\n| 330 MHz to <6.6 GHz                                                                                                                                                                        | 50 MHz                            | 50 MHz                                                         |\n| <sup > * < / sup >National Instruments does not guarantee device specifications if you set the NIRFSA_ATTR_FFT_WIDTH attribute greater than the warranted instantaneous bandwidth specification. |                                   |                                                                |\n\n**PXIe-5665/5667/5668**: The upper limit of the FFT width is the maximum device instantaneous bandwidth.\n\n----\n**Note**\n\n----\n\n----\n**Note**\nAt frequencies greater than 3.6 GHz, the PXIe-5605 provides a typical bandwidth of 47 MHz at   dB with the preselector enabled. The NIRFSA_ATTR_FFT_WIDTH attribute can override the typical bandwidth of the PXIe-5605 up to 57 MHz using an external digitizer and up to 50 MHz or 25 MHz depending on the PXIe-5622 digitizer option you purchased. The increase in bandwidth results in faster signal acquisitions, but amplitude accuracy is decreased for spectrum acquisitions, and magnitude and phase accuracy is decreased for I/Q acquisitions. National Instruments does not guarantee device specifications if you set the NIRFSA_ATTR_FFT_WIDTH attribute greater than the warranted instantaneous bandwidth specification.\n\n----\n\n----\n**Note**\nWhen using the PXIe-5606, the 765 MHz IF filter is only available at center frequencies of 3.6 GHz and above.\n\n----\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5663/5663E/5665/5667/5668'
        },
        'lv_property': 'Acquisition:Spectrum:FFT Width',
        'name': 'FFT_WIDTH',
        'type': 'ViReal64'
    },
    1150170: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether input isolation is enabled.\n\nEnabling this attribute isolates the input signal at the RF IN connector on the RF downconverter from the rest of the RF downconverter signal path. Disabling this attribute reintegrates the input signal into the RF downconverter signal path.\n\n----\n**Note**\nIf you enable input isolation for your device, the device impedance is changed from the characteristic 50  impedance. A change in the device impedance may also cause a VSWR value higher than the device specifications.\n\n----\n\nFor the PXIe-5830/5831/5832, input isolation is supported for all available ports for your hardware configuration.\n\n**Defined Values:**\n\n%enum_table{enable attr vals}\n\n**Default Value**: NIRFSA_VAL_DISABLED, if the device configuration is supported.\n\n**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5693, PXIe-5820/5830/5831/5832/5840/5841'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Signal Path:Advanced:Input Isolation Enabled',
        'name': 'INPUT_ISOLATION_ENABLED',
        'type': 'ViInt32'
    },
    1150172: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'This attribute is not for customer use.'
        },
        'lv_property': 'Acquisition:IQ:Advanced:Contiguous Multirecord',
        'name': 'CONTIGUOUS_MULTIRECORD',
        'type': 'ViInt32'
    },
    1150173: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'This attribute is not for customer use.'
        },
        'lv_property': 'Configuration List:Advanced:Timer Start Source',
        'name': 'TIMER_START_SOURCE',
        'type': 'ViString'
    },
    1150174: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the power of a virtual signal connected to the RF IN connector on the PXIe-5693 front panel when the calibration tone is enabled.\n\nYou can enable a calibration tone for the PXIe-5693 by setting the NIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_MODE attribute to NIRFSA_VAL_CAL_TONE_LOWBAND_RF or NIRFSA_VAL_CAL_TONE_HIGHBAND_RF.\n\n**Units**: dBm\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5693'
        },
        'lv_property': 'Vertical:Advanced:NI 5693:Cal Tone Power Referred to RF IN',
        'name': 'CAL_TONE_POWER_REFERRED_TO_RF_IN',
        'type': 'ViReal64'
    },
    1150175: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'This attribute is not for customer use.'
        },
        'lv_property': 'Triggers:Advanced:Start Trigger Delay',
        'name': 'START_TRIGGER_DELAY',
        'type': 'ViReal64'
    },
    1150176: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the device is the master for synchronizing the shared Start Trigger between multiple devices. \n\nThe master device distributes the synchronized Start Trigger to all devices in the system through the Start Trigger distribution line.\n\nWhen synchronizing the Start Trigger, one device must always be designated as the master. When the device is configured as a master, it actively drives the Start Trigger distribution line. When the device is configured as a slave, set the NIRFSA_ATTR_START_TRIGGER_TYPE attribute to NIRFSA_VAL_DIGITAL_EDGE, and the NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute to NIRFSA VAL SYNC START TRIGGER STR.\n\nRefer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.\n\n**Defined Values:**\n\n|Value          | Description                                                                         |\n|:---------|:-------------------------------------------------------------------------|\n| VI_TRUE  | The device is the master device for synchronizing the Start Trigger.     |\n| VI_FALSE | The device is not the master device for synchronizing the Start Trigger. |\n\n**Default Value**: VI_FALSE\n\n**Supported Devices:** PXIe-5644/5645/5646'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Start Trigger Master',
        'name': 'SYNC_START_TRIGGER_MASTER',
        'type': 'ViBoolean'
    },
    1150177: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies which external trigger line distributes the synchronized Start Trigger signal. \n\nWhen synchronizing the Start Trigger, configure all devices to use the same Start Trigger distribution line.\n\nRefer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.\n\n**Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Start Trigger Dist Line',
        'name': 'SYNC_START_TRIGGER_DIST_LINE',
        'type': 'ViString'
    },
    1150178: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the device is the master for synchronizing the shared Reference Trigger between multiple devices. \n\nThe master device distributes the synchronized Reference Trigger to all devices in the system through the Reference Trigger distribution line.\n\nWhen synchronizing the Reference Trigger, one device must always be designated as the master. When the device is configured as a master, it actively drives the Reference Trigger distribution line. When the device is configured as a slave, set the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute to NIRFSA_VAL_DIGITAL_EDGE, and the NIRFSA_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE attribute to NIRFSA VAL SYNC REF TRIGGER STR.\n\nRefer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.\n\n**Defined Values:**\n\n|Value          | Description                                                                       |\n|:---------|:-----------------------------------------------------------------------|\n| VI_TRUE  | The device is the master device for synchronizing the Ref Trigger.     |\n| VI_FALSE | The device is not the master device for synchronizing the Ref Trigger. |\n\n**Default Value**: VI_FALSE\n\n**Supported Devices:** PXIe-5644/5645/5646'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Ref Trigger Master',
        'name': 'SYNC_REF_TRIGGER_MASTER',
        'type': 'ViBoolean'
    },
    1150179: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies which external trigger line distributes the synchronized Reference Trigger signal. \n\nWhen synchronizing the Reference Trigger, configure all devices to use the same Reference Trigger distribution line.\n\nRefer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.\n\n**Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0\n\n**Default Value**: "" (empty string)\n\n**Supported Devices:** PXIe-5644/5645/5646'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Ref Trigger Dist Line',
        'name': 'SYNC_REF_TRIGGER_DIST_LINE',
        'type': 'ViString'
    },
    1150180: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the connector(s) to use to acquire the signal. \n\nTo set this attribute, the NI-RFSA device must be in the Configuration state.\n\n**Defined Values:**\n\n%enum_table{input port}\n\n**Default Values**:\n\n**PXIe-5820**: NIRFSA_VAL_IQ_IN\n\n**All other devices**: NIRFSA_VAL_RF_IN\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'enum': 'InputPort',
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Input Port',
        'name': 'INPUT_PORT',
        'type': 'ViInt32'
    },
    1150181: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the frequency of the signal. \n\nThe onboard signal processing (OSP) frequency shifts the signal at this frequency to baseband prior to acquiring it.\n\n----\n**Note**\nFor the PXIe-5645, this attribute is ignored if you are using the RF ports.\n\n----\n\n**Valid Values**:\n\n**PXIe-5645**: -60 MHz to +60 MHz\n\n**PXIe-5820**: -500 MHz to +500 MHz\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5645, PXIe-5820'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ In Port:Carrier Frequency',
        'name': 'IQ_IN_PORT_CARRIER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150182: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the terminal configuration of the I/Q port.\n\nTo use this attribute, you must use the channelName parameter of the nirfsa_SetAttributeViInt32 function to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).\n\n----\n**Note**\nFor the PXIe-5645, this attribute is ignored if you are using the RF ports.\n\n----\n\n**PXIe-5820**: The only valid value for this attribute is NIRFSA_VAL_DIFFERENTIAL.\n\n**Defined Values:**\n\n%enum_table{iq in port term cfg}\n\n**Default Value**: NIRFSA_VAL_DIFFERENTIAL\n\n**Supported Devices:** PXIe-5645, PXIe-5820'
        },
        'enum': 'IqInPortTermCfg',
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ In Port:Terminal Configuration',
        'name': 'IQ_IN_PORT_TERMINAL_CONFIGURATION',
        'type': 'ViInt32'
    },
    1150183: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the voltage range for the I/Q terminals.\n\nTo use this attribute, you must use the channelName parameter of the nirfsa_SetAttributeViReal64 function to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).\n\nThe voltage range in differential terminal configuration is configurable from 2 V<sub>pk-pk</sub> to 0.032 V<sub>pk-pk</sub> in 1 dB steps. In single-ended terminal configuration, valid ranges are half those for differential. Values are always coerced up to the next valid range.\n\n----\n**Note**\nFor the PXIe-5645, this attribute is ignored if you are using the RF ports.\n\n----\n\n**Valid Values:**\n\n**PXIe-5645**: 0 V<sub>pk-pk</sub> to 2 V<sub>pk-pk</sub> for differential terminal configuration, 0 V<sub>pk-pk</sub> to 1 V<sub>pk-pk</sub> for single-ended terminal configuration.\n\n**PXIe-5820**: 0 V<sub>pk-pk</sub> to 4 V<sub>pk-pk</sub> for differential terminal configuration.\n\n**Default Value**: 2 V<sub>pk-pk</sub>\n\n**Supported Devices:** PXIe-5645, PXIe-5820'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ In Port:Vertical Range',
        'name': 'IQ_IN_PORT_VERTICAL_RANGE',
        'type': 'ViReal64'
    },
    1150184: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the device is the master for synchronizing the shared Advance Trigger between multiple devices. \n\nThe master device distributes the synchronized Advance Trigger to all devices in the system through the Advance Trigger distribution line.\n\nWhen synchronizing the Advance Trigger, one device must always be designated as the master. When the device is configured as a master, it actively drives the Advance Trigger distribution line. When the device is configured as a slave, set the NIRFSA_ATTR_ADVANCE_TRIGGER_TYPE attribute to NIRFSA_VAL_DIGITAL_EDGE, and the NIRFSA_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_SOURCE attribute to NIRFSA VAL SYNC ADVANCE TRIGGER STR.\n\nRefer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.\n\n**Defined Values:**\n\n| Value         | Description                                                                           |\n|:---------|:---------------------------------------------------------------------------|\n| VI_TRUE  | The device is the master device for synchronizing the Advance Trigger.     |\n| VI_FALSE | The device is not the master device for synchronizing the Advance Trigger. |\n\n**Default Value**: VI_FALSE\n\n**Supported Devices:** PXIe-5644/5645/5646'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Advance Trigger Master',
        'name': 'SYNC_ADVANCE_TRIGGER_MASTER',
        'type': 'ViBoolean'
    },
    1150185: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies which external trigger line distributes the synchronized Advance Trigger signal. \n\nWhen synchronizing the Advance Trigger, configure all devices to use the same Advance Trigger distribution line.\n\nRefer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.\n\n**Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0\n\n**Default Value**: "" (empty string)\n\n**Supported Devices:** PXIe-5644/5645/5646'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Advance Trigger Dist Line',
        'name': 'SYNC_ADVANCE_TRIGGER_DIST_LINE',
        'type': 'ViString'
    },
    1150186: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the power level, in dBm, expected at the LO IN terminal when the NIRFSA_ATTR_LO_SOURCE attribute is set to NIRFSA_VAL_LO_IN_STR.\n\n----\n**Note**\nFor the PXIe-5644/5645/5646, this attribute is always read-only.\n\n----\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO In Power (dBm)',
        'name': 'LO_IN_POWER',
        'type': 'ViReal64'
    },
    1150187: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL). \n\nFractional mode gives a finer frequency step resolution, but it may result in non harmonic spurs. Refer to the device specifications for your device for more information about fractional mode and non harmonic spurs.\n\n----\n**Note**\nThe NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute is applicable only when using the internal LO.\n\n----\n\n----\n**Note**\nFor the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653, this attribute is ignored if the PXIe-5653 is used as the LO source. For the PXIe-5841 with PXIe-5655, this attribute is ignored if the PXIe-5655 is used as the LO source.\n\n----\n\nTo use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsa_SetAttributeViInt32 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n**Defined Values:**\n\n%enum_table{enable attr vals}\n\n**Default Value**: NIRFSA_VAL_ENABLED\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO PLL Fractional Mode Enabled',
        'name': 'LO_PLL_FRACTIONAL_MODE_ENABLED',
        'type': 'ViInt32'
    },
    1150188: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL).\n\nYou can only tune the LO frequency by multiples of the NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE attribute. For the PXIe-5644/5645/5646 and PXIe-5840/5841, the LO frequency can therefore be offset from the requested center frequency by as much as half of the NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE attribute. This offset is corrected by digitally frequency shifting the NIRFSA_ATTR_LO_FREQUENCY attribute to the value requested in either the NIRFSA_ATTR_IQ_CARRIER_FREQUENCY attribute or the NIRFSA_ATTR_CENTER_FREQUENCY attribute.\n\n----\n**Note**\nFor the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653, this attribute is ignored if the PXIe-5653 is used as the LO source.\n\n----\n\nThe valid values for this attribute depend on the NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute.\n\n**PXIe-5644/5645/5646**: If the NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute is set to NIRFSA_VAL_DISABLED, the specified value is coerced to the closest valid value.\n\n**PXIe-5840/5841/5842**: If the NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute is set to NIRFSA_VAL_DISABLED, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.\n\n| NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED | PXIe-5644/5645 | PXIe-5646 | PXIe-5840/5841 | PXIe-5830/5831/5832 | PXIe-5841 w/PXIe-5655 |\n|-------------------------------|-----------------|------------|----------------|---------------------|-----------------------------------|\n| NIRFSA_VAL_ENABLED | 50 kHz to 24 MHz | 50 kHz to 25 MHz | 50 kHz to 100 MHz | LO1: 8 Hz to 400 MHz<br>LO2: 4 kHz to 400 MHz | 1 nHz to 50 MHz |\n| NIRFSA_VAL_DISABLED | 4 MHz, 5 MHz, 6 MHz, 12 MHz, 24 MHz | 2 MHz, 5 MHz, 10 MHz, 25 MHz | 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, 100 MHz | LO1: --<br>LO2: -- | 1 nHz to 50 MHz |\n\n* Values up to 100 MHz are coerced to 50 MHz.\n\n----\n**Note**\nThe default value for the PXIe-5831 depends on the frequency range of the selected port for your instrument configuration. Refer to the `Instrument Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/instrument-configurations.html>`_ topic for more information about available ports for your hardware configuration.\n\n----\n\n**Default Values:**\n\n**PXIe-5644/5645/5646:** 200 kHz\n\n**PXIe-5830:** 2 MHz\n\n**PXIe-5831/5832 (RF port):** 8 MHz\n\n**PXIe-5831/5832 (IF port):** 2 MHz, 4 MHz\n\n**PXIe-5840/5841:**\n\n- Fractional mode: 500 kHz\n- Integer mode: 10 MHz for frequencies less than or equal to 4 GHz. 20 MHz for frequencies greater than 4 GHz.\n\n**PXIe-5841 with PXIe-5655:** 500 kHz\n\n**PXIe-5842:** 1 Hz\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO Frequency Step Size (Hz)',
        'name': 'LO_FREQUENCY_STEP_SIZE',
        'type': 'ViReal64'
    },
    1150189: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the Reference Trigger is delayed with the data. \n\nSet this attribute to NIRFSA_VAL_DISABLED when the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute is set to NIRFSA_VAL_IQ_POWER_EDGE or NIRFSA_VAL_IQ_ANALOG_EDGE.\n\nRefer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.\n\n**Defined Values:**\n\n%enum_table{enable attr vals}\n\n**Default Value**: NIRFSA_VAL_DISABLED\n\n**Supported Devices:** PXIe-5644/5645/5646'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Ref Trigger Delay Enabled',
        'name': 'SYNC_REF_TRIGGER_DELAY_ENABLED',
        'type': 'ViInt32'
    },
    1150191: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the sub-sample delay, in seconds, to apply to the acquired signal.\n\nTo set this attribute, the NI-RFSA device must be in the Configuration state.\n\n**Valid Values:** -4.16 ns to +4.16 ns\n\n**Default Value**: 0\n\n**Supported Devices:** PXIe-5644/5645/5646'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Decimation Delay',
        'name': 'DECIMATION_DELAY',
        'type': 'ViReal64'
    },
    1150192: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the channel from which the device monitors the trigger. \n\nUse a value of "I" to monitor the I channel. Use a value of "Q" to monitor the Q channel. Use a value of "I,Q" to monitor both I and Q channels. This attribute affects the device operation only when the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute is set to NIRFSA_VAL_IQ_ANALOG_EDGE.\n\n**Valid Values:** "I", "Q", "I,Q", "Q,I"\n\n**Default Value:** "I"\n\n**Supported Devices:** PXIe-5644/5645'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Ref:IQ Analog Edge:Source',
        'name': 'IQ_ANALOG_EDGE_REF_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150193: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the device asserts the trigger when the voltage level is rising or falling. \n\nWhen you set the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute to NIRFSA_VAL_IQ_ANALOG_EDGE, the device asserts the trigger when the signal level exceeds the specified level with the slope you specify. This attribute affects the device operation only when the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute is set to NIRFSA_VAL_IQ_ANALOG_EDGE.\n\n**Defined Values:**\n\n%enum_table{ref trig iq pwr edge slope}\n\n**Default Value**: NIRFSA_VAL_RISING_SLOPE\n\n**Supported Devices:** PXIe-5644/5645'
        },
        'enum': 'RefTrigIqPwrEdgeSlope',
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Ref:IQ Analog Edge:Slope',
        'name': 'IQ_ANALOG_EDGE_REF_TRIGGER_SLOPE',
        'type': 'ViInt32'
    },
    1150194: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the analog level, in volts, at which the device triggers. \n\nThe device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute affects the device operation only when the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute is set to NIRFSA_VAL_IQ_ANALOG_EDGE.\n\n**Default Value:** 0 V\n\n**Supported Devices:** PXIe-5644/5645'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Ref:IQ Analog Edge:Level',
        'name': 'IQ_ANALOG_EDGE_REF_TRIGGER_LEVEL',
        'type': 'ViReal64'
    },
    1150195: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the size of the hysteresis window on either side of the trigger level. \n\nThe device triggers when the signal passes through the threshold you specify with the NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_LEVEL attribute, has the slope you specify with the NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_SLOPE attribute, and passes through the hysteresis window that you specify with this attribute. This attribute affects the device operation only when the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute is set to NIRFSA_VAL_IQ_ANALOG_EDGE.\n\n**Valid Values:** 0 to (Voltage Range/2 + Trigger Level) for Rising Slope. 0 to (Voltage Range/2 -Trigger Level) for Falling Slope. These values limit the hysteresis to the entire voltage range that is below the trigger level for Rising Slope or that is above the trigger level for Falling Slope.\n\n**Default Value:** The default is calculated by the driver as (Range x 0.025).\n\n**Supported Devices:** PXIe-5644/5645R'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Ref:IQ Analog Edge:Hysteresis',
        'name': 'IQ_ANALOG_EDGE_REF_TRIGGER_HYSTERESIS',
        'type': 'ViReal64'
    },
    1150196: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the digitizer OSP block delays Reference Triggers, along with the data samples, moving through the OSP block or if the Reference Triggers bypass the OSP block and are processed immediately.\n\nEnabling this attribute requires the following equipment configurations:\n\n- All digitizers being used must be the same model and hardware revision.\n- All digitizers must use the same firmware.\n- All digitizers must be configured with the same I/Q rate.\n- All devices must use the same signal path.\n\n**PXIe-5663/5663E**: Read the value of the NIRFSA_ATTR_IF_FILTER attribute to determine the IF filters used by the PXIe-5663/5663E.\n\n**PXIe-5665/5667/5668**:Refer to the device-specific information in the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute to determine the IF filters used by the PXIe-5665/5667/5668. If you set the NIRFSA_ATTR_FFT_WIDTH attribute, refer to the device-specific information for this attribute and the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute to determine the IF filters used. For frequencies less than 3.6 GHz, set the NIRFSA_ATTR_RF_PREAMP_ENABLED to the same value for all devices.\n\n**PXIe-5665 14 GHz**: Set the NIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED to the same value for all devices.\n\nIf the I/Q rate is set programmatically for I/Q acquisitions, the following attributes should be identical for the best device synchronization:\n\n- NIRFSA_ATTR_DIGITAL_IF_EQUALIZATION_ENABLED\n- NIRFSA_ATTR_SPECTRUM_OSP_SAMPLING_RATIO\n\nFor spectrum acquisitions, the following attributes should be identical for the best device synchronization:\n\n- NIRFSA_ATTR_SPECTRUM_SPAN\n- NIRFSA_ATTR_RESOLUTION_BANDWIDTH_TYPE\n- NIRFSA_ATTR_DIGITAL_IF_EQUALIZATION_ENABLED\n- NIRFSA_ATTR_SPECTRUM_OSP_SAMPLING_RATIO\n\nFor more information about the digitizer OSP block and Reference Triggers, refer to the following topics in the *NI High-Speed Digitizers Help*:\n\n- NI 5622 Onboard Signal Processing (OSP)\n- NI 5142 Onboard Signal Processing (OSP)\n- NI PXIe-5622 Trigger Sources\n- NI PXI-5142 Trigger Sources\n- NI PXIe-5622 Block Diagram\n- NI PXI-5142 Trigger Sources\n\n**Defined Values:**\n\n%enum_table{enable attr vals}\n\n**Default Value**: NIRFSA_VAL_ENABLED\n\n**Supported Devices**:PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Triggers:Ref:Advanced:OSP Delay Enabled',
        'name': 'REF_TRIGGER_OSP_DELAY_ENABLED',
        'type': 'ViInt32'
    },
    1150203: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies an offset from the I/Q carrier frequency for the downconverter. \n\nIf you set this attribute, any measurements outside the instantaneous bandwidth of the device are invalid. After you set this attribute, the RF downconverter is locked to that frequency offset until the value is changed or the attribute is reset.\n\n**Valid Values:**\n\n**PXIe-5646:**: -100 MHz to +100 MHz\n\n**PXIe-5830/5831/5832/5840/5841:**: -500 MHz to +500 MHz\n\n**All other devices:**: -42 MHz to +42 MHz\n\n**Default Values:**: For spectrum acquisition types the driver automatically calculates the default to avoid residual LO power. For I/Q acquisition types the default is 0 Hz. If the center frequency is set to a non-multiple of the NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE attribute, the NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET attribute is set to compensate for the difference.\n\n**Supported Devices:**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-selection.html>`_\n\n`PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-selection.html>`_\n\n`PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-selection.html>`_'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Acquisition:Advanced:Downconverter Frequency Offset',
        'name': 'DOWNCONVERTER_FREQUENCY_OFFSET',
        'type': 'ViReal64'
    },
    1150204: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the temperature of the I/Q IN circuitry on the device.\n\n**Units:** degrees C\n\n**Supported Devices:** PXIe-5645, PXIe-5820'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ In Port:Temperature (Degrees C)',
        'name': 'IQ_IN_PORT_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150205: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the IF filter path bandwidth for your device configuration.\n\n----\n**Note**\nFor composite devices, such as the PXIe-5665/5667/5668, the IF filter path bandwidth includes all IF filters across the component modules of a composite device.\n\n----\n\nNI-RFSA uses this attribute in conjunction with the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute and the NIRFSA_ATTR_DIGITAL_IF_EQUALIZATION_ENABLED attribute to determine the settings for your measurement. NI-RFSA selects the next highest available filter based on the value you specify. The following table lists the IF filters available for NI devices. You may specify a higher value than your device instantaneous bandwidth if your measurement requires it, but specifying a lower value returns an error.\n\n| Device                   | IF Filter Bandwidth Range | IF Filter         |\n|:-------------------------|:--------------------------|:------------------|\n| PXIe-5603/5665 (3.6 GHz) | 2264300 kHz                  | 300 kHz IF filter |\n| PXIe-5603/5665 (3.6 GHz) | >300 kHz and 22645 MHz      | Through IF filter |\n| PXIe-5603/5665 (3.6 GHz) | >5 MHz                   | Through IF filter |\n| PXIe-5605/5665 (14 GHz)  | 2264300 kHz                  | 300 kHz IF filter |\n| PXIe-5603/5665 (14 GHz)  | >300 kHz and 22645 MHz      | 5 MHz IF filter   |\n| PXIe-5603/5665 (14 GHz)  | >5 MHz                   | Through IF filter |\n| PXIe-5668                | 2264300 kHz                  | 300 kHz IF filter |\n| PXIe-5668                | >300 kHz and 22645 MHz      | 5 MHz IF filter   |\n| PXIe-5668                | >5 MHz and 2264100 MHz      | 100 MHz IF filter |\n| PXIe-5668                | >100 MHz and 2264320 MHz    | 320 MHz IF filter |\n| PXIe-5668                | >320 MHz                 | 765 MHz IF filter |\n\n**Valid Values**:\n\n**PXIe-5603/5605**: 0 to 80 MHz\n\n**PXIe-5665/5667**: 0 to 50 MHz\n\n**PXIe-5668**: 0 to 765 MHz\n\n**PXIe-5694**: 0 to 50 MHz\n\n----\n**Note**\nTo set this attribute to values greater than 20 MHz, you must set the NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED attribute to NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED\n\n----\n\n**Default Values:** For spectrum acquisition types the default is greater than or equal to the NIRFSA_ATTR_SPECTRUM_SPAN attribute. NI-RFSA chooses the default value of the NIRFSA_ATTR_IF_FILTER_BANDWIDTH attribute to correspond to the appropriate IF filter. For I/Q acquisition types NI-RFSA chooses the default value corresponding to the widest IF filter possible for your equipment setup.\n\n**Supported Devices**: PXIe-5603/5605/5606, PXIe-5665/5667/5668, PXIe-5694'
        },
        'lv_property': 'Signal Path:IF Filter Bandwidth',
        'name': 'IF_FILTER_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150206: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the shape factor of the window used in the fast Fourier transform (FFT). \n\nThe window shape factor is defined as the ratio of the 60 dB to 6 dB bandwidths.\n\nThe following table shows the shape factor for each NI-RFSA FFT window type.\n\n| Window Type            | Shape Factor |\n|:-----------------------|:-------------|\n| Uniform                | 1.57:1       |\n| Hanning                | 1.94:1       |\n| Hamming                | 2.13:1       |\n| Exact Blackman         | 2.52:1       |\n| Flat Top               | 2.0:1        |\n| 4-term Blackman-Harris | 2.5:1        |\n| 7-term Blackman-Harris | 4.1:1        |\n| Low Side Lobe          | 2.78:1       |\n| Gaussian               | 2.3:1        |\n| Kaiser Bessel          | 2.55:1       |\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860'
        },
        'lv_property': 'Acquisition:Spectrum:FFT Window Shape Factor',
        'name': 'FFT_WINDOW_SHAPE_FACTOR',
        'type': 'ViReal64'
    },
    1150207: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to use the low-frequency bypass path for the incoming RF signal.\n\n|                            |                                         |\n|:---------------------------|:----------------------------------------|\n| NIRFSA_VAL_DISABLED (1900) | Disables the low-frequency bypass path. |\n| NIRFSA_VAL_ENABLED (1901)  | Enables the low-frequency bypass path.  |\n\n**Default Value**: NIRFSA_VAL_DISABLED\n\n**Supported Devices**: PXIe-5693, PXIe-5667'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Signal Path:Advanced:Low Frequency Bypass Enabled',
        'name': 'LOW_FREQUENCY_BYPASS_ENABLED',
        'type': 'ViInt32'
    },
    1150208: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the location in a signal path where an RF conditioning calibration tone is injected or whether the tone is disabled.\n\n**Defined Values:**\n\n%enum_table{conditioning cal tone mode}\n\n**Default Value**: NIRFSA_VAL_DISABLED\n\n**Supported Devices**: PXIe-5667, PXIe-5693/5698'
        },
        'enum': 'ConditioningCalToneMode',
        'lv_property': 'Self Calibration:RF Conditioning Cal Tone Mode',
        'name': 'RF_CONDITIONING_CAL_TONE_MODE',
        'type': 'ViInt32'
    },
    1150209: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the frequency of the RF conditioning calibration tone, in hertz (Hz).\n\n**Valid Values**: 34.5 MHz to 7.5 GHz\n\n**Default Value**: 1.0 GHz\n\n**Supported Devices**: PXIe-5667, PXIe-5693/5698'
        },
        'lv_property': 'Self Calibration:RF Conditioning Cal Tone Frequency',
        'name': 'RF_CONDITIONING_CAL_TONE_FREQUENCY',
        'type': 'ViReal64'
    },
    1150210: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the current temperature, in degrees Celsius, of the IF conditioning module associated with the NI-RFSA device.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5667'
        },
        'lv_property': 'Device Characteristics:IF Conditioning Temperature (Degrees C)',
        'name': 'IF_CONDITIONING_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150211: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the current temperature, in degrees Celsius, of the RF conditioning module associated with the NI-RFSA device.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5667'
        },
        'lv_property': 'Device Characteristics:RF Conditioning Temperature (Degrees C)',
        'name': 'RF_CONDITIONING_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150215: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the RF lowband signal conditioning path.\n\n**Valid Values**: \n\nNIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_1\n\nNIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_2\n\n**Default Value**: NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_1\n\n**Supported Devices**: PXIe-5606'
        },
        'enum': 'RfLbSigCondPathSel',
        'lv_property': 'Factory Calibration:NI 5665/5668R:RF Lowband Signal Conditioning Path Selection',
        'name': 'CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_SELECTION',
        'type': 'ViInt32'
    },
    1150216: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the size of the selected IF attenuation table.\n\n**Valid Values**: 0-132\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5606'
        },
        'lv_property': 'Factory Calibration:NI 5665/5668R:IF Attenuation Table Size',
        'name': 'CAL_IF_ATTENUATION_TABLE_SIZE',
        'type': 'ViInt32'
    },
    1150217: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the device is the master device for synchronizing the Sample Clock between multiple devices. \n\nThe master device distributes the Sample Clock sync signal to all devices in the system through the Sample Clock sync distribution line.\n\nWhen synchronizing the Sample Clock, one device must always be designated as the master. The master device actively drives the Sample Clock sync distribution line.\n\nRefer to [Synchronization Using NI-RFSA and NI-RFSG](PXIe-5646.chm/synchronization-rfsa-g.html) for more information about PXIe-5646 device synchronization.\n\n**Defined Values:**\n\n| Value         | Description                                                                    |\n|:---------|:--------------------------------------------------------------------|\n| VI_TRUE  | The device is the master device for synchronizing the Sample Clock. |\n| VI_FALSE | The device is not the master for synchronizing the Sample Clock.    |\n\n**Default Value:** VI_FALSE\n\n**Supported Devices:** PXIe-5646'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Sample Clock Master',
        'name': 'SYNC_SAMPLE_CLOCK_MASTER',
        'type': 'ViBoolean'
    },
    1150218: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies which external trigger line distributes the Sample Clock sync signal. \n\nWhen synchronizing the Sample Clock, configure all devices to use the same Sample Clock distribution line.\n\nRefer to `Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/pxie-5644-feature/page/synchronization-rfsa-g.html>`_ for more information about PXIe-5646 device synchronization.\n\n**Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0\n\n**Default Value:** "" (empty string)\n\n**Supported Devices:** PXIe-5646'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Sample Clock Dist Line',
        'name': 'SYNC_SAMPLE_CLOCK_DIST_LINE',
        'type': 'ViString'
    },
    1150219: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies that an optimized IF filtering selection is made at different spectrum frequency ranges during spectrum acquisition.\n\nThe IF filter used depends on the configured RF center frequency, as shown in the following table.\n\n| Center Frequency    | IF Filter |\n|:--------------------|:----------|\n| 0 Hz and <80 MHz | 300 kHz   |\n| 0 MHz             | 50 MHz    |\n\n----\n**Note**\nSetting this attribute to **Enabled** prevents you from setting NIRFSA_ATTR_IF_FILTER_BANDWIDTH or NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH.\n\n----\n\n**Defined Values:**\n\n%enum_table{enable attr vals}\n\n**Default Value**: NIRFSA_VAL_DISABLED\n\n**Supported Devices**: PXIe-5665/5668'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Acquisition:Spectrum:Smooth Spectrum Enabled',
        'name': 'SMOOTH_SPECTRUM_ENABLED',
        'type': 'ViInt32'
    },
    1150220: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the maximum corner frequency of the highpass filter in the RF signal path. \n\nThe device uses the highest frequency highpass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables highpass filtering.\n\nFor multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this attribute returns the value you specified rather than a coerced value if multiple highpass filters are used during the acquisition.\n\nThe PXIe-5606 features highpass filters at 1.35 GHz and 2.2 GHz.\n\n**Valid Values**: 0 to 26.5\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5606, PXIe-5668'
        },
        'lv_property': 'Signal Path:Advanced:RF Highpass Filtering',
        'name': 'RF_HIGH_PASS_FILTERING',
        'type': 'ViReal64'
    },
    1150221: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string containing the path to the location of the current NI-RFSA instrument driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device. \n\nYou can specify the bitfile location using the Driver Setup string in the **optionString** parameter of the nirfsa_InitWithOptions function.\n\nNI-RFSA instrument driver FPGA extensions enable you to use pre-compiled FPGA bitfiles to customize the behavior of the device FPGA while maintaining the functionality of the NI-RFSA instrument driver.\n\nRefer to `NI-RFSA Instrument Driver FPGA Extensions <https://www.ni.com/docs/en-US/bundle/ni-rf-vst/page/rfsa-rfsg-instrument-driver-fpga-extensions.html>`_ for more information about using NI-RFSA instrument driver FPGA extensions for NI devices.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:FPGA Bitfile Path',
        'name': 'FPGA_BITFILE_PATH',
        'type': 'ViString'
    },
    1150222: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables the 28 V DC source on the device front panel.\n\n**PXIe-5668 with PXIe-5698**: When this attribute is set to NIRFSA_VAL_ENABLED, the PXIe-5698 noise source is used instead of the PXIe-5668 noise source.\n\n**Units**: dB\n\n**Default Value**: NIRFSA_VAL_DISABLED\n\n**Supported Devices**: PXIe-5606, PXIe-5668, PXIe-5698'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Device Specific:5606:Noise Source Power Enabled',
        'name': 'NOISE_SOURCE_POWER_ENABLED',
        'type': 'ViInt32'
    },
    1150223: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the internal gain self-calibration correction for the 100 MHz IF filter path.\n\nThe value you specify using this attribute overrides any previously-set value.\n\n**Units**: dB\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5606'
        },
        'lv_property': 'Self Calibration:NI 5665/5668R:Calibration Correction for 100 MHz Filter',
        'name': 'CALIBRATION_CORRECTION_100_MHZ_FILTER',
        'type': 'ViReal64'
    },
    1150224: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the internal gain self-calibration correction for the 320 MHz IF filter path.\n\nThe value you specify using this attribute overrides any previously-set value.\n\n**Units**: dB\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5606'
        },
        'lv_property': 'Self Calibration:NI 5665/5668R:Calibration Correction for 320 MHz Filter',
        'name': 'CALIBRATION_CORRECTION_320_MHZ_FILTER',
        'type': 'ViReal64'
    },
    1150225: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the internal gain self-calibration correction for the 765 MHz IF filter path.\n\nThe value you specify using this attribute overrides any previously-set value.\n\n**Units**: dB\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5606'
        },
        'lv_property': 'Self Calibration:NI 5665/5668R:Calibration Correction for 765 MHz Filter',
        'name': 'CALIBRATION_CORRECTION_765_MHZ_FILTER',
        'type': 'ViReal64'
    },
    1150226: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the currently associated digitizer ID.\n\nAllows the use of self calibration data when configured in external digitizer mode.\n\n**Default Value**: "" (empty string) in external digitizer mode\n\n**Supported Devices**: PXIe-5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668'
        },
        'lv_property': 'Self Calibration:Digitizer ID',
        'name': 'CAL_DIGITIZER_ID',
        'type': 'ViString'
    },
    1150228: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the actual frequency, in hertz (Hz), of the digitizer Sample Clock.\n\n**Units**: hertz (Hz)\n\n**Supported Devices**: PXIe-5668'
        },
        'lv_property': 'Clocking:Digitizer Sample Clock Rate',
        'name': 'DIGITIZER_SAMPLE_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1150229: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the terminal at which to export the Digitizer Sample Clock.\n\n**Valid Values**: \n%enum_table{digitizer samp clk exported term}\n\n**Default Value**: "" (empty string)\n\n**Supported Devices**: PXIe-5668'
        },
        'enum': 'DigitizerSampClkExportedTerm',
        'lv_property': 'Clocking:Digitizer Sample Clock Exported Terminal',
        'name': 'EXPORTED_DIGITIZER_SAMPLE_CLOCK_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150233: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string containing the name of the FPGA target being used. \n\nThis name can be used with the RIO open session to open a reference to the FPGA.\n\nThis attribute is channel dependent if multiple targets are supported.\n\n**Supported Devices:** PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:FPGA Target Name',
        'name': 'FPGA_TARGET_NAME',
        'type': 'ViString'
    },
    1150234: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Use subspan overlap process to eliminate or reduce analyzer spurs. \n\nTo enable this feature, specify a non-zero percentage overlap between consecutive subspans in a spectrum acquisition.\n\nIf a value greater than 0 is specified, then for each spectral line in the resulting spectrum, the driver acquires data twice with slightly different hardware settings, so that the analyzer spurs, if any, are present at different frequencies in the two acquisitions. Typically, LO frequency is shifted between the acquisitions causing analyzer spurs that are relative to the LO frequency, to move from one frequency to another. Those spurs, which are present in only one of the acquisitions for each spectral line, get removed.\n\nThe subspan overlap feature will not remove any spurs from the Device Under Test or modify the signal being measured; unlike the analyzer spurs, the spurs in the signal being measured stay at a constant frequency in the two acquisitions.\n\n----\n**Note**\nSubspan overlap process effectively is performing minimum averaging, which might reduce the measured noise floor level. NI-RFSA Spectrum Averaging can be enabled to minimize the effect of subspan overlap on the noise floor.\n\n----\n\n----\n**Note**\nNI-RFSA may apply further shifts to the specified value to accommodate fixed-frequency edges of components such as preselectors.\n\n----\n\n**Valid Values**:\n\n**PXIe-5665/5668**: 0 to < 100\n\n**PXIe-5820/5830/5831/5832/5840/5841/5860**: 0\n\n**PXIe-5842**: 0, 50\n\n**Default Value**: 0\n\n**Supported Devices**: PXIe-5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n----\n**Note**\nSubspan overlap will not be supported by PXIe-5842, if RMM-5585 (54GHz Frequency Extension) is connected.\n\n----'
        },
        'lv_property': 'Acquisition:Spectrum:Subspan Overlap',
        'name': 'SUBSPAN_OVERLAP',
        'type': 'ViReal64'
    },
    1150235: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to enable the LO2 OUT terminal on the installed devices.\n\nSet this attribute to TRUE to export the 4 GHz LO signal from the device LO2 IN terminal to the LO2 OUT terminal.\n\nYou can also export the LO2 signal by setting the NIRFSA_ATTR_LO_EXPORT_ENABLED attribute and the NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE attribute.\n\n**Defined Values:**\n\n|          |                                |\n|:---------|:-------------------------------|\n| VI_TRUE  | Enables the LO2 OUT terminal.  |\n| VI_FALSE | Disables the LO2 OUT terminal. |\n\n**Default Value:** VI_FALSE\n\n**Supported Devices:** PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5668'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Signal Path:LO2 Export Enabled',
        'name': 'LO2_EXPORT_ENABLED',
        'type': 'ViInt32'
    },
    1150236: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the maximum instantaneous bandwidth of the device.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:Max Device Instantaneous Bandwidth',
        'name': 'MAX_DEVICE_INSTANTANEOUS_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150237: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the maximum I/Q rate.\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:Max IQ Rate',
        'name': 'MAX_IQ_RATE',
        'type': 'ViReal64'
    },
    1150246: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the power level, in dBm, of the signal at the LO OUT terminal when the NIRFSA_ATTR_LO_EXPORT_ENABLED attribute is set to VI_TRUE.\n\nTo use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsa_SetAttributeViReal64 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n**Units:** dBm\n\n**Supported Devices:** PXIe-5830/5831/5832/5840/5841/5842'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO Out Power (dBm)',
        'name': 'LO_OUT_POWER',
        'type': 'ViReal64'
    },
    1150254: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the current temperature, in degrees Celsius, of the FPGA.\n\n----\n**Note**\nIf you query this attribute during RF list mode, list steps may take longer to complete during list execution.\n\n----\n\n**Units**: degrees Celcius\n\n**Default Value**: N/A\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:FPGA Temperature (Degrees C)',
        'name': 'FPGA_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150255: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the module power consumption.\n\n----\n**Note**\nIf you query this attribute during RF list mode, list steps may take longer to complete during list execution.\n\n----\n\n**Units**: watts\n\n**Default Value**: N/A\n\n**Supported Devices:**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:Module Power Consumption (W)',
        'name': 'MODULE_POWER_CONSUMPTION',
        'type': 'ViReal64'
    },
    1150256: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables or disables warnings and errors when you set frequency, power, or bandwidth values beyond the limits of the NI-RFSA device specifications.\n\nWhen you set this attribute to NIRFSA_VAL_ENABLED, the driver does not report out-of-specification warnings and errors.\n\n**Defined Values:**\n\n%enum_table{enable attr vals}\n\n**Default Value**: NIRFSA_VAL_DISABLED\n\n**Supported Devices:** PXIe-5820/5830/5831/5840/5841/5842/5860'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Acquisition:Advanced:Allow Out Of Specification User Settings',
        'name': 'ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS',
        'type': 'ViInt32'
    },
    1150266: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the sub-sample clock delay, in seconds, to apply to the acquired signal.\n\nUse this attribute to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. \nThis attribute can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurement to the current session.\n\nTo set this attribute, the NI-RFSA device must be in the Configuration state.\n\n----\n**Note**\nIf this attribute is set, NI-TClk cannot do any sub-sample clock adjustment.\n\n----\n\n**Units:** Seconds\n\n**Valid Values:** Plus or minus half of one sample clock period\n\n**Default Value**: 0\n\n**Supported Devices:** PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Absolute Delay',
        'name': 'ABSOLUTE_DELAY',
        'type': 'ViReal64'
    },
    1150267: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': "Specifies the bandwidth of the input signal around the NIRFSA_ATTR_IQ_CARRIER_FREQUENCY. \n\nThis value must be less than or equal to (0.8 7 [I/Q rate](NIRFSA_ATTR_IQ_RATE.html)).\n\nNI-RFSA defines *signal bandwidth* as twice the maximum I/Q signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the signal bandwidth is simply the baseband signal's minimum frequency subtracted from its maximum frequency, or *f* < sub>max</sub> - *f*< sub>min</sub>.\n\nIf you do not set this attribute, NI-RFSA uses the maximum available signal bandwidth. Depending on your device settings, setting this attribute enables certain optimizations. Based on the specified signal bandwidth, NI-RFSA decides the minimum equalized bandwidth and equalizer gain.\n\n----\n**Note**\nYou must set this attribute to enable the NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE attribute.\n\n----\n\nEnsure you set the signal bandwidth wide enough to encompass all significant anticipated input power. In cases where NI-RFSA optimizes the input gain based on the signal bandwidth, significant input power outside the signal bandwidth can lead to clipping and associated overflow warnings if you do not have enough margin in your [reference level.](NIRFSA_ATTR_REFERENCE_LEVEL.html)\n\n**Units**: Hz\n\n**Default Value**: 0 Hz\n\n**Supported Devices:**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-selection.html>`_\n\n`PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-selection.html>`_\n\n`PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-selection.html>`_"
        },
        'lv_property': 'Acquisition:IQ:Signal Bandwidth (Hz)',
        'name': 'SIGNAL_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150269: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the common-mode level presented at each differential input terminal.\n\nCommon-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT).\n\n**Units**: volts\n\n**Default Value**: 0 V\n\n**Supported Devices**: PXIe-5820'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ In Port:Common Mode Level',
        'name': 'COMMON_MODE',
        'type': 'ViReal64'
    },
    1150271: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures error reporting for ADC and onboard signal processing overflows. \n\nOverflows lead to clipping of the waveform.\n\n**Defined Values:**\n\n%enum_table{overflow error reporting}\n\n**Default Value**: NIRFSA_VAL_ERROR_REPORTING_WARNING\n\n**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'enum': 'OverflowErrorReporting',
        'lv_property': 'Vertical:Advanced:Overflow Error Reporting',
        'name': 'OVERFLOW_ERROR_REPORTING',
        'type': 'ViInt32'
    },
    1150285: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the size of the DMA buffer in computer memory, in bytes. \n\nTo set this attribute, the NI-RFSA device must be in the Configuration state.\n\nA sufficiently large host DMA buffer improves performance by allowing large fetches to be transferred more efficiently.\n\n**Default Value:** 8 MB\n\n**Supported Devices**: PXI-5820/5830/5831/5840/5841/5842/5860'
        },
        'lv_property': 'Acquisition:Fetch:Data Transfer:Host DMA Buffer Size',
        'name': 'HOST_DMA_BUFFER_SIZE',
        'type': 'ViInt64'
    },
    1150297: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the port to configure.\n\n----\n**Note**\nWhen using RF list mode, ports cannot be shared with NI-RFSA.\n\n----\n\n**Valid Values**:\n\n**PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860**: "" (empty string)\n\n**PXIe-5830**: if0, if1\n\n**PXIe-5831/5832**: if0, if1, rf <0-1> port <x>, where\n\n*0-1* indicates one (*0*) or two (*1*) mmRH-5582 connections and\n\n*x* is the port number on the mmRH-5582 front panel.\n\n**Default Value:**\n\n**PXIe-5830/5831/5832:**: if1\n\n**PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860**: "" (empty string)\n\n**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\nNIRFSA_ATTR_AVAILABLE_PORTS'
        },
        'lv_property': 'Signal Path:Advanced:Selected Ports',
        'name': 'SELECTED_PORTS',
        'type': 'ViString'
    },
    1150298: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to enable the RF OUT LO OUT terminal on the PXIe-5840/5841.\n\nWhen this attribute is enabled, if the NIRFSA_ATTR_LO_SOURCE attribute is set to NIRFSA_VAL_LO_IN_STR and you do not set the NIRFSA_ATTR_LO_FREQUENCY or NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY attributes, NI-RFSA rounds the LO frequency to approximately an LO step size as if the source was NIRFSA_VAL_ONBOARD_STR. This ensures that when you configure NI-RFSA and NI-RFSG with compatible settings that result in the same LO frequency, the rounding also is compatible.\n\n**Defined Values:**\n\n%enum_table{enable unspecified attr vals}\n\n**Default Value:**: NIRFSA_VAL_UNSPECIFIED\n\n**Supported Devices**: PXIe-5840/5841/5842'
        },
        'enum': 'EnableUnspecifiedAttrVals',
        'lv_property': 'Signal Path:RF Out LO Export Enabled',
        'name': 'RF_OUT_LO_EXPORT_ENABLED',
        'type': 'ViInt32'
    },
    1150299: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to allow NI-RFSG to control the NI-RFSA LO out export.\n\nSet this attribute to NIRFSA_VAL_ENABLED to allow NI-RFSG to control the LO out export. Use the NIRFSG ATTR RF IN LO EXPORT ENABLED attribute to control the NI-RFSA LO out export from NI-RFSG.\n\n**Defined Values:**\n\n%enum_table{enable attr vals}\n\n**Default Value:** NIRFSA_VAL_DISABLED\n\n**Supported Devices**: PXIe-5840/5841/5842'
        },
        'enum': 'EnableAttrVals',
        'lv_property': 'Signal Path:LO Out Export Configure From RFSG',
        'name': 'LO_OUT_EXPORT_CONFIGURE_FROM_RFSG',
        'type': 'ViInt32'
    },
    1150300: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the temperature change required before NI-RFSA recalculates the thermal correction settings when entering the Running state.\n\n**Units:** degrees Celsius (C)\n\n**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Default Values**:\n\n**PXIe-5830/5831/5832/5842/5860**: 0.2\n\n**PXIe-5840/5841**: 1.0'
        },
        'lv_property': 'Vertical:Advanced:Thermal Correction Temperature Resolution (Degrees C)',
        'name': 'THERMAL_CORRECTION_TEMPERATURE_RESOLUTION',
        'type': 'ViReal64'
    },
    1150301: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the scaling factor applied to the time-domain voltage data in the digitizer.\n\nNI-RFSA does not compensate for the specified digital gain.\n\nYou can use this attribute to account for external gain changes without changing the analog signal path.\n\n----\n**Note**\nThe PXIe-5644/5645/5646 applies this gain when the data is scaled. The raw data does not include this scaling on these devices.\n\n----\n\n**Units:** dB\n\n**Default Value:** 0 dB\n\n**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Vertical:Advanced:Digital Gain (dB)',
        'name': 'DIGITAL_GAIN',
        'type': 'ViReal64'
    },
    1150305: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to allow NI-RFSA to select the downconveter frequency offset. \n\nYou can either set an offset yourself or let NI-RFSA select one for you.\n\nPlacing the downconverter center frequency outside the bandwidth of your input signal can help avoid issues such as LO leakage.\n\nTo set an offset yourself, set this attribute to NIRFSA_VAL_AUTOMATIC or NIRFSA_VAL_USER_DEFINED, and set either the NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY or the NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET attributes.\n\nTo allow NI-RFSA to automatically select the downconverter frequency offset, set this attribute to NIRFSA_VAL_AUTOMATIC or NIRFSA_VAL_ENABLED and configure the NIRFSA_ATTR_SIGNAL_BANDWIDTH attribute to describe your expected input signal. The signal bandwidth must be no greater than half the specified value of the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute, minus a device-specific guard band. Do not set the NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY or NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET attributes. If all conditions are met, NI-RFSA places the downconverter center frequency outside the signal bandwidth. Set this attribute to NIRFSA_VAL_ENABLED if you want to receive an error any time NI-RFSA is unable to apply automatic offset.\n\nWhen you set an offset yourself or do not use an offset, the reference frequency for gain is near the downconverter center frequency, and NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE returns NIRFSA_VAL_USER_DEFINED. When NI-RFSA automatically sets an offset, the reference frequency for gain is the NIRFSA_ATTR_IQ_CARRIER_FREQUENCY, and NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE returns NIRFSA_VAL_ENABLED. Refer to the specifications document for your device for more information about gain, flatness, and reference frequencies.\n\n----\n**Note**\nBelow 120 MHz, the PXIe-5841 does not use an LO and NIRFSA_VAL_ENABLED is unavailable. Refer to the *PXIe-5841 Automatic Frequency Offset* topic for more information about using an automatic offset with an external LO.\n\n----\n\n**Defined Values:**\n\n%enum_table{downconverter frequency offset mode}\n\n**Default Value:** NIRFSA_VAL_AUTOMATIC\n\n**Supported Devices**: PXIe-5830/5831/5832/5841/5842\n\n**Related Topics**\n\n`PXIe-5830 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/automatic-frequency-offset.html>`_\n\n`PXIe-5831/5832 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/automatic-frequency-offset.html>`_\n\n`PXIe-5841 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/automatic-frequency-offset.html>`_'
        },
        'enum': 'DownconverterFrequencyOffsetMode',
        'lv_property': 'Acquisition:Advanced:Downconverter Frequency Offset Mode',
        'name': 'DOWNCONVERTER_FREQUENCY_OFFSET_MODE',
        'type': 'ViInt32'
    },
    1150306: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a comma-separated list of the available ports for use based on your instrument configuration.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Signal Path:Advanced:Available Ports',
        'name': 'AVAILABLE_PORTS',
        'type': 'ViString'
    },
    1150307: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the type of de-embedding to apply to measurements on the specified port.\n\nTo use this attribute, you must use the channelName parameter of the nirfsa_SetAttributeViInt32 function to specify the name of the port to configure for de-embedding.\n\nIf you set this attribute to NIRFSA_VAL_DEEMBEDDING_TYPE_SCALAR or NIRFSA_VAL_DEEMBEDDING_TYPE_VECTOR, NI-RFSA adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT.\n\n**Defined Values:**\n\n%enum_table{deembedding type attr vals}\n\n**Default Value**: NIRFSA_VAL_DEEMBEDDING_TYPE_SCALAR\n\n**Valid Values for PXIe-5830/5832/5840/5841/5842/5860** : NIRFSA_VAL_DEEMBEDDING_TYPE_SCALAR or  NIRFSA_VAL_DEEMBEDDING_TYPE_NONE\n\n**Valid Values for PXIe-5831:** NIRFSA_VAL_DEEMBEDDING_TYPE_VECTOR, NIRFSA_VAL_DEEMBEDDING_TYPE_SCALAR, or NIRFSA_VAL_DEEMBEDDING_TYPE_NONE. NIRFSA_VAL_DEEMBEDDING_TYPE_VECTOR is only supported for TRX Ports in a Semiconductor Test System (STS).\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'enum': 'DeembeddingTypeAttrVals',
        'lv_property': 'De-embedding:Type',
        'name': 'DEEMBEDDING_TYPE',
        'type': 'ViInt32'
    },
    1150308: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Selects the de-embedding table to apply to the measurements on the specified port.\n\nTo use this attribute, you must use the channelName parameter of the nirfsa_SetAttributeViString function to specify the name of the port to configure for de-embedding.\n\nIf de-embedding is enabled, NI-RFSA uses the specified table to remove the effects of the external network between the instrument and the DUT.\n\nUse the nirfsa_CreateDeembeddingSparameterTableArray function to create tables.\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'De-embedding:Selected Table',
        'name': 'DEEMBEDDING_SELECTED_TABLE',
        'type': 'ViString'
    },
    1150309: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the margin NI-RFSA adds to the NIRFSA_ATTR_REFERENCE_LEVEL attribute. \n\nThe margin helps to avoid clipping and overflow warnings if the input signal exceeds the configured reference level.\n\nNI-RFSA configures the input gain to avoid clipping and associated overflow warnings as long as the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or have already included margin in the reference level, you may be able to improve the signal-to-noise ratio by reducing the reference level headroom.\n\n**Units**: dB\n\n**Default Value**:\n\n**PXIe-5830/5831/5832/5841/5842/5860**: 1 dB\n\n**PXIe-5840**: 0 dB\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Vertical:Advanced:Reference Level Headroom (dB)',
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'ViReal64'
    },
    1150312: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal.\n\n----\n**Note**\nDo not set this attribute with the NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE attribute.\n\n----\n\n**Valid Values**:\n\nLO1: 1 Hz to 50 MHz\n\nLO2: 1 Hz to 100 MHz\n\n**Default Values**: 1 MHz\n\n**Supported Devices**: PXIe-5830/5831/5832'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO VCO Frequency Step Size (Hz)',
        'name': 'LO_VCO_FREQUENCY_STEP_SIZE',
        'type': 'ViReal64'
    },
    1150316: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the NIRFSA_ATTR_DEVICE_TEMPERATURE attribute.\n\nFor example, if this property is set to 5.0, and the device is self-calibrated at 35 C, then you can expect to run the device from 30 C to 40 C with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance and ADC or DSP overflows.\n\n**Units:** degrees Celsius (C)\n\n**Default Value**:\n\n**PXIe-5830/5831/5832/5842/5860**: 5\n\n**PXIe-5840/5841**: 10\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Vertical:Advanced:Thermal Correction Headroom Range (Degrees C)',
        'name': 'THERMAL_CORRECTION_HEADROOM_RANGE',
        'type': 'ViReal64'
    },
    1150321: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the pulse width units for the User Source. \n\nWhen the value is NIRFSA_VAL_PULSE_WIDTH_UNITS_SECONDS, it is assumed that the clock rate of the signal is the data clock. Use NIRFSA_VAL_PULSE_WIDTH_UNITS_CLOCK_PERIODS if the user source clock rate is anything else.\n\n**Defined Values:**\n\n%enum_table{user source pulse width units}\n\n**Default Value**: NIRFSA_VAL_PULSE_WIDTH_UNITS_SECONDS\n\n**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'enum': 'UserSourcePulseWidthUnits',
        'lv_property': 'Events:User Source:Pulse Width Units',
        'name': 'USER_SOURCE_PULSE_WIDTH_UNITS',
        'type': 'ViInt32'
    },
    1150322: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the pulse width for the User Source. \n\nUse the NIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH_UNITS attribute to set the units for the pulse width.\n\n**Default Value**: 200E(-9)\n\n**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Events:User Source:Pulse Width',
        'name': 'USER_SOURCE_PULSE_WIDTH',
        'type': 'ViReal64'
    },
    1150324: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies a comma-separated list of ports for which to fix the group delay.\n\n**Valid Values**:\n\nPXIe-5831/5832: rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel.\n\n**Default Value**:\n\nPXIe-5831/5832: (empty string), which specifies that the group delay will not be fixed for any port.\n\n**Supported Devices**: PXIe-5831/5832'
        },
        'lv_property': 'Signal Path:Advanced:Fixed Group Delay Across Ports',
        'name': 'FIXED_GROUP_DELAY_ACROSS_PORTS',
        'type': 'ViString'
    },
    1150325: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the de-embedding gain applied to compensate for the mismatch on the specified port. Use the Active Channel property to specify the name of the port to configure for de-embedding.\n\nIf de-embedding is enabled, NI-RFSA uses the returned compensation gain to remove the effects of the external network between the instrument and the DUT.\n\n**Supported Devices**: PXIe-5830/5831/5840/5841/5842/5860'
        },
        'lv_property': 'De-embedding:Compensation Gain',
        'name': 'DEEMBEDDING_COMPENSATION_GAIN',
        'type': 'ViReal64'
    },
    1150326: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the Reference Clock Rate, in Hz, of the signal sent to the Ref Clock Exported Terminal.\n\n**Default Value**: 10 MHz\n\n**Valid Values**:\n\nPXIe-5820/5830/5831/5832/5840/5841: 10 MHz\n\nPXIe-5842: 10 MHz, 100 MHz, 1 GHz\n\nPXIe-5860: 10 MHz, 100 MHz\n\n**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'enum': 'ReferenceClockExportedRate',
        'lv_property': 'Clocking:Ref Clock Exported Rate:Ref Clock Exported Rate',
        'name': 'EXPORTED_REF_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1150331: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies which path to configure to acquire a signal.\n\n**Default Value**: "" (empty string)'
        },
        'lv_property': 'Signal Path:Advanced:Selected Path',
        'name': 'SELECTED_PATH',
        'type': 'ViString'
    },
    1150332: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a comma separated list of the configurable paths available for use based on your instrument configuration.'
        },
        'lv_property': 'Signal Path:Advanced:Available Paths',
        'name': 'AVAILABLE_PATHS',
        'type': 'ViString'
    },
    1150333: {
        'access': 'read only',
        'name': 'CREATED_SESSION_CHANNEL',
        'type': 'ViInt32'
    },
    1150334: {
        'access': 'read only',
        'name': 'MIN_FUNDAMENTAL_SILO_FREQUENCY',
        'type': 'ViReal64'
    },
    1150335: {
        'access': 'read only',
        'name': 'MAX_FUNDAMENTAL_SILO_FREQUENCY',
        'type': 'ViReal64'
    },
    1150337: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the configurations to skip to reset while loading configurations from a file.\n\n**Default Value:**  NIRFSA_VAL_SKIP_NONE\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSA_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE',
                    'NI-RFSA resets all configurations.'
                ],
                [
                    'NIRFSA_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_DEEMBEDDING_TABLES',
                    'NI-RFSA skips resetting the de-embedding tables.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'LoadConfigurationResetOptions',
        'lv_property': 'Load Configurations:Reset Options',
        'name': 'LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS',
        'type': 'ViInt32'
    },
    1150356: {
        'access': 'read only',
        'name': 'ASSOC_AUX_SWITCH_GAIN_UID',
        'type': 'ViInt32'
    }
}
