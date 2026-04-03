# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import nirfsa._attributes as _attributes
import nirfsa._converters as _converters
import nirfsa._library_interpreter as _library_interpreter
import nirfsa.enums as enums
import nirfsa.errors as errors

import hightime
import nitclk

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


class _Acquisition(object):
    def __init__(self, session):
        self._session = session
        self._session.initiate()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.abort()


# From https://stackoverflow.com/questions/5929107/decorators-with-parameters
def ivi_synchronized(f):
    @wraps(f)
    def aux(*xs, **kws):
        session = xs[0]  # parameter 0 is 'self' which is the session object
        with session.lock():
            return f(*xs, **kws)
    return aux


class _Lock(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        # _lock_session is called from the lock() function, not here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.unlock()


class _RepeatedCapabilities(object):
    def __init__(self, session, prefix, current_repeated_capability_list):
        self._session = session
        self._prefix = prefix
        # We need at least one element. If we get an empty list, make the one element an empty string
        self._current_repeated_capability_list = current_repeated_capability_list if len(current_repeated_capability_list) > 0 else ['']
        # Now we know there is at lease one entry, so we look if it is an empty string or not
        self._separator = '/' if len(self._current_repeated_capability_list[0]) > 0 else ''

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)
        complete_rep_cap_list = [current_rep_cap + self._separator + rep_cap for current_rep_cap in self._current_repeated_capability_list for rep_cap in rep_caps_list]

        return _SessionBase(
            repeated_capability_list=complete_rep_cap_list,
            all_channels_in_session=self._session._all_channels_in_session,
            interpreter=self._session._interpreter,
            freeze_it=True
        )


# This is a very simple context manager we can use when we need to set/get attributes
# or call functions from _SessionBase that require no channels. It is tied to the specific
# implementation of _SessionBase and how repeated capabilities are handled.
class _NoChannel(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._repeated_capability_cache = self._session._repeated_capability
        self._session._repeated_capability = ''

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._repeated_capability = self._repeated_capability_cache


class _SessionBase(object):
    '''Base class for all NI-RFSA sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    _5665_preselector_tuning_dac_value = _attributes.AttributeViInt32(1150158)
    '''Type: int

    Specifies the preselector tuning DAC value during the preselector external alignment step.

    This value is valid only during a external alignment session.

    **Valid Values:**

    | Device    | Value       |
    |:----------|:------------|
    | PXIe-5605 | 0 to 16,383 |
    | PXIe-5606 | 0 to 65,535 |

    **Defined Values:** 0 to 15.5

    **Default Value**: N/A

    **Supported Devices**: PXIe-5605/5606 (external digitizer mode), PXIe-5665/5668
    '''
    absolute_delay = _attributes.AttributeViReal64(1150266)
    '''Type: float

    Specifies the sub-sample clock delay, in seconds, to apply to the acquired signal.

    Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk.
    This property can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurement to the current session.

    To set this property, the NI-RFSA device must be in the Configuration state.

    ----
    **Note**
    If this property is set, NI-TClk cannot do any sub-sample clock adjustment.

    ----

    **Units:** Seconds

    **Valid Values:** Plus or minus half of one sample clock period

    **Default Value**: 0

    **Supported Devices:** PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    acquisition_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AcquisitionType, 1150001)
    '''Type: enums.AcquisitionType

    Configures the session to either acquire I/Q data or to compute a power spectrum over the specified frequency range.

    **Defined Values:**

    %enum_table{acquisition type}

    **Default Value**: AcquisitionType.IQ

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

    **High-Level Methods**:

    - configure_acquisition_type
    '''
    active_configuration_list = _attributes.AttributeViString(1150092)
    '''Type: str

    Specifies the configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_ to make active for configuration or initiation.

    Activating a list makes all properties in the list reflect the value of the properties that correspond to the set specified by the active_configuration_list and the active_configuration_list_step properties.

    Set this property to an empty string to disable RF list mode.

    **Default Value**: "" (empty string) for devices that support RF list mode. For all other devices, the default value is N/A.

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

    **Related Topics**

    `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

    **High-Level Methods**:

    - create_configuration_list
    '''
    active_configuration_list_step = _attributes.AttributeViInt64(1150093)
    '''Type: int

    Specifies the step in the configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_ to make active for configuration or initiation.

    Activating a list makes all properties in the list reflect the value of the properties that correspond to the set specified by the active_configuration_list and the active_configuration_list_step properties.

    **Default Value**: 0 for devices that support RF list mode. For all other devices, the default value is N/A.

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

    **Related Topics**

    `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

    **High-Level Methods**:

    - create_configuration_list_step
    '''
    advance_trigger_terminal_name = _attributes.AttributeViString(1150124)
    '''Type: str

    Returns the fully qualified signal name as a string.

    **Default Values**:

    **PXIe-5830/5831/5832**:  /<i>BasebandModule</i>/<i>ai</i>/0/<i>AdvanceTrigger</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

    **PXIe-5820/5840/5841/5842**: /<i>ModuleNameai</i>/0/<i>AdvanceTrigger</i>, where *ModuleName* is the name of your device in MAX.

    **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>AdvanceTrigger</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **All other devices**: /<i>DigitizerName</i>/<i>AdvanceTrigger</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

    **High-Level Methods**:

    - get_terminal_name
    '''
    advance_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AdvanceTrigType, 1150036)
    '''Type: enums.AdvanceTrigType

    Specifies whether you want the Advance Trigger to be a digital edge or software trigger.

    ----
    **Note**
    Set this property to AdvanceTrigType.NONE if you set the acquisition_type property to AcquisitionType.SPECTRUM or if you set the **acquisitionType** parameter to AcquisitionType.SPECTRUM using the configure_acquisition_type method.

    ----

    **Defined Values:**

    %enum_table{advance trig type}

    **Default Value**: AdvanceTrigType.NONE

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    allow_more_records_than_memory = _attributes.AttributeViBoolean(1150154)
    '''Type: bool

    Specifies whether to allow the device to acquire more records than can fit in the device memory of the PXIe-5622/5624.

    ----
    **Note**
    If you set the property to FALSE and attempt to acquire more records than can fit into the PXIe-5622/5624 device memory, NI-RFSA returns an error. If this property is set to TRUE, NI-RFSA returns an error only in the event of an acquisition buffer overflow.

    ----

    ----
    **Note**
    This property is always set to True for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841.

    ----

    **Defined Values:**

    |Value         | Description                                                                       |
    |:---------|:-----------------------------------------------------------------------|
    | True  | Allows acquisition of more records than fit in device memory.          |
    | False | Does not allow acquisitions of more records than fit in device memory. |

    **Default Value**: False

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    allow_out_of_specification_user_settings = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150256)
    '''Type: enums.EnableAttrVals

    Enables or disables warnings and errors when you set frequency, power, or bandwidth values beyond the limits of the NI-RFSA device specifications.

    When you set this property to EnableAttrVals.ENABLED, the driver does not report out-of-specification warnings and errors.

    **Defined Values:**

    %enum_table{enable attr vals}

    **Default Value**: EnableAttrVals.DISABLED

    **Supported Devices:** PXIe-5820/5830/5831/5840/5841/5842/5860

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    amplitude_settling = _attributes.AttributeViReal64(1150163)
    '''Type: float

    Configures the amplitude settling accuracy in decibels.

    NI-RFSA waits until the RF power settles within the specified accuracy level after calling the initiate method.

    Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.

    **Units**: dB

    **Default Value:** 0.5

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    arm_ref_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ArmRefTrigType, 1150039)
    '''Type: enums.ArmRefTrigType

    Specifies whether you want the Arm Reference Trigger to be a digital edge or software trigger.

    ----
    **Note**
    The PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841 only support ArmRefTrigType.NONE.

    ----

    ----
    **Note**
    Set this property to ArmRefTrigType.NONE if you set the acquisition_type property to AcquisitionType.SPECTRUM or if you set the **acquisitionType** parameter to AcquisitionType.SPECTRUM using the configure_acquisition_type method.

    ----

    **Defined Values:**

    %enum_table{arm ref trig type}

    **Default Value**: ArmRefTrigType.NONE

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    assoc_aux_switch_gain_uid = _attributes.AttributeViInt32(1150356)
    attenuation = _attributes.AttributeViReal64(1150005)
    '''Type: float

    Specifies the nominal attenuation setting, in dB, for all attenuators before the first mixer in the RF signal chain.

    If you do not set this property, NI-RFSA automatically chooses an attenuation setting based on the reference level you configure. The valid values for this property depend on the device configuration.

    **PXI-5600/5661**: You can change the attenuation value to modify the amount of noise and distortion. Higher attenuation levels increase the noise level while decreasing distortion; lower attenuation levels decrease the noise level while increasing distortion.

    **PXIe-5601/5663/5663E**: You can change the attenuation value and the value of the if_attenuation property to modify the amount of noise and distortion. Higher attenuation levels increase the noise level while decreasing distortion; lower attenuation levels decrease the noise level while increasing distortion.

    **PXIe-5603/5605/5606/5665/5668**: You can set multiple properties to modify the attenuation values for the device. Refer to `PXIe-5665 RF Attenuation and Signal Levels <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/attenuation-and-signal-levels.html>`_ for more information about configuring attenuation.

    **PXIe-5667**: This property specifies the nominal attenuation setting for all attenuators before the first RF mixer in the input signal path. This property is read-only when the low_frequency_bypass_enabled property is set to NIRFSA_VAL_DISABLED.

    **PXIe-5693**: This property is read-only and returns the nominal RF attenuation of the PXIe-5693.

    **Units**: dB

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    available_paths = _attributes.AttributeViString(1150332)
    '''Type: str

    Returns a comma separated list of the configurable paths available for use based on your instrument configuration.
    '''
    available_ports = _attributes.AttributeViString(1150306)
    '''Type: str

    Returns a comma-separated list of the available ports for use based on your instrument configuration.

    **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    cache = _attributes.AttributeViBoolean(1050004)
    '''Type: bool

    Specifies whether to cache the value of properties.

    If you set this property to True, NI-RFSA tracks the current NI-RFSA device settings and avoids sending redundant commands to the device.

    NI-RFSA can always cache or never cache particular properties, regardless of the setting of this property.

    Use the init_with_options method to override the default value.

    **Defined Values:**

    |Value          | Description                      |
    |:---------|:---------------------|
    | True  | Caching is enabled.  |
    | False | Caching is disabled. |

    **Default Value**: True

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    calibration_correction_100_mhz_filter = _attributes.AttributeViReal64(1150223)
    '''Type: float

    Specifies the internal gain self-calibration correction for the 100 MHz IF filter path.

    The value you specify using this property overrides any previously-set value.

    **Units**: dB

    **Default Value**: 0

    **Supported Devices**: PXIe-5606
    '''
    calibration_correction_300_khz_filter = _attributes.AttributeViReal64(1150147)
    '''Type: float

    Specifies the internal gain self-calibration correction for the 300 kHz IF filter path.

    The value you specify using this property overrides any previously-set value.

    **Units**: dB

    **Default Value**: 0

    **Supported Devices**: PXIe-5603/5605/5606
    '''
    calibration_correction_320_mhz_filter = _attributes.AttributeViReal64(1150224)
    '''Type: float

    Specifies the internal gain self-calibration correction for the 320 MHz IF filter path.

    The value you specify using this property overrides any previously-set value.

    **Units**: dB

    **Default Value**: 0

    **Supported Devices**: PXIe-5606
    '''
    calibration_correction_5_mhz_filter = _attributes.AttributeViReal64(1150148)
    '''Type: float

    Specifies the internal gain self-calibration correction for the 5 MHz IF filter path.

    The value you specify using this property overrides any previously-set value.

    **Units**: dB

    **Default Value**: 0

    **Supported Devices**: PXIe-5603/5605/5606
    '''
    calibration_correction_765_mhz_filter = _attributes.AttributeViReal64(1150225)
    '''Type: float

    Specifies the internal gain self-calibration correction for the 765 MHz IF filter path.

    The value you specify using this property overrides any previously-set value.

    **Units**: dB

    **Default Value**: 0

    **Supported Devices**: PXIe-5606
    '''
    calibration_correction_through_filter = _attributes.AttributeViReal64(1150146)
    '''Type: float

    Specifies the internal gain self-calibration correction for the IF filter through path.

    The value you specify using this property overrides any previously-set value.

    **Units**: dB

    **Default Value**: 0

    **Supported Devices**: PXIe-5603/5605
    '''
    cal_digitizer_id = _attributes.AttributeViString(1150226)
    '''Type: str

    Returns the currently associated digitizer ID.

    Allows the use of self calibration data when configured in external digitizer mode.

    **Default Value**: "" (empty string) in external digitizer mode

    **Supported Devices**: PXIe-5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668
    '''
    cal_if_attenuation_index = _attributes.AttributeViInt32(1150109)
    '''Type: int

    Specifies the IF attenuation index from a table of valid settings.

    To select a correct attenuation table, set this property in conjunction with the cal_if_filter_selection property. This property is valid only during a calibration session.

    **Valid Values**: 0 to 25

    **Default Value**: 0

    **Supported Devices:** PXIe-5694
    '''
    cal_if_attenuation_table_selection = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.IFattenTableSel, 1150141)
    '''Type: enums.IFattenTableSel

    Specifies the IF attenuation table to be used for external calibration.

    This property is valid only in a calibration session.

    **Defined Values**:

    %enum_table{i fatten table sel}

    **Default Value**: IFattenTableSel.STANDARD

    **Supported Devices**: PXIe-5603/5605
    '''
    cal_if_attenuation_table_size = _attributes.AttributeViInt32(1150216)
    '''Type: int

    Returns the size of the selected IF attenuation table.

    **Valid Values**: 0-132

    **Default Value**: 0

    **Supported Devices**: PXIe-5606
    '''
    cal_if_filter_selection = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.IFfilterSel, 1150112)
    '''Type: enums.IFfilterSel

    Specifies the IF filter path during calibration.

    The property is valid only during a calibration session.

    **Defined Values:**

    %enum_table{i ffilter sel}

    **Default Value**: IFfilterSel._4

    **Supported Devices**: PXIe-5694
    '''
    cal_lo1_attenuation = _attributes.AttributeViReal64(1150114)
    '''Type: float

    Specifies the LO1 attenuation, in dB, during a calibration session.

    This property is valid only during a calibration session.

    **Valid Values and Default Values**:

    | Device         | Valid Values | Default Value |
    |:---------------|:-------------|:--------------|
    | PXIe-5603/5605 | 0 to 15.5    | 15.5          |
    | PXIe-5606      | 0 to 31      | 31            |

    **Supported Devices**: PXIe-5603/5605/5606
    '''
    cal_lo2_attenuation = _attributes.AttributeViReal64(1150115)
    '''Type: float

    Specifies the LO2 attenuation, in dB, during a calibration session.

    This property is valid only during a calibration session.

    **Valid Values and Default Values**:

    | Device         | Valid Values | Default Value |
    |:---------------|:-------------|:--------------|
    | PXIe-5603/5605 | 0 to 15.5    | 15.5          |
    | PXIe-5606      | 0 to 31      | 31            |

    **Supported Devices**: PXIe-5603/5605/5606
    '''
    cal_lo3_attenuation = _attributes.AttributeViReal64(1150116)
    '''Type: float

    Specifies the LO3 attenuation, in dB, during a calibration session. This property is valid only during a calibration session.

    **Valid Values and Default Values**:

    | Device         | Valid Values | Default Value |
    |:---------------|:-------------|:--------------|
    | PXIe-5603/5605 | 0 to 15.5    | 15.5          |
    | PXIe-5606      | 0 to 31      | 31            |

    **Supported Devices**: PXIe-5603/5605/5606
    '''
    cal_lo_path_selection = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoPathSel, 1150113)
    '''Type: enums.LoPathSel

    Selects the LO signal path used during calibration.

    				During noncalibration sessions, NI-RFSA implicitly derives the LO signal path from the center frequency. During calibration sessions, you must explicitly specify the LO signal path. This property is valid only during a calibration session.

    **Defined Values:**

    %enum_table{lo path sel}

    **Default Value**: LoPathSel._1

    **Supported Devices**: PXIe-5603/5605/5606
    '''
    cal_rf_electronic_attenuation_index = _attributes.AttributeViInt32(1150110)
    '''Type: int

    Selects the value of RF electronic attenuation from a table of valid configurations.

    This property is valid only during a calibration session and when you set the cal_rf_path_selection property to RfPathSel._1.

    **Default Value**: N/A

    **Supported Devices:** PXIe-5603/5605/5606
    '''
    cal_rf_lowband_signal_conditioning_path_selection = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RfLbSigCondPathSel, 1150215)
    '''Type: enums.RfLbSigCondPathSel

    Specifies the RF lowband signal conditioning path.

    **Valid Values**:

    RfLbSigCondPathSel._1

    RfLbSigCondPathSel._2

    **Default Value**: RfLbSigCondPathSel._1

    **Supported Devices**: PXIe-5606
    '''
    cal_rf_mechanical_attenuation_index = _attributes.AttributeViInt32(1150111)
    '''Type: int

    Selects the value of the RF mechanical attenuation configuration from a table of valid configurations.

    This property is valid only during a calibration session.

    **Default Values**:

    **PXIe-5603/5605**: 3

    **PXIe-5606**: 2

    **Supported Devices:** PXIe-5603/5605/5606
    '''
    cal_rf_path_selection = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RfPathSel, 1150083)
    '''Type: enums.RfPathSel

    Specifies the RF path to use during calibration.

    This property is valid only during a calibration session. When you set this property, NI-RFSA does not select the RF path based on the downconverter center frequency.

    The following table lists the RF bands used by the supported devices.

    | Device                                               | RF Band   | Frequency Range      |
    |:-----------------------------------------------------|:----------|:---------------------|
    | PXIe-5603                                            | RF band 1 | 20 Hz to 3.6 GHz     |
    | PXIe-5605 (low band signal path)                     | RF band 1 | 20 Hz to 3.6 GHz     |
    | PXIe-5605 (high band signal path)                    | RF band 2 | 3.6 GHz to 14 GHz    |
    | PXIe-5606 (low band signal path)                     | RF band 1 | 20 Hz to 3.6 GHz     |
    | PXIe-5606 (high band signal path)                    | RF band 2 | 3.6 GHz to 26.5 GHz  |
    | PXIe-5606 (low band signal path, 320 MHz IF filter)  | RF band 1 | 20 Hz to 3.41 GHz    |
    | PXIe-5606 (high band signal path, 320 MHz IF filter) | RF band 2 | 3.41 GHz to 26.5 GHz |

    **Defined and Valid Values:**

    | Value                                  | Description                 | Valid For                |
    |:---------------------------------------|:----------------------------|:-------------------------|
    | RfPathSel._1 (1700)    | Specifies to use RF band 1. | PXIe-5601/5603/5605/5606 |
    | RfPathSel._2 (1701)    | Specifies to use RF band 2. | PXIe-5601/5605/5606      |
    | RfPathSel._3 (1702)    | Specifies to use RF band 3. | PXIe-5601                |
    | RfPathSel._4 (1703)    | Specifies to use RF band 4. | PXIe-5601                |

    **Default Values**:

    **PXIe-5603/5605 (low band)/5606**: RfPathSel._1

    **PXIe-5601/5605 (high band)**: RfPathSel._2

    **Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5698
    '''
    cal_tone_power_referred_to_rf_in = _attributes.AttributeViReal64(1150174)
    '''Type: float

    Returns the power of a virtual signal connected to the RF IN connector on the PXIe-5693 front panel when the calibration tone is enabled.

    You can enable a calibration tone for the PXIe-5693 by setting the rf_conditioning_cal_tone_mode property to NIRFSA_VAL_CAL_TONE_LOWBAND_RF or NIRFSA_VAL_CAL_TONE_HIGHBAND_RF.

    **Units**: dBm

    **Default Value**: N/A

    **Supported Devices**: PXIe-5693

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    cal_tone_step_attenuation = _attributes.AttributeViReal64(1150168)
    '''Type: float

    Specifies the step attenuator to engage in the calibration tone path.

    **Units**: dB

    **Valid Values**: 2.00, 10.00

    **Default Value**: 2.00 dB

    **Supported Devices**: PXIe-5693
    '''
    center_frequency = _attributes.AttributeViReal64(1150002)
    '''Type: float

    Specifies the center frequency in a spectrum acquisition.

    The value is expressed in hertz (Hz). An acquisition consists of a span of data surrounding the center frequency.

    ----
    **Note**
    Use this property to tune the downconverter when using external digitizer mode.

    ----

    **Units**: hertz (Hz)

    **Default Values**:

    **PXIe-5694**: 193.6 MHz

    **PXIe-5820**: 0 Hz

    **PXIe-5830/5831/5832**: 6.5 GHz

    **All other devices**: 1 GHz

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    channel_coupling = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ChannelCoupling, 1150149)
    '''Type: enums.ChannelCoupling

    Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter.

    ----
    **Note**
    For the PXIe-5605/5606/5665/5667/5668, this property must be set to ChannelCoupling.AC when the DC block is present and set to ChannelCoupling.DC when the DC block is not present to ensure device specifications are met and proper calibration data is used. For more information about removing or attaching the DC block, refer to the `PXIe-5665 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/block-diagram.2.html>`_, the `PXIe-5605 Front Panel and LEDs <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/pinout.4.html>`_, the `PXIe-5667 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/block-diagram.html>`_, or the `PXIe-5668 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/block-diagram.html>`_ topics in this help file.

    ----

    **Valid Values**:

    **PXIe-5603/5665 (3.6 GHz)**: ChannelCoupling.AC, ChannelCoupling.DC

    **PXIe-5605/5665 (14 GHz)**: ChannelCoupling.AC, ChannelCoupling.DC

    **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low-frequency bypass path**: ChannelCoupling.AC, ChannelCoupling.DC

    **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**: ChannelCoupling.AC

    **PXIe-5667 (7 GHz)**: ChannelCoupling.AC

    **PXIe-5606/5668**: ChannelCoupling.AC, ChannelCoupling.DC

    **Defined Values**:

    %enum_table{channel coupling}

    **Default Value**: ChannelCoupling.AC

    **Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668
    '''
    common_mode = _attributes.AttributeViReal64(1150269)
    '''Type: float

    Specifies the common-mode level presented at each differential input terminal.

    Common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT).

    **Units**: volts

    **Default Value**: 0 V

    **Supported Devices**: PXIe-5820
    '''
    configuration_list_step_in_progress = _attributes.AttributeViInt64(1150126)
    '''Type: int

    Returns the configuration list step that is currently programmed to the hardware.

    The list is zero-indexed. You can query this property only when a list is executed.

    **PXIe-5663E/5665/5667**: This property can be read only when a configuration list is running.

    **PXIe-5644/5645/5646**: This property always returns 0 when the configuration list is not running.

    **PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters**: If a configuration list is not running, this property returns the last step of a configuration list that is programmed to the hardware. If the device was last initiated without an active configuration list, this property returns 0.

    **Default Value**: N/A

    **Supported Devices:**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

    **Related Topics**

    `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_
    '''
    contiguous_multirecord = _attributes.AttributeViInt32(1150172)
    '''Type: int

    This property is not for customer use.
    '''
    created_session_channel = _attributes.AttributeViInt32(1150333)
    data_transfer_block_size = _attributes.AttributeViInt32(1150105)
    '''Type: int

    Specifies the maximum number of samples to transfer at one time from the device to host memory.

    Increasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may increase the amount of page-locked memory required from the system.

    **Default Values**:

    **PXIe-5668**: 0x2,000,000

    **All Other Devices**: 0x400,000

    **Supported Devices:**: PXI-5661, PXIe-5663/5663E/5665/5667/5668
    '''
    data_transfer_maximum_bandwidth = _attributes.AttributeViReal64(1150104)
    '''Type: float

    Specifies the maximum bandwidth that the device can consume.

    ----
    **Note**
    The NI device limits itself to transfer fewer bytes per second on the PCI Express bus than the value you specify for this property.

    ----

    **Default Value**: N/A

    **Supported Devices:**: PXI-5661, PXIe-5663/5663E/5665
    '''
    ddc_ref_trigger_override = _attributes.AttributeViBoolean(1150164)
    '''Type: bool

    This property is not for customer use.
    '''
    decimation_delay = _attributes.AttributeViReal64(1150191)
    '''Type: float

    Specifies the sub-sample delay, in seconds, to apply to the acquired signal.

    To set this property, the NI-RFSA device must be in the Configuration state.

    **Valid Values:** -4.16 ns to +4.16 ns

    **Default Value**: 0

    **Supported Devices:** PXIe-5644/5645/5646
    '''
    deembedding_compensation_gain = _attributes.AttributeViReal64(1150325)
    '''Type: float

    Returns the de-embedding gain applied to compensate for the mismatch on the specified port. Use the Active Channel property to specify the name of the port to configure for de-embedding.

    If de-embedding is enabled, NI-RFSA uses the returned compensation gain to remove the effects of the external network between the instrument and the DUT.

    **Supported Devices**: PXIe-5830/5831/5840/5841/5842/5860
    '''
    deembedding_selected_table = _attributes.AttributeViString(1150308)
    '''Type: str

    Selects the de-embedding table to apply to the measurements on the specified port.

    To use this property, you must use the channelName parameter of the set_attribute_vi_string method to specify the name of the port to configure for de-embedding.

    If de-embedding is enabled, NI-RFSA uses the specified table to remove the effects of the external network between the instrument and the DUT.

    Use the _create_deembedding_sparameter_table_array method to create tables.

    **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860
    '''
    deembedding_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DeembeddingTypeAttrVals, 1150307)
    '''Type: enums.DeembeddingTypeAttrVals

    Specifies the type of de-embedding to apply to measurements on the specified port.

    To use this property, you must use the channelName parameter of the set_attribute_vi_int32 method to specify the name of the port to configure for de-embedding.

    If you set this property to DeembeddingTypeAttrVals.SCALAR or DeembeddingTypeAttrVals.VECTOR, NI-RFSA adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT.

    **Defined Values:**

    %enum_table{deembedding type attr vals}

    **Default Value**: DeembeddingTypeAttrVals.SCALAR

    **Valid Values for PXIe-5830/5832/5840/5841/5842/5860** : DeembeddingTypeAttrVals.SCALAR or  DeembeddingTypeAttrVals.NONE

    **Valid Values for PXIe-5831:** DeembeddingTypeAttrVals.VECTOR, DeembeddingTypeAttrVals.SCALAR, or DeembeddingTypeAttrVals.NONE. DeembeddingTypeAttrVals.VECTOR is only supported for TRX Ports in a Semiconductor Test System (STS).

    **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860
    '''
    device_configuration_temperature = _attributes.AttributeViReal64(1150159)
    '''Type: float

    Specifies the temperature, in degrees Celsius, that NI-RFSA uses to calculate the device configuration settings.

    ----
    **Note**
    For most applications, you can choose not to set this property, so NI-RFSA uses the device temperature to calculate best attenuation settings. Set this property only if you want NI-RFSA to maintain the same device configuration settings from acquisition to acquisition, independent of device temperature changes.

    ----

    **PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: This property is read-only.

    **Units**: degrees Celsius

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    device_instantaneous_bandwidth = _attributes.AttributeViReal64(1150125)
    '''Type: float

    Specifies the instantaneous bandwidth of the device in hertz (Hz).

    The instantaneous bandwidth is the effective real-time bandwidth of the signal path for your configuration.

    Specify the maximum instantaneous bandwidth needed for your measurement. NI-RFSA coerces the actual IF filter to use based on other measurement constraints such as the if_filter_bandwidth property and the digital_if_equalization_enabled property.

    To change the value that NI-RFSA uses for the maximum size of multispan acquisition subspans, use the fft_width property.

    ----
    **Note**
    If your application uses the PXIe-5622 IF digitizer, your maximum device instantaneous bandwidth is constrained to 50 MHz or 25 MHz, depending on the digitizer option you purchased. If your application uses the PXIe-5624 digitizer, your maximum device instantaneous bandwidth is constrained by the hardware option you purchased and your FPGA image.

    ----

    **PXI-5661**: The PXI-5600 RF downconverter instantaneous bandwidth is 20 MHz.

    **PXIe-5663/5663E**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the `PXIe-5601 RF Signal Downconverter Overview <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/overview.3.html>`_ for more information about instantaneous bandwidth.

    ----
    **Note**
    For the PXIe-5663/5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the instantaneous bandwidth for frequencies above 120 MHz is different than the instantaneous bandwidth for frequencies less than 120 MHz, which are 20 MHz and 10 MHz respectively.

    ----

    **PXIe-5665**: Your maximum allowed instantaneous bandwidth is independent of the downconverter center frequency. Refer to the *NI PXIe-5665 Specifications* for more information about instantaneous bandwidth.

    **PXIe-5665 (14 GHz), PXIe-5668**: If you have enabled the preselector for the PXIe-5605/5606, the device instantaneous bandwidth value is only a typical specification. For multispan acquisitions, NI-RFSA uses this typical specification as the maximum size for the acquisition subspans.

    ----
    **Note**
    When used with an external digitizer, the PXIe-5603 and the low band signal path of the PXIe-5605 provide a nominal 80 MHz bandwidth at   dB. At frequencies greater than 3.6 GHz, the PXIe-5605 provides a typical bandwidth of 47 MHz at   dB with the preselector (YIG-tuned filter) enabled.

    ----

    ----
    **Note**
    For PXIe-5606 devices, the 765 MHz IF filter is available only at center frequencies above 3.6 GHz.

    ----

    **PXIe-5693**: This property is read-only for the PXIe-5693. The value for the device instantaneous bandwidth depends on the value for the RF preselector filter.

    **PXIe-5694/PXIe-5667**: If your application uses the PXIe-5694 as part of an PXIe-5667 spectrum monitoring receiver or the PXIe-5694 as a stand-alone device, NI-RFSA determines the appropriate IF filter to use based on the value that you set for this property.

    ----
    **Note**

    ----

    **PXIe-5644/5645/5646**: This property is read-only for the PXIe-5644/5645/5646. Refer to the specifications document for your device for more information about instantaneous bandwidth.

    **PXIe-5840/5841/5860**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the *PXIe-5840/5841/5860 Specifications* for more information about instantaneous bandwidth. Set this property to select different device instantaneous bandwidths for a given downconverter center frequency. The device instantaneous bandwidth that you select is greater than or equal to the requested instantaneous bandwidth. If this property is not set, NI-RFSA uses the maximum allowed instantaneous bandwidth.

    **PXIe-5842**: Your maximum allowed instantaneous bandwidth depends on the device's hardware options, configured device personality, and the downconverter center frequency you use. Refer to the *PXIe-5842 Specifications* for more information about instantaneous bandwidth. Set this property to select different device instantaneous bandwidths for a given downconverter center frequency. The device instantaneous bandwidth that you select is greater than or equal to the requested instantaneous bandwidth. If this property is not set, NI-RFSA uses the maximum allowed instantaneous bandwidth.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-selection.html>`_

    `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-selection.html>`_

    `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-selection.html>`_
    '''
    device_temperature = _attributes.AttributeViReal64(1150051)
    '''Type: float

    Returns the current temperature, in degrees Celsius, of the module.

    **PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860**: If you query this property during RF list mode, list steps may take longer to complete during list execution.

    **PXIe-5830/5831/5832**: To use this property, you must first set the channelName parameter of the set_attribute_vi_real64 method to using the appropriate string for your instrument configuration. Setting the set_attribute_vi_real64 property is not required for the PXIe-3621/3622. Refer to the following table to determine which strings are valid for your configuration.

    | Hardware Module               |         TRX Port Type          | Active Channel String     |
    |:------------------------------|:------------------------------:|:--------------------------|
    | PXIe-3621/3622/5842           |            -                    | if or "" (empty string)   |
    | PXIe-5820                     |            -                    | fpga                      |
    | PXIe-5860                     |            -                    | 5860 or "" (empty string) |
    | First connected mmRH-5582     |     DIRECT TRX PORTS Only      | rf0                       |
    | First connected mmRH-5582     |   SWITCHED TRX PORTS [0-7]   | rf0switch0                |
    | First connected mmRH-5582     |   SWITCHED TRX PORTS [8-15]   | rf0switch1                |
    | Second connected mmRH-5582    |     DIRECT TRX PORTS Only      | rf1                       |
    | Second connected mmRH-5582    |   SWITCHED TRX PORTS [0-7]   | rf1switch0                |
    | Second connected mmRH-5582    |   SWITCHED TRX PORTS [8-15]   | rf1switch1                |
    | First connected RMM-5544/5546 |             -                   | rmm0                      |
    | Second connected RMM-5544/5546 |            -                   | rmm1                      |

    **Units**: degrees Celcius

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    digital_edge_advance_trigger_source = _attributes.AttributeViString(1150037)
    '''Type: str

    Specifies the source terminal for the Advance Trigger.

    This property is used only when the advance_trigger_type property is set to NIRFSA_VAL_DIGITAL_EDGE.

    **Defined Values:**

    %enum_table{output term}

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - configure_digital_edge_ref_trigger

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digital_edge_arm_ref_trigger_source = _attributes.AttributeViString(1150040)
    '''Type: str

    Specifies the source terminal for the digital edge Arm Reference Trigger.

    This property is used only when the arm_ref_trigger_type property is set to NIRFSA_VAL_DIGITAL_EDGE.

    **Defined Values:**

    %enum_table{output term}

    **Default Value**: "" (empty string)

    ----
    **Note**
    The PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841 devices only support "" (empty string).

    The trigger is received on PFI0 from the front panel DIO terminal.

    The trigger is received on PFI1 from the front panel DIO terminal.

    The trigger is received on PFI2 from the front panel DIO terminal.

    The trigger is received on PFI3 from the front panel DIO terminal.

    The trigger is received on PFI4 from the front panel DIO terminal.

    The trigger is received on PFI5 from the front panel DIO terminal.

    The trigger is received on PFI6 from the front panel DIO terminal.

    The trigger is received on PFI7 from the front panel DIO terminal.

    ----

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digital_edge_configuration_list_step_trigger_source = _attributes.AttributeViString(1150095)
    '''Type: str

    Configures the list trigger source.

    The default value is the Signal.END_OF_RECORD_EVENT. When the value is Signal.END_OF_RECORD_EVENT, this will signal the instrument to reconfigure from configuration N to configuration N + 1 after the End Of Record Event, and before the Ready For Advance Event. If you configure this property to any other value, the instrument reconfiguration will occur whenever the specified trigger is asserted, which may be decoupled from the acquisition state machine. Therefore, if you trigger a reconfiguration during a record acquisition, you may see transient data in the record, which should be discarded by the application. NI recommends you to use this property only in case of streaming.
    '''
    digital_edge_ref_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RefTrigDigEdgeEdge, 1150030)
    '''Type: enums.RefTrigDigEdgeEdge

    Specifies the active edge for the Reference Trigger.

    This property is used only when the ref_trigger_type property is set to NIRFSA_VAL_DIGITAL_EDGE.

    **Defined Values:**

    %enum_table{ref trig dig edge edge}

    **Default Value**: RefTrigDigEdgeEdge.RISING

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    **High-Level Methods**:

    - configure_digital_edge_ref_trigger

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digital_edge_ref_trigger_source = _attributes.AttributeViString(1150029)
    '''Type: str

    Specifies the source terminal for the digital edge Reference Trigger.

    This property is used only when the ref_trigger_type property is set to NIRFSA_VAL_DIGITAL_EDGE.

    **Defined Values:**

    %enum_table{output term}

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digital_edge_start_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.StartTrigDigEdgeEdge, 1150026)
    '''Type: enums.StartTrigDigEdgeEdge

    Specifies the active edge for the Start Trigger.

    This property is used only when the start_trigger_type property is set to NIRFSA_VAL_DIGITAL_EDGE.

    **Defined and Valid Values:**

    | Value                         | Description                                           | Valid For                           |
    |:------------------------------|:------------------------------------------------------|:------------------------------------|
    | StartTrigDigEdgeEdge.RISING (900)  | The trigger asserts on the rising edge of the signal. | PXI-5661, PXIe-5663/5663E/5665/5668 |
    | StartTrigDigEdgeEdge.FALLING (901) | The trigger asserts on the falling edge of the signal | PXIe-5668                           |

    **Default Value**: StartTrigDigEdgeEdge.RISING

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    **High-Level Methods**:

    - configure_digital_edge_start_trigger

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digital_edge_start_trigger_source = _attributes.AttributeViString(1150025)
    '''Type: str

    Specifies the source terminal for the Start Trigger.

    This property is used only when the start_trigger_type property is set to NIRFSA_VAL_DIGITAL_EDGE.

    **Defined Values**:

    %enum_table{output term}

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    **High-Level Methods**:

    - configure_digital_edge_start_trigger

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digital_gain = _attributes.AttributeViReal64(1150301)
    '''Type: float

    Specifies the scaling factor applied to the time-domain voltage data in the digitizer.

    NI-RFSA does not compensate for the specified digital gain.

    You can use this property to account for external gain changes without changing the analog signal path.

    ----
    **Note**
    The PXIe-5644/5645/5646 applies this gain when the data is scaled. The raw data does not include this scaling on these devices.

    ----

    **Units:** dB

    **Default Value:** 0 dB

    **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    digital_if_equalization_enabled = _attributes.AttributeViBoolean(1150048)
    '''Type: bool

    Enables use of the digital equalization filter for the RF downconverter.

    **PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: The only valid value for this property is True.

    ----
    **Note**
    For PXIe-5665/5667 devices, digital IF equalization is supported only with a 150 MHz clock. You cannot set this property to True if the digitizer_sample_clock_timebase_source property is set to DigitizerSampClkTimebaseSrc.LO_REF_CLK.

    ----

    ----
    **Note**
    For the PXIe-5665 (14 GHz)/5667 (7 GHz)/5668, the preselector is not part of the IF filter path, so NI-RFSA does not equalize the preselector distortions.

    ----

    **Defined Values:**

    |Value          | Description                                                          |
    |:---------|:----------------------------------------------------------|
    | True  | Enables digital IF equalization on the RF downconverter.  |
    | False | Disables digital IF equalization on the RF downconverter. |

    **Default Value**: True, if the device configuration is supported.

    **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841
    '''
    digitizer_dither_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150080)
    '''Type: enums.EnableAttrVals

    Specifies whether dithering is enabled on the digitizer.

    Dithering adds band-limited noise in the analog signal path to help reduce the quantization effects of the A/D converter and improve spectral performance. On the PXIe-5622, this out-of-band noise is added at low frequencies up to approximately 12 MHz. On the PXIe-5624, this out-of-band noise is added at low frequencies up to approximately 50 MHz.

    **PXIe-5663/5663E/5665/5667**: When you enable dithering, the maximum signal level is reduced by up to 3 dB. This signal level reduction is accounted for in the nominal input ranges of the PXIe-5622. Therefore, you can overrange the input by up to 3 dB with dither disabled. For example, the +4 dBm input range can handle signal levels up to +7 dBm with dither disabled. For wider bandwidth acquisitions, such as 40 MHz, disable dithering to eliminate residual leakage of the dither signal into the lower frequencies of the IF passband, which starts at 12.5 MHz and ends at 62.5 MHz. This leakage can slightly raise the noise floor in the lower frequencies, thus degrading the performance in high-sensitivity applications. When taking spectral measurements, this leakage can also appear as a wide, low-amplitude signal near 12.5 MHz and 62.5 MHz. The width and amplitude of the signal depends on your resolution bandwidth and the type of time-domain window you apply to your FFT.

    **PXIe-5668**: When you enable dithering, the maximum signal level is reduced by up to 2 dB. For the PXIe-5624, the maximum input power with dither off is 8 dBm and the maximum input power with dither on is 6 dBm. When acquiring an 800 MHz bandwidth signal, the I/Q data contains the dither even if the dither signal is not in the displayed spectrum. The dither can affect actions like power level triggering.

    ----
    **Note**
    For the PXIe-5668, disabling dithering can negatively affect absolute amplitude accuracy.

    ----

    **Defined Values:**

    %enum_table{enable attr vals}

    ----
    **Note**
    For the PXIe-5820/5830/5831/5832/5840/5841/5842, only EnableAttrVals.ENABLED is supported.

    ----

    **Default Value**: EnableAttrVals.ENABLED

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digitizer_sample_clock_rate = _attributes.AttributeViReal64(1150228)
    '''Type: float

    Returns the actual frequency, in hertz (Hz), of the digitizer Sample Clock.

    **Units**: hertz (Hz)

    **Supported Devices**: PXIe-5668
    '''
    digitizer_sample_clock_timebase_rate = _attributes.AttributeViReal64(1150022)
    '''Type: float

    Specifies the frequency, in hertz (Hz), of the external clock used as the timebase source if you set the digitizer_sample_clock_timebase_source property to an external source, such as NIRFSA_VAL_CLK_IN_STR, DigitizerSampClkTimebaseSrc.LO_REF_CLK, or DigitizerSampClkTimebaseSrc.DOWNCONVERTER_LO2_OUT

    **PXI-5661**If this property is set to a value less than 60 MHz, signals at frequencies just above the 20 MHz passband of the downconverter may be aliased back into the passband. This aliasing occurs because the IF frequency of the downconverter is 15 MHz, and the upper end of the passband is 25 MHz. At sampling rates below 60 MHz, the Nyquist frequency is close to the end of the passband and creates aliases that are not filtered effectively by the downconverter.

    **Units**: hertz (Hz)

    **Valid and Default Values**:

    | Device                    | Valid Values            | Default Value |
    |:--------------------------|:------------------------|:--------------|
    | PXI-5661                  | Any frequency 226552.5 MHz | 100 MHz       |
    | PXIe-5663/5663E/5665/5667 | 150 MHz                 | 150 MHz       |
    | PXIe-5668                 | 2 GHz                   | 2 GHz         |

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digitizer_sample_clock_timebase_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.DigitizerSampClkTimebaseSrc, 1150021)
    '''Type: enums.DigitizerSampClkTimebaseSrc

    Specifies the source of the Sample Clock timebase, which is the timebase used to control waveform sampling.

    **Defined Values:**

    %enum_table{digitizer samp clk timebase src}

    **Default Value**: DigitizerSampClkTimebaseSrc.ONBOARD_CLOCK

    **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digitizer_temperature = _attributes.AttributeViReal64(1150090)
    '''Type: float

    Returns the current temperature, in degrees Celsius, of the digitizer module.

    **PXIe-5820/5840/5841/5842**: If you query this property during RF list mode, list steps may take longer to complete during list execution.

    **Default Value**: N/A

    **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842
    '''
    digitizer_vertical_range = _attributes.AttributeViReal64(1150070)
    '''Type: float

    Specifies the vertical range of the digitizer.

    The vertical range is defined as the absolute value of the input range for a channel. The default vertical range works for all device configurations, but you can use this property to optimize performance if you know that the signal level at the digitizer input terminal is low.

    ----
    **Note**
    For most applications, NI-RFSA selects an appropriate value for this property.

    ----

    This value is expressed in volts. For example, to acquire a sine wave that spans between 20130.5 V and +0.5 V, set this property to 1.0.

    **PXIe-5840/5841/5842/5860**: This property is read-only.

    **Default Value**: 1.0

    **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5840/5841/5842/5860
    '''
    done_event_terminal_name = _attributes.AttributeViString(1150121)
    '''Type: str

    Returns the fully qualified signal name as a string.

    **Default Values**:

    **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>DoneEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

    **PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>DoneEvent</i>, where *ModuleName* is the name of your device in MAX.

    **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>DoneEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **All other devices**: /<i>DigitizerName</i>/<i>DoneEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - get_terminal_name
    '''
    downconverter_cal_tone_frequency = _attributes.AttributeViReal64(1150140)
    '''Type: float

    Specifies the frequency of the RF downconverter calibration tone, in hertz (Hz).

    **Valid Values**

    **PXIe-5603/5605**: 134 MHz to 13.2 GHz

    **PXIe-5606**: 34.5 MHz to 4 GHz

    **Default Value**: 612.5 MHz

    **Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668
    '''
    downconverter_cal_tone_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.CalToneMode, 1150139)
    '''Type: enums.CalToneMode

    Specifies the location in a signal path where an RF downconverter calibration tone is injected or whether the tone is disabled.

    Refer to `PXIe-5665 Theory of Operation <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/block-diagram.2.html>`_, `PXIe-5667 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/block-diagram.html>`_, or `PXIe-5668 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/block-diagram.html>`_ for more information about signal paths for your device.

    **Defined and Valid Values:**

    | Value                                          | Description                                                                                | Valid For           |
    |:-----------------------------------------------|:-------------------------------------------------------------------------------------------|:--------------------|
    |  CalToneMode.DISABLED (2700)            | Disables the calibration tone for the associated signal path.                              | PXIe-5603/5605/5606 |
    | CalToneMode.CAL_TONE_LOWBAND_RF (2701)          | Injects the calibration tone into the low band RF signal path.                             | PXIe-5603/5605/5606 |
    | CalToneMode.CAL_TONE_HIGHBAND_RF (2702)         | Injects the calibration tone into the high band RF signal path.                            | PXIe-5605/5606      |
    | CalToneMode.CAL_TONE_HIGHBAND_IF (2703)         | Injects the calibration tone into the high band IF signal path.                            | PXIe-5605           |
    | CalToneMode.CAL_TONE_LOWBAND_RF_WITHOUT_ALC (2704) | Injects the calibration tone into the low band RF signal path, bypassing the ALC.          | PXIe-5606           |
    | CalToneMode.CAL_TONE_COMB_GENERATOR (2705)      | Injects the calibration tone into the high band RF signal path through the Comb Generator. | PXIe-5606           |

    **Default Value**:  CalToneMode.DISABLED

    **Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    downconverter_center_frequency = _attributes.AttributeViReal64(1150082)
    '''Type: float

    Enables in-band retuning and specifies the current frequency, in hertz (Hz), of the RF downconverter.

    If you set this property, any measurements outside the instantaneous bandwidth of the device are invalid. To disable in-band retuning, reset the property or call the reset_device method.

    After you set this property, the downconverter is locked to that frequency until the value is changed or the property is reset. Locking the downconverter to a fixed value allows frequencies within the instantaneous bandwidth of the downconverter to be measured with minimal overhead, decreasing tuning time.

    **Valid Values**: Any supported tuning frequency of the device

    **PXIe-5820**: The only valid value for this property is 0 Hz.

    **Default Value**:

    **PXIe-5694**: The default value for the PXIe-5694 is 193.6 MHz unless you set the signal_conditioning_enabled property to  SignalConditioningEnabled.BYPASSED, in which case the default value is 187.5 MHz.

    **All other devices**: The carrier frequency or spectrum center frequency. NI-RFSA sets this property to the default value based on the value of the acquisition_type property.

    **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842
    '''
    downconverter_frequency_offset = _attributes.AttributeViReal64(1150203)
    '''Type: float

    Specifies an offset from the I/Q carrier frequency for the downconverter.

    If you set this property, any measurements outside the instantaneous bandwidth of the device are invalid. After you set this property, the RF downconverter is locked to that frequency offset until the value is changed or the property is reset.

    **Valid Values:**

    **PXIe-5646:**: -100 MHz to +100 MHz

    **PXIe-5830/5831/5832/5840/5841:**: -500 MHz to +500 MHz

    **All other devices:**: -42 MHz to +42 MHz

    **Default Values:**: For spectrum acquisition types the driver automatically calculates the default to avoid residual LO power. For I/Q acquisition types the default is 0 Hz. If the center frequency is set to a non-multiple of the lo_frequency_step_size property, the downconverter_frequency_offset property is set to compensate for the difference.

    **Supported Devices:**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-selection.html>`_

    `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-selection.html>`_

    `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-selection.html>`_
    '''
    downconverter_frequency_offset_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DownconverterFrequencyOffsetMode, 1150305)
    '''Type: enums.DownconverterFrequencyOffsetMode

    Specifies whether to allow NI-RFSA to select the downconveter frequency offset.

    You can either set an offset yourself or let NI-RFSA select one for you.

    Placing the downconverter center frequency outside the bandwidth of your input signal can help avoid issues such as LO leakage.

    To set an offset yourself, set this property to DownconverterFrequencyOffsetMode.AUTOMATIC or DownconverterFrequencyOffsetMode.USER_DEFINED, and set either the downconverter_center_frequency or the downconverter_frequency_offset properties.

    To allow NI-RFSA to automatically select the downconverter frequency offset, set this property to DownconverterFrequencyOffsetMode.AUTOMATIC or DownconverterFrequencyOffsetMode.ENABLED and configure the signal_bandwidth property to describe your expected input signal. The signal bandwidth must be no greater than half the specified value of the device_instantaneous_bandwidth property, minus a device-specific guard band. Do not set the downconverter_center_frequency or downconverter_frequency_offset properties. If all conditions are met, NI-RFSA places the downconverter center frequency outside the signal bandwidth. Set this property to DownconverterFrequencyOffsetMode.ENABLED if you want to receive an error any time NI-RFSA is unable to apply automatic offset.

    When you set an offset yourself or do not use an offset, the reference frequency for gain is near the downconverter center frequency, and downconverter_frequency_offset_mode returns DownconverterFrequencyOffsetMode.USER_DEFINED. When NI-RFSA automatically sets an offset, the reference frequency for gain is the iq_carrier_frequency, and downconverter_frequency_offset_mode returns DownconverterFrequencyOffsetMode.ENABLED. Refer to the specifications document for your device for more information about gain, flatness, and reference frequencies.

    ----
    **Note**
    Below 120 MHz, the PXIe-5841 does not use an LO and DownconverterFrequencyOffsetMode.ENABLED is unavailable. Refer to the *PXIe-5841 Automatic Frequency Offset* topic for more information about using an automatic offset with an external LO.

    ----

    **Defined Values:**

    %enum_table{downconverter frequency offset mode}

    **Default Value:** DownconverterFrequencyOffsetMode.AUTOMATIC

    **Supported Devices**: PXIe-5830/5831/5832/5841/5842

    **Related Topics**

    `PXIe-5830 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/automatic-frequency-offset.html>`_

    `PXIe-5831/5832 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/automatic-frequency-offset.html>`_

    `PXIe-5841 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/automatic-frequency-offset.html>`_

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    downconverter_gain = _attributes.AttributeViReal64(1150065)
    '''Type: float

    Returns the net signal gain for the NI-RFSA device at the current NI-RFSA settings and temperature.

    NI-RFSA scales the acquired I/Q and spectrum data from the digitizer using the value of this property.

    For a vector signal analyzer (VSA), the system is defined as the RF downconverter and all interfaces between the RF IN connector on the RF downconverter front panel and the IF IN connector on the digitizer front panel. For a spectrum monitoring receiver, the system is defined as the RF preselector, RF downconverter, and IF conditioning modules including all interfaces between the RF IN connector on the RF preselector module front panel and the IF IN connector on the digitizer front panel.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5830/5831/5832/5840/5841/5842/5860
    '''
    downconverter_loop_bandwidth = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DownconverterLoopBandwidth, 1150067)
    '''Type: enums.DownconverterLoopBandwidth

    Configures the loop bandwidth of the RF downconverter tuning PLLs.

    To set this property, the NI-RFSA device must be in the Configuration state.

    **PXI-5600/5661** : For signal bandwidths greater than 10 MHz, DownconverterLoopBandwidth.WIDE is the only value supported for this property.

    **PXIe-5601/5663/5663E** : The PXIe-5601 does not support the DownconverterLoopBandwidth.MEDIUM value. This property is not supported if you are using an external LO.

    **PXIe-5830/5831/5832/5840/5841/5842** : The PXIe-5840/5841/5842 supports only DownconverterLoopBandwidth.MEDIUM for this property. This property is not supported if you are using an external LO.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the set_attribute_vi_int32 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Defined Values:**

    %enum_table{downconverter loop bandwidth}

    **Default Values**:

    **PXI-5600** : DownconverterLoopBandwidth.WIDE

    **PXIe-5601** : DownconverterLoopBandwidth.NARROW

    **PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842** : DownconverterLoopBandwidth.MEDIUM

    **Supported Devices**: PXI-5600, PXIe-5601 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E, PXIe-5830/5831/5832/5840/5841/5842
    '''
    downconverter_preselector_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnablePreselector, 1150132)
    '''Type: enums.EnablePreselector

    Specifies whether the tunable preselector is enabled on the downconverter.

    ----
    **Note**
    All devices support setting this property to EnablePreselector.DISABLED or EnablePreselector.ENABLED_WHEN_IN_SIGNAL_PATH. Only devices with a preselector support setting this property to EnablePreselector.ENABLED.

    ----

    **Defined Values:**

    %enum_table{enable preselector}

    **Default Value**: EnablePreselector.DISABLED if the device has no preselector. EnablePreselector.ENABLED_WHEN_IN_SIGNAL_PATH if the device has a preselector.

    **Supported Devices:** PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860
    '''
    driver_setup = _attributes.AttributeViString(1050007)
    '''Type: str

    The Driver Setup string returns the initial values for properties that are specific to NI-RFSA.

    The Driver Setup string uses the following format:

    DriverSetup= <i>Tag</i>:<i>Value</i>

    *Tag* is the name of the Driver Setup string property. *Value* is the value set to the property. If multiple properties are set, their assignments are separated with a semicolon.

    This property only returns the Driver Setup string that has already been defined. Refer to `Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_ for more information about configuring the Driver Setup string. Refer to the init_with_options method for additional information about using the **option string** parameter.

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    enable_fractional_resampling = _attributes.AttributeViBoolean(1150071)
    '''Type: bool

    Specifies whether fractional resampling is enabled on the digitizer.

    Fractional resampling allows the digitizer to achieve very fine resolution on the I/Q rate value. Setting this property to False improves spectral performance.

    **PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: The only valid value for this property is True.

    **PXIe-5668**: When using a 400 MHz FPGA image, the only valid value for this property is True. When using a 800 MHz FPGA image, the only valid value for this property is False. Refer to `NI-RFSA Instrument Driver FPGA Extensions <https://www.ni.com/docs/en-US/bundle/ni-rf-vst/page/rfsa-rfsg-instrument-driver-fpga-extensions.html>`_ for more information about FPGA images.

    **Defined Values:**

    | Value         | Description                                |
    |:---------|:--------------------------------|
    | True  | Enables fractional resampling.  |
    | False | Disables fractional resampling. |

    **Default Value**: True

    **Supported Devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    end_of_record_event_terminal_name = _attributes.AttributeViString(1150120)
    '''Type: str

    Returns the fully qualified signal name as a string.

    **Default Values**:

    **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>EndOfRecordEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

    **PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>EndOfRecordEvent</i>, where *ModuleName* is the name of your device in MAX.

    **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>EndOfRecordEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **All other devices**: /<i>DigitizerName</i>/<i>EndOfRecordEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

    **High-Level Methods**:

    - get_terminal_name
    '''
    exported_advance_trigger_output_terminal = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ExportOutputTerm, 1150038)
    '''Type: enums.ExportOutputTerm

    Specifies the destination terminal for the exported Advance Trigger.

    **Defined Values:**

    %enum_table{export output term}

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - export_signal
    '''
    exported_digitizer_sample_clock_output_terminal = _attributes.AttributeEnum(_attributes.AttributeViString, enums.DigitizerSampClkExportedTerm, 1150229)
    '''Type: enums.DigitizerSampClkExportedTerm

    Specifies the terminal at which to export the Digitizer Sample Clock.

    **Valid Values**:
    %enum_table{digitizer samp clk exported term}

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5668
    '''
    exported_done_event_output_terminal = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ExportOutputTerm, 1150054)
    '''Type: enums.ExportOutputTerm

    Specifies the destination terminal for the Done Event.

    **Defined Values:**

    %enum_table{export output term}

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - export_signal
    '''
    exported_end_of_record_event_output_terminal = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ExportOutputTerm, 1150044)
    '''Type: enums.ExportOutputTerm

    Specifies the destination terminal for the End of Record Event.

    **Defined Values:**

    %enum_table{export output term}

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

    `Signal Routing <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/signal-routing.html>`_

    **High-Level Methods**:

    - export_signal
    '''
    exported_ready_for_advance_event_output_terminal = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ExportOutputTerm, 1150042)
    '''Type: enums.ExportOutputTerm

    Specifies the destination terminal for the Ready for Advance Event.

    | Value                                           | Description                                                                                                                                                                   |
    |:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | ExportOutputTerm.DO_NOT_EXPORT ("")          | The signal is not exported.                                                                                                                                        |
    | ExportOutputTerm.CLK_OUT ("ClkOut")          | The signal is exported to the CLK OUT connector on the PXIe-5622/5624 front panel.                                                                                 |
    | ExportOutputTerm.REF_OUT ("RefOut")          | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652 and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841. |
    | ExportOutputTerm.REF_OUT2 ("RefOut2")        | The signal is exported to the REF OUT2 terminal on the LO. This connector exists on only the PXIe-5652.                                                            |
    | ExportOutputTerm.PFI0 ("PFI0")               | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.                                    |
    | ExportOutputTerm.PFI1 ("PFI1")               | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.                                                                                       |
    | ExportOutputTerm.PXI_TRIG0 ("PXI_Trig0")     | The signal is exported to the PXI trigger line 0.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG1 ("PXI_Trig1")     | The signal is exported to the PXI trigger line 1.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG2 ("PXI_Trig2")     | The signal is exported to the PXI trigger line 2.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG3 ("PXI_Trig3")     | The signal is exported to the PXI trigger line 3.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG4 ("PXI_Trig4")     | The signal is exported to the PXI trigger line 4.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG5 ("PXI_Trig5")     | The signal is exported to the PXI trigger line 5.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG6 ("PXI_Trig6")     | The signal is exported to the PXI trigger line 6.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG7 ("PXI_Trig7")     | The signal is exported to the PXI trigger line 7.                                                                                                                  |
    | ExportOutputTerm.PXI_STAR ("PXI_Star")       | The signal is exported to the PXI star trigger line.                                                                                                               |
    | ExportOutputTerm.PXIE_DSTARC ("PXIe_DStarC") | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                      |
    | ExportOutputTerm.DIO_PFI0 ("DIO/PFI0")           | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI1("DIO/PFI1")           | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI2 ("DIO/PFI2")           | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI3 ("DIO/PFI3")           | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI4 ("DIO/PFI4")           | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI5 ("DIO/PFI5")           | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI6 ("DIO/PFI6")           | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI7 ("DIO/PFI7")           | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                 |

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - export_signal

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    exported_ready_for_ref_event_output_terminal = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ExportOutputTerm, 1150043)
    '''Type: enums.ExportOutputTerm

    Specifies the destination terminal for the Ready for Reference Event.

    | Value                                           | Description                                                                                                                                                                   |
    |:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | ExportOutputTerm.DO_NOT_EXPORT ("")          | The signal is not exported.                                                                                                                                        |
    | ExportOutputTerm.CLK_OUT ("ClkOut")          | The signal is exported to the CLK OUT connector on the PXIe-5622/5624 front panel.                                                                                 |
    | ExportOutputTerm.REF_OUT ("RefOut")          | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652 and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841. |
    | ExportOutputTerm.REF_OUT2 ("RefOut2")        | The signal is exported to the REF OUT2 terminal on the LO. This connector exists on only the PXIe-5652.                                                            |
    | ExportOutputTerm.PFI0 ("PFI0")               | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.                                    |
    | ExportOutputTerm.PFI1 ("PFI1")               | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.                                                                                       |
    | ExportOutputTerm.PXI_TRIG0 ("PXI_Trig0")     | The signal is exported to the PXI trigger line 0.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG1 ("PXI_Trig1")     | The signal is exported to the PXI trigger line 1.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG2 ("PXI_Trig2")     | The signal is exported to the PXI trigger line 2.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG3 ("PXI_Trig3")     | The signal is exported to the PXI trigger line 3.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG4 ("PXI_Trig4")     | The signal is exported to the PXI trigger line 4.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG5 ("PXI_Trig5")     | The signal is exported to the PXI trigger line 5.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG6 ("PXI_Trig6")     | The signal is exported to the PXI trigger line 6.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG7 ("PXI_Trig7")     | The signal is exported to the PXI trigger line 7.                                                                                                                  |
    | ExportOutputTerm.PXI_STAR ("PXI_Star")       | The signal is exported to the PXI star trigger line.                                                                                                               |
    | ExportOutputTerm.PXIE_DSTARC ("PXIe_DStarC") | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                      |
    | ExportOutputTerm.DIO_PFI0 ("DIO/PFI0")           | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI1("DIO/PFI1")           | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI2 ("DIO/PFI2")           | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI3 ("DIO/PFI3")           | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI4 ("DIO/PFI4")           | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI5 ("DIO/PFI5")           | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI6 ("DIO/PFI6")           | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI7 ("DIO/PFI7")           | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                 |

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - export_signal

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    exported_ready_for_start_event_output_terminal = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ExportOutputTerm, 1150041)
    '''Type: enums.ExportOutputTerm

    Specifies the destination terminal for the Ready for Start Event.

    | Value                                           | Description                                                                                                                                                                   |
    |:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | ExportOutputTerm.DO_NOT_EXPORT ("")          | The signal is not exported.                                                                                                                                        |
    | ExportOutputTerm.CLK_OUT ("ClkOut")          | The signal is exported to the CLK OUT connector on the PXIe-5622/5624 front panel.                                                                                 |
    | ExportOutputTerm.REF_OUT ("RefOut")          | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652 and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841. |
    | ExportOutputTerm.REF_OUT2 ("RefOut2")        | The signal is exported to the REF OUT2 terminal on the LO. This connector exists only on the PXIe-5652.                                                            |
    | ExportOutputTerm.PFI0 ("PFI0")               | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.                                    |
    | ExportOutputTerm.PFI1 ("PFI1")               | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.                                                                                       |
    | ExportOutputTerm.PXI_TRIG0 ("PXI_Trig0")     | The signal is exported to the PXI trigger line 0.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG1 ("PXI_Trig1")     | The signal is exported to the PXI trigger line 1.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG2 ("PXI_Trig2")     | The signal is exported to the PXI trigger line 2.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG3 ("PXI_Trig3")     | The signal is exported to the PXI trigger line 3.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG4 ("PXI_Trig4")     | The signal is exported to the PXI trigger line 4.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG5 ("PXI_Trig5")     | The signal is exported to the PXI trigger line 5.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG6 ("PXI_Trig6")     | The signal is exported to the PXI trigger line 6.                                                                                                                  |
    | ExportOutputTerm.PXI_TRIG7 ("PXI_Trig7")     | The signal is exported to the PXI trigger line 7.                                                                                                                  |
    | ExportOutputTerm.PXI_STAR ("PXI_Star")       | The signal is exported to the PXI star trigger line.                                                                                                               |
    | ExportOutputTerm.PXIE_DSTARC ("PXIe_DStarC") | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                      |
    | ExportOutputTerm.DIO_PFI0 ("DIO/PFI0")           | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI1("DIO/PFI1")           | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI2 ("DIO/PFI2")           | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI3 ("DIO/PFI3")           | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI4 ("DIO/PFI4")           | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI5 ("DIO/PFI5")           | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI6 ("DIO/PFI6")           | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                 |
    | ExportOutputTerm.DIO_PFI7 ("DIO/PFI7")           | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                 |

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - export_signal

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    exported_ref_clock_output_terminal = _attributes.AttributeEnum(_attributes.AttributeViString, enums.RefClkExportedTerm, 1150072)
    '''Type: enums.RefClkExportedTerm

    Specifies a comma-separated list of the terminals at which to export the Reference Clock.

    **Defined Values:**

    %enum_table{ref clk exported term}

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - export_signal
    '''
    exported_ref_clock_rate = _attributes.AttributeEnum(_attributes.AttributeViReal64, enums.ReferenceClockExportedRate, 1150326)
    '''Type: enums.ReferenceClockExportedRate

    Specifies the Reference Clock Rate, in Hz, of the signal sent to the Ref Clock Exported Terminal.

    **Default Value**: 10 MHz

    **Valid Values**:

    PXIe-5820/5830/5831/5832/5840/5841: 10 MHz

    PXIe-5842: 10 MHz, 100 MHz, 1 GHz

    PXIe-5860: 10 MHz, 100 MHz

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    exported_ref_trigger_output_terminal = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ExportOutputTerm, 1150032)
    '''Type: enums.ExportOutputTerm

    Specifies the destination terminal for the exported Reference Trigger.

    **Defined Values:**

    %enum_table{export output term}

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - export_signal
    '''
    exported_start_trigger_output_terminal = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ExportOutputTerm, 1150027)
    '''Type: enums.ExportOutputTerm

    Specifies the destination terminal for the exported Start Trigger.

    **Defined Values:**

    %enum_table{export output term}

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - export_signal
    '''
    external_gain = _attributes.AttributeViReal64(1150094)
    '''Type: float

    Specifies the gain, in dB, of a switch (or cable) connected before the RF IN connector of an NI-RFSA system.

    When you set this property, NI-RFSA calculates appropriate attenuator settings based on the value of this property and the value of the reference_level property. In this case, NI-RFSA interprets the reference level as the maximum expected power level of the signal at the input of the external gain device. For more information about attenuation, refer to the *Attenuation and Signal Levels* topic for your device in the *NI RF Vector Signal Analyzers Help*.

    ----
    **Note**
    For the PXIe-5820, this property specifies the gain, in dB, of a switch (or cable) connected before the IQ IN connector.

    ----

    ----
    **Note**
    For the PXIe-5645, this property is ignored if you are using the I/Q ports.

    ----

    With this property set, NI-RFSA reads the iq_power_edge_ref_trigger_level property value as the power level at the input of the external gain device at which the NI-RFSA device should trigger.

    Negative values indicate attenuation.

    **Valid Values**: INF to +INF

    **Units**: dB

    **Default Value**: 0

    **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    fetch_offset = _attributes.AttributeViInt64(1150046)
    '''Type: int

    Specifies the offset relative to the position specified by the fetch_relative_to property from which to start fetching data.

    Offset can be a positive or negative value.

    **Default Value**: 0

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    fetch_relative_to = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.FetchRelativeTo, 1150045)
    '''Type: enums.FetchRelativeTo

    Specifies the reference location within the acquired record from which to begin fetching.

    **Defined Values:**

    %enum_table{fetch relative to}

    **Default Value**: N/A

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    fft_size = _attributes.AttributeViInt32(1150050)
    '''Type: int

    Returns the size of the fast Fourier transform (FFT).

    **Default Value**: N/A

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    fft_width = _attributes.AttributeViReal64(1150169)
    '''Type: float

    Specifies the FFT width of the device.

    The FFT width is the effective bandwidth of the signal path during each signal acquisition.

    ----
    **Note**
    The maximum FFT width when using the PXIe-5622 is constrained to 50 MHz or 25 MHz, depending on the digitizer option you purchased. The maximum FFT width when using thing PXIe-5624 is constrained to 400 MHz or 765 MHz, depending on the digitizer configuration.

    ----

    ----
    **Note**
    You can use the fft_width property with in-band retuning. For more information about in-band retuning, refer to the downconverter_center_frequency property.

    ----

    NI-RFSA treats the *device instantaneous bandwidth* as the effective real-time bandwidth of the signal path. The *span* specifies the frequency range of the computed spectrum. An RF vector signal analyzer can acquire a bandwidth only within the device instantaneous bandwidth frequency. If the span you choose is greater than the device instantaneous bandwidth, NI-RFSA obtains multiple acquisitions and combines them into a single spectrum. By specifying the FFT width, you can control the specific bandwidth obtained in each signal acquisition. If you read the fft_width property without setting it, NI-RFSA returns the value of the device_instantaneous_bandwidth property.

    **Valid Values**:

    The lower limit for all FFT width supported devices using the PXIe-5622 IF digitizer is 7.325 kHz. The lower limit for all FFT width supported devices using the PXIe-5624 IF digitizer is 400 MHz or 800 MHz, depending on the FPGA image that is downloaded upon opening the session to the PXIe-5624 IF digitizer.

    **PXIe-5663/5663E**: The FFT width upper limit for the PXIe-5663/5663E depends on the downconverter center frequency and on the module revision of the PXIe-5601 as illustrated in the following table. Refer to the `Identifying Module Revision <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/identifying-module-revision.html>`_ topic for more information about determining which revision of the PXIe-5601 RF downconverter you have installed.

    | Downconverter Center Frequency                                                                                                                                                              | PXIe-5601 Instantaneous Bandwidth | FFT Width Upper Limit                                          |
    |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------|:---------------------------------------------------------------|
    | 10 MHz to <120 MHz                                                                                                                                                                         | 10 MHz                            | 10 MHz (Revision E), 20 MHz< sup >* < /sup> (Revision G or later) |
    | 120 MHz to <330 MHz                                                                                                                                                                        | 20 MHz                            | 20 MHz (Revision E), 30 MHz< sup > * < /sup> (Revision G or later) |
    | 330 MHz to <6.6 GHz                                                                                                                                                                        | 50 MHz                            | 50 MHz                                                         |
    | <sup > * < / sup >National Instruments does not guarantee device specifications if you set the fft_width property greater than the warranted instantaneous bandwidth specification. |                                   |                                                                |

    **PXIe-5665/5667/5668**: The upper limit of the FFT width is the maximum device instantaneous bandwidth.

    ----
    **Note**

    ----

    ----
    **Note**
    At frequencies greater than 3.6 GHz, the PXIe-5605 provides a typical bandwidth of 47 MHz at   dB with the preselector enabled. The fft_width property can override the typical bandwidth of the PXIe-5605 up to 57 MHz using an external digitizer and up to 50 MHz or 25 MHz depending on the PXIe-5622 digitizer option you purchased. The increase in bandwidth results in faster signal acquisitions, but amplitude accuracy is decreased for spectrum acquisitions, and magnitude and phase accuracy is decreased for I/Q acquisitions. National Instruments does not guarantee device specifications if you set the fft_width property greater than the warranted instantaneous bandwidth specification.

    ----

    ----
    **Note**
    When using the PXIe-5606, the 765 MHz IF filter is only available at center frequencies of 3.6 GHz and above.

    ----

    **Default Value**: N/A

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668
    '''
    fft_window_shape_factor = _attributes.AttributeViReal64(1150206)
    '''Type: float

    Returns the shape factor of the window used in the fast Fourier transform (FFT).

    The window shape factor is defined as the ratio of the 60 dB to 6 dB bandwidths.

    The following table shows the shape factor for each NI-RFSA FFT window type.

    | Window Type            | Shape Factor |
    |:-----------------------|:-------------|
    | Uniform                | 1.57:1       |
    | Hanning                | 1.94:1       |
    | Hamming                | 2.13:1       |
    | Exact Blackman         | 2.52:1       |
    | Flat Top               | 2.0:1        |
    | 4-term Blackman-Harris | 2.5:1        |
    | 7-term Blackman-Harris | 4.1:1        |
    | Low Side Lobe          | 2.78:1       |
    | Gaussian               | 2.3:1        |
    | Kaiser Bessel          | 2.55:1       |

    **Default Value**: N/A

    **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860
    '''
    fft_window_size = _attributes.AttributeViInt32(1150049)
    '''Type: int

    Returns the size of the window used in the fast Fourier transform (FFT), in terms of the number of samples in the window.

    **Default Value**: N/A

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    fft_window_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SpectrumFfTwindowType, 1150017)
    '''Type: enums.SpectrumFfTwindowType

    Specifies the time-domain window type.

    **Defined Values:**

    %enum_table{spectrum ff twindow type}

    **Default Values**:

    **PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: SpectrumFfTwindowType._7_TERM_BLACKMAN_HARRIS

    **PXIe-5667**: SpectrumFfTwindowType._4_TERM_BLACKMAN_HARRIS

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Resolution Bandwidth <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/resolution-bandwidth.html>`_
    '''
    fixed_group_delay_across_ports = _attributes.AttributeViString(1150324)
    '''Type: str

    Specifies a comma-separated list of ports for which to fix the group delay.

    **Valid Values**:

    PXIe-5831/5832: rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel.

    **Default Value**:

    PXIe-5831/5832: (empty string), which specifies that the group delay will not be fixed for any port.

    **Supported Devices**: PXIe-5831/5832
    '''
    fpga_bitfile_path = _attributes.AttributeViString(1150221)
    '''Type: str

    Returns a string containing the path to the location of the current NI-RFSA instrument driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device.

    You can specify the bitfile location using the Driver Setup string in the **optionString** parameter of the init_with_options method.

    NI-RFSA instrument driver FPGA extensions enable you to use pre-compiled FPGA bitfiles to customize the behavior of the device FPGA while maintaining the functionality of the NI-RFSA instrument driver.

    Refer to `NI-RFSA Instrument Driver FPGA Extensions <https://www.ni.com/docs/en-US/bundle/ni-rf-vst/page/rfsa-rfsg-instrument-driver-fpga-extensions.html>`_ for more information about using NI-RFSA instrument driver FPGA extensions for NI devices.

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    fpga_target_name = _attributes.AttributeViString(1150233)
    '''Type: str

    Returns a string containing the name of the FPGA target being used.

    This name can be used with the RIO open session to open a reference to the FPGA.

    This property is channel dependent if multiple targets are supported.

    **Supported Devices:** PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    fpga_temperature = _attributes.AttributeViReal64(1150254)
    '''Type: float

    Returns the current temperature, in degrees Celsius, of the FPGA.

    ----
    **Note**
    If you query this property during RF list mode, list steps may take longer to complete during list execution.

    ----

    **Units**: degrees Celcius

    **Default Value**: N/A

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    frequency_settling = _attributes.AttributeViReal64(1150088)
    '''Type: float

    Specifies the value used for local oscillator (LO) frequency settling.

    The units and interpretation for this scalar value are specified using the frequency_settling_units property. This property is not supported if you are using an external LO.

    The valid values for this property depend on the frequency_settling_units property.

    | Device | FrequencySettlingUnits.SECONDS_AFTER_LOCK | FrequencySettlingUnits.SECONDS_AFTER_IO | %enum_value{frequency settling units.fsu
    ppm} |
    |:-------|:----------------------------------|:--------------------------------|:------------------|
    | PXIe-5663/5663E | 2 microseconds<sup>1</sup> to 80 milliseconds, resolution of approximately 2 microseconds | 0 microseconds to 80 milliseconds<sup>2</sup>, resolution of 1 microsecond | 1.0, 0.1, 0.01 |
    | PXIe-5665/5667/5668 | 4 microseconds to 80 milliseconds, resolution of approximately 4 microseconds | 0 microseconds to 80 milliseconds<sup>2</sup>, resolution of 1 microsecond | 1.0, 0.1, 0.01, 0.001 |
    | PXIe-5644/5645/5646 | 1 microsecond<sup>1</sup> to 65 milliseconds, resolution of 1 microsecond | 1 microsecond<sup>1</sup> to 65 milliseconds, resolution of 1 microsecond | 1.0, 0.1, 0.01 |
    | PXIe-5830/5831/5832/5840/5841/5842 | 1 microsecond<sup>1</sup> to 10 seconds, resolution of 1 microsecond | 0 microseconds to 10 seconds, resolution of 1 microsecond | 1.0 to 0.01 |
    | PXIe-5831/5832 with PXIe-5653 (using PXIe-3622 LO)<sup>3</sup> | 1 microsecond<sup>1</sup> to 10 seconds, resolution of 1 microsecond | 0 microseconds to 10 seconds, resolution of 1 microsecond | 1.0 to 0.01 |
    | PXIe-5831/5832 with PXIe-5653 (using PXIe-5653 LO)<sup>3</sup> | 4 microseconds to 80 milliseconds, resolution of approximately 4 microseconds | 0 microseconds to 80 milliseconds, resolution of 1 microsecond | 1.0 to 0.01 |

    **Notes:**
    1. If the frequency settling units property is set to FrequencySettlingUnits.SECONDS_AFTER_LOCK and the downconverter loop bandwidth property is set to narrow, NI recommends a minimum settling time of 128 microseconds to ensure that the phase-locked loop (PLL) lock stabilizes. If the downconverter loop bandwidth is set to wide, NI recommends a minimum settling time of 16 microseconds.
    2. When in RF list mode, the valid values for FrequencySettlingUnits.SECONDS_AFTER_IO are 0 microseconds to 50 milliseconds.
    3. The valid values for this configuration depend on the module used as the LO source. Refer to the lo source property for more information.

    **Default Value**: 0.1

    **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842
    '''
    frequency_settling_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.FrequencySettlingUnits, 1150087)
    '''Type: enums.FrequencySettlingUnits

    Specifies the delay duration units and interpretation for LO settling.

    Specify the actual settling value using the frequency_settling property. This property is not supported if you are using an external LO.

    **Defined Values:**

    %enum_table{frequency settling units}

    **Default Value**: FrequencySettlingUnits.PPM

    **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842
    '''
    host_dma_buffer_size = _attributes.AttributeViInt64(1150285)
    '''Type: int

    Specifies the size of the DMA buffer in computer memory, in bytes.

    To set this property, the NI-RFSA device must be in the Configuration state.

    A sufficiently large host DMA buffer improves performance by allowing large fetches to be transferred more efficiently.

    **Default Value:** 8 MB

    **Supported Devices**: PXI-5820/5830/5831/5840/5841/5842/5860
    '''
    if1_atten_value = _attributes.AttributeViReal64(1150078)
    '''Type: float

    Specifies the IF1 attenuation, in dB. The device IF1 attenuator is set to this nominal value.

    Use this property, along with the if2_atten_value property, when you set the if_filter property to IFfilter.BYPASS.

    **Valid Values**: 0 to 15

    **Units**: dB

    **Default Value**: N/A

    **Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E
    '''
    if2_atten_value = _attributes.AttributeViReal64(1150079)
    '''Type: float

    Specifies the IF2 attenuation, in dB. The device IF2 attenuator is set to this nominal value.

    Use this property, along with the if1_atten_value property, when you set the if_filter property to IFfilter.BYPASS.

    **Valid Values**: 0 to 15

    **Units**: dB

    **Default Value**: N/A

    **Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E
    '''
    if_attenuation = _attributes.AttributeViReal64(1150074)
    '''Type: float

    Configures the device attenuation to a value that has the actual calibrated IF attenuation closest to the desired value.

    **Valid Values**: 0 to 30

    **Default Value**: N/A

    **Supported Devices**: PXIe-5601/5603/5605 (external digitizer mode), PXIe-5663/5663E/5665/5667, PXIe-5693
    '''
    if_conditioning_down_conversion_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150161)
    '''Type: enums.EnableAttrVals

    Specifies whether downconversion to 21.4 MHz is enabled for the IF conditioning module.

    The IF output frequency is 21.4 MHz when you enable this property, and it is 193.6 MHz when you disable this property.

    ----
    **Note**
    If you set the signal_conditioning_enabled property to SignalConditioningEnabled.BYPASSED, you cannot set the if_conditioning_down_conversion_enabled property to EnableAttrVals.ENABLED.

    ----

    ----
    **Note**
    For the PXI-5661, PXIe-5663/5663E/5665, the only valid value for this property is EnableAttrVals.DISABLED.

    ----

    **Defined Values:**

    %enum_table{enable attr vals}

    **Default Values**: EnableAttrVals.DISABLED

    **Supported Devices**: PXIe-5667, PXIe-5694

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    if_conditioning_temperature = _attributes.AttributeViReal64(1150210)
    '''Type: float

    Returns the current temperature, in degrees Celsius, of the IF conditioning module associated with the NI-RFSA device.

    **Default Value**: N/A

    **Supported Devices**: PXIe-5667
    '''
    if_filter = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.IFfilter, 1150075)
    '''Type: enums.IFfilter

    Specifies the desired IF filter path, regardless of the RF band chosen by NI-RFSA.

    **Defined Values:**

    %enum_table{i ffilter}

    **Default Value**: N/A

    **Supported Devices**: PXIe-5601
    '''
    if_filter_bandwidth = _attributes.AttributeViReal64(1150205)
    '''Type: float

    Specifies the IF filter path bandwidth for your device configuration.

    ----
    **Note**
    For composite devices, such as the PXIe-5665/5667/5668, the IF filter path bandwidth includes all IF filters across the component modules of a composite device.

    ----

    NI-RFSA uses this property in conjunction with the device_instantaneous_bandwidth property and the digital_if_equalization_enabled property to determine the settings for your measurement. NI-RFSA selects the next highest available filter based on the value you specify. The following table lists the IF filters available for NI devices. You may specify a higher value than your device instantaneous bandwidth if your measurement requires it, but specifying a lower value returns an error.

    | Device                   | IF Filter Bandwidth Range | IF Filter         |
    |:-------------------------|:--------------------------|:------------------|
    | PXIe-5603/5665 (3.6 GHz) | 2264300 kHz                  | 300 kHz IF filter |
    | PXIe-5603/5665 (3.6 GHz) | >300 kHz and 22645 MHz      | Through IF filter |
    | PXIe-5603/5665 (3.6 GHz) | >5 MHz                   | Through IF filter |
    | PXIe-5605/5665 (14 GHz)  | 2264300 kHz                  | 300 kHz IF filter |
    | PXIe-5603/5665 (14 GHz)  | >300 kHz and 22645 MHz      | 5 MHz IF filter   |
    | PXIe-5603/5665 (14 GHz)  | >5 MHz                   | Through IF filter |
    | PXIe-5668                | 2264300 kHz                  | 300 kHz IF filter |
    | PXIe-5668                | >300 kHz and 22645 MHz      | 5 MHz IF filter   |
    | PXIe-5668                | >5 MHz and 2264100 MHz      | 100 MHz IF filter |
    | PXIe-5668                | >100 MHz and 2264320 MHz    | 320 MHz IF filter |
    | PXIe-5668                | >320 MHz                 | 765 MHz IF filter |

    **Valid Values**:

    **PXIe-5603/5605**: 0 to 80 MHz

    **PXIe-5665/5667**: 0 to 50 MHz

    **PXIe-5668**: 0 to 765 MHz

    **PXIe-5694**: 0 to 50 MHz

    ----
    **Note**
    To set this property to values greater than 20 MHz, you must set the signal_conditioning_enabled property to SignalConditioningEnabled.BYPASSED

    ----

    **Default Values:** For spectrum acquisition types the default is greater than or equal to the spectrum_span property. NI-RFSA chooses the default value of the if_filter_bandwidth property to correspond to the appropriate IF filter. For I/Q acquisition types NI-RFSA chooses the default value corresponding to the widest IF filter possible for your equipment setup.

    **Supported Devices**: PXIe-5603/5605/5606, PXIe-5665/5667/5668, PXIe-5694
    '''
    if_output_frequency = _attributes.AttributeViReal64(1150086)
    '''Type: float

    Returns the center frequency of the IF output signal that corresponds to the configured RF center frequency.

    The downconverter translates the RF input frequency to the IF output frequency by mixing it with the LO signal. The nominal values for the IF output frequency are shown in the following table.

    | Downconverter | Nominal IF Output Frequency |
    |:--------------|:---------------------------|
    | PXI-5600 | 15 MHz |
    | PXIe-5601 | 53 MHz or 187.5 MHz |
    | PXIe-5603 | 187.5 MHz or 199 MHz |
    | PXIe-5605 | 187.5 MHz, 190 MHz, or 199 MHz |
    | PXIe-5606 | 187.5 MHz, 190 MHz, 199 MHz, 507.5 MHz, or 730 MHz |
    | PXIe-5694 | - signal_conditioning_enabled set to SIGNAL_CONDITIONING_ENABLED and if_conditioning_down_conversion_enabled set to disabled: 193.6 MHz<br>- if_conditioning_down_conversion_enabled set to enabled: 21.4 MHz<br>- signal_conditioning_enabled set to SIGNAL_CONDITIONING_BYPASSED: 162.5 MHz to 212.5 MHz |

    The coarse nature of the LO settings can cause the downconverter to be unable to tune to the exact LO frequency that would produce the nominal IF output frequency. Any coercion in the actual LO frequency results in the IF output frequency being slightly off from the nominal value.

    Additionally, if you use the downconverter_center_frequency and lo_frequency properties to program the downconverter, the IF output frequency could vary from the nominal value. NI-RFSA adjusts the acquired spectrum or I/Q data for the difference between nominal and actual IF output frequency. If you use an external digitizer with a RF downconverter, use this property to specify the actual IF output frequency.

    **Default Value**: N/A

    **Supported Devices**:PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694
    '''
    if_output_power_level = _attributes.AttributeViReal64(1150130)
    '''Type: float

    Specifies the level of the IF signal leaving the system, in dBm.

    Use this property to increase or decrease the nominal IF signal output level to achieve better measurement results.

    If you set the if_output_power_level and if_output_power_level_offset properties at the same time, NI-RFSA returns an error.

    ----
    **Note**
    If you set the if_output_power_level property to a value less than 201310 dBm, the IF output power level may be higher than the value you request. Read the value of this property to determine the configured IF output power level.

    ----

    ----
    **Note**
    The value of this property is limited by the amount of IF attenuation that the downconverter can apply, the reference_level property, the downconverter_center_frequency property, and the center_frequency property or iq_carrier_frequency property, depending on your acquisition type.

    ----

    **Units**: dBm

    **Default Value**:

    **PXIe-5667**: -2 dBm

    **PXIe-5668**: -1 dBm

    **All other devices**:   dBm

    **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694
    '''
    if_output_power_level_offset = _attributes.AttributeViReal64(1150131)
    '''Type: float

    Specifies the number of dB by which to adjust the default IF output power level.

    This property does not depend on absolute IF output power levels, so you can use it to adjust the IF output power level on all NI-RFSA devices without knowing the exact default value. Use this property to increase or decrease the nominal output level to achieve better measurement results. The default value for the offset is 0 dB.

    If you set the if_output_power_level and if_output_power_level_offset properties at the same time, NI-RFSA returns an error.

    **Units**: dB

    **Default Value**: 0

    **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668
    '''
    input_isolation_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150170)
    '''Type: enums.EnableAttrVals

    Specifies whether input isolation is enabled.

    Enabling this property isolates the input signal at the RF IN connector on the RF downconverter from the rest of the RF downconverter signal path. Disabling this property reintegrates the input signal into the RF downconverter signal path.

    ----
    **Note**
    If you enable input isolation for your device, the device impedance is changed from the characteristic 50  impedance. A change in the device impedance may also cause a VSWR value higher than the device specifications.

    ----

    For the PXIe-5830/5831/5832, input isolation is supported for all available ports for your hardware configuration.

    **Defined Values:**

    %enum_table{enable attr vals}

    **Default Value**: EnableAttrVals.DISABLED, if the device configuration is supported.

    **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5693, PXIe-5820/5830/5831/5832/5840/5841

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    input_port = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.InputPort, 1150180)
    '''Type: enums.InputPort

    Specifies the connector(s) to use to acquire the signal.

    To set this property, the NI-RFSA device must be in the Configuration state.

    **Defined Values:**

    %enum_table{input port}

    **Default Values**:

    **PXIe-5820**: InputPort.IQ_IN

    **All other devices**: InputPort.RF_IN

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    Returns a string that contains the firmware revision information for the NI-RFSA downconverter for the composite device you are currently using.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    ----
    **Note**
    PXIe-5820/5830/5831/5832/5840/5841/5842/5860 devices will return "No revision information available." To retrieve the firmware revision, use MAX, Hardware Configuration Utility, or NI System Configuration API.

    ----
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    Returns a string that contains the name of the manufacturer for the NI-RFSA device you are currently using.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    Returns a string that contains the model number or name of the NI-RFSA device that you are currently using.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    interchange_check = _attributes.AttributeViBoolean(1050021)
    '''Type: bool

    Specifies whether to perform interchangeability checking and retrieve interchangeability warnings.

    ----
    **Note**
    Interchangeability check is unsupported.

    ----

    **Defined Values:**

    | Value         | Description                                                                           |
    |:---------|:---------------------------------------------------------------------------|
    | True  | NI-RFSA performs interchangeability-checking and retrieves warnings.       |
    | False | NI-RFSA does not perform interchangeability-checking or retrieve warnings. |

    **Default Value**: False

    **Supported Devices**: None
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    Indicates the resource name NI-RFSA uses to identify the physical device.

    If you initialize NI-RFSA with a logical name, this property contains the resource name that corresponds to the entry in the IVI Configuration Utility.

    If you initialize NI-RFSA with the resource name, this property contains that value.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    iq_analog_edge_ref_trigger_hysteresis = _attributes.AttributeViReal64(1150195)
    '''Type: float

    Specifies the size of the hysteresis window on either side of the trigger level.

    The device triggers when the signal passes through the threshold you specify with the iq_analog_edge_ref_trigger_level property, has the slope you specify with the iq_analog_edge_ref_trigger_slope property, and passes through the hysteresis window that you specify with this property. This property affects the device operation only when the ref_trigger_type property is set to RefTrigType.IQ_ANALOG_EDGE.

    **Valid Values:** 0 to (Voltage Range/2 + Trigger Level) for Rising Slope. 0 to (Voltage Range/2 -Trigger Level) for Falling Slope. These values limit the hysteresis to the entire voltage range that is below the trigger level for Rising Slope or that is above the trigger level for Falling Slope.

    **Default Value:** The default is calculated by the driver as (Range x 0.025).

    **Supported Devices:** PXIe-5644/5645R
    '''
    iq_analog_edge_ref_trigger_level = _attributes.AttributeViReal64(1150194)
    '''Type: float

    Specifies the analog level, in volts, at which the device triggers.

    The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property affects the device operation only when the ref_trigger_type property is set to RefTrigType.IQ_ANALOG_EDGE.

    **Default Value:** 0 V

    **Supported Devices:** PXIe-5644/5645
    '''
    iq_analog_edge_ref_trigger_slope = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RefTrigIqPwrEdgeSlope, 1150193)
    '''Type: enums.RefTrigIqPwrEdgeSlope

    Specifies whether the device asserts the trigger when the voltage level is rising or falling.

    When you set the ref_trigger_type property to RefTrigType.IQ_ANALOG_EDGE, the device asserts the trigger when the signal level exceeds the specified level with the slope you specify. This property affects the device operation only when the ref_trigger_type property is set to RefTrigType.IQ_ANALOG_EDGE.

    **Defined Values:**

    %enum_table{ref trig iq pwr edge slope}

    **Default Value**: RefTrigIqPwrEdgeSlope.RISING

    **Supported Devices:** PXIe-5644/5645
    '''
    iq_analog_edge_ref_trigger_source = _attributes.AttributeViString(1150192)
    '''Type: str

    Specifies the channel from which the device monitors the trigger.

    Use a value of "I" to monitor the I channel. Use a value of "Q" to monitor the Q channel. Use a value of "I,Q" to monitor both I and Q channels. This property affects the device operation only when the ref_trigger_type property is set to RefTrigType.IQ_ANALOG_EDGE.

    **Valid Values:** "I", "Q", "I,Q", "Q,I"

    **Default Value:** "I"

    **Supported Devices:** PXIe-5644/5645
    '''
    iq_carrier_frequency = _attributes.AttributeViReal64(1150059)
    '''Type: float

    Specifies the expected carrier frequency of the incoming signal for demodulation.

    The NI-RFSA device tunes to this frequency. NI-RFSA may coerce this value based on hardware settings and the RF downconverter specifications.

    ----
    **Note**
    For the PXIe-5645, this property is ignored if you are using the I/Q ports.

    ----

    **Units**: hertz (Hz)

    **Default Values**:

    **PXIe-5644/5645/5646, PXIe-5840/5841/5860, PXIe-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options)**: 1 GHz

    **PXIe-5842 (4 GHz bandwidth option) using the Standard personality**: 1 GHz

    **PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality**: 6.5 GHz

    **PXIe-5820**: 0 Hz

    **PXIe-5830/5831/5832**: 6.5 GHz

    **All other devices**: 100 MHz

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Carrier Wave <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/fund-carrierwave.html>`_

    `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

    **High-Level Methods**:

    - configure_iq_carrier_frequency
    '''
    iq_in_port_carrier_frequency = _attributes.AttributeViReal64(1150181)
    '''Type: float

    Configures the frequency of the signal.

    The onboard signal processing (OSP) frequency shifts the signal at this frequency to baseband prior to acquiring it.

    ----
    **Note**
    For the PXIe-5645, this property is ignored if you are using the RF ports.

    ----

    **Valid Values**:

    **PXIe-5645**: -60 MHz to +60 MHz

    **PXIe-5820**: -500 MHz to +500 MHz

    **Default Value**: 0

    **Supported Devices**: PXIe-5645, PXIe-5820
    '''
    iq_in_port_temperature = _attributes.AttributeViReal64(1150204)
    '''Type: float

    Returns the temperature of the I/Q IN circuitry on the device.

    **Units:** degrees C

    **Supported Devices:** PXIe-5645, PXIe-5820
    '''
    iq_in_port_terminal_configuration = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.IqInPortTermCfg, 1150182)
    '''Type: enums.IqInPortTermCfg

    Configures the terminal configuration of the I/Q port.

    To use this property, you must use the channelName parameter of the set_attribute_vi_int32 method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

    ----
    **Note**
    For the PXIe-5645, this property is ignored if you are using the RF ports.

    ----

    **PXIe-5820**: The only valid value for this property is IqInPortTermCfg.DIFFERENTIAL.

    **Defined Values:**

    %enum_table{iq in port term cfg}

    **Default Value**: IqInPortTermCfg.DIFFERENTIAL

    **Supported Devices:** PXIe-5645, PXIe-5820
    '''
    iq_in_port_vertical_range = _attributes.AttributeViReal64(1150183)
    '''Type: float

    Specifies the voltage range for the I/Q terminals.

    To use this property, you must use the channelName parameter of the set_attribute_vi_real64 method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

    The voltage range in differential terminal configuration is configurable from 2 V<sub>pk-pk</sub> to 0.032 V<sub>pk-pk</sub> in 1 dB steps. In single-ended terminal configuration, valid ranges are half those for differential. Values are always coerced up to the next valid range.

    ----
    **Note**
    For the PXIe-5645, this property is ignored if you are using the RF ports.

    ----

    **Valid Values:**

    **PXIe-5645**: 0 V<sub>pk-pk</sub> to 2 V<sub>pk-pk</sub> for differential terminal configuration, 0 V<sub>pk-pk</sub> to 1 V<sub>pk-pk</sub> for single-ended terminal configuration.

    **PXIe-5820**: 0 V<sub>pk-pk</sub> to 4 V<sub>pk-pk</sub> for differential terminal configuration.

    **Default Value**: 2 V<sub>pk-pk</sub>

    **Supported Devices:** PXIe-5645, PXIe-5820
    '''
    iq_power_edge_ref_trigger_level = _attributes.AttributeViReal64(1150056)
    '''Type: float

    Specifies the power level, in dBm, at which the device triggers.

    The device asserts the trigger when the signal crosses the level specified by the value of this property, taking into consideration the specified slope. If you are using external gain, refer to the external_gain property for more information about how this property affects the I/Q power edge trigger level.

    **Default Value**: 0

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    **High-Level Methods**:

    - configure_iq_power_edge_ref_trigger
    '''
    iq_power_edge_ref_trigger_slope = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RefTrigIqPwrEdgeSlope, 1150057)
    '''Type: enums.RefTrigIqPwrEdgeSlope

    Specifies whether the device asserts the trigger when the signal power is rising or falling.

    When you set the ref_trigger_type property to RefTrigType.IQ_POWER_EDGE, the device asserts the trigger when the signal power exceeds the specified level with the slope you specify.

    **Defined Values:**

    %enum_table{ref trig iq pwr edge slope}

    **Default Value**: RefTrigIqPwrEdgeSlope.RISING

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    **High-Level Methods**:

    - configure_iq_power_edge_ref_trigger
    '''
    iq_power_edge_ref_trigger_source = _attributes.AttributeViString(1150055)
    '''Type: str

    Specifies the channel from which the device monitors the trigger.

    NI-RFSA currently supports only 0 as the value of this property.

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    **High-Level Methods**:

    - configure_iq_power_edge_ref_trigger
    '''
    iq_rate = _attributes.AttributeViReal64(1150007)
    '''Type: float

    Specifies the I/Q rate for the acquisition.

    The value is expressed in samples per second (S/s).

    Refer to the device_instantaneous_bandwidth property for more information about device specific instantaneous bandwidth limits. You can also refer to the *NI PXIe-5665 Specifications* for more information about instantaneous bandwidth device specifications.

    ----
    **Note**
    For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. At I/Q rates above 50 MS/s, the dither noise can affect phase coherency performance and leak into the lower frequencies and the upper frequencies of the IF passband. Refer to the digitizer_dither_enabled property for more information about dithering.

    For the PXIe-5663/5663E/5665/5667, when you set the digitizer_sample_clock_timebase_source property to NIRFSA_VAL_ONBOARD_CLOCK_STR, the downconverter instantaneous bandwidth is greater than or equal to the coerced I/Q rate times 0.8. For the PXIe-5665, the actual signal bandwidth is further limited by the combination of the chosen IF filter and anti-aliasing filter.

    ----

    **PXI-5661**: You should not need to configure an I/Q rate higher than 25 megasamples per second (MS/s) because the PXI-5600 RF downconverter bandwidth is 20 MHz. If you configure a higher I/Q rate, you may see aliasing effects at negative frequencies because the IF frequency of the PXI-5600 is 15 MHz.

    **PXIe-5663/5663E**: Your maximum allowed instantaneous bandwidth depends on the I/Q carrier frequency you use. Refer to the `PXIe-5601 RF downconverter overview <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/overview.3.html>`_ for more information about instantaneous bandwidth.

    **PXIe-5665**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency if you have enabled the preselector (YIG-tuned filter).

    **PXIe-5667**: Your maximum allowed instantaneous bandwidth depends on the selected [RF preselector filter](rf_preselector_filter.html) and whether the preselector on the [RF downconverter](PRESELECTOR_ENABLED.html) is enabled.

    **PXIe-5668**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use and whether or not you enable the highpass filter or preselector (YIG-tuned filter).

    **Units**: S/s

    **Default Values:**

    **PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality**: 5 GS/s only.

    **All Other Devices**: 1 MS/s

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

    **High-Level Methods**:

    - configure_iq_rate

    Note:
    One or more of the referenced properties are not in the Python API for this driver.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    lo2_export_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150235)
    '''Type: enums.EnableAttrVals

    Specifies whether to enable the LO2 OUT terminal on the installed devices.

    Set this property to TRUE to export the 4 GHz LO signal from the device LO2 IN terminal to the LO2 OUT terminal.

    You can also export the LO2 signal by setting the lo_export_enabled property and the digitizer_sample_clock_timebase_source property.

    **Defined Values:**

    |          |                                |
    |:---------|:-------------------------------|
    | True  | Enables the LO2 OUT terminal.  |
    | False | Disables the LO2 OUT terminal. |

    **Default Value:** False

    **Supported Devices:** PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5668
    '''
    load_configurations_from_file_reset_options = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoadConfigurationResetOptions, 1150337)
    '''Type: enums.LoadConfigurationResetOptions

    Specifies the configurations to skip to reset while loading configurations from a file.

    **Default Value:**  NIRFSA_VAL_SKIP_NONE
    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +--------------------------------------------------+--------------------------------------------------+
    | Value                                            | Description                                      |
    +==================================================+==================================================+
    | LoadConfigurationResetOptions.NONE               | NI-RFSA resets all configurations.               |
    +--------------------------------------------------+--------------------------------------------------+
    | LoadConfigurationResetOptions.DEEMBEDDING_TABLES | NI-RFSA skips resetting the de-embedding tables. |
    +--------------------------------------------------+--------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    Contains the logical name you specified when opening the current IVI session.

    You may pass a logical name to the init method or the init_with_options method. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a driver session section in the IVI Configuration file. The driver session section specifies a physical device and initial user options.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    low_frequency_bypass_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150207)
    '''Type: enums.EnableAttrVals

    Specifies whether to use the low-frequency bypass path for the incoming RF signal.

    |                            |                                         |
    |:---------------------------|:----------------------------------------|
    | EnableAttrVals.DISABLED (1900) | Disables the low-frequency bypass path. |
    | EnableAttrVals.ENABLED (1901)  | Enables the low-frequency bypass path.  |

    **Default Value**: EnableAttrVals.DISABLED

    **Supported Devices**: PXIe-5693, PXIe-5667

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    lo_export_enabled = _attributes.AttributeViBoolean(1150134)
    '''Type: bool

    Specifies whether to enable the LO OUT terminals on the installed devices.

    **PXIe-5601**: The only valid value for this property is True.

    **PXIe-5603/5605/5606**: If you want to daisy-chain multiple devices together using the same LO source, set this property to TRUE to export the LO input signals on the LO1 IN, LO2 IN, and LO3 IN terminals to LO1 OUT, LO2 OUT, and LO3 OUT, respectively.

    **PXIe-5694**: You can enable this property only if you set the lo_source property to LoSourceVals.LO_IN, or if you set the lo_source property to LoSourceVals.ONBOARD and the if_conditioning_down_conversion_enabled property to NIRFSA_VAL_ENABLED.

    **PXIe-5830/5831**: To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the set_attribute_vi_boolean method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

    ----
    **Note**
    If you are sharing an LO for the PXIe-5830/5831/5832 between an NI-RFSA and NI-RFSG session, ensure both sessions use the same shared setting.

    ----

    **Defined Values:**

    | Value         |  Description                              |
    |:---------|:-------------------------------|
    | True  | Enables the LO OUT terminals.  |
    | False | Disables the LO OUT terminals. |

    **Default Values**:

    **PXIe-5601, PXIe-5663/5663E**: True

    **PXIe-5603/5605/5606, PXIe-5644/5645/5646, PXIe-5665/5667/5668, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842**: False

    **Supported Devices**: PXIe-5601/5603/5605 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    lo_frequency = _attributes.AttributeViReal64(1150068)
    '''Type: float

    Specifies the LO signal frequency for the configured center frequency.

    If you are using the NI RF vector signal analyzer with an external LO, use this property to specify the LO frequency that the external LO source passes into the LO IN or LO1 IN connector on the RF downconverter front panel. If you are using an external LO, reading the value of this property after configuring the rest of the parameters returns the LO frequency needed by the device.

    Set this property to the actual LO frequency because NI-RFSA corrects for any difference between expected and actual LO frequencies.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the set_attribute_vi_real64 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Default Values**:

    **PXIe-5694**: 215 MHz

    **All other devices**: 0

    **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `PXIe-5830 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-configuration.html>`_

    `PXIe-5831/5832 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-configuration.html>`_

    `PXIe-5841 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-configuration.html>`_
    '''
    lo_frequency_step_size = _attributes.AttributeViReal64(1150188)
    '''Type: float

    Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL).

    You can only tune the LO frequency by multiples of the lo_frequency_step_size property. For the PXIe-5644/5645/5646 and PXIe-5840/5841, the LO frequency can therefore be offset from the requested center frequency by as much as half of the lo_frequency_step_size property. This offset is corrected by digitally frequency shifting the lo_frequency property to the value requested in either the iq_carrier_frequency property or the center_frequency property.

    ----
    **Note**
    For the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653, this property is ignored if the PXIe-5653 is used as the LO source.

    ----

    The valid values for this property depend on the lo_pll_fractional_mode_enabled property.

    **PXIe-5644/5645/5646**: If the lo_pll_fractional_mode_enabled property is set to NIRFSA_VAL_DISABLED, the specified value is coerced to the closest valid value.

    **PXIe-5840/5841/5842**: If the lo_pll_fractional_mode_enabled property is set to NIRFSA_VAL_DISABLED, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.

    | lo_pll_fractional_mode_enabled | PXIe-5644/5645 | PXIe-5646 | PXIe-5840/5841 | PXIe-5830/5831/5832 | PXIe-5841 w/PXIe-5655 |
    |-------------------------------|-----------------|------------|----------------|---------------------|-----------------------------------|
    | NIRFSA_VAL_ENABLED | 50 kHz to 24 MHz | 50 kHz to 25 MHz | 50 kHz to 100 MHz | LO1: 8 Hz to 400 MHz<br>LO2: 4 kHz to 400 MHz | 1 nHz to 50 MHz |
    | NIRFSA_VAL_DISABLED | 4 MHz, 5 MHz, 6 MHz, 12 MHz, 24 MHz | 2 MHz, 5 MHz, 10 MHz, 25 MHz | 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, 100 MHz | LO1: --<br>LO2: -- | 1 nHz to 50 MHz |

    \* Values up to 100 MHz are coerced to 50 MHz.

    ----
    **Note**
    The default value for the PXIe-5831 depends on the frequency range of the selected port for your instrument configuration. Refer to the `Instrument Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/instrument-configurations.html>`_ topic for more information about available ports for your hardware configuration.

    ----

    **Default Values:**

    **PXIe-5644/5645/5646:** 200 kHz

    **PXIe-5830:** 2 MHz

    **PXIe-5831/5832 (RF port):** 8 MHz

    **PXIe-5831/5832 (IF port):** 2 MHz, 4 MHz

    **PXIe-5840/5841:**

    - Fractional mode: 500 kHz
    - Integer mode: 10 MHz for frequencies less than or equal to 4 GHz. 20 MHz for frequencies greater than 4 GHz.

    **PXIe-5841 with PXIe-5655:** 500 kHz

    **PXIe-5842:** 1 Hz

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    lo_injection_side = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoInjection, 1150069)
    '''Type: enums.LoInjection

    Specifies the LO injection side.

    **PXIe-5601/5663/5663E**: For frequencies below 517.5 MHz or above 6.4125 GHz, the LO injection side is fixed and NI-RFSA returns an error if you specify the incorrect value. If you do not configure this property, NI-RFSA selects the default LO injection side based on the downconverter center frequency. Reset this property to return to automatic behavior.

    **PXIe-5603/5605/5665 (3.6 GHz)/5667 (3.6 GHz)**: Setting this property to LoInjection.LOW is not supported for this device.

    **PXIe-5605/5665 (14 GHz)/5667 (7 GHz)**: Setting this property to LoInjection.LOW is supported for this device for frequencies greater than 4 GHz, but this configuration is not calibrated, and device specifications are not guaranteed.

    **PXIe-5606/5668**: Setting this property to LoInjection.LOW is supported for certain frequencies in high band, varying by final IF frequency. This configuration is not calibrated and device specifications are not guaranteed.

    **Defined Values:**

    %enum_table{lo injection}

    **Default Values**:

    **PXIe-5601 (external digitizer mode), PXIe-5663/5663E (frequencies < 3.0 GHz)**: LoInjection.HIGH

    **PXIe-5601 (external digitizer mode), PXIe-5663/5663E (frequencies  3.0 GHz)**: LoInjection.LOW

    **PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668**: LoInjection.HIGH

    **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668
    '''
    lo_in_power = _attributes.AttributeViReal64(1150186)
    '''Type: float

    Returns the power level, in dBm, expected at the LO IN terminal when the lo_source property is set to LoSourceVals.LO_IN.

    ----
    **Note**
    For the PXIe-5644/5645/5646, this property is always read-only.

    ----

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842
    '''
    lo_out_export_configure_from_rfsg = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150299)
    '''Type: enums.EnableAttrVals

    Specifies whether to allow NI-RFSG to control the NI-RFSA LO out export.

    Set this property to EnableAttrVals.ENABLED to allow NI-RFSG to control the LO out export. Use the NIRFSG ATTR RF IN LO EXPORT ENABLED property to control the NI-RFSA LO out export from NI-RFSG.

    **Defined Values:**

    %enum_table{enable attr vals}

    **Default Value:** EnableAttrVals.DISABLED

    **Supported Devices**: PXIe-5840/5841/5842

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    lo_out_power = _attributes.AttributeViReal64(1150246)
    '''Type: float

    Specifies the power level, in dBm, of the signal at the LO OUT terminal when the lo_export_enabled property is set to True.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the set_attribute_vi_real64 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Units:** dBm

    **Supported Devices:** PXIe-5830/5831/5832/5840/5841/5842
    '''
    lo_pll_fractional_mode_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150187)
    '''Type: enums.EnableAttrVals

    Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL).

    Fractional mode gives a finer frequency step resolution, but it may result in non harmonic spurs. Refer to the device specifications for your device for more information about fractional mode and non harmonic spurs.

    ----
    **Note**
    The lo_pll_fractional_mode_enabled property is applicable only when using the internal LO.

    ----

    ----
    **Note**
    For the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653, this property is ignored if the PXIe-5653 is used as the LO source. For the PXIe-5841 with PXIe-5655, this property is ignored if the PXIe-5655 is used as the LO source.

    ----

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the set_attribute_vi_int32 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Defined Values:**

    %enum_table{enable attr vals}

    **Default Value**: EnableAttrVals.ENABLED

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    lo_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.LoSourceVals, 1150162)
    '''Type: enums.LoSourceVals

    Specifies the LO signal source used to downconvert the RF input signal.

                    If no signal downconversion is required, this property is ignored. If this property is set to "" (empty string), NI-RFSA uses the internal LO source.

                    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the set_attribute_vi_string method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

                    ----
                    **Note**
                    For the PXIe-5841 with PXIe-5655, RF list mode is not supported when this property is set to LoSourceVals.LO_SOURCE_SG_SA_SHARED.

                    ----

                    **Defined Values:**
                    %enum_table{lo source vals}

                    **Default Value**: LoSourceVals.ONBOARD ("Onboard")

                    **Supported Devices**: PXIe-5644/5645/5646, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842

                    **Related Topics**
                    `PXIe-5830 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/lo-sharing-using-rfsa-rfsg.html>`_
                    `PXIe-5831/5832 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/lo-sharing-using-rfsa-rfsg.html>`_
    '''
    lo_temperature = _attributes.AttributeViReal64(1150089)
    '''Type: float

    Returns the current temperature, in degrees Celsius, of the LO module.

    **PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode) PXI-5661, PXIe-5663/5663E/5665/5667/5668** This property is not supported if you are using an external LO.

    **PXIe-5840/5841/5842**: If you query this property during RF list mode, list steps may take longer to complete during list execution.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode) PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5840/5841/5842
    '''
    lo_vco_frequency_step_size = _attributes.AttributeViReal64(1150312)
    '''Type: float

    Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal.

    ----
    **Note**
    Do not set this property with the lo_frequency_step_size property.

    ----

    **Valid Values**:

    LO1: 1 Hz to 50 MHz

    LO2: 1 Hz to 100 MHz

    **Default Values**: 1 MHz

    **Supported Devices**: PXIe-5830/5831/5832
    '''
    lo_yig_main_coil_drive = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoYigMainCoilDrive, 1150135)
    '''Type: enums.LoYigMainCoilDrive

    Adjusts the dynamics of the current driving the YIG main coil.

    ----
    **Note**
    Setting this property to LoYigMainCoilDrive.FAST allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise. This property is not supported if you are using an external LO.

    ----

    **Defined Values:**

    %enum_table{lo yig main coil drive}

    **Default Value**: LoYigMainCoilDrive.NORMAL

    **Supported Devices:** PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668
    '''
    max_device_instantaneous_bandwidth = _attributes.AttributeViReal64(1150236)
    '''Type: float

    Returns the maximum instantaneous bandwidth of the device.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    max_fundamental_silo_frequency = _attributes.AttributeViReal64(1150335)
    max_iq_rate = _attributes.AttributeViReal64(1150237)
    '''Type: float

    Returns the maximum I/Q rate.

    **Default Value**: N/A

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    mechanical_attenuation = _attributes.AttributeViReal64(1150128)
    '''Type: float

    Specifies the level of mechanical attenuation for the RF path, in dB.

    **PXIe-5667**: This property is read-only when the low_frequency_bypass_enabled property is set to NIRFSA_VAL_DISABLED.

    **PXIe-5668with PXIe-5698**: This property is read-only when the rf_preamp_enabled property is set to EnableRfPreamp.ENABLED.

    **Units**: dB

    **Valid Values:**

    **PXIe-5601/5663/5663E**: 0, 16

    **PXIe-5603/5665 (3.6 GHz)**: 0, 10, 20, 30

    **PXIe-5605/5665 (14 GHz), PXIe-5606/5668**: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75

    **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 0, 10, 20, 30

    **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**: 0

    **PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75

    **PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector filter path**: 0

    **PXIe-5668 with PXIe-5698 with the** rf_preamp_enabled property set to EnableRfPreamp.ENABLED: 5

    **Default Value**: N/A

    **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    mechanical_attenuator_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150081)
    '''Type: enums.EnableAttrVals

    Specifies whether the mechanical attenuator is enabled.

    Set this property to EnableAttrVals.ENABLED to allow NI-RFSA to use the mechanical attenuator.

    Disabling this attenuator can improve device performance. Refer to `PXIe-5663/5663E Programming Attenuation <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/programming-attenuation.html>`_ for more information about the attenuators.

    **Defined Values:**

    %enum_table{enable attr vals}

    **Default Value**: EnableAttrVals.ENABLED

    **Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    memory_size = _attributes.AttributeViInt64(1150085)
    '''Type: int

    Returns the digitizer onboard memory size, in bytes.

    **Default Value**: N/A

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    minimum_acpr = _attributes.AttributeViReal64(1150142)
    '''Type: float

    Specifies the minimum adjacent channel power ratio (ACPR), in dB, relative to the main channel reference level.

    This property configures NI-RFSA to optimize downconverter gain to measure a lower-power adjacent channel, adding gain only after filtering the main channel. The gain NI-RFSA applies is always less than or equal to the ACPR value you specify.

    ----
    **Note**
    For the PXIe-5665 (3.6 GHz), this property is supported only if you set the device_instantaneous_bandwidth, spectrum_span, or if_filter_bandwidth property to a value less than 300 kHz. For the PXIe-5665 (14 GHz), this property is supported for device_instantaneous_bandwidth, spectrum_span, or if_filter_bandwidth property values less than 300 kHz by using the 300 kHz IF filter, and it is supported for values between 300 kHz and 5 MHz by using the 5 MHz IF filter.

    ----

    ----
    **Note**
    NI-RFSA coerces this property to zero for the PXI-5600, PXIe-5601 and the PXIe-5667. For all other devices, read the coerced value of this property to determine the actual amount of gain applied.

    ----

    ----
    **Note**
    For the PXIe-5668, this property alters the if_output_power_level property. This property will not affect the reference_level property.

    ----

    **Default Value**: 0

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668
    '''
    minimum_reconfig_time = _attributes.AttributeViReal64(1150165)
    '''Type: float

    This property is not for customer use.
    '''
    min_fundamental_silo_frequency = _attributes.AttributeViReal64(1150334)
    mixer_level = _attributes.AttributeViReal64(1150006)
    '''Type: float

    Specifies the mixer level, in dBm.

    The mixer level represents the attenuation value to apply to the input RF signal as it reaches the first mixer in the signal chain. If you do not set this property, NI-RFSA automatically selects an optimal mixer level value based on the reference level. The valid values for this property depend on your device configuration.

    If you set the mixer_level and mixer_level_offset properties at the same time, NI-RFSA returns an error.

    **PXIe-5601/5663/5663E**: This property is read-only.

    **PXIe-5667**: This property is read-only when the low_frequency_bypass_enabled property is set to NIRFSA_VAL_DISABLED.

    **Units**: dBm

    **Default Values**:

    **PXI-5600/5661**: -30

    **PXIe-5603/5605/5665/5667/5668**: -10

    **All other devices**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    mixer_level_offset = _attributes.AttributeViReal64(1150127)
    '''Type: float

    Specifies the number of dB by which to adjust the device mixer level.

    The default value is 0, which specifies device settings that are the best compromise between distortion and noise. Specifying a positive value for this property configures the device for moderate distortion and low noise, and specifying a negative value results in low distortion and higher noise.

    You cannot set the mixer_level and mixer_level_offset properties at the same time.

    **PXIe-5667**: This property is read-only when the low_frequency_bypass_enabled property is set to NIRFSA_VAL_DISABLED.

    **Units**: dB

    **Default Value**: 0

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    module_power_consumption = _attributes.AttributeViReal64(1150255)
    '''Type: float

    Returns the module power consumption.

    ----
    **Note**
    If you query this property during RF list mode, list steps may take longer to complete during list execution.

    ----

    **Units**: watts

    **Default Value**: N/A

    **Supported Devices:**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    module_revision = _attributes.AttributeViString(1150091)
    '''Type: str

    Returns the revision of the RF downconverter module.

    ----
    **Note**
    For the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5840/5841, this property returns the revision of the VST module. For the PXIe-5830/5831/5832, this property returns the revision of the PXIe-3621/3622

    ----

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    noise_source_power_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150222)
    '''Type: enums.EnableAttrVals

    Enables the 28 V DC source on the device front panel.

    **PXIe-5668 with PXIe-5698**: When this property is set to EnableAttrVals.ENABLED, the PXIe-5698 noise source is used instead of the PXIe-5668 noise source.

    **Units**: dB

    **Default Value**: EnableAttrVals.DISABLED

    **Supported Devices**: PXIe-5606, PXIe-5668, PXIe-5698

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    notch_filter_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.NotchFilterEnabled, 1150167)
    '''Type: enums.NotchFilterEnabled

    Specifies whether the notch filter is enabled on the RF conditioning module.

    ----
    **Note**
    The PXI-5661 and PXIe-5663/5663E/5665 only support setting this property to NotchFilterEnabled.DISABLED.

    ----

    **Defined Values**:

    %enum_table{notch filter enabled}

    **Default Value**: NotchFilterEnabled.DISABLED

    **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5693
    '''
    number_of_records = _attributes.AttributeViInt64(1150011)
    '''Type: int

    Specifies the number of records to acquire if the number_of_records_is_finite property is set to True.

    **Default Value**: 1

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

    **High-Level Methods**:

    - configure_number_of_records
    '''
    number_of_records_is_finite = _attributes.AttributeViBoolean(1150010)
    '''Type: bool

    Specifies whether the device stops after acquiring the specified number of records or acquires records continuously.

    **Defined Values:**

    |Value          | Description                                                              |
    |:---------|:--------------------------------------------------------------|
    | True  | Acquire a finite number of records.                           |
    | False | Acquire records continuously until you abort the acquisition. |

    **Default Value**: True

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

    **High-Level Methods**:

    - configure_number_of_records
    '''
    number_of_samples = _attributes.AttributeViInt64(1150009)
    '''Type: int

    Specifies the number of samples to acquire.

    This property is valid only if the number_of_samples_is_finite property is set to True.

    **Default Value**: 1,000

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

    **High-Level Methods**:

    - configure_number_of_samples
    '''
    number_of_samples_is_finite = _attributes.AttributeViBoolean(1150008)
    '''Type: bool

    Specifies whether the device acquires a finite number of samples or acquires continuously.

    **Defined Values:**

    | Value         |  Description                                                     |
    |:---------|:------------------------------------------------------|
    | True  | Acquire a finite number of samples.                   |
    | False | Acquire continuously until you abort the acquisition. |

    **Default Value**: True

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

    **High-Level Methods**:

    - configure_number_of_samples
    '''
    number_of_spectral_lines = _attributes.AttributeViInt32(1150018)
    '''Type: int

    Specifies the number of spectral lines expected with the current power spectrum configuration.

    If you do not configure this property, NI-RFSA selects an appropriate value based on the resolution_bandwidth property. If you configure this property, NI-RFSA coerces the resolution_bandwidth value based on the number of spectral lines requested and the value of the spectrum_span property.

    **Default Value**: N/A

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    osp_data_scaling_factor = _attributes.AttributeViReal64(1150151)
    '''Type: float

    Specifies the scaling factor applied to the time-domain voltage data in the IF digitizer.

    Use this property to maximize the dynamic range of the digitizer by increasing the maximum IF power the digitizer can measure without creating OSP overflows.

    Because of the device amplitude response, some wide-band signals normally attenuated by the downconverter go through the IF digitizer without causing an ADC overflow. During IF equalization, these wide-band digitizer input signals may become amplified. These amplified input signal values overflow the available numeric range used in the signal processing algorithm.

    You can use this property when OSP calculations would generate an overflow while applying digital filters to the data. The OSP module in the digitizer multiplies the time-domain signal amplitude, in volts, by the specified property value before further onboard processing. Set this property to a value less than 1 to avoid OSP overflow for near full-scale IF signals and to use the maximum dynamic range of the digitizer. NI-RFSA compensates for the specified OSP data scaling factor to ensure that the correct scaled data, in absolute levels, is always returned regardless of the value of this property.

    **Valid Values:**: 0.25 to 1.0

    **Default Values:**

    **PXI-5661, PXIe-5663/5663E/5665 (3.6 GHz)/5667 (3.6 GHz)/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: 1.0

    **PXIe-5665 (14 GHz)/5667 (7 GHz)**: 0.8

    **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    overflow_error_reporting = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OverflowErrorReporting, 1150271)
    '''Type: enums.OverflowErrorReporting

    Configures error reporting for ADC and onboard signal processing overflows.

    Overflows lead to clipping of the waveform.

    **Defined Values:**

    %enum_table{overflow error reporting}

    **Default Value**: OverflowErrorReporting.WARNING

    **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    p2p_enabled = _attributes.AttributeViBoolean(1150097)
    '''Type: bool

    Specifies whether peer-to-peer streaming is enabled for the active stream endpoint.

    This property is `endpoint based <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/configuring-peer-to-peer-endpoint-ni-rfsa.html>`_.

    **Defined Values:**

    | Value                | Description                    |
    |:----------------|:--------------------|
    | True (1900)  | Enables streaming.  |
    | False (1901) | Disables streaming. |

    **Default Value**: False

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842
    '''
    p2p_endpoint_overflow = _attributes.AttributeViBoolean(1150103)
    '''Type: bool

    Indicates whether the endpoint has overflowed.

    An overflow condition occurs when data is written to the endpoint faster than it can be streamed from it. During an overflow, data in the endpoint begins to be overwritten. Reset the device or close the session to reset the overflow condition.

    **Defined Values:**

    | Value         | Description                                               |
    |:---------|:-----------------------------------------------|
    | True  | The endpoint has overflowed.                   |
    | False | You can write additional data to the endpoint. |

    **Default Value**: False

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842
    '''
    p2p_endpoint_size = _attributes.AttributeViInt64(1150102)
    '''Type: int

    Returns the size, in samples, of the peer-to-peer endpoint.

    **Default Value**: 0

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842
    '''
    p2p_fifo_endpoint_count = _attributes.AttributeViInt64(1150098)
    '''Type: int

    Returns the number of peer-to-peer streams supported by the device.

    **Default Value**: 0

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842
    '''
    p2p_most_samples_available_in_endpoint = _attributes.AttributeViInt64(1150101)
    '''Type: int

    Returns the largest number of complex samples available in the peer-to-peer endpoint since this property was last read.

    **Default Value**: 0

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842
    '''
    p2p_onboard_memory_enabled = _attributes.AttributeViBoolean(1150107)
    '''Type: bool

    Specifies whether a limit is placed on the number of records and the size of the records by the size of the device onboard memory.

    When a peer-to-peer stream is enabled and onboard memory is disabled, any fetch calls result in an error.

    **Default Value**: False

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842
    '''
    p2p_samples_available_in_endpoint = _attributes.AttributeViInt64(1150100)
    '''Type: int

    Returns the current number of complex samples available in the peer-to-peer endpoint.

    ----
    **Note**
    The complex samples are composed of two 16-bit words with the I data as the LSB.

    ----

    **Default Value**: 0

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842
    '''
    p2p_samples_transferred = _attributes.AttributeViInt64(1150099)
    '''Type: int

    Returns the number of complex samples transferred through the peer-to-peer stream endpoint since the endpoint was last reset.

    **Default Value**: 0

    **Supported Devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842
    '''
    phase_offset = _attributes.AttributeViReal64(1150106)
    '''Type: float

    Specifies the offset to apply to the initial I and Q phases.

    **Valid Values**: 0 to 180

    **Default Value**: 0

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842
    '''
    power_spectrum_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SpectrumUnits, 1150012)
    '''Type: enums.SpectrumUnits

    Specifies the units of the power spectrum.

    **Defined Values:**

    %enum_table{spectrum units}

    **Default Value**: SpectrumUnits.DBM

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    preselector_present = _attributes.AttributeViBoolean(1150136)
    '''Type: bool

    Returns whether a preselector is available on the RF downconverter module.

    **Defined Values:**

    | Value         | Description                                                  |
    |:---------|:--------------------------------------------------|
    | True  | A preselector is available on the downconverter.  |
    | False | No preselector is available on the downconverter. |

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842
    '''
    pxi_chassis_clk10_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.PxiChassisClk10Src, 1150023)
    '''Type: enums.PxiChassisClk10Src

    Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane.

    This option can be configured only when the PXI-5600 is installed in Slot 2 of the PXI chassis.

    **Defined Values:**

    %enum_table{pxi chassis clk10 src}

    **Default Value**: N/A

    **Supported Devices**: PXI-5600 (external digitizer mode), PXI-5661

    **Related Topics**

    [System Reference Clock](nirfsa.chm/system-reference-clock.html)

    **High-Level Methods**:

    - configure_pxi_chassis_clk10
    '''
    query_instrument_status = _attributes.AttributeViBoolean(1050003)
    '''Type: bool

    Specifies whether NI-RFSA queries the NI-RFSA device status after each operation.

    Querying the device status is useful for debugging. After you validate your program, you can set this property to False to disable status checking and maximize performance.

    NI-RFSA can choose to ignore status checking for particular properties regardless of the setting of this property.

    ----
    **Note**
    Use the init_with_options method to override this value.

    ----

    **Defined Values:**

    | Value         | Description                                                               |
    |:---------|:---------------------------------------------------------------|
    | True  | NI-RFSA queries the device status after each operation.        |
    | False | NI-RFSA does not query the device status after each operation. |

    **Default Value**: False

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    range_check = _attributes.AttributeViBoolean(1050002)
    '''Type: bool

    Specifies whether to validate property values and method parameters.

    If enabled, NI-RFSA validates the parameter values that you pass to NI-RFSA methods. Range checking parameters is very useful for debugging. After you validate your program, you can set this property to False to disable range checking and maximize performance.

    ----
    **Note**
    Use the init_with_options method to override this value.

    ----

    **Defined Values:**

    | Value         | Description                                                                    |
    |:---------|:--------------------------------------------------------------------|
    | True  | NI-RFSA validates property values and method parameters.         |
    | False | NI-RFSA does not validate property values and method parameters. |

    **Default Value**: True

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    ready_for_advance_event_terminal_name = _attributes.AttributeViString(1150118)
    '''Type: str

    Returns the fully qualified signal name as a string.

    **Default Values**:

    **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>ReadyForAdvanceEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

    **PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>ReadyForAdvanceEvent</i>, where *ModuleName* is the name of your device in MAX.

    **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>ReadyForAdvanceEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **All other devices**: /<i>DigitizerName</i>ReadyForAdvanceEvent, where *DigitizerName* is the name associated with your digitizer module in MAX.

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

    **High-Level Methods**:

    - get_terminal_name
    '''
    ready_for_ref_event_terminal_name = _attributes.AttributeViString(1150119)
    '''Type: str

    Returns the fully qualified signal name as a string.

    **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>ReadyForReferenceEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

    **PXIe-5820/5840/5841/5842**: /<i>ModuleName/<i>ai/0/<i>ReadyForReferenceEvent</i>, where *ModuleName* is the name of your device in MAX.

    **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>ReadyForReferenceEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **All other devices**: /<i>DigitizerName</i>/<i>ReadyForReferenceEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

    **High-Level Methods**:

    - get_terminal_name
    '''
    ready_for_start_event_terminal_name = _attributes.AttributeViString(1150117)
    '''Type: str

    Returns the fully qualified signal name as a string.

    **Default Values**:

    **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>ReadyForStartEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

    **PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>ReadyForStartEvent</i>, where *ModuleName* is the name of your device in MAX.

    **PXIe-5860**: /<i>ModuleName/<i>ai</i>/<i>ChannelNumber</i>/<i>ReadyForStartEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **All other devices**: /<i>DigitizerName</i>/<i>ReadyForStartEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

    **High-Level Methods**:

    - get_terminal_name
    '''
    records_done = _attributes.AttributeViInt64(1150047)
    '''Type: int

    Returns the number of records the RF vector signal analyzer has acquired.

    **Default Value**: N/A

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    record_coercions = _attributes.AttributeViBoolean(1050006)
    '''Type: bool

    Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties.

    ----
    **Note**
    This property is currently not supported.

    ----

    **Defined Values:**

    | Value         | Description                                                            |
    |:---------|:------------------------------------------------------------|
    | True  | The IVI engine keeps a list of the value coercions.         |
    | False | The IVI engine does not keep a list of the value coercions. |

    **Default Value**: False

    **Supported Devices**: None
    '''
    reference_level = _attributes.AttributeViReal64(1150004)
    '''Type: float

    Specifies the reference level, in dBm.

    The reference level represents the maximum expected power of an RF input signal.

    ----
    **Note**
    For the PXIe-5645, this property is ignored if you are using the I/Q ports.

    ----

    Refer to the external_gain property for more information about how configuring an external gain and a reference level affect attenuation.

    **Default Value**: 0

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Improving Your Measurements <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/measurement_guidelines.html>`_

    `Programming Attenuation-Related Properties and Properties Using NI-RFSA <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/programming-attenuation.html>`_

    **High-Level Methods**:

    - configure_reference_level
    '''
    reference_level_headroom = _attributes.AttributeViReal64(1150309)
    '''Type: float

    Specifies the margin NI-RFSA adds to the reference_level property.

    The margin helps to avoid clipping and overflow warnings if the input signal exceeds the configured reference level.

    NI-RFSA configures the input gain to avoid clipping and associated overflow warnings as long as the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or have already included margin in the reference level, you may be able to improve the signal-to-noise ratio by reducing the reference level headroom.

    **Units**: dB

    **Default Value**:

    **PXIe-5830/5831/5832/5841/5842/5860**: 1 dB

    **PXIe-5840**: 0 dB

    **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860
    '''
    ref_clock_rate = _attributes.AttributeViReal64(1150020)
    '''Type: float

    Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector.

    This property is only valid when the ref_clock_source property is set to NIRFSA_VAL_CLK_IN_STR,NIRFSA_VAL_REF_IN_STR , or RefClockSrc.REF_IN_2.

    **Valid Values**:

    **PXIe-5644/5645/5646, PXIe-5601/5663/5663E, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841**: 10 MHz

    **PXIe-5603/5605/5665/5667/5668**: 5 MHz to 100 MHz, in increments of 1 MHz

    **PXIe-5841 with PXIe-5655, PXIe-5842**: 10 MHz, 100 MHz, 270 MHz, and 3.84 MHz  *y*, where *y* is 4, 8, 16, 24, 25, or 32.

    **PXIe-5860**: 10 MHz, 100 MHz

    **Default Value**: 10 MHz

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - configure_ref_clock

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    ref_clock_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.RefClockSrc, 1150019)
    '''Type: enums.RefClockSrc

    Specifies the Reference Clock source.

    ----
    **Note**
    For the PXIe-5694, if your application requires an external LO source, set this property to RefClockSrc.NONE.

    ----

    **Defined Values:**

    %enum_table{ref clock src}

    **Default Values**:

    **PXIe-5694**: RefClockSrc.REF_IN

    **All other devices**: RefClockSrc.ONBOARD_CLOCK

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - configure_ref_clock

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    ref_to_ref_trigger_holdoff = _attributes.AttributeViReal64(1150034)
    '''Type: float

    Specifies the minimum time, in seconds, that must elapse between Reference Triggers of two records.

    The device does not recognize the Reference Trigger of the next record before this minimum time elapses.

    **Units:**: seconds

    **Default Value**: 0

    **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    ref_trigger_delay = _attributes.AttributeViReal64(1150060)
    '''Type: float

    Specifies the trigger delay time, in seconds.

    The trigger delay time is the length of time the IF digitizer waits after it receives the trigger before it asserts the Reference Event.

    **Units:**: seconds

    **Default Value**: 0

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    ref_trigger_minimum_quiet_time = _attributes.AttributeViReal64(1150058)
    '''Type: float

    Specifies a time duration, in seconds, for which the signal must be quiet before the device arms the trigger.

    The signal is quiet when it is below the trigger level if the trigger slope, specified by the iq_power_edge_ref_trigger_slope property, is set to RefTrigIqPwrEdgeSlope.RISING or when it is above the trigger level if the trigger slope is set to RefTrigIqPwrEdgeSlope.FALLING.

    By default, this value is set to 0, which means the device does not wait for a quiet time before arming the trigger. This property is useful to trigger the acquisition on signals containing repeated bursts, but for which each burst may have large changes in signal power within itself. By configuring the minimum quiet time to the time between bursts, you can ensure that the trigger occurs at the beginning of a burst rather than at the signal power change within a burst.

    **Default Value**: 0

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    ref_trigger_osp_delay_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150196)
    '''Type: enums.EnableAttrVals

    Specifies whether the digitizer OSP block delays Reference Triggers, along with the data samples, moving through the OSP block or if the Reference Triggers bypass the OSP block and are processed immediately.

    Enabling this property requires the following equipment configurations:

    - All digitizers being used must be the same model and hardware revision.
    - All digitizers must use the same firmware.
    - All digitizers must be configured with the same I/Q rate.
    - All devices must use the same signal path.

    **PXIe-5663/5663E**: Read the value of the if_filter property to determine the IF filters used by the PXIe-5663/5663E.

    **PXIe-5665/5667/5668**:Refer to the device-specific information in the device_instantaneous_bandwidth property to determine the IF filters used by the PXIe-5665/5667/5668. If you set the fft_width property, refer to the device-specific information for this property and the device_instantaneous_bandwidth property to determine the IF filters used. For frequencies less than 3.6 GHz, set the rf_preamp_enabled to the same value for all devices.

    **PXIe-5665 14 GHz**: Set the downconverter_preselector_enabled to the same value for all devices.

    If the I/Q rate is set programmatically for I/Q acquisitions, the following properties should be identical for the best device synchronization:

    - digital_if_equalization_enabled
    - spectrum_osp_sampling_ratio

    For spectrum acquisitions, the following properties should be identical for the best device synchronization:

    - spectrum_span
    - resolution_bandwidth_type
    - digital_if_equalization_enabled
    - spectrum_osp_sampling_ratio

    For more information about the digitizer OSP block and Reference Triggers, refer to the following topics in the *NI High-Speed Digitizers Help*:

    - NI 5622 Onboard Signal Processing (OSP)
    - NI 5142 Onboard Signal Processing (OSP)
    - NI PXIe-5622 Trigger Sources
    - NI PXI-5142 Trigger Sources
    - NI PXIe-5622 Block Diagram
    - NI PXI-5142 Trigger Sources

    **Defined Values:**

    %enum_table{enable attr vals}

    **Default Value**: EnableAttrVals.ENABLED

    **Supported Devices**:PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    ref_trigger_pretrigger_samples = _attributes.AttributeViInt64(1150035)
    '''Type: int

    Specifies the number of pretrigger samples the samples acquired before the Reference Trigger is received to be acquired per record.

    **Default Value**: 0

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    **High-Level Methods**:

    - configure_digital_edge_ref_trigger
    - configure_software_edge_ref_trigger
    - configure_iq_power_edge_ref_trigger
    '''
    ref_trigger_terminal_name = _attributes.AttributeViString(1150123)
    '''Type: str

    Returns the fully qualified signal name as a string.

    **Default Values**:

    **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>RefTrigger</i>, where *BasebandModule* is the name of your baseband module of your device in MAX.

    **PXIe-5820/5840/5841/5842**: /<i>ModuleName/<i>ai</i>/0/<i>RefTrigger</i>, where *ModuleName* is the name of your device in MAX.

    **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>RefTrigger</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **All other devices**: /<i>DigitizerName</i>/<i>RefTrigger</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - get_terminal_name
    '''
    ref_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RefTrigType, 1150028)
    '''Type: enums.RefTrigType

    Specifies whether you want the Reference Trigger to be a digital edge, I/Q power edge, or software trigger.

    **Defined Values:**

    %enum_table{ref trig type}

    **Default Value**: RefTrigType.NONE

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    resolution_bandwidth = _attributes.AttributeViReal64(1150013)
    '''Type: float

    Specifies the resolution along the x-axis of the spectrum.

    NI-RFSA uses the resolution bandwidth value to determine the acquisition size. If specified, the number_of_spectral_lines property value overrides this value.

    **Units**: hertz (Hz)

    **Default Value**: 100 kHz

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - configure_resolution_bandwidth
    '''
    resolution_bandwidth_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SpectrumResolutionBandwidthType, 1150014)
    '''Type: enums.SpectrumResolutionBandwidthType

    Specifies how the resolution_bandwidth property is expressed.

    **Defined Values:**

    %enum_table{spectrum resolution bandwidth type}

    **Default Value**: SpectrumResolutionBandwidthType._3DB

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    rf_attenuation_index = _attributes.AttributeViInt32(1150076)
    '''Type: int

    Specifies the value of the RF attenuation from a table of valid configurations.

    This property is valid only during a calibration session and when you set the low_frequency_bypass_enabled property to NIRFSA_VAL_DISABLED.

    **Valid Values**: 0 to 64

    **Default Value**: N/A

    **Supported Devices**: PXIe-5693

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    rf_attenuation_step_size = _attributes.AttributeViReal64(1150155)
    '''Type: float

    Specifies the step size for the RF attenuation level.

    The actual RF attenuation is coerced up to the next highest multiple of this step size. You can also set this value to change the step size for the device within the supported device precision and configuration.

    **PXI-5600**: The device configuration supports only the following attenuation step size values: 10, 20, 30, 40, and 50.

    **PXIe-5601**: The attenuation is calculated based on the actual calibrated value closest to the desired value, so the step size varies as the actual gain values vary between consecutive attenuation settings.

    **PXIe-5603**: The device configuration supports attenuation changes in 1 dB steps.

    **PXIe-5605**: The available attenuation step size depends on the specified center frequency. In the high band signal path (input frequencies greater than 3.6 GHz), the only available attenuation is the step attenuator that you can change in 5 dB steps. In the low band signal path (input frequencies less than or equal to 3.6 GHz), an additional 31 dB of solid-state attenuation is available in 1 dB steps. The 5 dB default value indicates that, even when in the low band signal path, NI-RFSA changes the attenuation in 5 dB steps using only the mechanical attenuator. You can use this property to affect when the device changes the attenuation settings. To use the solid-state attenuation in the low band signal path, change the step size to a value other than a multiple of 5 (for example, a step size of 1 dB). If you use a value other than a multiple of 5 while in the high band of the PXIe-5605, NI-RFSA returns an error.

    **Units**: dB

    **Valid Values:**

    **PXI-5600/5661**: 10, 20, 30, 40, and 50

    **PXIe-5601/5663/5663E**: 0.0 to 93.0, continuous

    **PXIe-5603/5665 (3.6 GHz)**: 1.0 to 74.0, in 1 dB steps

    **PXIe-5605/5665 (14 GHz) (low band), PXIe-5606/5668 (low band)**: 1.0 to 106.0, in 1 dB steps

    **PXIe-5605/5665 (14 GHz) (high band), PXIe-5606/5668 (high band)**: 5.0 to 75.0, in 5 dB steps

    **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 1.0 to 74.0, in 1 dB steps

    **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**:  1.0

    **PXIe-5667 (7 GHz) using the PXIe-5693 preselector low frequency bypass path**:  1.0 to 106.0 in 1 dB steps

    **PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector filter path**:  1.0

    **Default Value:**

    **PXI-5600/5661**: 10.0

    **PXIe-5601/5663/5663E**: 0.0

    **PXIe-5603/5665 (3.6 GHz)**: 1.0

    **PXIe-5605/5665 (14 GHz), PXIe-5606/5668**: 5.0

    **PXIe-5667**: 1.0

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668
    '''
    rf_attenuation_table = _attributes.AttributeViInt32(1150077)
    '''Type: int

    Specifies which RF attenuator table to use.

    **Valid Values**: 0 to 1

    **Default Value**: N/A

    **Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E
    '''
    rf_conditioning_cal_tone_frequency = _attributes.AttributeViReal64(1150209)
    '''Type: float

    Specifies the frequency of the RF conditioning calibration tone, in hertz (Hz).

    **Valid Values**: 34.5 MHz to 7.5 GHz

    **Default Value**: 1.0 GHz

    **Supported Devices**: PXIe-5667, PXIe-5693/5698
    '''
    rf_conditioning_cal_tone_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ConditioningCalToneMode, 1150208)
    '''Type: enums.ConditioningCalToneMode

    Specifies the location in a signal path where an RF conditioning calibration tone is injected or whether the tone is disabled.

    **Defined Values:**

    %enum_table{conditioning cal tone mode}

    **Default Value**: ConditioningCalToneMode.DISABLED

    **Supported Devices**: PXIe-5667, PXIe-5693/5698

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    rf_conditioning_temperature = _attributes.AttributeViReal64(1150211)
    '''Type: float

    Returns the current temperature, in degrees Celsius, of the RF conditioning module associated with the NI-RFSA device.

    **Default Value**: N/A

    **Supported Devices**: PXIe-5667
    '''
    rf_high_pass_filtering = _attributes.AttributeViReal64(1150220)
    '''Type: float

    Specifies the maximum corner frequency of the highpass filter in the RF signal path.

    The device uses the highest frequency highpass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables highpass filtering.

    For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this property returns the value you specified rather than a coerced value if multiple highpass filters are used during the acquisition.

    The PXIe-5606 features highpass filters at 1.35 GHz and 2.2 GHz.

    **Valid Values**: 0 to 26.5

    **Default Value**: 0

    **Supported Devices**: PXIe-5606, PXIe-5668
    '''
    rf_out_lo_export_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableUnspecifiedAttrVals, 1150298)
    '''Type: enums.EnableUnspecifiedAttrVals

    Specifies whether to enable the RF OUT LO OUT terminal on the PXIe-5840/5841.

    When this property is enabled, if the lo_source property is set to LoSourceVals.LO_IN and you do not set the lo_frequency or downconverter_center_frequency properties, NI-RFSA rounds the LO frequency to approximately an LO step size as if the source was LoSourceVals.ONBOARD. This ensures that when you configure NI-RFSA and NI-RFSG with compatible settings that result in the same LO frequency, the rounding also is compatible.

    **Defined Values:**

    %enum_table{enable unspecified attr vals}

    **Default Value:**: EnableUnspecifiedAttrVals.UNSPECIFIED

    **Supported Devices**: PXIe-5840/5841/5842
    '''
    rf_preamp_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableRfPreamp, 1150129)
    '''Type: enums.EnableRfPreamp

    Specifies whether the RF preamplifier is enabled in the system.

    **PXIe-5667, PXIe-5644/5645/5646, PXIe-5830/5831/5840/5841/5842**: The  EnableRfPreamp.AUTOMATIC value enables the RF preamplifier based on the value of the reference_level property and the center frequency. Except on the PXIe-5830/5831/5832, NI-RFSA coerces this property from EnableRfPreamp.AUTOMATIC to the selected value.

    ----
    **Note**
    For the PXIe-5840/5841, the automatically selected value may not be optimal for all measurements. At some reference levels, EnableRfPreamp.ENABLED may improve the noise floor while EnableRfPreamp.DISABLED may improve distortion.

    ----

    **PXIe-5667**: The EnableRfPreamp.AUTOMATIC value is supported only when the low_frequency_bypass_enabled property is set to EnableRfPreamp.DISABLED. If the reference level is greater than -25 dBm, NI-RFSA disables the preamplifier. If the reference level is less than or equal to -25 dBm, NI-RFSA sets the rf_preamp_enabled property to EnableRfPreamp.ENABLED_WHEN_IN_SIGNAL_PATH.

    **PXIe-5668 with PXIe-5698**: If you set this property to rf_preamp_enabled, only the preamplifier on the PXIe-5698 is used, and the preamplifier on the PXIe-5668 remains disabled.

    **Defined Values:**

    %enum_table{enable rf preamp}

    **Default Value**:

    **PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842**: EnableRfPreamp.AUTOMATIC

    **All other devices**: EnableRfPreamp.DISABLED

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5698, PXIe-5830/5831/5832/5840/5841/5842
    '''
    rf_preamp_present = _attributes.AttributeViBoolean(1150137)
    '''Type: bool

    Returns whether an RF preamplifier is available on the RF downconverter module.

    **Defined Values:**

    | Value         | Description                                                     |
    |:---------|:-----------------------------------------------------|
    | True  | The device has an enabled RF preamplifier available. |
    | False | The device has no RF preamplifier available.         |

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842
    '''
    rf_preselector_filter = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RfPreselectorFilter, 1150166)
    '''Type: enums.RfPreselectorFilter

    Specifies the RF preselector filter to use.

    ----
    **Note**
    You can write to this property when using only the PXIe-5693 as a stand-alone device.

    ----

    **Defined Values**:

    %enum_table{rf preselector filter}

    **Default Values**:

    **PXIe-5667, PXIe-5693**: RfPreselectorFilter._9

    **PXIe-5665**: RfPreselectorFilter.NONE

    **Supported Devices**: PXIe-5665/5667, PXIe-5693
    '''
    selected_path = _attributes.AttributeViString(1150331)
    '''Type: str

    Specifies which path to configure to acquire a signal.

    **Default Value**: "" (empty string)
    '''
    selected_ports = _attributes.AttributeViString(1150297)
    '''Type: str

    Specifies the port to configure.

    ----
    **Note**
    When using RF list mode, ports cannot be shared with NI-RFSA.

    ----

    **Valid Values**:

    **PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860**: "" (empty string)

    **PXIe-5830**: if0, if1

    **PXIe-5831/5832**: if0, if1, rf <0-1> port <x>, where

    *0-1* indicates one (*0*) or two (*1*) mmRH-5582 connections and

    *x* is the port number on the mmRH-5582 front panel.

    **Default Value:**

    **PXIe-5830/5831/5832:**: if1

    **PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    available_ports
    '''
    serial_number = _attributes.AttributeViString(1150053)
    '''Type: str

    Returns the serial number of the RF downconverter module.

    ----
    **Note**
    For the PXIe-5644/5645/5646 and PXIe-5820/5840/5841, this property returns the serial number of the VST module. For the PXIe-5830/5831/5832, this property returns the serial number of the PXIe-3621/3622.

    ----

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    signal_bandwidth = _attributes.AttributeViReal64(1150267)
    '''Type: float

    Specifies the bandwidth of the input signal around the iq_carrier_frequency.

    This value must be less than or equal to (0.8 7 [I/Q rate](iq_rate.html)).

    NI-RFSA defines *signal bandwidth* as twice the maximum I/Q signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the signal bandwidth is simply the baseband signal's minimum frequency subtracted from its maximum frequency, or *f* < sub>max</sub> - *f*< sub>min</sub>.

    If you do not set this property, NI-RFSA uses the maximum available signal bandwidth. Depending on your device settings, setting this property enables certain optimizations. Based on the specified signal bandwidth, NI-RFSA decides the minimum equalized bandwidth and equalizer gain.

    ----
    **Note**
    You must set this property to enable the downconverter_frequency_offset_mode property.

    ----

    Ensure you set the signal bandwidth wide enough to encompass all significant anticipated input power. In cases where NI-RFSA optimizes the input gain based on the signal bandwidth, significant input power outside the signal bandwidth can lead to clipping and associated overflow warnings if you do not have enough margin in your [reference level.](reference_level.html)

    **Units**: Hz

    **Default Value**: 0 Hz

    **Supported Devices:**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-selection.html>`_

    `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-selection.html>`_

    `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-selection.html>`_
    '''
    signal_conditioning_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SignalConditioningEnabled, 1150160)
    '''Type: enums.SignalConditioningEnabled

    Specifies whether all signal conditioning is enabled on the PXIe-5694.

    ----
    **Note**
    If you set this property to SignalConditioningEnabled.BYPASSED, NI-RFSA bypasses all signal conditioning, prevents any signal downconversion, and fixes the values for downconverter_gain property, the device_instantaneous_bandwidth property, and the if_filter_bandwidth property.

    ----

    **Defined Values:**

    %enum_table{signal conditioning enabled}

    **Default Value**: SignalConditioningEnabled.ENABLED

    **Supported Devices**: PXIe-5694
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Specifies whether NI-RFSA simulates I/O operations. This property is useful for debugging applications without using hardware. After a session is opened, you cannot change the simulation state. Use the init_with_options method to enable simulation.

    ----
    **Note**
    PXI-5600/5661 support setting this property to False only.

    ----

    **Defined Values:**

    | Value         | Description                                                           |
    |:---------|:-----------------------------------------------------------|
    | True  | NI-RFSA simulates NI-RFSA I/O operations.                  |
    | False | NI-RFSA does not support simulated NI-RFSA I/O operations. |

    **Default Value**: False

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode); PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    smooth_spectrum_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150219)
    '''Type: enums.EnableAttrVals

    Specifies that an optimized IF filtering selection is made at different spectrum frequency ranges during spectrum acquisition.

    The IF filter used depends on the configured RF center frequency, as shown in the following table.

    | Center Frequency    | IF Filter |
    |:--------------------|:----------|
    | 0 Hz and <80 MHz | 300 kHz   |
    | 0 MHz             | 50 MHz    |

    ----
    **Note**
    Setting this property to **Enabled** prevents you from setting if_filter_bandwidth or device_instantaneous_bandwidth.

    ----

    **Defined Values:**

    %enum_table{enable attr vals}

    **Default Value**: EnableAttrVals.DISABLED

    **Supported Devices**: PXIe-5665/5668

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    Returns a string that contains a brief description of NI-RFSA.

    This property returns

    RF Signal Analyzer Instrument Driver.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_prefix = _attributes.AttributeViString(1050302)
    '''Type: str

    Returns a string that contains the prefix for NI-RFSA. The name of each user-callable method in NI-RFSA starts with this prefix.

    This property returns

    niRFSA.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_revision = _attributes.AttributeViString(1050551)
    '''Type: str

    Returns a string that contains additional version information about NI-RFSA.

    For example, NI-RFSA can return

    Driver: NI-RFSA 2.6, Compiler: MSVC 7.10, Components: IVI Engine 4.00, VISA-Spec 4.00 as the value of this property.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    '''Type: str

    Returns a string that contains the name of the vendor that supplies NI-RFSA.

    This property returns

    National Instruments.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    spectrum_averaging_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SpectrumAveragingMode, 1150016)
    '''Type: enums.SpectrumAveragingMode

    Specifies the averaging mode for the spectrum acquisition.

    **Defined Values:**

    %enum_table{spectrum averaging mode}

    **Default Value**: SpectrumAveragingMode.NO

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    spectrum_number_of_averages = _attributes.AttributeViInt32(1150015)
    '''Type: int

    Specifies the number of acquisitions to average.

    The averaging process returns the final result after the number of averages is complete.

    **Default Value**: 10

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    spectrum_osp_sampling_ratio = _attributes.AttributeViReal64(1150144)
    '''Type: float

    Specifies the oversampling ratio used by the digitizer onboard signal processing (OSP) when you are in spectrum acquisition mode. This property allows you to acquire a larger bandwidth in hardware and reduce that bandwidth in software, decreasing the possibility of hardware data path overflows.

    **PXIe-5644/5645/5646**: The only valid value for this property is 1.

    **Default Value**: 1.0

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    spectrum_span = _attributes.AttributeViReal64(1150003)
    '''Type: float

    Specifies the frequency range of the computed spectrum in hertz (Hz).

    For example, if you specify a center frequency of 1 GHz and a span of 100 MHz, the spectrum ranges from 950 MHz to 1,050 MHz after zoom processing. This value may be coerced based on hardware settings and RF downconverter specifications.

    NI-RFSA performs multispan acquisitions by dividing the total requested span into equally sized subspans based on the device instantaneous bandwidth at the range of frequencies you specify. NI-RFSA combines these subspans to yield a multispan acquisition. You can use the fft_width property to improve amplitude accuracy and avoid unwanted effects such as filter roll-off and spurs across the span you select.

    ----
    **Note**
    If you configure the spectrum span to a value larger than the hardware instantaneous bandwidth, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you requested.

    ----

    ----
    **Note**
    For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect measurements. Refer to the digitizer_dither_enabled property for more information about dithering.

    ----

    **PXIe-5663/5663E**: NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the instantaneous bandwidth for frequencies above 120 MHz is different than instantaneous bandwidth for frequencies less than 120 MHz, which are 20 MHz and 10 MHz respectively.

    **PXIe-5665 (14 GHz)/5667 (7 GHz)**: If you enable the downconverter preselector filter, the device instantaneous bandwidth is only a typical specification.

    **Default Value**: 10 MHz

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

    **High-Level Methods**:

    - configure_spectrum_frequency_center_span
    '''
    start_to_ref_trigger_holdoff = _attributes.AttributeViReal64(1150033)
    '''Type: float

    Specifies the minimum time, in seconds, that must elapse after the Start Trigger is received before the device recognizes a Reference Trigger.

    **Units:** seconds

    **Default Value**: 0

    **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    start_trigger_delay = _attributes.AttributeViReal64(1150175)
    '''Type: float

    This property is not for customer use.
    '''
    start_trigger_terminal_name = _attributes.AttributeViString(1150122)
    '''Type: str

    Returns the fully qualified signal name as a string.

    **Default Values**:

    **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>StartTrigger</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

    **PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>StartTrigger</i>, where *ModuleName* is the name of your device in MAX.

    **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>StartTrigger</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **All other devices**: /<i>DigitizerName</i>/StartTrigger</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

    **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

    **High-Level Methods**:

    - get_terminal_name
    '''
    start_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.StartTrigType, 1150024)
    '''Type: enums.StartTrigType

    Specifies whether you want the Start Trigger to be a digital edge or software trigger.

    ----
    **Note**
    Set this property to StartTrigType.NONE if you set the acquisition_type property to AcquisitionType.SPECTRUM or if you set the **acquisitionType** parameter to AcquisitionType.SPECTRUM using the [cviconfigure_acquisition_type](cviconfigure_acquisition_type.html) method.

    ----

    **Defined Values:**

    %enum_table{start trig type}

    **Default Value**: StartTrigType.NONE

    **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    step_gain_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.StepGainEnabled, 1150157)
    '''Type: enums.StepGainEnabled

    Specifies whether to enable the step gain amplifier.

    **Defined Values:**

    %enum_table{step gain enabled}

    **Default Value**: StepGainEnabled.DISABLED

    **Supported Devices**: PXIe-5694
    '''
    subspan_overlap = _attributes.AttributeViReal64(1150234)
    '''Type: float

    Use subspan overlap process to eliminate or reduce analyzer spurs.

    To enable this feature, specify a non-zero percentage overlap between consecutive subspans in a spectrum acquisition.

    If a value greater than 0 is specified, then for each spectral line in the resulting spectrum, the driver acquires data twice with slightly different hardware settings, so that the analyzer spurs, if any, are present at different frequencies in the two acquisitions. Typically, LO frequency is shifted between the acquisitions causing analyzer spurs that are relative to the LO frequency, to move from one frequency to another. Those spurs, which are present in only one of the acquisitions for each spectral line, get removed.

    The subspan overlap feature will not remove any spurs from the Device Under Test or modify the signal being measured; unlike the analyzer spurs, the spurs in the signal being measured stay at a constant frequency in the two acquisitions.

    ----
    **Note**
    Subspan overlap process effectively is performing minimum averaging, which might reduce the measured noise floor level. NI-RFSA Spectrum Averaging can be enabled to minimize the effect of subspan overlap on the noise floor.

    ----

    ----
    **Note**
    NI-RFSA may apply further shifts to the specified value to accommodate fixed-frequency edges of components such as preselectors.

    ----

    **Valid Values**:

    **PXIe-5665/5668**: 0 to < 100

    **PXIe-5820/5830/5831/5832/5840/5841/5860**: 0

    **PXIe-5842**: 0, 50

    **Default Value**: 0

    **Supported Devices**: PXIe-5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    ----
    **Note**
    Subspan overlap will not be supported by PXIe-5842, if RMM-5585 (54GHz Frequency Extension) is connected.

    ----
    '''
    supported_instrument_models = _attributes.AttributeViString(1050327)
    '''Type: str

    Returns a comma-separated list of supported devices.

    **Default Value**: N/A

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    sync_advance_trigger_dist_line = _attributes.AttributeViString(1150185)
    '''Type: str

    Specifies which external trigger line distributes the synchronized Advance Trigger signal.

    When synchronizing the Advance Trigger, configure all devices to use the same Advance Trigger distribution line.

    Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

    **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

    **Default Value**: "" (empty string)

    **Supported Devices:** PXIe-5644/5645/5646
    '''
    sync_advance_trigger_master = _attributes.AttributeViBoolean(1150184)
    '''Type: bool

    Specifies whether the device is the master for synchronizing the shared Advance Trigger between multiple devices.

    The master device distributes the synchronized Advance Trigger to all devices in the system through the Advance Trigger distribution line.

    When synchronizing the Advance Trigger, one device must always be designated as the master. When the device is configured as a master, it actively drives the Advance Trigger distribution line. When the device is configured as a slave, set the advance_trigger_type property to NIRFSA_VAL_DIGITAL_EDGE, and the digital_edge_advance_trigger_source property to NIRFSA VAL SYNC ADVANCE TRIGGER STR.

    Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

    **Defined Values:**

    | Value         | Description                                                                           |
    |:---------|:---------------------------------------------------------------------------|
    | True  | The device is the master device for synchronizing the Advance Trigger.     |
    | False | The device is not the master device for synchronizing the Advance Trigger. |

    **Default Value**: False

    **Supported Devices:** PXIe-5644/5645/5646

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    sync_ref_trigger_delay_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnableAttrVals, 1150189)
    '''Type: enums.EnableAttrVals

    Specifies whether the Reference Trigger is delayed with the data.

    Set this property to EnableAttrVals.DISABLED when the ref_trigger_type property is set to RefTrigType.IQ_POWER_EDGE or RefTrigType.IQ_ANALOG_EDGE.

    Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

    **Defined Values:**

    %enum_table{enable attr vals}

    **Default Value**: EnableAttrVals.DISABLED

    **Supported Devices:** PXIe-5644/5645/5646

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    sync_ref_trigger_dist_line = _attributes.AttributeViString(1150179)
    '''Type: str

    Specifies which external trigger line distributes the synchronized Reference Trigger signal.

    When synchronizing the Reference Trigger, configure all devices to use the same Reference Trigger distribution line.

    Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

    **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

    **Default Value**: "" (empty string)

    **Supported Devices:** PXIe-5644/5645/5646
    '''
    sync_ref_trigger_master = _attributes.AttributeViBoolean(1150178)
    '''Type: bool

    Specifies whether the device is the master for synchronizing the shared Reference Trigger between multiple devices.

    The master device distributes the synchronized Reference Trigger to all devices in the system through the Reference Trigger distribution line.

    When synchronizing the Reference Trigger, one device must always be designated as the master. When the device is configured as a master, it actively drives the Reference Trigger distribution line. When the device is configured as a slave, set the ref_trigger_type property to NIRFSA_VAL_DIGITAL_EDGE, and the digital_edge_ref_trigger_source property to NIRFSA VAL SYNC REF TRIGGER STR.

    Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

    **Defined Values:**

    |Value          | Description                                                                       |
    |:---------|:-----------------------------------------------------------------------|
    | True  | The device is the master device for synchronizing the Ref Trigger.     |
    | False | The device is not the master device for synchronizing the Ref Trigger. |

    **Default Value**: False

    **Supported Devices:** PXIe-5644/5645/5646

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    sync_sample_clock_dist_line = _attributes.AttributeViString(1150218)
    '''Type: str

    Specifies which external trigger line distributes the Sample Clock sync signal.

    When synchronizing the Sample Clock, configure all devices to use the same Sample Clock distribution line.

    Refer to `Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/pxie-5644-feature/page/synchronization-rfsa-g.html>`_ for more information about PXIe-5646 device synchronization.

    **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5646
    '''
    sync_sample_clock_master = _attributes.AttributeViBoolean(1150217)
    '''Type: bool

    Specifies whether the device is the master device for synchronizing the Sample Clock between multiple devices.

    The master device distributes the Sample Clock sync signal to all devices in the system through the Sample Clock sync distribution line.

    When synchronizing the Sample Clock, one device must always be designated as the master. The master device actively drives the Sample Clock sync distribution line.

    Refer to [Synchronization Using NI-RFSA and NI-RFSG](PXIe-5646.chm/synchronization-rfsa-g.html) for more information about PXIe-5646 device synchronization.

    **Defined Values:**

    | Value         | Description                                                                    |
    |:---------|:--------------------------------------------------------------------|
    | True  | The device is the master device for synchronizing the Sample Clock. |
    | False | The device is not the master for synchronizing the Sample Clock.    |

    **Default Value:** False

    **Supported Devices:** PXIe-5646
    '''
    sync_start_trigger_dist_line = _attributes.AttributeViString(1150177)
    '''Type: str

    Specifies which external trigger line distributes the synchronized Start Trigger signal.

    When synchronizing the Start Trigger, configure all devices to use the same Start Trigger distribution line.

    Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

    **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

    **Default Value**: "" (empty string)

    **Supported Devices**: PXIe-5644/5645/5646
    '''
    sync_start_trigger_master = _attributes.AttributeViBoolean(1150176)
    '''Type: bool

    Specifies whether the device is the master for synchronizing the shared Start Trigger between multiple devices.

    The master device distributes the synchronized Start Trigger to all devices in the system through the Start Trigger distribution line.

    When synchronizing the Start Trigger, one device must always be designated as the master. When the device is configured as a master, it actively drives the Start Trigger distribution line. When the device is configured as a slave, set the start_trigger_type property to NIRFSA_VAL_DIGITAL_EDGE, and the digital_edge_start_trigger_source property to NIRFSA VAL SYNC START TRIGGER STR.

    Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

    **Defined Values:**

    |Value          | Description                                                                         |
    |:---------|:-------------------------------------------------------------------------|
    | True  | The device is the master device for synchronizing the Start Trigger.     |
    | False | The device is not the master device for synchronizing the Start Trigger. |

    **Default Value**: False

    **Supported Devices:** PXIe-5644/5645/5646

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    temperature_read_interval = _attributes.AttributeViReal64(1150061)
    '''Type: float

    Indicates the minimum time between temperature sensor readings in seconds.

    When you call the read_power_spectrum_f64 method, the read_iq_single_record_complex_f64 method, or the initiate method, NI-RFSA checks whether at least the amount of time specified by this property has elapsed before reading the hardware temperature.

    ----
    **Note**
    NI-RFSA ignores this property if you call the perform_thermal_correction method or read the downconverter_gain property.

    ----

    **Default Value**: 30 seconds

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    thermal_correction_headroom_range = _attributes.AttributeViReal64(1150316)
    '''Type: float

    Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the device_temperature property.

    For example, if this property is set to 5.0, and the device is self-calibrated at 35 C, then you can expect to run the device from 30 C to 40 C with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance and ADC or DSP overflows.

    **Units:** degrees Celsius (C)

    **Default Value**:

    **PXIe-5830/5831/5832/5842/5860**: 5

    **PXIe-5840/5841**: 10

    **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860
    '''
    thermal_correction_temperature_resolution = _attributes.AttributeViReal64(1150300)
    '''Type: float

    Specifies the temperature change required before NI-RFSA recalculates the thermal correction settings when entering the Running state.

    **Units:** degrees Celsius (C)

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Default Values**:

    **PXIe-5830/5831/5832/5842/5860**: 0.2

    **PXIe-5840/5841**: 1.0
    '''
    timer_event_interval = _attributes.AttributeViReal64(1150096)
    '''Type: float

    Specifies the time, in seconds, that the timer counts before generating a Timer Event.

    After the timer reaches zero, it automatically restarts.

    ----
    **Note**
    For the PXIe-5820/5830/5831/5832/5840/5841/5842 and the PXIe-5842 with S-parameters, this property must be set for the timer to start. If you do not set this property, the timer is disabled.

    ----

    **Units**: seconds

    **Default Value**: 0.01

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters
    '''
    timer_start_source = _attributes.AttributeViString(1150173)
    '''Type: str

    This property is not for customer use.
    '''
    user_source_pulse_width = _attributes.AttributeViReal64(1150322)
    '''Type: float

    Specifies the pulse width for the User Source.

    Use the user_source_pulse_width_units property to set the units for the pulse width.

    **Default Value**: 200E(-9)

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    user_source_pulse_width_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.UserSourcePulseWidthUnits, 1150321)
    '''Type: enums.UserSourcePulseWidthUnits

    Specifies the pulse width units for the User Source.

    When the value is UserSourcePulseWidthUnits.SECONDS, it is assumed that the clock rate of the signal is the data clock. Use UserSourcePulseWidthUnits.CLOCK_PERIODS if the user source clock rate is anything else.

    **Defined Values:**

    %enum_table{user source pulse width units}

    **Default Value**: UserSourcePulseWidthUnits.SECONDS

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''

    def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._interpreter = interpreter

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("interpreter=" + pp.pformat(interpreter))
        self._param_list = ', '.join(param_list)

        # Instantiate any repeated capability objects
        self.markers = _RepeatedCapabilities(self, 'marker', repeated_capability_list)
        self.script_triggers = _RepeatedCapabilities(self, 'scripttrigger', repeated_capability_list)
        self.waveforms = _RepeatedCapabilities(self, 'waveform::', repeated_capability_list)
        self.ports = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.los = _RepeatedCapabilities(self, 'LO', repeated_capability_list)
        self.device_temperatures = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.channels = _RepeatedCapabilities(self, '', repeated_capability_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nirfsa', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    ''' These are code-generated '''

    @ivi_synchronized
    def cal_adjust_cal_tone_power(self, measurement):
        r'''cal_adjust_cal_tone_power

        Specifies the calibration tone power during calibration tone amplitude calibration.

                        You must call the initiate method before calling this method.

                        **Supported Devices**: PXIe-5693

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].cal_adjust_cal_tone_power`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.cal_adjust_cal_tone_power`

        Args:
            measurement (float): Specifies the calibration tone power, in dBm, for the current device setting.

        '''
        self._interpreter.cal_adjust_cal_tone_power(self._repeated_capability, measurement)

    @ivi_synchronized
    def cal_adjust_device_gain(self, frequency, gain):
        r'''cal_adjust_device_gain

        Records measured gain information that is gathered during the Reference Level Calibration step and IF Attenuation Calibration step.

                        This method internally queries the properties you set, and you must commit all properties appropriate for your device calibration procedure prior to calling this method. Refer to ni.com/manuals for the most recent version of the calibration procedure for your device.

                        Call this method immediately after a measurement is made and while the device under test (DUT) is still in the same state as it was during the measurement.

                        **Supported Devices**: PXIe-5693/5694/5698

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].cal_adjust_device_gain`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.cal_adjust_device_gain`

        Args:
            frequency (float): Specifies the RF frequency, in Hz, of the measurement taken.

            gain (float): Specifies the gain measurement, in dB.

        '''
        self._interpreter.cal_adjust_device_gain(self._repeated_capability, frequency, gain)

    @ivi_synchronized
    def cal_adjust_downconverter_gain(self, frequency, gain):
        r'''cal_adjust_downconverter_gain

        Records measured gain information that is gathered during the Reference Level Calibration step and IF Attenuation Calibration step.

                        This method internally queries the properties you set, and you must set and commit the following properties prior to calling this method.

                        - cal_rf_electronic_attenuation_index (This property is required only when the cal_rf_path_selection property is set to RfPathSel._1.)
                        - cal_rf_mechanical_attenuation_index
                        - cal_if_attenuation_table_selection
                        - cal_if_attenuation_index
                        - cal_if_filter_selection
                        - channel_coupling
                        - rf_preamp_enabled

                        Call this method immediately after a measurement is made and while the device under test (DUT) is still in the same state as it was during the measurement.

                        **Supported Devices**: PXIe-5603/5605/5606

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].cal_adjust_downconverter_gain`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.cal_adjust_downconverter_gain`

        Args:
            frequency (float): Specifies the RF frequency, in Hz, of the measurement taken.

            gain (float): Specifies the gain measurement, in dB.

        '''
        self._interpreter.cal_adjust_downconverter_gain(self._repeated_capability, frequency, gain)

    @ivi_synchronized
    def cal_adjust_if_attenuation_calibration(self, if_filter, number_of_attenuators, measurement):
        r'''cal_adjust_if_attenuation_calibration

        Specifies the IF attenuation settings.

                        **Supported Devices**: PXIe-5601, PXIe-5694

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].cal_adjust_if_attenuation_calibration`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.cal_adjust_if_attenuation_calibration`

        Args:
            if_filter (int): Specifies the IF filter used by the downconverter.

                                        |Value                                     |Description                                             |
                                        |:------------------------------------|:--------------------------------------------|
                                        | IFfilter._187_5_MHZ_NARROW (1400)  | Uses the 187.5 MHz wide bandwidth filter.   |
                                        | IFfilter._187_5_MHZ_NARROW (1401) | Uses the 187.5 MHz narrow bandwidth filter. |
                                        | IFfilter._53_MHZ (1402)            | Uses the 53 MHz filter.                     |
                                        | IFfilter.BYPASS (1403)            | Bypasses the IF filter.                     |

            number_of_attenuators (int): Specifies the number of attenuators to use during the IF attenuation adjustment.

            measurement (float): Specifies the relevant measurement taken for the current configuration.


        Returns:
            attenuator_settings (float): Specifies the IF attenuator settings for the measurement. The first element in the array corresponds with IF1, the next element corresponds to IF2, and so on.

        '''
        attenuator_settings = self._interpreter.cal_adjust_if_attenuation_calibration(self._repeated_capability, if_filter, number_of_attenuators, measurement)
        return attenuator_settings

    @ivi_synchronized
    def cal_adjust_if_response_calibration(self, if_filter, rf_frequency, band_width, number_of_measurements):
        r'''cal_adjust_if_response_calibration

        Specifies the IF response settings.

                        **Supported Devices**: PXIe-5601, PXIe-5694

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].cal_adjust_if_response_calibration`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.cal_adjust_if_response_calibration`

        Args:
            if_filter (int): Specifies the IF filter used by the downconverter.

                                        |Value                                     |Description                                           |
                                        |:------------------------------------|:------------------------------------------|
                                        | IFfilter._187_5_MHZ_NARROW (1400)   | Uses the 187.5 MHz wide bandwidth path.   |
                                        | IFfilter._187_5_MHZ_NARROW (1401) | Uses the 187.5 MHz narrow bandwidth path. |
                                        | IFfilter._53_MHZ (1402)            | Uses the 53 MHz path.                     |
                                        | IFfilter.BYPASS (1403)            | Bypasses the IF path.                     |

            rf_frequency (float): Specifies the RF frequency, in Hz, used during the IF response adjustment.

            band_width (float): Specifies the bandwidth, in Hz, to use for the IF response adjustment.

            number_of_measurements (int): Specifies the number of measurements to make.


        Returns:
            measurements (float): Specifies the relevant measurements taken for each IF filter configuration, in dB.

        '''
        measurements = self._interpreter.cal_adjust_if_response_calibration(self._repeated_capability, if_filter, rf_frequency, band_width, number_of_measurements)
        return measurements

    @ivi_synchronized
    def cal_adjust_lo_export_calibration(self, lo_number, number_of_frequency_points):
        r'''cal_adjust_lo_export_calibration

        LO export calibration measures the PXIe-5603/5605 LO output power level.

                        The LO output power measurements are taken from the PXIe-5653 module. In MIMO applications, when the LO is exported from one PXIe-5603/5605 module to another subsequent PXIe-5603/5605, an output power signal of approximately +7 dBm is expected on each LO connector (LO1, LO2, and LO3). This method records the LO attenuation that results in an output power of +7 dBm (or greater) on the three LO output terminals.

                        The PXIe-5665/5668 uses three LOs, but only LO1 is variable in frequency. This method accepts an array of frequencies and attenuations; however, for LO2 and LO3, this array must have only one element because these two LO sources operate only at one frequency. LO1 can have multiple values for specific frequencies.

                        **Supported Devices**: PXIe-5603/5605/5606

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].cal_adjust_lo_export_calibration`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.cal_adjust_lo_export_calibration`

        Args:
            lo_number (int): Specifies the LO source to use for the LO export calibration.

                                        |Value                                   |Description                                                                    |
                                        |:----------------------------------|:-------------------------------------------------------------------|
                                        | LoNumber.LO1  (2200) | Selects LO1, which is the 3.2 GHz to 8.3 GHz variable signal path. |
                                        | LoNumber.LO2 (2201) | Selects LO2, which is the 4 GHz signal path.                       |
                                        | LoNumber.LO3  (2202) | Selects LO3, which is the 800 MHz signal path.                     |

            number_of_frequency_points (int): Specifies the length of the **frequencies** and **LO_ATTENUATION** arrays.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            frequency_points (float): Specifies frequencies for the LO output power measurement. The length of this array equals the **NUMBER_OF_FREQUENCY_POINTS** parameter.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            lo_attenuation (float): Specifies the attenuation value of the corresponding frequency point that results in a +7 dBm output signal on the respective LO OUT connector. The length of this array equals the **NUMBER_OF_FREQUENCY_POINTS** parameter.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        frequency_points, lo_attenuation = self._interpreter.cal_adjust_lo_export_calibration(self._repeated_capability, lo_number, number_of_frequency_points)
        return frequency_points, lo_attenuation

    @ivi_synchronized
    def cal_adjust_ref_level_calibration(self, reference_level_data_type, rf_band, attenuator_table_number, frequency, measurement):
        r'''cal_adjust_ref_level_calibration

        Writes the reference level calibration data settings to the driver.

                        **Supported Devices**: PXIe-5601

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].cal_adjust_ref_level_calibration`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.cal_adjust_ref_level_calibration`

        Args:
            reference_level_data_type (int): Specifies whether the reference level calibration data being used is the default configuration data or the mechanical relay disabled configuration data.

                                        |Value                                                          |Description                                                                                                                                                           |
                                        |:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | ReferenceLevelDataType.DEFAULT (1800)                        | The data is the default configuration data.                                                                                                               |
                                        | ReferenceLevelDataType.MECHANICAL_ATTENUATOR_DISABLED (1801) | The data is the configuration data when the mechanical relay is disabled. Use this option to save uncalibrated measurements for more advanced operations. |

            rf_band (int): Specifies the RF band used during the reference level calibration.

                                        |Value                      |Description                             |
                                        |:---------------------|:----------------------------|
                                        | RfPathSel._1 | The RF band 1 path is used. |
                                        | RfPathSel._2| The RF band 2 path is used. |
                                        | RfPathSel._3 | The RF band 3 path is used. |
                                        | RfPathSel._4 | The RF band 4 path is used. |

            attenuator_table_number (int): Specifies which attenuation table you are using. Valid values are 0 and 1.

            frequency (float): Specifies the frequency for the reference level adjustment.

            measurement (float): Specifies the relevant measurement taken for the current configuration.

        '''
        self._interpreter.cal_adjust_ref_level_calibration(self._repeated_capability, reference_level_data_type, rf_band, attenuator_table_number, frequency, measurement)

    @ivi_synchronized
    def cal_set_temperature(self, temperature):
        r'''cal_set_temperature

        Writes the calibration temperature to the driver.

                        **Supported Devices**: PXIe-5601

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].cal_set_temperature`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.cal_set_temperature`

        Args:
            temperature (float): Specifies the calibration temperature, in degrees Celsius.

        '''
        self._interpreter.cal_set_temperature(self._repeated_capability, temperature)

    @ivi_synchronized
    def configure_iq_carrier_frequency(self, carrier_frequency):
        r'''configure_iq_carrier_frequency

        Configures the `carrier frequency <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/fund-carrierwave.html>`_ of the RF vector signal analyzer hardware for an I/Q acquisition.

                        The carrier frequency is the center frequency of the I/Q acquisition.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Carrier Wave <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/fund-carrierwave.html>`_

                        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_iq_carrier_frequency`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_iq_carrier_frequency`

        Args:
            carrier_frequency (float): Specifies the carrier frequency, in hertz (Hz), of the RF signal to acquire.

                                        The RF vector signal analyzer tunes to this frequency. NI-RFSA may coerce this value based on hardware settings and downconversion settings.

                                        NI-RFSA sets the iq_carrier_frequency property to this value. Refer to the specifications document that shipped with your device for allowable frequency settings.

        '''
        self._interpreter.configure_iq_carrier_frequency(self._repeated_capability, carrier_frequency)

    @ivi_synchronized
    def configure_iq_rate(self, iq_rate):
        r'''configure_iq_rate

        Specifies the I/Q rate for the acquisition.

                        The value is expressed in samples per second (S/s).

                        For the PXIe-5663/5663E/5665/5667/5668, when you set the digitizer_sample_clock_timebase_source property to NIRFSA_VAL_ONBOARD_CLOCK_STR, the digitizer bandwidth is greater than or equal to the coerced **iq_rate** times 0.8. Actual signal bandwidth is limited for all supported devices by the anti-aliasing filter. Further device-specific limitations are as follows.

                        ----
                        **Note**
                        For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect your measurements. Refer to the digitizer_dither_enabled property for more information about dithering.

                        ----

                        - **PXI-5661** You should not need to configure an **iq_rate** higher than 25 megasamples per second (MS/s) because the PXI-5600 RF downconverter bandwidth is 20 MHz. If you configure a higher I/Q rate, you may see aliasing effects at negative frequencies because the IF frequency of the PXI-5600 RF downconverter is 15 MHz.
                        - **PXIe-5663/5663E** Maximum allowed instantaneous bandwidth depends on the I/Q carrier frequency you use. Refer to the `PXIe-5601 RF downconverter overview <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/overview.3.html>`_  for more information about instantaneous bandwidth.
                        - **PXIe-5665** Actual signal bandwidth is limited by the preselector and the combination of the chosen IF filter and anti-aliasing filter. Maximum allowed instantaneous bandwidth is independent of the downconverter center frequency for frequencies less than 3.6 GHz. At frequencies greater than 3.6 GHz, if your device supports the preselector (YIG-tuned filter) and you have enabled it for your application, the maximum allowed instantaneous bandwidth is limited to the instantaneous bandwidth of the preselector. Refer to the *NI PXIe-5665 Specifications* for more information about instantaneous bandwidth limits.
                        - **PXIe-5667** Actual signal bandwidth is limited by the preselector and the combination of the chosen IF filter and anti-aliasing filter. Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the *NI PXIe-5667 Specifications* for more information about instantaneous bandwidth limits.
                        - **PXIe-5668** Actual signal bandwidth is limited by the FPGA image that is downloaded upon opening the session to the PXIe-5624 digitizer. Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the *PXIe-5668 Specifications* for more information about instantaneous bandwidth limits.
                        - **PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842** Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the specifications document for your device for more information about instantaneous bandwidth limits.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        Note:
        One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_iq_rate`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_iq_rate`

        Args:
            iq_rate (float): Specifies the I/Q rate for the acquisition. The value is expressed in samples per second (S/s).

        '''
        self._interpreter.configure_iq_rate(self._repeated_capability, iq_rate)

    @ivi_synchronized
    def configure_number_of_records(self, number_of_records_is_finite, number_of_records):
        r'''configure_number_of_records

        Configures the number of records in a finite acquisition or configures the device to continuously acquire records.

                        You can only configure the device to acquire multiple records if you set the **number_of_records_is_finite** parameter to True.

                        If you configure the device to continuously acquire samples, it continues acquiring data until you call the abort method to abort the acquisition. The device stores data in onboard memory in a circular fashion. After the device fills the memory, it starts overwriting previously acquired data from the beginning of the memory buffer. Retrieve the samples as they are being acquired, using one of the niRFSA fetch I/Q methods, to avoid overwriting data before you retrieve it.

                        To acquire more records than will fit into the device memory without continuously acquiring records, set the **number_of_records_is_finite** parameter in this method to True and the allow_more_records_than_memory property to True.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_number_of_records`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_number_of_records`

        Args:
            number_of_records_is_finite (bool): Specifies whether to configure the device to acquire a finite number of records or to acquire records continuously. The default is True.

                                        | Value         | Description                                                                                                                                                                                                                |
                                        |:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | True  | The device acquires a finite number of records.                                                                                                                                                                 |
                                        | False | The NI-RFSA device acquires records continuously until you call the abort method to abort the acquisition. |

            number_of_records (int): Specifies the number of records to acquire if **number_of_records_is_finite** is set to True.

        '''
        self._interpreter.configure_number_of_records(self._repeated_capability, number_of_records_is_finite, number_of_records)

    @ivi_synchronized
    def configure_number_of_samples(self, number_of_samples_is_finite, samples_per_record):
        r'''configure_number_of_samples

        Configures the number of samples in a finite acquisition or configures the device to continuously acquire samples.

                        If you configure the device for finite acquisition, it acquires the specified number of samples and then stops the acquisition. You can configure the device to acquire multiple records using the configure_number_of_records method. Each record contains the number of samples specified in this method.

                        If you configure the device to continuously acquire samples, it continues acquiring data until you call the abort method to abort the acquisition. The device stores data in onboard memory in a circular fashion. After the device fills the memory, it starts overwriting previously acquired data from the beginning of the memory buffer. Retrieve the samples as they are being acquired, using one of the niRFSA fetch I/Q methods, to avoid overwriting data before you retrieve it.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_number_of_samples`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_number_of_samples`

        Args:
            number_of_samples_is_finite (bool): Specifies whether to configure the device to acquire a finite number of samples or to acquire samples continuously. The default is True.

                                        | Value         | Description                                                                                                                                                                                                        |
                                        |:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | True  | The device acquires a finite number of samples.                                                                                                                                                         |
                                        | False | The device acquires samples continuously until you call the abort method to abort the acquisition. |

            samples_per_record (int): Specifies the number of samples per record if **number_of_samples_is_finite** is set to True.

        '''
        self._interpreter.configure_number_of_samples(self._repeated_capability, number_of_samples_is_finite, samples_per_record)

    @ivi_synchronized
    def configure_reference_level(self, reference_level):
        r'''configure_reference_level

        Configures the reference level.

                        The reference level represents the maximum expected power of an input RF signal.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Improving Your Measurements <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/measurement_guidelines.html>`_

                        `Programming Attenuation-Related Properties and Properties Using NI-RFSA <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/programming-attenuation.html>`_

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_reference_level`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_reference_level`

        Args:
            reference_level (float): Specifies the expected total power, in dBm, of the RF input signal.

        '''
        self._interpreter.configure_reference_level(self._repeated_capability, reference_level)

    @ivi_synchronized
    def configure_resolution_bandwidth(self, resolution_bandwidth):
        r'''configure_resolution_bandwidth

        Configures the resolution bandwidth of a spectrum acquisition.

                        The resolution bandwidth controls the width of the frequency bins in the power spectrum computed by NI-RFSA. A larger value for resolution bandwidth means the frequency bins are wider, so you get fewer bins, or spectral lines.

                        By default, the resolution bandwidth value corresponds to the 3 decibels (dB) bandwidth of the window type NI-RFSA uses to compute the spectrum. To directly specify the frequency bin width, set the resolution_bandwidth_type property to SpectrumResolutionBandwidthType.BIN_WIDTH

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Resolution Bandwidth <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/resolution-bandwidth.html>`_

                        `Improving Your Measurements <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/measurement_guidelines.html>`_

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_resolution_bandwidth`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_resolution_bandwidth`

        Args:
            resolution_bandwidth (float): Specifies the resolution bandwidth of a spectrum acquisition. The value is expressed in hertz (Hz). Configure the type of resolution bandwidth with the resolution_bandwidth_type property.

        '''
        self._interpreter.configure_resolution_bandwidth(self._repeated_capability, resolution_bandwidth)

    @ivi_synchronized
    def configure_spectrum_frequency_center_span(self, center_frequency, span):
        r'''configure_spectrum_frequency_center_span

        Configures the span and center frequency of the spectrum read by NI-RFSA.

                        A spectrum acquisition consists of data surrounding the center frequency.

                        ----
                        **Note**
                        If you configure the spectrum span to a value larger than the instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you requested.

                        ----

                        ----
                        **Note**
                         For the PXIe-5663/5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the bandwidths that correspond to each span are different (10 MHz and 20 MHz, respectively).

                        ----

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_spectrum_frequency_center_span`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_spectrum_frequency_center_span`

        Args:
            center_frequency (float): Specifies the center frequency in a spectrum acquisition. The value is expressed in hertz (Hz). The NI-RFSA device you use determines the valid range. Refer to your device specifications document for more information about frequency range.

            span (float): Specifies the span of a spectrum acquisition. The value is expressed in hertz (Hz).

                                        ----

                                        *Note* For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect your measurements. Refer to the digitizer_dither_enabled property for more information about dithering.

                                        ----

        '''
        self._interpreter.configure_spectrum_frequency_center_span(self._repeated_capability, center_frequency, span)

    @ivi_synchronized
    def configure_spectrum_frequency_start_stop(self, start_frequency, stop_frequency):
        r'''configure_spectrum_frequency_start_stop

        Configures the start and stop frequencies of a spectrum read by NI-RFSA.

                        ----
                        **Note**
                        If you configure the spectrum span (**STOP_FREQUENCY**  **START_FREQUENCY**) to a value larger than the instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you request.

                        ----

                        ----
                        **Note**
                         For the PXIe-5663/5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the bandwidths that correspond to each span are different (10 MHz and 20 MHz, respectively).

                        ----

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_spectrum_frequency_start_stop`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.configure_spectrum_frequency_start_stop`

        Args:
            start_frequency (float): Specifies the lower limit of a span of frequencies. This value is expressed in hertz (Hz).

            stop_frequency (float): Specifies the upper limit of a span of frequencies. This value is expressed in hertz (Hz).

        '''
        self._interpreter.configure_spectrum_frequency_start_stop(self._repeated_capability, start_frequency, stop_frequency)

    @ivi_synchronized
    def fetch_iq_multi_record_complex_f32(self, starting_record, number_of_records, number_of_samples, timeout):
        r'''fetch_iq_multi_record_complex_f32

        Fetches I/Q data from multiple records in an acquisition.

                        A fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.

                        This method is not necessary if you use the read_iq_single_record_complex_f64 method because the read_iq_single_record_complex_f64 method performs the fetch as part of the method.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch_iq_multi_record_complex_f32`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.fetch_iq_multi_record_complex_f32`

        Args:
            starting_record (int): Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.

            number_of_records (int): Specifies the number of records to fetch.

            number_of_samples (int): Specifies the number of samples per record.

            timeout (float): **PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the method to complete before returning a timeout error.

                                        **PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.

                                        ----

                                        For all supported devices, a value of  specifies the method waits until all data is available. A value of 0 specifies the method immediately returns available data.

                                        ----


        Returns:
            data (ni_complex_number_f32): Returns the acquired waveform for each record fetched. The waveforms are written sequentially in the array. Allocate an array at least as large as **number_of_samples** times **number_of_records** for this parameter.

            wfm_info (niRFSA_wfmInfo): Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read. Each element of this array corresponds to a record.

                                        The following list provides more information about each of these properties:

                                        - **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.

                                        ----

                                        The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5840/5841/5842/5860.

                                        ----

                                        - **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.

                                        ----

                                        The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.

                                        ----

                                        - **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.
                                        - **actual samples read** Returns an integer representing the number of samples in the waveform.The actual number of samples for each record can vary if the NIRFSA ATTR NUMBER OF SAMPLES property changes per step during RF list mode.
                                        - **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.
                                        - **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.

        '''
        data, wfm_info = self._interpreter.fetch_iq_multi_record_complex_f32(self._repeated_capability, starting_record, number_of_records, number_of_samples, timeout)
        return data, wfm_info

    @ivi_synchronized
    def fetch_iq_multi_record_complex_f64(self, starting_record, number_of_records, number_of_samples, timeout):
        r'''fetch_iq_multi_record_complex_f64

        Fetches I/Q data from multiple records in an acquisition.

                        A fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.

                        This method is not necessary if you use the read_iq_single_record_complex_f64 method because the read_iq_single_record_complex_f64 method performs the fetch as part of the method.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch_iq_multi_record_complex_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.fetch_iq_multi_record_complex_f64`

        Args:
            starting_record (int): Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.

            number_of_records (int): Specifies the number of records to fetch.

            number_of_samples (int): Specifies the number of samples per record.

            timeout (float): **PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the method to complete before returning a timeout error.

                                        **PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.

                                        ----

                                        For all supported devices, a value of  specifies the method waits until all data is available. A value of 0 specifies the method immediately returns available data.

                                        ----


        Returns:
            data (ni_complex_number_f64): Returns the acquired waveform for each record fetched. The waveforms are written sequentially in the array. Allocate an array at least as large as **number_of_samples** times **number_of_records** for this parameter.

            wfm_info (niRFSA_wfmInfo): Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read. Each element of this array corresponds to a record.

                                        The following list provides more information about each of these properties:

                                        - **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.

                                        ----

                                        The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5840/5841/5842/5860.

                                        ----

                                        - **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.

                                        ----

                                        The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.

                                        ----

                                        - **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.
                                        - **actual samples read** Returns an integer representing the number of samples in the waveform.The actual number of samples for each record can vary if the NIRFSA ATTR NUMBER OF SAMPLES property changes per step during RF list mode.
                                        - **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.
                                        - **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.

        '''
        data, wfm_info = self._interpreter.fetch_iq_multi_record_complex_f64(self._repeated_capability, starting_record, number_of_records, number_of_samples, timeout)
        return data, wfm_info

    @ivi_synchronized
    def get_attribute_vi_boolean(self, attribute_id):
        r'''get_attribute_vi_boolean

        Queries the value of a ViBoolean property.

                        You can use this low-level method to get the values of inherent IVI properties and instrument-specific properties.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            value (bool): Returns the current value of the property. Pass the address of a ViBoolean variable.

        '''
        value = self._interpreter.get_attribute_vi_boolean(self._repeated_capability, attribute_id)
        return value

    @ivi_synchronized
    def get_attribute_vi_int32(self, attribute_id):
        r'''get_attribute_vi_int32

        Queries the value of a ViInt32 property.

                        You can use this low-level method to get the values of inherent IVI properties and instrument-specific properties.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            value (int): Returns the current value of the property. Pass the address of a ViInt32 variable.

        '''
        value = self._interpreter.get_attribute_vi_int32(self._repeated_capability, attribute_id)
        return value

    @ivi_synchronized
    def get_attribute_vi_int64(self, attribute_id):
        r'''get_attribute_vi_int64

        Queries the value of a ViInt64 property.

                        You can use this low-level method to get the values of inherent IVI properties and instrument-specific properties.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_attribute_vi_int64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            value (int): Returns the current value of the property. Pass the address of a ViInt64 variable.

        '''
        value = self._interpreter.get_attribute_vi_int64(self._repeated_capability, attribute_id)
        return value

    @ivi_synchronized
    def get_attribute_vi_real64(self, attribute_id):
        r'''get_attribute_vi_real64

        Queries the value of a ViReal64 property.

                        You can use this low-level method to get the values of inherent IVI properties and instrument-specific properties.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            value (float): Returns the current value of the property. Pass the address of a ViReal64 variable.

        '''
        value = self._interpreter.get_attribute_vi_real64(self._repeated_capability, attribute_id)
        return value

    @ivi_synchronized
    def get_attribute_vi_session(self, attribute_id):
        r'''get_attribute_vi_session

        Queries the value of a ViSession property.

                        You can use this low-level method to get the values of inherent IVI properties and instrument-specific properties.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_attribute_vi_session`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_attribute_vi_session`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            value (int): Returns the current value of the property. Pass the address of a ViSession variable.

        '''
        value = self._interpreter.get_attribute_vi_session(self._repeated_capability, attribute_id)
        return value

    @ivi_synchronized
    def get_attribute_vi_string(self, attribute_id):
        r'''get_attribute_vi_string

        Queries the value of a ViString property.

                        You can use this low-level method to get the values of inherent IVI properties and instrument-specific properties.

                        You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **BUF_SIZE** parameter. If the current value of the property, including the terminating NULL byte, is larger than the size you indicate in the **BUF_SIZE** parameter, the method copies buffer size  1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the method places "123" into the buffer and returns 7.

                        If you want to call this method just to get the required buffer size, you can pass 0 for **BUF_SIZE** and VI_NULL for the **attributeValue** buffer.

                        **Supported Devices:** PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            value (str): The buffer in which the method returns the current value of the property. The buffer must be of type ViChar and have at least as many bytes as indicated in **BUF_SIZE**.

                                        If you specify 0 for the **BUF_SIZE** parameter, you can pass VI_NULL for this parameter.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        value = self._interpreter.get_attribute_vi_string(self._repeated_capability, attribute_id)
        return value

    @ivi_synchronized
    def get_device_response(self, response_type, buffer_size):
        r'''get_device_response

        Returns the requested response type, based on current NI-RFSA settings.

                        The PXI-5661 and PXIe-5663/5663E/5665/5667/5668 automatically corrects for the IF and RF response when you set the digital_if_equalization_enabled property to True. If you are using external digitizer mode, you can use information returned from this method to correct your measurement.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_device_response`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_device_response`

        Args:
            response_type (int): Specifies the IF, RF, or combined (IF and RF) response of the downconverter or NI-RFSA device that NI-RFSA returns. The default value is ResponseType.DOWNCONVERTER_IF.

                                        %enum_table{response type}

            buffer_size (int): Specifies the size of the array you specify for the FREQUENCIES, **MAGNITUDE_RESPONSE**, and **PHASE_RESPONSE** parameters.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            frequencies (array.array("d")): Returns an array containing the frequencies, in hertz (Hz), that correspond to the response data.

                                        Pass VI_NULL if you do not want to use this parameter.

            magnitude_response (array.array("d")): Returns an array containing the magnitude of the requested response, in decibels (dB). The magnitude response is normalized to the center frequency at each frequency in the FREQUENCIES array.

                                        Pass VI_NULL if you do not want to use this parameter.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            phase_response (array.array("d")): Returns an array containing the phase of the requested response, in radians. The phase response is normalized to the center frequency at each frequency entry in the FREQUENCIES array.

                                        Pass VI_NULL if you do not want to use this parameter. This array may contain zeros if the device does not contain a stored phase response in its calibration data.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            number_of_frequencies (int): Returns the required number of elements in the FREQUENCIES array and the response arrays. If **BUFFER_SIZE** is 0, this parameter returns the expected array size. The expected array size depends on which NI-RFSA device you use (PXI-5661, PXIe-5663/5663E/5665) and on the current settings (PXIe-5663/5663E/5665 only).

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        frequencies, magnitude_response, phase_response, number_of_frequencies = self._interpreter.get_device_response(self._repeated_capability, response_type, buffer_size)
        return frequencies, magnitude_response, phase_response, number_of_frequencies

    @ivi_synchronized
    def get_fetch_backlog(self, record_number):
        r'''get_fetch_backlog

        Returns the number of points acquired that have not yet been fetched.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_fetch_backlog`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_fetch_backlog`

        Args:
            record_number (int): Specifies the record from which to read the backlog. Record numbers are zero-based.


        Returns:
            backlog (int): Returns the number of samples available to read for the requested record.

        '''
        backlog = self._interpreter.get_fetch_backlog(self._repeated_capability, record_number)
        return backlog

    @ivi_synchronized
    def get_frequency_response(self, buffer_size):
        r'''get_frequency_response

        Returns the requested response type, based on current NI-RFSA settings. The PXI-5661 and PXIe-5663/5663E/5665/5667/5668 automatically corrects the IF and RF response when you set the Digital IF Equalization Enabled property to TRUE. If you are using external digitizer mode, you can use information returned from this VI to correct your measurement.

                        Refer to the *Factory Calibration* topic for your device for more information about frequency-response calibration.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_frequency_response`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_frequency_response`

        Args:
            buffer_size (int): Specifies the size of the array you specify for the FREQUENCIES, **MAGNITUDE_RESPONSE**, and **PHASE_RESPONSE** parameters.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            frequencies (array.array("d")): Returns an array containing the frequencies, in hertz (Hz), that correspond to the response data.

                                        Pass VI_NULL if you do not want to use this parameter.

            magnitude_response (array.array("d")): Returns an array containing the magnitude of the requested response, in decibels (dB). The magnitude response is normalized to the center frequency at each frequency in the FREQUENCIES array.

                                        Pass VI_NULL if you do not want to use this parameter.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            phase_response (array.array("d")): Returns an array containing the phase of the requested response, in radians. The phase response is normalized to the center frequency at each frequency entry in the FREQUENCIES array.

                                        Pass VI_NULL if you do not want to use this parameter. This array may contain zeros if the device does not contain a stored phase response in its calibration data.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            number_of_frequencies (int): Returns the required number of elements in the FREQUENCIES array and the response arrays. If **BUFFER_SIZE** is 0, this parameter returns the expected array size. The expected array size depends on which NI-RFSA device you use (PXI-5661, PXIe-5663/5663E/5665) and on the current settings (PXIe-5663/5663E/5665 only).

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        frequencies, magnitude_response, phase_response, number_of_frequencies = self._interpreter.get_frequency_response(self._repeated_capability, buffer_size)
        return frequencies, magnitude_response, phase_response, number_of_frequencies

    @ivi_synchronized
    def get_number_of_spectral_lines(self):
        r'''get_number_of_spectral_lines

        Returns the number of spectral lines that NI-RFSA computes with the current power spectrum configuration.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_number_of_spectral_lines`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_number_of_spectral_lines`

        Returns:
            number_of_spectral_lines (int): Returns the value of the number_of_spectral_lines property.

        '''
        number_of_spectral_lines = self._interpreter.get_number_of_spectral_lines(self._repeated_capability)
        return number_of_spectral_lines

    @ivi_synchronized
    def get_relay_name(self, index):
        r'''get_relay_name

        Returns the name of a relay for your device.

                        When you call this method and pass a VI_NULL pointer to the NAME parameter, **BUFFER_SIZE** is populated with the size of name including the terminating NULL byte. When you call this method and specify a value for **BUFFER_SIZE** that is greater than or equal to the name of relay, the NAME parameter returns the appropriate value.

                        **Supported Devices**: PXIe-5603/5605/5606.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_relay_name`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_relay_name`

        Args:
            index (int): Specifies the index of the relay.


        Returns:
            name (str): Specifies the relay name, when used as an input. You can select VI_NULL or a pointer to a ViInt32 array. VI_NULL is the default. When **BUFFER_SIZE** is greater than or equal to the number of relays, NAME returns the relay name.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        name = self._interpreter.get_relay_name(self._repeated_capability, index)
        return name

    @ivi_synchronized
    def get_relay_operations_count(self):
        r'''get_relay_operations_count

        Returns an array consisting of all the relay counts for your device.

                        When you call this method and pass a VI_NULL pointer to the **OPERATIONS_COUNT** parameter, **BUFFER_SIZE** is populated with the number of relays on the device. When you call this method and specify a value for **BUFFER_SIZE** that is greater than or equal to the number of relays, the **OPERATIONS_COUNT** parameter returns the appropriate value.

                        **Supported Devices**: PXIe-5603/5605/5606, PXIe-5698

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_relay_operations_count`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.get_relay_operations_count`

        Returns:
            operations_count (array.array("l")): Specifies the operations count array, when used as an input. You can select VI_NULL or a pointer to a ViInt32 array. VI_NULL is the default. When **BUFFER_SIZE** is greater than or equal to the number of relays, **OPERATIONS_COUNT** returns the number of relay operations.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        operations_count = self._interpreter.get_relay_operations_count(self._repeated_capability)
        return operations_count

    @ivi_synchronized
    def load_configurations_from_file(self, file_path):
        r'''load_configurations_from_file

        Loads the configurations from the specified file to the NI-RFSA driver session.

        The VI does an implicit reset before loading the configurations from the file.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].load_configurations_from_file`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.load_configurations_from_file`

        Args:
            file_path (str): Specifies the absolute path of the file from which the NI-RFSA loads the configurations.

        '''
        self._interpreter.load_configurations_from_file(self._repeated_capability, file_path)

    @ivi_synchronized
    def read_iq_single_record_complex_f64(self, timeout, data_array_size):
        r'''read_iq_single_record_complex_f64

        Initiates an acquisition and fetches a single I/Q data record.

                        Do not use this method if you have configured the device to continuously acquire data samples or to acquire multiple records.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read_iq_single_record_complex_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.read_iq_single_record_complex_f64`

        Args:
            timeout (float): Specifies in seconds the time allotted for the method to complete before returning a timeout error. A value of  specifies the method waits until all data is available.

            data_array_size (int): Specifies the size of the array for the DATA parameter. The array needs to be at least as large as the number of samples configured in the configure_number_of_samples method.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            data (ni_complex_number_f64): Returns the acquired waveform. Allocate an NIComplexNumber array at least as large as the number of samples configured in the configure_number_of_samples method.

            wfm_info (niRFSA_wfmInfo): Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read.

                                        The following list provides more information about each of these properties:

                                        - **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.

                                        ----

                                        The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.

                                        ----

                                        - **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.

                                        ----


                                        The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.

                                        ----

                                        - **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.
                                        - **actual samples read** Returns an integer representing the number of samples in the waveform.
                                        - **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.
                                        - **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.

        '''
        data, wfm_info = self._interpreter.read_iq_single_record_complex_f64(self._repeated_capability, timeout, data_array_size)
        return data, wfm_info

    @ivi_synchronized
    def read_power_spectrum_f32(self, timeout, data_array_size):
        r'''read_power_spectrum_f32

        Initiates a spectrum acquisition and returns power spectrum data.

                        ----
                        **Note**
                         Under certain configurations, negative infinity is returned from this VI. If the Reference Level is very high and if the Signal Bandwidth is comparatively less, the ADC returns zero, which equates to negative infinity in dBm. This is expected behavior.

                        ----

                        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read_power_spectrum_f32`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.read_power_spectrum_f32`

        Args:
            timeout (float): Specifies the time, in seconds, allotted for the method to complete before returning a timeout error. A value of specifies the method waits until all data is available.

            data_array_size (int): Specifies the size of the array that is returned by the **POWER_SPECTRUM_DATA** parameter. Use the get_number_of_spectral_lines method to obtain the array size to allocate. The array must be at least as large as the number of spectral lines that NI-RFSA computes for the power spectrum.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            power_spectrum_data (array.array("f")): Returns power spectrum data. Allocate an array as large as **DATA_ARRAY_SIZE**.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            spectrum_info (niRFSA_spectrumInfo): Returns additional information about the **POWER_SPECTRUM_DATA** array. This information includes the frequency, in hertz (Hz), corresponding to the first element in the array, the frequency increment, in Hz, between adjacent array elements, and the number of spectral lines the method returned.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        power_spectrum_data, spectrum_info = self._interpreter.read_power_spectrum_f32(self._repeated_capability, timeout, data_array_size)
        return power_spectrum_data, spectrum_info

    @ivi_synchronized
    def read_power_spectrum_f64(self, timeout, data_array_size):
        r'''read_power_spectrum_f64

        Initiates a spectrum acquisition and returns power spectrum data.

                        ----
                        **Note**
                         Under certain configurations, negative infinity is returned from this VI. If the Reference Level is very high and if the Signal Bandwidth is comparatively less, the ADC returns zero, which equates to negative infinity in dBm. This is expected behavior.

                        ----

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read_power_spectrum_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.read_power_spectrum_f64`

        Args:
            timeout (float): Specifies the time, in seconds, allotted for the method to complete before returning a timeout error. A value of specifies the method waits until all data is available.

            data_array_size (int): Specifies the size of the array that is returned by the **POWER_SPECTRUM_DATA** parameter. Use the get_number_of_spectral_lines method to obtain the array size to allocate. The array must be at least as large as the number of spectral lines that NI-RFSA computes for the power spectrum.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            power_spectrum_data (array.array("d")): Returns power spectrum data. Allocate an array as large as **DATA_ARRAY_SIZE**.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            spectrum_info (niRFSA_spectrumInfo): Returns additional information about the **POWER_SPECTRUM_DATA** array. This information includes the frequency, in hertz (Hz), corresponding to the first element in the array, the frequency increment, in Hz, between adjacent array elements, and the number of spectral lines the method returned.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        power_spectrum_data, spectrum_info = self._interpreter.read_power_spectrum_f64(self._repeated_capability, timeout, data_array_size)
        return power_spectrum_data, spectrum_info

    @ivi_synchronized
    def reset_attribute(self, attribute_id):
        r'''reset_attribute

        Resets the property to its default value.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].reset_attribute`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.reset_attribute`

        Args:
            attribute_id (int): Pass the ID of a property.

        '''
        self._interpreter.reset_attribute(self._repeated_capability, attribute_id)

    @ivi_synchronized
    def save_configurations_to_file(self, file_path):
        r'''save_configurations_to_file

        Saves the configurations of the session to the specified file.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].save_configurations_to_file`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.save_configurations_to_file`

        Args:
            file_path (str): Specifies the absolute path of the file to which the NI-RFSA saves the configurations.

        '''
        self._interpreter.save_configurations_to_file(self._repeated_capability, file_path)

    @ivi_synchronized
    def set_attribute_vi_boolean(self, attribute_id, value):
        r'''set_attribute_vi_boolean

        Sets the value of a ViBoolean property.

                        Use this low-level method to set the values of inherent IVI properties and instrument-specific properties.

                        NI-RFSA contains high-level methods that set most of the instrument properties. NI recommends you use the high-level methods as much as possible. High-level methods handle order dependencies and multithread locking for you.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.set_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.

            value (bool): Pass the value to which you want to set the property.

                                        ----

                                        Some of the values might not be valid depending on the current state of the instrument session.

                                        ----

        '''
        self._interpreter.set_attribute_vi_boolean(self._repeated_capability, attribute_id, value)

    @ivi_synchronized
    def set_attribute_vi_int32(self, attribute_id, value):
        r'''set_attribute_vi_int32

        Sets the value of a ViInt32 property.

                        Use this low-level method to set the values of inherent IVI properties and instrument-specific properties.

                        NI-RFSA contains high-level methods that set most of the instrument properties. NI recommends you use the high-level methods as much as possible. High-level methods handle order dependencies and multithread locking for you.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.set_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.

            value (int): Pass the value to which you want to set the property.

                                        ----

                                        Some of the values might not be valid depending on the current state of the instrument session.

                                        ----

        '''
        self._interpreter.set_attribute_vi_int32(self._repeated_capability, attribute_id, value)

    @ivi_synchronized
    def set_attribute_vi_int64(self, attribute_id, value):
        r'''set_attribute_vi_int64

        Sets the value of a ViInt64 property.

                        Use this low-level method to set the values of inherent IVI properties and instrument-specific properties.

                        NI-RFSA contains high-level methods that set most of the instrument properties. NI recommends you use the high-level methods as much as possible. High-level methods handle order dependencies and multithread locking for you.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.set_attribute_vi_int64`

        Args:
            attribute_id (int): Pass the ID of a property.

            value (int): Pass the value to which you want to set the property.

                                        ----

                                        Some of the values might not be valid depending on the current state of the instrument session.

                                        ----

        '''
        self._interpreter.set_attribute_vi_int64(self._repeated_capability, attribute_id, value)

    @ivi_synchronized
    def set_attribute_vi_real64(self, attribute_id, value):
        r'''set_attribute_vi_real64

        Sets the value of a ViReal64 property.

                        Use this low-level method to set the values of inherent IVI properties, and instrument-specific properties.

                        NI-RFSA contains high-level methods that set most of the instrument properties. NI recommends you use the high-level methods as much as possible. High-level methods handle order dependencies and multithread-locking for you.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.set_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.

            value (float): Pass the value to which you want to set the property.

                                        ----

                                        Some of the values might not be valid depending on the current state of the instrument session.

                                        ----

        '''
        self._interpreter.set_attribute_vi_real64(self._repeated_capability, attribute_id, value)

    @ivi_synchronized
    def set_attribute_vi_session(self, attribute_id):
        r'''set_attribute_vi_session

        Sets the value of a ViSession property.

                        Use this low-level method to set the values of inherent IVI properties and instrument-specific properties.

                        NI-RFSA contains high-level methods that set most of the instrument properties. NI recommends you use the high-level methods as much as possible. High-level methods handle order dependencies and multithread locking for you.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].set_attribute_vi_session`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.set_attribute_vi_session`

        Args:
            attribute_id (int): Pass the ID of a property.

        '''
        self._interpreter.set_attribute_vi_session(self._repeated_capability, attribute_id)

    @ivi_synchronized
    def set_attribute_vi_string(self, attribute_id, value):
        r'''set_attribute_vi_string

        Sets the value of a ViString property.

                        Use this low-level method to set the values of inherent IVI properties and instrument-specific properties.

                        NI-RFSA contains high-level methods that set most of the instrument properties. NI recommends you use the high-level methods as much as possible. High-level methods handle order dependencies and multithread locking for you.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

        Example: :py:meth:`my_session.set_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.

            value (str): Pass the value to which you want to set the property.

                                        ----

                                        Some of the values might not be valid depending on the current state of the instrument session.

                                        ----

        '''
        self._interpreter.set_attribute_vi_string(self._repeated_capability, attribute_id, value)


class Session(_SessionBase):
    '''An NI-RFSA session to the NI-RFSA driver'''

    def __init__(self, resource_name, id_query, reset, options={}, *, grpc_options=None):
        r'''An NI-RFSA session to the NI-RFSA driver

        Creates a new session for the device.

                        This method sets the initial value of certain properties and sends initialization commands to reset all hardware modules to a known state necessary for NI-RFSA operation.

                        To create a new session, pass the downconverter resource name for the RF vector signal analyzer to the **resource name** parameter.

                        You can access the device session this VI creates using the NI-RFSA Soft Front Panel (SFP). Accessing the device session with the SFP can help you debug your code. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about accessing your session with the SFP.

                        ----
                        **Note**
                        Before initializing your device, you must first associate the modules that comprise your device in MAX. After associating the modules, pass the resource name of the device to this method to initialize all the modules. Refer to `Associating NI-RFSA Modules <https://www.ni.com/docs/en-US/bundle/ni-rfsa-max/page/maxrfsa/mi_rf_associating.html>`_ for information about MAX association.

                        ----

                        ----
                        **Note**
                        For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending *ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.

                        ----

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_

        Args:
            resource_name (str): Specifies the resource name of the device to initialize.

                                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.

                                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.

            id_query (bool): Specifies whether NI-RFSA performs an ID query. When you perform an ID query, NI-RFSA verifies the device you initialize is supported.

                                        | Value               |  Description                                               |
                                        |:--------------|:------------------------------------------------|
                                        | True (Yes) | Perform an ID query. This value is the default. |
                                        | False (No) | Do not perform an ID query.                     |

            reset (bool): Specifies whether the NI-RFSA device is reset during the initialization procedure.

                                        | Value              |  Description                                                   |
                                        |:--------------|:----------------------------------------------------|
                                        | True (Yes) | The device is reset.                                |
                                        | False (No) | The device is not reset. This value is the default. |

            options (str): Specifies the initial value of certain properties for the session. The
                syntax for **options** is a dictionary of properties with an assigned
                value. For example:

                { 'simulate': False }

                You do not have to specify a value for all the properties. If you do not
                specify a value for a property, the default value is used.

                Advanced Example:
                { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

                +-------------------------+---------+
                | Property                | Default |
                +=========================+=========+
                | range_check             | True    |
                +-------------------------+---------+
                | query_instrument_status | False   |
                +-------------------------+---------+
                | cache                   | True    |
                +-------------------------+---------+
                | simulate                | False   |
                +-------------------------+---------+
                | record_value_coersions  | False   |
                +-------------------------+---------+
                | driver_setup            | {}      |
                +-------------------------+---------+

            grpc_options (nirfsa.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (nirfsa.Session): A session object representing the device.

        '''
        if grpc_options:
            import nirfsa._grpc_stub_interpreter as _grpc_stub_interpreter
            interpreter = _grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        else:
            interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')

        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            interpreter=interpreter,
            freeze_it=False,
            all_channels_in_session=None
        )

        # Call specified init function
        # Note that _interpreter default-initializes the session handle in its constructor, so that
        # if init_with_options fails, the error handler can reference it.
        # And then here, once init_with_options succeeds, we call set_session_handle
        # with the actual session handle.
        self._interpreter.set_session_handle(self.init_with_options(resource_name, id_query, reset, options))

        # NI-TClk does not work over NI gRPC Device Server
        if not grpc_options:
            self.tclk = nitclk.SessionReference(self._interpreter.get_session_handle())

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("id_query=" + pp.pformat(id_query))
        param_list.append("reset=" + pp.pformat(reset))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle is set
        try:
            self._all_channels_in_session = self.get_channel_names(range(self.channel_count))
        except AttributeError:
            self._all_channels_in_session = None

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._interpreter._close_on_exit:
            self.close()

    def initiate(self):
        '''initiate

        Commits settings to hardware, waits for hardware settling, and starts an acquisition.

                        You can use this method in conjunction with one of the niRFSA fetch I/Q methods to retrieve acquired I/Q data, or you can use the read_iq_single_record_complex_f64 method to both initiate the acquisition and retrieve I/Q data at one time.

                        ----
                        **Note**
                        If you are using external digitizer mode, this method commits settings and waits for settling, but it does not start an acquisition. Notice that using the commit method on its own commits settings to hardware, but the device does not wait for hardware settling.

                        ----

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

                        `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

                        `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/hardware-state-diagram.html>`_

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Acquisition(self)

    def close(self):
        '''close

        Closes the session to the device.

                        If you close a session that has Soft Front Panel (SFP) session access enabled, any application connected to the shared device session is no longer usable. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about using SFP session access.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Stops an acquisition previously started with the initiate method or the read_power_spectrum_f64 method.

                        You can also use the abort method to stop a self-calibration. Calling this method is optional, unless you want to stop an acquisition before it is complete or you are continuously acquiring data.

                        You can stop the following kinds of acquisitions:

                        - Triggered spectrum acquisitions that have not yet been triggered
                        - Multispan acquisitions in progress
                        - Average spectrum acquisitions in progress
                        - Single-record spectrum acquisitions in progress
                        - Streaming in progress

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
        '''
        self._interpreter.abort()

    @ivi_synchronized
    def change_ext_cal_password(self, old_password, new_password):
        r'''change_ext_cal_password

        Changes the password that is required to initialize an external calibration session.

                        **Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            old_password (str): Specifies the old (current) external calibration password.

                                        The maximum length of the password varies by device.

            new_password (str): Specifies the new (desired) external calibration password.

                                        The maximum length of the password varies by device.

        '''
        self._interpreter.change_ext_cal_password(old_password, new_password)

    @ivi_synchronized
    def check_acquisition_status(self):
        r'''check_acquisition_status

        Checks the status of the acquisition.

                        Use this method to check for any errors that may occur during signal acquisition or to check whether the device has completed the acquisition operation.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/hardware-state-diagram.html>`_

        Returns:
            is_done (bool): Returns signal acquisition status.

                                        |Value          |Description                                     |
                                        |:---------|:------------------------------------|
                                        | True  | Signal acquisition is complete.     |
                                        | False | Signal acquisition is not complete. |

        '''
        is_done = self._interpreter.check_acquisition_status()
        return is_done

    @ivi_synchronized
    def clear_error(self):
        r'''clear_error

        Clears the error information associated with the session.

                        If you pass VI_NULL for the VI parameter, this method clears the error information for the current execution thread.

                        ----
                        **Note**
                        The _get_error method clears the error information after it is retrieved. A call to the clear_error method is necessary only when a call to the _get_error method is not used to retrieve error information.

                        ----

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5840

        Note:
        One or more of the referenced properties are not in the Python API for this driver.
        '''
        self._interpreter.clear_error()

    @ivi_synchronized
    def clear_self_calibrate_range(self):
        r'''clear_self_calibrate_range

        Clears the data obtained from the self_calibrate_range method.

                        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842
        '''
        self._interpreter.clear_self_calibrate_range()

    @ivi_synchronized
    def close(self):
        r'''close

        Closes the session to the device.

                        If you close a session that has Soft Front Panel (SFP) session access enabled, any application connected to the shared device session is no longer usable. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about using SFP session access.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
        '''
        self._interpreter.close()

    @ivi_synchronized
    def close_calibration_step(self):
        r'''close_calibration_step

        Closes the current calibration step.

                        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698
        '''
        self._interpreter.close_calibration_step()

    @ivi_synchronized
    def close_ext_cal(self, action):
        r'''close_ext_cal

        Closes an NI-RFSA external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM.

                        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            action (int): Specifies how to use the calibration values from this session as the session is closed.

                                        |Value                           |Description                                                                         |
                                        |:--------------------------|:------------------------------------------------------------------------|
                                        | Action.ABORT  | The old calibration constants are kept, and the new ones are discarded. |
                                        | Action.COMMIT | The new calibration constants are stored in the EEPROM.                 |

        '''
        self._interpreter.close_ext_cal(action)

    @ivi_synchronized
    def close_external_alignment(self, action):
        r'''close_external_alignment

        Closes an NI-RFSA external alignment session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM.

                        **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

        Args:
            action (int): Specifies how to use the alignment values from this session as the session is closed.

                                        |Value                           |Description                                                                       |
                                        |:--------------------------|:----------------------------------------------------------------------|
                                        | Action.ABORT  | The old alignment constants are kept, and the new ones are discarded. |
                                        |  Action.COMMIT| The new alignment constants are stored in the EEPROM.                 |

        '''
        self._interpreter.close_external_alignment(action)

    @ivi_synchronized
    def close_external_alignment_step(self):
        r'''close_external_alignment_step

        Closes an EEPROM-specific external alignment step.

                        **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)
        '''
        self._interpreter.close_external_alignment_step()

    @ivi_synchronized
    def commit(self):
        r'''commit

        Commits settings to hardware.

                        Calling this method is optional. Settings are automatically committed to hardware when you call the initiate method, the read_iq_single_record_complex_f64 method, or the read_power_spectrum_f64 method.

                        ----
                        **Note**
                        This method does not wait for settling time, unlike the initiate method.

                        ----

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/hardware-state-diagram.html>`_
        '''
        self._interpreter.commit()

    @ivi_synchronized
    def configure_acquisition_type(self, acquisition_type):
        r'''configure_acquisition_type

        Configures whether the session acquires I/Q data or computes a power spectrum over the specified frequency range.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        Args:
            acquisition_type (int): Configures the type of acquisition.

                                        | Value                    | Description                                                                       |
                                        |:--------------------|:-----------------------------------------------------------------------|
                                        | AcquisitionType.IQ       | Configures the driver for I/Q acquisitions. This value is the default. |
                                        | AcquisitionType.SPECTRUM | Configures the driver for spectrum acquisitions.                       |

        '''
        self._interpreter.configure_acquisition_type(acquisition_type)

    @ivi_synchronized
    def configure_deembedding_table_interpolation_linear(self, port, table_name, format):
        r'''configure_deembedding_table_interpolation_linear

        Selects the linear interpolation method.

                        If the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

                        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

            format (int): Specifies the format of parameters to interpolate.

                                        %enum_table{format}

        '''
        self._interpreter.configure_deembedding_table_interpolation_linear(port, table_name, format)

    @ivi_synchronized
    def configure_deembedding_table_interpolation_nearest(self, port, table_name):
        r'''configure_deembedding_table_interpolation_nearest

        Selects the nearest interpolation method.

                        NI-RFSA uses the parameters of the table nearest to the carrier frequency for de-embedding.

                        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

        '''
        self._interpreter.configure_deembedding_table_interpolation_nearest(port, table_name)

    @ivi_synchronized
    def configure_deembedding_table_interpolation_spline(self, port, table_name):
        r'''configure_deembedding_table_interpolation_spline

        Selects the spline interpolation method.

                        If the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

                        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

        '''
        self._interpreter.configure_deembedding_table_interpolation_spline(port, table_name)

    @ivi_synchronized
    def configure_digital_edge_advance_trigger(self, source, edge):
        r'''configure_digital_edge_advance_trigger

        Configures the device to wait for a digital edge Advance Trigger.

                        The Advance Trigger indicates where a new record begins.

                        ----
                        **Note**
                         This method is not supported if you set the **acquisitionType** parameter to AcquisitionType.SPECTRUM using the configure_acquisition_type method or if you set the acquisition_type property to AcquisitionType.SPECTRUM.

                        ----

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        Args:
            source (str): Specifies the source of the digital edge for the Advance Trigger.

                                        | Value                                           | Description                                                                                                                                                                                                                |
                                        |:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | NIRFSA_VAL_PFI0_STR ('PFI0')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                            |
                                        | NIRFSA_VAL_PFI1_STR ('PFI1')               | The trigger is received on PFI 1.                                                                                                                                                                              |
                                        | NIRFSA_VAL_PXI_TRIG0_STR ('PXI_Trig0')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG1_STR ('PXI_Trig1')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG2_STR ('PXI_Trig2')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG3_STR ('PXI_Trig3')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG4_STR ('PXI_Trig4')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG5_STR ('PXI_Trig5')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG6_STR ('PXI_Trig6')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG7_STR ('PXI_Trig7')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_STAR_STR ('PXI_STAR')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                             |
                                        | OutputTerm.PXIE_DSTARB ('PXIE_DSTARB') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |
                                        | OutputTerm.TIMER_EVENT ('TimerEvent')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |
                                        | NIRFSA_VAL_DIO_PFI0_STR ('PFI0')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI1_STR('PFI1')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI2_STR ('PFI2')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI3_STR ('PFI3')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI4_STR ('PFI4')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI5_STR ('PFI5')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI6_STR ('PFI6')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI7_STR ('PFI7')               | The trigger is received on PFI 7 of the DIO Terminal. |

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            edge (int): Specifies the trigger edge to detect. The default value is NIRFSA_VAL_RISING_EDGE.

                                        | Value                              | Description                                |
                                        |:------------------------------|:--------------------------------|
                                        | NIRFSA_VAL_RISING_EDGE (900)  | NI-RFSA detects a rising edge.  |
                                        | NIRFSA_VAL_FALLING_EDGE (901) | NI-RFSA detects a falling edge. |

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        self._interpreter.configure_digital_edge_advance_trigger(source, edge)

    @ivi_synchronized
    def configure_digital_edge_ref_trigger(self, source, edge, pretrigger_samples):
        r'''configure_digital_edge_ref_trigger

        Configures the device to wait for a digital edge Reference Trigger to mark a reference point within the record.

                        You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

                        ----
                        **Note**
                         The PXIe-5644/5645/5646 does not support the NI-TClk API.

                        ----

                        ----
                        **Note**
                         This method is not supported if you set the **acquisitionType** parameter to AcquisitionType.SPECTRUM using the configure_acquisition_type method or if you set the acquisition_type property to AcquisitionType.SPECTRUM.

                        ----

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        Args:
            source (str): Specifies the source of the digital edge for the Reference trigger.

                                        |Value                                            |Description                                                                                                                                                                                                                               |
                                        |:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | NIRFSA_VAL_PFI0_STR ('PFI0')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                                           |
                                        | NIRFSA_VAL_PFI1_STR ('PFI1')               | The trigger is received on PFI 1.                                                                                                                                                                                             |
                                        | NIRFSA_VAL_PXI_TRIG0_STR ('PXI_Trig0')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                                |
                                        | NIRFSA_VAL_PXI_TRIG1_STR ('PXI_Trig1')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                                |
                                        | NIRFSA_VAL_PXI_TRIG2_STR ('PXI_Trig2')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                                |
                                        | NIRFSA_VAL_PXI_TRIG3_STR ('PXI_Trig3')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                                |
                                        | NIRFSA_VAL_PXI_TRIG4_STR ('PXI_Trig4')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                                |
                                        | NIRFSA_VAL_PXI_TRIG5_STR ('PXI_Trig5')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                                |
                                        | NIRFSA_VAL_PXI_TRIG6_STR ('PXI_Trig6')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                                |
                                        | NIRFSA_VAL_PXI_TRIG7_STR ('PXI_Trig7')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                                |
                                        | NIRFSA_VAL_PXI_STAR_STR ('PXI_STAR')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                                            |
                                        | OutputTerm.PXIE_DSTARB ('PXIE_DSTARB') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |
                                        | OutputTerm.TIMER_EVENT ('TimerEvent')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |
                                        | NIRFSA_VAL_DIO_PFI0_STR ('PFI0')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI1_STR('PFI1')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI2_STR ('PFI2')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI3_STR ('PFI3')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI4_STR ('PFI4')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI5_STR ('PFI5')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI6_STR ('PFI6')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI7_STR ('PFI7')               | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                          |

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            edge (int): Specifies the trigger edge to detect. The default value is NIRFSA_VAL_RISING_EDGE.

                                        |Value                               |Description                                 |
                                        |:------------------------------|:--------------------------------|
                                        | NIRFSA_VAL_RISING_EDGE (900)  | NI-RFSA detects a rising edge.  |
                                        | NIRFSA_VAL_FALLING_EDGE (901) | NI-RFSA detects a falling edge. |

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            pretrigger_samples (int): Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.

        '''
        self._interpreter.configure_digital_edge_ref_trigger(source, edge, pretrigger_samples)

    @ivi_synchronized
    def configure_digital_edge_start_trigger(self, source, edge):
        r'''configure_digital_edge_start_trigger

        Configures the device to wait for a digital edge Start Trigger at the beginning of the acquisition.

                        You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

                        ----
                        **Note**
                         The PXIe-5644/5645/5646 does not support the NI-TClk API.

                        ----

                        ----
                        **Note**
                         This method is not supported if you set the **acquisitionType** parameter to AcquisitionType.SPECTRUM using the configure_acquisition_type method or if you set the acquisition_type property to AcquisitionType.SPECTRUM.

                        ----

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        Args:
            source (str): Specifies the source of the digital edge for the Start Trigger.

                                        | Value                                           | Description                                                                                                                                                                                                               |
                                        |:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | NIRFSA_VAL_PFI0_STR ('PFI0')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                            |
                                        | NIRFSA_VAL_PFI1_STR ('PFI1')               | The trigger is received on PFI 1.                                                                                                                                                                              |
                                        | NIRFSA_VAL_PXI_TRIG0_STR ('PXI_Trig0')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG1_STR ('PXI_Trig1')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG2_STR ('PXI_Trig2')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG3_STR ('PXI_Trig3')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG4_STR ('PXI_Trig4')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG5_STR ('PXI_Trig5')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG6_STR ('PXI_Trig6')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_TRIG7_STR ('PXI_Trig7')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                 |
                                        | NIRFSA_VAL_PXI_STAR_STR ('PXI_STAR')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                             |
                                        | OutputTerm.PXIE_DSTARB ('PXIE_DSTARB') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |
                                        | OutputTerm.TIMER_EVENT ('TimerEvent')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |
                                        | NIRFSA_VAL_DIO_PFI0_STR ('PFI1')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI1_STR('PFI2')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI2_STR ('PFI3')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI3_STR ('PFI4')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI4_STR ('PFI5')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI5_STR ('PFI6')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI6_STR ('PFI7')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI7_STR ('PFI8')               | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                          |

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            edge (int): Specifies the trigger edge to detect. The default value is NIRFSA_VAL_RISING_EDGE.

                                        | Value                              | Description                                |
                                        |:------------------------------|:--------------------------------|
                                        | NIRFSA_VAL_RISING_EDGE (900)  | NI-RFSA detects a rising edge.  |
                                        | NIRFSA_VAL_FALLING_EDGE (901) | NI-RFSA detects a falling edge. |

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        self._interpreter.configure_digital_edge_start_trigger(source, edge)

    @ivi_synchronized
    def configure_iq_power_edge_ref_trigger(self, source, level, slope, pretrigger_samples):
        r'''configure_iq_power_edge_ref_trigger

        Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

                        To trigger on burst signals, add a minimum quiet time, configured with the ref_trigger_minimum_quiet_time property, to ensure the trigger does not occur in the middle of a burst if the acquisition starts while a burst is being generated. The quiet time should be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

                        You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

                        ----
                        **Note**
                         This method is not supported if you set the **acquisitionType** parameter to AcquisitionType.SPECTRUM using the configure_acquisition_type method or if you set the acquisition_type property to AcquisitionType.SPECTRUM.

                        ----

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        Args:
            source (str): Specifies the source of the RF signal for the power edge Reference trigger. The only supported value is "0".

            level (float): Specifies the threshold, in dBm, above or below which the device triggers.

            slope (int): Specifies whether the device detects a positive or negative slope on the trigger signal. The default value is RefTrigIqPwrEdgeSlope.RISING.

                                        | Value                                | Description                                                |
                                        |:--------------------------------|:-------------------------------------------------|
                                        | RefTrigIqPwrEdgeSlope.RISING (1000)  | NI-RFSA detects a rising edge (positive slope).  |
                                        | RefTrigIqPwrEdgeSlope.FALLING (1001) | NI-RFSA detects a falling edge (negative slope). |

            pretrigger_samples (int): Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.

        '''
        self._interpreter.configure_iq_power_edge_ref_trigger(source, level, slope, pretrigger_samples)

    @ivi_synchronized
    def configure_pxi_chassis_clk10(self, pxi_clk10_source):
        r'''configure_pxi_chassis_clk10

        Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane.

                        This option can be configured only when the PXI-5600 is installed in the Star Trigger Controller Slot, also known as the System Timing Slot, of the PXI chassis.

                        **Supported Devices**: PXI-5600 (external digitizer mode), PXI-5661

                        **Related Topics**

                        `System Reference Clock <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/system-reference-clock.html>`_

        Args:
            pxi_clk10_source (str): Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. This option can only be configured when the PXI-5600 is in Slot 2 of the PXI chassis.

                                        | Value                                              | Description                                                                                                                                                                                                                                                |
                                        |:----------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | NIRFSA_VAL_NONE_STR ('None')                  | The device does not drive the PXI 10 MHz backplane Reference Clock.                                                                                                                                                                             |
                                        | NIRFSA_VAL_ONBOARD_CLOCK_STR ('OnboardClock') | The device drives the PXI 10 MHz backplane Reference Clock with the PXI-5600 onboard clock. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O connector on the PXI-5600 front panel to use this option.                           |
                                        | NIRFSA_VAL_REF_IN_STR ('RefIn')               | The device drives the PXI 10 MHz backplane Reference Clock with the reference source attached to the PXI-5600 REF IN connector. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O on the PXI-5600 front panel to use this option. |

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        self._interpreter.configure_pxi_chassis_clk10(pxi_clk10_source)

    @ivi_synchronized
    def configure_ref_clock(self, clock_source, ref_clock_rate):
        r'''configure_ref_clock

        Configures the NI-RFSA device Reference Clock.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `PXI-5661 Reference Clock <https://www.ni.com/docs/en-US/bundle/pxi-5661-feature/page/reference-clock.html>`_

                        `PXIe-5663 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/timing-configurations.html>`_

                        `PXIe-5665 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/timing-configurations.html>`_

                        `PXIe-5667 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/timing-configurations.html>`_

                        `PXIe-5668 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/timing-configurations.html>`_

                        `PXIe-5830 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/timing-configurations.html>`_

                        `PXIe-5831 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/timing-configurations.html>`_

        Args:
            clock_source (str): specifies the source of the Reference Clock signal.
                                        | Clock Source          | Description |
                                        |-----------------------|-------------|
                                        | **Onboard Clock (default)** | Uses the onboard Reference Clock as the clock source. <br/>**PXIe-5830/5831/5832**-<br>- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT. <br>- PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br/>**PXIe-5831 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. <br/>**PXIe-5841 with PXIe-5655**-<br>- Lock to PXIe-5655 onboard clock. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. <br/>**PXIe-5842**-<br>- Lock to PXIe-5655 onboard clock. Use cables as shown in the Getting Started Guide. |
                                        | **RefIn** | Uses the signal at the front panel REF IN connector. <br/>**PXIe-5830/5831/5832**-<br>- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT; lock external signal to PXIe-3621 REF IN. <br>- PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT; lock external signal to PXIe-3622 REF IN. <br>- PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT; lock external signal to PXIe-3623 REF IN. <br/>**PXIe-5831 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. <br>- Lock external signal to PXIe-5653 REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. <br>- Lock external signal to PXIe-5653 REF IN. <br/>**PXIe-5841 with PXIe-5655**-<br>- Lock to signal at REF IN on PXIe-5655. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. <br/>**PXIe-5842**-<br>- Lock to signal at REF IN on PXIe-5655. Use cables as shown in the Getting Started Guide. |
                                        | **PXI Clock** | Uses the PXI_CLK signal present on the PXI backplane. |
                                        | **PXI_ClkMaster** | Valid only for PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653. <br/>**PXIe-5831 with PXIe-5653**-<br>- NI-RFSG configures PXIe-5653 to export Reference Clock. <br>- Configures PXIe-5820 and PXIe-3622 to use PXI_Clk. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- NI-RFSG configures PXIe-5653 to export Reference Clock. <br>- Configures PXIe-5820 and PXIe-3623 to use PXI_Clk. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. |

            ref_clock_rate (float): specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. This parameter is only valid when the **ref clock source** parameter is set to **RefIn**. The default value is Auto (-1.0), which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. Refer to the Reference Clock Rate property for possible values.

        '''
        self._interpreter.configure_ref_clock(clock_source, ref_clock_rate)

    @ivi_synchronized
    def configure_software_edge_advance_trigger(self):
        r'''configure_software_edge_advance_trigger

        Configures the device to wait for a software Advance Trigger.

                        The Advance Trigger indicates where a new record begins. The device waits until you call the send_software_edge_trigger method to assert the trigger.

                        ----
                        **Note**
                         This method is not supported if you set the **acquisitionType** parameter to AcquisitionType.SPECTRUM using the configure_acquisition_type method or if you set the acquisition_type property to AcquisitionType.SPECTRUM.

                        ----

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_
        '''
        self._interpreter.configure_software_edge_advance_trigger()

    @ivi_synchronized
    def configure_software_edge_ref_trigger(self, pretrigger_samples):
        r'''configure_software_edge_ref_trigger

        Configures the device to wait for a software Reference Trigger to mark a reference point within the record.

                        The device waits until you call the send_software_edge_trigger method to assert the trigger.

                        You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

                        ----
                        **Note**
                         The PXIe-5644/5645/5646 does not support the NI-TClk API.

                        ----

                        ----
                        **Note**
                         This method is not supported if you set the **acquisitionType** parameter to AcquisitionType.SPECTRUM using the configure_acquisition_type method or if you set the acquisition_type property to AcquisitionType.SPECTRUM.

                        ----

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        Args:
            pretrigger_samples (int): Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.

        '''
        self._interpreter.configure_software_edge_ref_trigger(pretrigger_samples)

    @ivi_synchronized
    def configure_software_edge_start_trigger(self):
        r'''configure_software_edge_start_trigger

        Configures the device to wait for a software Start Trigger at the beginning of the acquisition.

                        The device waits until you call the send_software_edge_trigger method to assert the trigger.

                        You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

                        ----
                        **Note**
                         The PXIe-5644/5645/5646 does not support the NI-TClk API.

                        ----

                        ----
                        **Note**
                         This method is not supported if you set the **acquisitionType** parameter to AcquisitionType.SPECTRUM using the configure_acquisition_type method or if you set the acquisition_type property to AcquisitionType.SPECTRUM.

                        ----

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_
        '''
        self._interpreter.configure_software_edge_start_trigger()

    @ivi_synchronized
    def create_configuration_list(self, list_name, number_of_list_attributes, set_as_active_list):
        r'''create_configuration_list

        Creates an empty configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_.

                        After a configuration list is created, enable the list using the **setAsActiveList** parameter. Call the create_configuration_list_step method to add steps to the active configuration list.

                        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

                        **Related Topics**

                        `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

        Args:
            list_name (str): Specifies the name of the configuration list. This string may not contain spaces, special characters, or punctuation marks.

            number_of_list_attributes (int): Specifies the number of configuration list properties to set.

            set_as_active_list (bool): Sets this list as the active configuration list when this parameter is set to True.


        Returns:
            list_attribute_i_ds (int): Specifies the properties that you intend to change between configuration list steps. Calling the create_configuration_list method allocates space for each of the configuration list properties. When you use an NI-RFSG Set property method to set one of the properties in the configuration list, that property is set for one of the configuration list steps. Use the active_configuration_list_step property to specify which configuration list step to configure.

                                        You can include the following properties in your configuration list based on your device:

                                        | Property                                                                                              | PXIe-5663E | PXIe-5665 | PXIe-5667 | PXIe-5644/5646 | PXIe-5645 | PXIe-5820 | PXIe-5830/5831/5832 | PXIe-5840/5841 | PXIe-5841 with PXIe-5655 | PXIe-5842 |
                                        |:-------------------------------------------------------------------------------------------------------|:-----------|:----------|:----------|:----------------|:----------|:----------|:----------------------|:---------------|:--------------------------|:-----------|
                                        | channel_coupling                                                                           |            |           | Supported |                |           |           |                      |                |                            |            |
                                        | device_instantaneous_bandwidth                                                             | Supported  | Supported | Supported |                |           | Supported |                      | Supported      |                            | Supported  |
                                        | downconverter_center_frequency                                                             |            |           |           |                | Supported | Supported |                      | Supported      | Supported                  | Supported  |
                                        | downconverter_frequency_offset                                                      |            |           |           |                |           | Supported |                      |                |                            |            |
                                        | downconverter_preselector_enabled                                                        | Supported  | Supported |           |                |           |           |                      | Supported      | Supported                  | Supported  |
                                        | external_gain                                                                              |            |           |           |                |           |           |                      | Supported      | Supported                  | Supported  |
                                        | frequency_settling                                                                         | Supported  | Supported | Supported | Supported       | Supported | Supported | Supported            | Supported      |                            |            |
                                        | if_filter_bandwidth                                                                        |            |           | Supported | Supported       | Supported | Supported | Supported            |                |                            | Supported  |
                                        | if_output_power_level                                                                      |            | Supported |           |                |           |           |                      | Supported      |                            |            |
                                        | if_output_power_level_offset                                                               |            | Supported |           |                |           |           |                      | Supported      |                            |            |
                                        | iq_carrier_frequency                                                                       |            | Supported |           |                |           |           |                      | Supported      |                            |            |
                                        | iq_in_port_carrier_frequency                                                               |            | Supported |           |                |           |           |                      | Supported      |                            |            |
                                        | iq_in_port_vertical_range                                                                  |            |           |           |                |           |           |                      |                | Supported                  | Supported  |
                                        | iq_power_edge_ref_trigger_level                                                            |            |           |           |                | Supported | Supported |                      |                |                            |            |
                                        | lo_source                                                                                  | Supported  | Supported | Supported | Supported       |           |           | Supported            | Supported      | Supported                  | Supported  |
                                        | if_output_power_level                                                                                | Supported  | Supported | Supported |                | Supported | Supported | Supported            |                | Supported                  | Supported  |
                                        | low_frequency_bypass_enabled                                                               |            |           |           |                |           |           | Supported            | Supported      | Supported                  | Supported  |
                                        | mechanical_attenuation                                                                     |            |           |           |                | Supported | Supported | Supported            |                |                            |            |
                                        | mechanical_attenuator_enabled                                                              |            |           |           |                |           |           |                      |                | Supported                  |            |
                                        | minimum_acpr                                                                                  |            |           |           |                |           |           |                      |                | Supported                  |            |
                                        | notch_filter_enabled                                                                       |            |           |           |                |           |           |                      | Supported      |                            | Supported  |
                                        | number_of_samples                                                                          | Supported  | Supported | Supported |                | Supported | Supported | Supported            | Supported      | Supported                  | Supported  |
                                        | osp_data_scaling_factor                                                                     | Supported  | Supported |           |                |           |           | Supported            |                |                            | Supported  |
                                        | reference_level                                                                            |            |           |           |                |           |           |                      |                |                            | Supported  |
                                        | attenuation                                                                                |            |           |           |                |           |           |                      |                |                            | Supported  |
                                        | rf_out_lo_export_enabled                                                                   |            |           |           |                |           |           |                      |                | Supported                  | Supported  |
                                        | rf_preamp_enabled                                                                          |            |           |           |                |           |           |                      |                | Supported                  | Supported  |
                                        | rf_preselector_filter                                                                      |            |           |           |                |           |           |                      |                | Supported                  | Supported  |
                                        | selected_ports                                                                              |            |           |           |                |           |           |                      |                | Supported                  | Supported  |
                                        | timer_event_interval                                                                       |            |           |           |                |           |           |                      |                | Supported                  | Supported  |

        '''
        list_attribute_i_ds = self._interpreter.create_configuration_list(list_name, number_of_list_attributes, set_as_active_list)
        return list_attribute_i_ds

    @ivi_synchronized
    def create_configuration_list_step(self, set_as_active_step):
        r'''create_configuration_list_step

        Creates a new configuration list step in the configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_ specified by the active_configuration_list property.

                        When you create a configuration list step, a new instance of each property specified by the configuration list properties is created. Configuration list properties are specified when a configuration list is created.

                        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

                        **Related Topics**

                        `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

        Args:
            set_as_active_step (bool): Sets this step as the active step for the active configuration list. The default value for this parameter is True.

                                        If you set this parameter to False, you can select the active configuration list step using the active_configuration_list_step property.

        '''
        self._interpreter.create_configuration_list_step(set_as_active_step)

    @ivi_synchronized
    def _create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation):
        r'''_create_deembedding_sparameter_table_array

        Creates an s-parameter de-embedding table for the port from the input data.

                        If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.

                        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_

                        `S-parameters <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html#GUID-0AD828DE-398A-45C6-ABBA-4208DEB7DE1B__GUID-67A69775-E4DB-4FA2-84FE-C05977ED4184>`_

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

            frequencies (numpy.array(dtype=numpy.float64)): Specifies the frequencies for the SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            sparameter_table (numpy.array(dtype=numpy.complex128)): Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.

            sparameter_orientation (int): Specifies the orientation of the data in the S2P file relative to the port on the DUT port.

                                        %enum_table{sparameter orientation}

        '''
        import numpy

        if type(frequencies) is not numpy.ndarray:
            raise TypeError('frequencies must be {0}, is {1}'.format(numpy.ndarray, type(frequencies)))
        if numpy.isfortran(frequencies) is True:
            raise TypeError('frequencies must be in C-order')
        if frequencies.dtype is not numpy.dtype('float64'):
            raise TypeError('frequencies must be numpy.ndarray of dtype=float64, is ' + str(frequencies.dtype))
        if frequencies.ndim != 1:
            raise TypeError('frequencies must be numpy.ndarray of dimension=1, is ' + str(frequencies.ndim))
        if type(sparameter_table) is not numpy.ndarray:
            raise TypeError('sparameter_table must be {0}, is {1}'.format(numpy.ndarray, type(sparameter_table)))
        if numpy.isfortran(sparameter_table) is True:
            raise TypeError('sparameter_table must be in C-order')
        if sparameter_table.dtype is not numpy.dtype('complex128'):
            raise TypeError('sparameter_table must be numpy.ndarray of dtype=complex128, is ' + str(sparameter_table.dtype))
        if sparameter_table.ndim != 3:
            raise TypeError('sparameter_table must be numpy.ndarray of dimension=3, is ' + str(sparameter_table.ndim))
        self._interpreter.create_deembedding_sparameter_table_array(port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation)

    @ivi_synchronized
    def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation):
        r'''create_deembedding_sparameter_table_s2p_file

        Creates an S-parameter de-embedding table for the port based on the specified S2P file.

                        If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.

                        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_

                        `S-parameters <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html#GUID-0AD828DE-398A-45C6-ABBA-4208DEB7DE1B__GUID-67A69775-E4DB-4FA2-84FE-C05977ED4184>`_

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

            s2p_file_path (str): Specifies the path to the S2P file that contains de-embedding information for the specified port.

            sparameter_orientation (int): Specifies the orientation of the data in the S2P file relative to the port on the DUT port.

                                       %enum_table{sparameter orientation}

        '''
        self._interpreter.create_deembedding_sparameter_table_s2p_file(port, table_name, s2p_file_path, sparameter_orientation)

    @ivi_synchronized
    def delete_all_deembedding_tables(self):
        r'''delete_all_deembedding_tables

        Deletes all configured de-embedding tables for the session.

                        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860
        '''
        self._interpreter.delete_all_deembedding_tables()

    @ivi_synchronized
    def delete_configuration_list(self, list_name):
        r'''delete_configuration_list

        Deletes a previously created configuration list and all the configuration list steps in the `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_ configuration list.

                        When a configuration list step is deleted, all the instances of the properties associated with the configuration list step are also removed. When you delete the active configuration list, NI-RFSA automatically resets the active_configuration_list property to "" (empty string), which indicates no list is active, and the active_configuration_list_step property to 0.

                        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

                        **Related Topics**

                        `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

        Args:
            list_name (str): Specifies the name of the configuration list. This string may not contain spaces, special characters, or punctuation marks.

        '''
        self._interpreter.delete_configuration_list(list_name)

    @ivi_synchronized
    def delete_deembedding_table(self, port, table_name):
        r'''delete_deembedding_table

        Deletes the selected de-embedding table for a given port.

                        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

        '''
        self._interpreter.delete_deembedding_table(port, table_name)

    @ivi_synchronized
    def disable(self):
        r'''disable

        TBD
        '''
        self._interpreter.disable()

    @ivi_synchronized
    def disable_advance_trigger(self):
        r'''disable_advance_trigger

        Configures the device to not use an Advance Trigger.

                        This method is necessary only if you configured an Advance Trigger in the past and now want to disable it.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_
        '''
        self._interpreter.disable_advance_trigger()

    @ivi_synchronized
    def disable_ref_trigger(self):
        r'''disable_ref_trigger

        Configures the device to not wait for a Reference Trigger to mark a reference point within a record.

                        This method is necessary only if you previously configured a Reference trigger in the past and now want to disable it.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_
        '''
        self._interpreter.disable_ref_trigger()

    @ivi_synchronized
    def disable_start_trigger(self):
        r'''disable_start_trigger

        Configures the device to not wait for a Start Trigger at the beginning of the acquisition.

                        This method is necessary only if you previously configured a Start Trigger in the past and now want to disable it.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_
        '''
        self._interpreter.disable_start_trigger()

    @ivi_synchronized
    def enable_session_access(self, enable):
        r'''enable_session_access

        Enables or disables SFP session access for the specified instrument.

                        SFP session access allows the NI-RFSA Soft Front Panel (SFP) to access a device with an existing open session and can help you debug your code. To enable session access, pass True to the **enabled** parameter. To disable session access, pass False to the **enabled** parameter.

                        Refer to `Configuring SFP Session Access using LabWindows/CVI or C <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/configuring_session_access_labwindows.html>`_ for more information about SFP session access.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842/5860

                        ----
                        **Note**
                        NI-RFSA does not support NI-TClk when driver session debugging is enabled.

                        ----

        Args:
            enable (bool): Enables or disables SFP session access for the specified device.

                                        | Value         | Description                         |
                                        |:---------|:-------------------------|
                                        | True  | Enables session access.  |
                                        | False | Disables session access. |

        '''
        self._interpreter.enable_session_access(enable)

    @ivi_synchronized
    def error_message(self, status_code, error_message):
        r'''error_message

        Converts a status code returned by an NI-RFSA method into a user-readable string.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5840

        Args:
            status_code (int): Passes the **status** parameter that is returned from any NI-RFSA method.

            error_message (str): Returns the user-readable message string that corresponds to the status code you specify.

                                        You must pass a ViChar array with at least 256 bytes to this parameter.

        '''
        self._interpreter.error_message(status_code, error_message)

    @ivi_synchronized
    def error_query(self):
        r'''error_query

        Reads an error code and a message from the instrument error queue.

        Returns:
            error_code (int): Passes the **status** parameter that is returned from any NI-RFSA method.

            error_message (str): Returns the user-readable message string that corresponds to the error code.

                                        You must pass a ViChar array with at least 256 bytes to this parameter.

        '''
        error_code, error_message = self._interpreter.error_query()
        return error_code, error_message

    @ivi_synchronized
    def export_signal(self, signal, signal_identifier, output_terminal):
        r'''export_signal

        Routes signals (triggers, clocks, and events) to the specified output terminal.

                        If you export a signal with this method and [commit](rfsacref.chm/cvicommit.html) the session, the signal is routed to the output terminal you specify. If you then reconfigure the signal to have a different output terminal, the previous output terminal is tri-stated when the session is next committed. If you set the **OUTPUT_TERMINAL** parameter to NIRFSA_VAL_DO_NOT_EXPORT_STR and commit, the previous output terminal is tristated.

                        Any signals, except for those exported over PXI trigger lines, that are exported within a session persist after the session closes to prevent signal glitches between sessions. PXI trigger lines are always set to tristate when a session is closed. If you wish to have the output terminal tristated when the session closes, change the **OUTPUT_TERMINAL** for the exported signal to NIRFSA_VAL_DO_NOT_EXPORT_STR, and commit the session again before closing it.

                        You can also tristate all PFI lines by setting the **resetDevice** parameter in the init method to True or by using the reset method.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Note:
        One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        Args:
            signal (int): Specifies the type of signal to route.

                                        %enum_table{signal}

            signal_identifier (str): Specifies the user-defined signal to route. Specify the signal you have implemented using FPGA extensions.

            output_terminal (str): Specifies the terminal where the signal will be exported. You can also choose not to export any signal. For the PXIe-5841 with PXIe-5655, the signal is exported to the terminal on the PXIe-5841.

                                        | Value                             | Description                                                                                                                                                                                                                                |
                                        |:-----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | NIRFSA_VAL_DO_NOT_EXPORT_STR | The signal is not exported.                                                                                                                                                                                                     |
                                        | NIRFSA_VAL_CLK_OUT_STR       | The signal is exported to the CLK OUT connector on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                       |
                                        | NIRFSA_VAL_REF_OUT_STR       | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
                                        | NIRFSA_VAL_REF_OUT2_STR          | The signal is exported to the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                                  |
                                        | NIRFSA_VAL_PFI0_STR          | The signal is exported to the PFI 0 connector.                                                                                                                                                                                  |
                                        | NIRFSA_VAL_PFI1_STR          | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.                                                                                                                                                    |
                                        | NIRFSA_VAL_PXI_TRIG0_STR     | The signal is exported to the PXI trigger line 0.                                                                                                                                                                               |
                                        | NIRFSA_VAL_PXI_TRIG1_STR     | The signal is exported to the PXI trigger line 1.                                                                                                                                                                               |
                                        | NIRFSA_VAL_PXI_TRIG2_STR     | The signal is exported to the PXI trigger line 2.                                                                                                                                                                               |
                                        | NIRFSA_VAL_PXI_TRIG3_STR     | The signal is exported to the PXI trigger line 3.                                                                                                                                                                               |
                                        | NIRFSA_VAL_PXI_TRIG4_STR     | The signal is exported to the PXI trigger line 4.                                                                                                                                                                               |
                                        | NIRFSA_VAL_PXI_TRIG5_STR     | The signal is exported to the PXI trigger line 5.                                                                                                                                                                               |
                                        | NIRFSA_VAL_PXI_TRIG6_STR     | The signal is exported to the PXI trigger line 6.                                                                                                                                                                               |
                                        | NIRFSA_VAL_PXI_TRIG7_STR     | The signal is exported to the PXI trigger line 7.                                                                                                                                                                               |
                                        | NIRFSA_VAL_PXI_STAR_STR      | The signal is exported to the PXI star trigger line.                                                                                                                                                                            |
                                        | ExportOutputTerm.PXIE_DSTARC   | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                                          |
                                        | NIRFSA_VAL_DIO_PFI0_STR ('PFI0') | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                                           |
                                        | NIRFSA_VAL_DIO_PFI1_STR ('PFI1') | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                                           |
                                        | NIRFSA_VAL_DIO_PFI2_STR ('PFI2') | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                                           |
                                        | NIRFSA_VAL_DIO_PFI3_STR ('PFI3') | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                                           |
                                        | NIRFSA_VAL_DIO_PFI4_STR ('PFI4') | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                                           |
                                        | NIRFSA_VAL_DIO_PFI5_STR ('PFI5') | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                                           |
                                        | NIRFSA_VAL_DIO_PFI6_STR ('PFI6') | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                                           |
                                        | NIRFSA_VAL_DIO_PFI7_STR ('PFI7') | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                                           |

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        self._interpreter.export_signal(signal, signal_identifier, output_terminal)

    @ivi_synchronized
    def ext_cal_store_baseline_for_self_calibration(self, password, self_calibration_step):
        r'''ext_cal_store_baseline_for_self_calibration

        Specifies the external calibration step to run and stores the associated constants in the device memory so that they can be compared with the computed constants at run time.

                        A password is required to run the method.

                        **Supported Devices**: PXIe-5603/5605/5606, PXIe-5665/5668

        Args:
            password (str): Specifies the password for the calibration session. The initial password is factory configured to NI. PASSWORD can be a maximum of ten alphanumeric characters.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            self_calibration_step (int): Specifies the step for which constants are computed.

                                        %enum_table{self calibration step}

        '''
        self._interpreter.ext_cal_store_baseline_for_self_calibration(password, self_calibration_step)

    @ivi_synchronized
    def external_alignment_adjust_preselector(self, coefficients):
        r'''external_alignment_adjust_preselector

        Stores the preselector alignment coefficients that NI-RFSA uses to compute the preselector-tuning DAC value whenever the preselector is enabled.

                        These coefficients are based on the desired center frequency for the preselector.

                        **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

        Args:
            coefficients (array.array("d")): Specifies the coefficients in the polynomial used to map the preselector center frequency to a preselector-tuning DAC value. Enter the coefficients in the array in order of highest order coefficient first (index 0) down to lowest order coefficient last.

        '''
        self._interpreter.external_alignment_adjust_preselector(coefficients)

    @ivi_synchronized
    def get_cal_user_defined_info(self):
        r'''get_cal_user_defined_info

        Returns user-defined information from the onboard EEPROM.

                        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698

        Returns:
            info (str): Returns a string containing the user-defined information.

        '''
        info = self._interpreter.get_cal_user_defined_info()
        return info

    @ivi_synchronized
    def get_cal_user_defined_info_max_size(self):
        r'''get_cal_user_defined_info_max_size

        Returns the number of characters of user-defined information that can be stored in the device onboard EEPROM.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

        Returns:
            info_size (int): Returns the number of characters of user-defined information that can be stored in the device onboard EEPROM. The maximum size of the user-defined information array is 21 characters.

        '''
        info_size = self._interpreter.get_cal_user_defined_info_max_size()
        return info_size

    @ivi_synchronized
    def get_ext_cal_last_date_and_time(self):
        r'''get_ext_cal_last_date_and_time

        Returns the date and time of the last successful external calibration.

                        The time returned is 24-hour local time, and the date is returned as integer values. For example, if the device was calibrated at 2:30 PM on December 31, 2010, this method returns 14 for the HOUR parameter, 30 for the MINUTE parameter, 12 for the MONTH parameter, 31 for the DAY parameter, and 2010 for the YEAR parameter.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Returns:
            year (int): Returns the year of the last external calibration.

            month (int): Returns the month of the last external calibration.

            day (int): Returns the day of the last external calibration.

            hour (int): Returns the hour of the last external calibration.

            minute (int): Returns the minute of the last external calibration.

        '''
        year, month, day, hour, minute = self._interpreter.get_ext_cal_last_date_and_time()
        return year, month, day, hour, minute

    @ivi_synchronized
    def get_ext_cal_last_temp(self):
        r'''get_ext_cal_last_temp

        Returns the temperature of the last successful external calibration.

                        The temperature is returned in degrees Celsius.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

        Returns:
            temperature (float): Returns the temperature, in degrees Celsius, of the last external calibration.

        '''
        temperature = self._interpreter.get_ext_cal_last_temp()
        return temperature

    @ivi_synchronized
    def get_ext_cal_recommended_interval(self):
        r'''get_ext_cal_recommended_interval

        Returns the recommended interval between external calibrations, in months.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            months (int): Returns the recommended maximum interval between external calibrations, in months.

        '''
        months = self._interpreter.get_ext_cal_recommended_interval()
        return months

    @ivi_synchronized
    def get_gain_reference_cal_baseline(self, buffer_size):
        r'''get_gain_reference_cal_baseline

        Returns the gain reference calibration constants.

                        **Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5668

        Args:
            buffer_size (int): Specifies the buffer size.


        Returns:
            gain_reference_cal_constants (array.array("d")): Returns the gain reference calibration constants.

            number_of_gain_reference_cal_constants (int): Specifies the number of elements in the **GAIN_REFERENCE_CAL_CONSTANTS** array.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        gain_reference_cal_constants, number_of_gain_reference_cal_constants = self._interpreter.get_gain_reference_cal_baseline(buffer_size)
        return gain_reference_cal_constants, number_of_gain_reference_cal_constants

    @ivi_synchronized
    def get_self_cal_last_date_and_time(self, self_calibration_step):
        r'''get_self_cal_last_date_and_time

        Returns the date and time of the last successful self-calibration.

                        The time returned is 24-hour local time, and the date is returned as integer values. For example, if the device was calibrated at 2:30 PM on December 31, 2010, this method returns 14 for the HOUR parameter, 30 for the MINUTE parameter, 12 for the MONTH parameter, 31 for the DAY parameter, and 2010 for the YEAR parameter.

                        ----
                        **Note**
                        For the PXIe-5644/5645/5646, you must select SelfCalibrationStep.IMAGE_SUPPRESSION for the **SELF_CALIBRATION_STEP** parameter.

                        ----

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            self_calibration_step (int): Specifies the self-calibration step to query for the last successful self-calibration date and time data.

                                        %enum_table{self calibration step}


        Returns:
            year (int): Returns the year of the last external calibration.

            month (int): Returns the month of the last external calibration.

            day (int): Returns the day of the last external calibration.

            hour (int): Returns the year of the last external calibration. It is expressed as an integer.

            minute (int): Returns the minute of the last external calibration.

        '''
        year, month, day, hour, minute = self._interpreter.get_self_cal_last_date_and_time(self_calibration_step)
        return year, month, day, hour, minute

    @ivi_synchronized
    def get_self_cal_last_temp(self, self_calibration_step):
        r'''get_self_cal_last_temp

        Returns the temperature, in degrees Celsius, at the last successful self-calibration.

                        ----
                        **Note**
                        For the PXIe-5644/5645/5646, you must select SelfCalibrationStep.IMAGE_SUPPRESSION for the **selfCalibrationStep** parameter.

                        ----

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860

        Args:
            self_calibration_step (int): Specifies the self-calibration step to query for the last successful self-calibration date and time data.

                                        %enum_table{self calibration step}


        Returns:
            temp (float): Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

        '''
        temp = self._interpreter.get_self_cal_last_temp(self_calibration_step)
        return temp

    @ivi_synchronized
    def get_spectral_info_for_smt(self):
        r'''get_spectral_info_for_smt

        Returns information about the power spectrum NI-RFSA computes.

                        ----
                        **Note**
                        The NI Spectral Measurements Toolkit (SMT) requires this information.

                        ----

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            spectrum_info (SmtSpectrumInfo): Returns returns properties of the computed spectrum such as spectrum type, spectrum scale (linear or logarithmic), the window type the method used to compute the spectrum, window size, and FFT size. Pass this parameter to subsequent methods that contain the **SPECTRUM_INFO** parameter.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        spectrum_info = self._interpreter.get_spectral_info_for_smt()
        return spectrum_info

    @ivi_synchronized
    def get_stream_endpoint_handle(self, stream_endpoint):
        r'''get_stream_endpoint_handle

        Returns a writer endpoint handle that you can use with NI-P2P to configure a peer-to-peer stream with the digitizer as an endpoint.

                        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Configuring An Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_

                        [Peer-to-Peer Streaming](nirfsa.chm/p2p-streaming.html)

                        [Configuring a Peer-to-Peer Stream](nirfsa.chm/configuring-p2p-stream.html)

        Args:
            stream_endpoint (str): Specifies the name of the stream resources you want to use.


        Returns:
            writer_handle (int): Returns the writer endpoint handle which you use with NI-P2P to create a stream with the digitizer as an endpoint.

        '''
        writer_handle = self._interpreter.get_stream_endpoint_handle(stream_endpoint)
        return writer_handle

    @ivi_synchronized
    def get_terminal_name(self, signal, signal_identifier):
        r'''get_terminal_name

        Returns the fully qualified name of the signal being queried.

                        Signals can be triggers, clocks, or events.

                        You can pass the **TERMINAL_NAME** parameter that is returned to the **source** parameter of a configure trigger method.

                        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            signal (int): Specifies the signal for which you want to query the terminal.

                                       %enum_table{signal}

            signal_identifier (str): Specifies a particular instance of a trigger. NI-RFSA does not support this parameter.


        Returns:
            terminal_name (str): Returns the fully qualified name of the signal being queried.

        '''
        terminal_name = self._interpreter.get_terminal_name(signal, signal_identifier)
        return terminal_name

    @ivi_synchronized
    def get_user_data(self, identifier, buffer_size):
        r'''get_user_data

        TBD

        Args:
            identifier (str):

            buffer_size (int):


        Returns:
            data (array.array("b")):

            actual_data_size (int):

        '''
        data, actual_data_size = self._interpreter.get_user_data(identifier, buffer_size)
        return data, actual_data_size

    @ivi_synchronized
    def init(self, resource_name, id_query, reset):
        r'''init

        Creates a new session for the device. This method sends initialization commands to reset all hardware modules to a known state necessary for NI-RFSA operation.

                        To create a new session, pass the downconverter resource name for the RF vector signal analyzer to the **resource name** parameter.

                        You can access the device session this method creates using the NI-RFSA Soft Front Panel (SFP). Accessing the device session with the SFP can help you debug your code. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about accessing your session with the SFP.

                        ----
                        **Note**
                        Before initializing your device, you must first associate the modules that comprise your device in MAX. After associating the modules, pass the resource name of the device to this method to initialize all the modules. Refer to `Associating NI-RFSA Modules <https://www.ni.com/docs/en-US/bundle/ni-rfsa-max/page/maxrfsa/mi_rf_associating.html>`_ for information about MAX association.

                        ----

                        ----
                        **Note**
                        For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending *ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.

                        ----

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            resource_name (str): Specifies the resource name of the device to initialize.

                                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.

                                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.

            id_query (bool): Specifies whether NI-RFSA performs an ID query. When you perform an ID query, NI-RFSA verifies the device you initialize is supported.

                                        | Value              | Description                                                |
                                        |:--------------|:------------------------------------------------|
                                        | True (Yes) | Perform an ID query. This value is the default. |
                                        | False (No) | Do not perform an ID query.                     |

            reset (bool): Specifies whether the NI-RFSA device is reset during the initialization procedure.

                                        | Value              | Description                                                    |
                                        |:--------------|:----------------------------------------------------|
                                        | True (Yes) | The device is reset.                                |
                                        | False (No) | The device is not reset. This value is the default. |


        Returns:
            vi (int): Identifies your instrument session.

        '''
        vi = self._interpreter.init(resource_name, id_query, reset)
        return vi

    @ivi_synchronized
    def init_ext_cal(self, resource_name, password, option_string):
        r'''init_ext_cal

        Creates and initializes a special NI-RFSA external calibration session.

                        The ViSession returned is an NI-RFSA session that you can use to configure the device using normal properties and methods. However, NI-RFSA sets flags that allow you to program an external calibration procedure using the calibration properties and methods.

                        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            resource_name (str): Specifies the resource name of the device to initialize.

                                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI ** topic of the *Measurement & Automation Explorer Help*.

                                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.

            password (str): Specifies the password for the calibration session. The initial password is factory configured to NI. PASSWORD can have a maximum of ten alphanumeric characters.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            option_string (str): Sets the initial value of certain options for the session.

                                        The following options are used in this parameter.

                                        - calAction:create Use this option when starting a calibration step for the first time.
                                        - calAction:append Use this option when appending data to existing calibration data.


        Returns:
            vi (int): Identifies your instrument session.

        '''
        vi = self._interpreter.init_ext_cal(resource_name, password, option_string)
        return vi

    @ivi_synchronized
    def init_with_options(self, resource_name, id_query, reset, option_string):
        r'''init_with_options

        Creates a new session for the device.

                        This method sets the initial value of certain properties and sends initialization commands to reset all hardware modules to a known state necessary for NI-RFSA operation.

                        To create a new session, pass the downconverter resource name for the RF vector signal analyzer to the **resource name** parameter.

                        You can access the device session this VI creates using the NI-RFSA Soft Front Panel (SFP). Accessing the device session with the SFP can help you debug your code. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about accessing your session with the SFP.

                        ----
                        **Note**
                        Before initializing your device, you must first associate the modules that comprise your device in MAX. After associating the modules, pass the resource name of the device to this method to initialize all the modules. Refer to `Associating NI-RFSA Modules <https://www.ni.com/docs/en-US/bundle/ni-rfsa-max/page/maxrfsa/mi_rf_associating.html>`_ for information about MAX association.

                        ----

                        ----
                        **Note**
                        For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending *ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.

                        ----

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_

        Args:
            resource_name (str): Specifies the resource name of the device to initialize.

                                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.

                                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.

            id_query (bool): Specifies whether NI-RFSA performs an ID query. When you perform an ID query, NI-RFSA verifies the device you initialize is supported.

                                        | Value               |  Description                                               |
                                        |:--------------|:------------------------------------------------|
                                        | True (Yes) | Perform an ID query. This value is the default. |
                                        | False (No) | Do not perform an ID query.                     |

            reset (bool): Specifies whether the NI-RFSA device is reset during the initialization procedure.

                                        | Value              |  Description                                                   |
                                        |:--------------|:----------------------------------------------------|
                                        | True (Yes) | The device is reset.                                |
                                        | False (No) | The device is not reset. This value is the default. |

            option_string (str): Sets the initial value of certain properties for the session. The properties shown in the following table are used in this parameter.

                                        | Name             | Property                                                                                                                                  |
                                        |:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
                                        | RangeCheck       | range_check                         |
                                        | QueryInstrStatus | query_instrument_status |
                                        | Cache            | cache                                     |
                                        | RecordCoercions  | record_coercions               |
                                        | DriverSetup      | driver_setup                       |
                                        | Simulate         | simulate                               |

                                        The format of this string is *AttributeName=Value*, where *AttributeName* is the name of the property and *Value* is the value to which the property will be set. For example, you can simulate the PXIe-5663 using the following strings:

                                        *Simulate=1, DriverSetup=Model:5663\E*.

                                        *Simulate=1, DriverSetup=Model:5601*; *Digitizer:5622; LO:5652; LOBoardType:PXIe*.

                                        To set multiple properties, separate their assignments with a comma.

                                        Refer to `Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_ for more information about the driver setup string.

                                        Note: To simulate a device using the PXIe-5622 25 MHz digitizer, set the *Digitizer* field to 5622_25MHz_DDC and the *Simulate* field to 1. You can set the *Digitizer* field to 5622_25MHz_DDC only when using the PXIe-5665.


        Returns:
            vi (int): Identifies your instrument session.

        '''
        vi = self._interpreter.init_with_options(resource_name, id_query, reset, option_string)
        return vi

    @ivi_synchronized
    def initialize_calibration_step(self, calibration_step):
        r'''initialize_calibration_step

        Initializes an EEPROM-specific calibration step.

                        **Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698

        Args:
            calibration_step (int): Specifies the calibration step to initialize.

                                       %enum_table{self calibration step}

        '''
        self._interpreter.initialize_calibration_step(calibration_step)

    @ivi_synchronized
    def initialize_external_alignment(self, resource_name, option_string):
        r'''initialize_external_alignment

        Creates and initializes a special NI-RFSA external alignment session.

                        The ViSession returned is an NI-RFSA session that you can use to configure the device using normal properties and methods. However, NI-RFSA sets flags that allow you to program an external alignment procedure using the external alignment properties and methods.

                        **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

        Args:
            resource_name (str): Specifies the resource name of the device to initialize.
                                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.

                                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.

            option_string (str): Sets the initial value of certain properties for the session. The properties shown in the following table are used in this parameter.

                                        | Name             | Property                                                                                                                                        |
                                        |:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | RangeCheck       | range_check                         |
                                        | QueryInstrStatus | query_instrument_status |
                                        | Cache            | cache                                     |
                                        | RecordCoercions  | record_coercions               |
                                        | DriverSetup      | driver_setup                       |
                                        | Simulate         | simulate                               |

                                        The format of this string is "*AttributeName=Value*", where *AttributeName* is the name of the property and *Value* is the value to which the property will be set. To set multiple properties, separate their assignments with a comma.


        Returns:
            vi (int): Identifies your instrument session.

        '''
        vi = self._interpreter.initialize_external_alignment(resource_name, option_string)
        return vi

    @ivi_synchronized
    def initialize_external_alignment_step(self, external_alignment_step):
        r'''initialize_external_alignment_step

        Initializes an EEPROM-specific external alignment step.

                        **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

        Args:
            external_alignment_step (int): Specifies which external alignment step you want to initialize.

                                        | Value                                     | Description                                                                                                                                            |
                                        |:-------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
                                        | EXT ALIGNMENT PRESELECTOR | Initiates preselector alignment. This step generates coefficients to align the preselector across the frequency range of 3.6 GHz to 14 GHz. |

        '''
        self._interpreter.initialize_external_alignment_step(external_alignment_step)

    @ivi_synchronized
    def initiate(self):
        r'''initiate

        Commits settings to hardware, waits for hardware settling, and starts an acquisition.

                        You can use this method in conjunction with one of the niRFSA fetch I/Q methods to retrieve acquired I/Q data, or you can use the read_iq_single_record_complex_f64 method to both initiate the acquisition and retrieve I/Q data at one time.

                        ----
                        **Note**
                        If you are using external digitizer mode, this method commits settings and waits for settling, but it does not start an acquisition. Notice that using the commit method on its own commits settings to hardware, but the device does not wait for hardware settling.

                        ----

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

                        `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

                        `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/hardware-state-diagram.html>`_
        '''
        self._interpreter.initiate()

    @ivi_synchronized
    def invalidate_all_attributes(self):
        r'''invalidate_all_attributes

        TBD
        '''
        self._interpreter.invalidate_all_attributes()

    @ivi_synchronized
    def is_self_cal_valid(self):
        r'''is_self_cal_valid

        Indicates which calibration steps contain valid calibration data.

                        To omit steps with valid calibration data from self-calibration, you can pass the **VALID_STEPS** parameter to the **stepsToOmit** parameter of the self_calibrate method.

                        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Returns:
            self_cal_valid (bool): Returns True if all the calibration data is valid and False if any of the calibration data is invalid.

            valid_steps (int): Returns valid steps.

                                        ----
                                        If two or more calibration steps are valid, this parameter returns a bitwise-OR combination of the calibration steps. For example, if both SelfCalibrationStep.IF_FLATNESS and SelfCalibrationStep.LO_SELF_CAL steps are valid, NI-RFSA returns the following string:

                                        SelfCalibrationStep.IF_FLATNESS |

                                        SelfCalibrationStep.LO_SELF_CAL

                                        ----

                                        %enum_table{self calibration step}

        '''
        self_cal_valid, valid_steps = self._interpreter.is_self_cal_valid()
        return self_cal_valid, valid_steps

    @ivi_synchronized
    def lock_session(self):
        r'''lock_session

        Obtains a multithread lock on the instrument session.

                        Before doing so, this method waits until all other execution threads have released their locks on the instrument session.

                        Other threads might have obtained a lock on this session in the following ways:

                        - Your application already called this method.
                        - A call to NI-RFSA locked the session.

                        After the call to this method returns successfully, no other threads can access the instrument session until you call the unlock_session method. Use the lock_session method and the unlock_session method around a sequence of calls to NI-RFSA methods if you require that the NI-RFSA device retain its settings through the end of the sequence.

                        You can safely make nested calls to the lock_session method within the same thread. To completely unlock the session, balance each call to the lock_session method with a call to the unlock_session method. If, however, you use **CALLER_HAS_LOCK** in all calls to the lock_session method and the unlock_session method within a method, the IVI Library locks the session only once within the method regardless of the number of calls you make to the lock_session method. Locking the session only once allows you to call the unlock_session method just once at the end of the method.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Returns:
            caller_has_lock (bool): Keeps track of whether you obtain a lock and therefore need to unlock the session in complex methods. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to False. Pass the address of the same local variable to any other calls you make to this method or the unlock_session method in the same method.

                                        This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.

                                        The lock_session method and the unlock_session method each inspect the current value and take the actions shown in the following table.

                                        | Method             | Boolean Value | Action                                                                                               |
                                        |:---------------------|:--------------|:-----------------------------------------------------------------------------------------------------|
                                        | lock_session   | True       | The lock_session method does not lock the session again.                                     |
                                        |                      | False      | The lock_session method obtains the lock and sets the value of the parameter to True.     |
                                        | unlock_session | False      | The unlock_session method does not attempt to unlock the session.                            |
                                        |                      | True       | The unlock_session method releases the lock and sets the value of the parameter to False. |

                                        Thus, you can call the unlock_session method at the end of your method regardless of whether you actually have the lock.

        '''
        caller_has_lock = self._interpreter.lock_session()
        return caller_has_lock

    @ivi_synchronized
    def perform_thermal_correction(self):
        r'''perform_thermal_correction

        Corrects for temperature variations while acquiring the same signal for an extended period of time in a continuous acquisition.

                        NI-RFSA internally acquires the temperature every time you initiate an acquisition. If you are performing a continuous acquisition, National Instruments recommends calling this method once every 10 minutes in a stable temperature environment to periodically update temperature calibration. If the ambient temperature varies, call this method more frequently.

                        ----
                        **Note**
                        You cannot call this method if your device is operating in `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_.

                        ----

                        Refer to the *Thermal Management* section for your device for more information about typical operating temperatures.

                        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842
        '''
        self._interpreter.perform_thermal_correction()

    @ivi_synchronized
    def reset(self):
        r'''reset

        Resets all properties to default values, deletes all de-embedding tables, and stops the export of all external signals and events.

                        For the PXI-5600, this method does not reset the PXI Clock signal that is driven by devices installed in the Trigger Controller Slot, also known as the System Timing Slot.

                        This method resets all configured routes for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 in NI-RFSA and NI-RFSG. To avoid resetting routes on the device that are in use by NI-RFSG sessions, NI recommends using the reset_with_options method, with **stepsToOmit** set to StepsToOmit.ROUTES.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

                        `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_
        '''
        self._interpreter.reset()

    @ivi_synchronized
    def reset_device(self):
        r'''reset_device

        Performs a hard reset on the device.

                        A hard reset consists of the following actions:

                        - Signal acquisition is stopped.
                        - All routes are released.
                        - External bidirectional terminals are tristated.
                        - FPGAs are reset.
                        - Hardware is configured to its default state.
                        - All session properties are reset to their default states.

                        During a device reset, routes of signals between this and other devices are released, regardless of which device created the route. For example, a trigger signal exported to a PXI trigger line that is used by another device is no longer exported.

                        On the PXI-5600, if you are driving the PXI_CLK10 line, you continue to drive the clock even after a device reset. To stop driving the PXI_CLK10 line, use the configure_pxi_chassis_clk10 method and set the **pxiClk10Source** parameter to NIRFSA_VAL_NONE_STR or set the pxi_chassis_clk10_source property to NIRFSA_VAL_NONE_STR.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

        Note:
        One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
        '''
        self._interpreter.reset_device()

    @ivi_synchronized
    def reset_with_defaults(self):
        r'''reset_with_defaults

        TBD
        '''
        self._interpreter.reset_with_defaults()

    @ivi_synchronized
    def reset_with_options(self, steps_to_omit):
        r'''reset_with_options

        Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes.

                        For the PXI-5600, this method does not reset the PXI Clock signal that is driven by devices installed in the Star Trigger Controller Slot, also known as the System Timing Slot.

                        By default, this method resets all properties to their default values, deletes all de-embedding tables, aborts generation, clears all routes, and resets session properties to initial values. You can specify steps to omit using the steps to omit parameter. For example, if you specify StepsToOmit.ROUTES for the **STEPS_TO_OMIT** parameter, this method does not release signal routes during the reset process.

                        When routes of signals between two devices are released, they are released regardless of which device created the route.

                        To avoid resetting routes on PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSG sessions, NI recommends using this method instead of reset, with **STEPS_TO_OMIT** set to StepsToOmit.ROUTES.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

                        `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            steps_to_omit (int): Specifies a list of steps to skip during the reset process. The default value is StepsToOmit.NONE, which specifies that no step is omitted during reset.

                                        %enum_table{steps to omit}


                                        Note:StepsToOmit.ROUTES is not supported in external calibration or alignment sessions.


                                        Note:StepsToOmit.ROUTES is not supported for the PXI-5600/5661.

        '''
        self._interpreter.reset_with_options(steps_to_omit)

    @ivi_synchronized
    def revision_query(self):
        r'''revision_query

        Returns the revision numbers of the NI-RFSA instrument driver.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            driver_rev (str): Returns the instrument driver software revision numbers in the form of a string. The value of the specific_driver_revision property is returned.

                                        You must pass a ViChar array with 256 bytes or more to this parameter.

            instr_rev (str): Returns the instrument firmware revision numbers in the form of a string. The value of the instrument_firmware_revision property is returned.

                                        You must pass a ViChar array with 256 bytes or more to this parameter.

        '''
        driver_rev, instr_rev = self._interpreter.revision_query()
        return driver_rev, instr_rev

    @ivi_synchronized
    def self_cal(self):
        r'''self_cal

        TBD
        '''
        self._interpreter.self_cal()

    @ivi_synchronized
    def self_calibrate(self, steps_to_omit):
        r'''self_calibrate

        Self-calibrates the NI-RFSA device and associated modules that support self-calibration.

                        If self-calibration is performed successfully, the new calibration constants are stored immediately in the self-calibration area of the module EEPROM. Refer to the specifications document for your device for more information about how often to self-calibrate.

                        For best results, NI recommends that you perform a complete self-calibration without omitting any steps. However, if the is_self_cal_valid method indicates that the calibration data for a specific step is still valid, you can omit that step for faster execution.

                        **Open NI-RFSG Session for the PXIe-5820/5830/5831/5832/5840/5841/5842/5860**

                        If there is an existing NI-RFSG session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this method runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSG Commit or niRFSG Initiate. For the existing open session to use the new self-calibration data, the session will need to be closed and reopened.

                         **PXIe-5860**

                         While this VI is running on one channel, if there are any existing NI-RFSG or NI-RFSA sessions open on the other channel, they may remain open but cannot be used for operations that access the hardware, for example niRFSG Commit or niRFSG Initiate or niRFSA Commit or niRFSA Initiate. For the existing open session to use the new self-calibration data, the session will need to be closed and reopened.

                         **PXIe-5841 with PXIe-5655**

                        The PXIe-5841 maintains separate self-calibration data for both the PXIe-5841 standalone and when associated with the PXIe-5655. Use this method once for each intended configuration.

                        **IF Flatness Step Time**

                        - The IF Flatness step can take approximately 15 minutes to complete on the PXIe-5665 (3.6 GHz) and approximately 25 minutes to complete on the PXIe-5665 (14 GHz).
                        - The IF Flatness step can take approximately 1 minute to complete on the PXIe-5667 (3.6 GHz) and approximately 1.5 minutes to complete on the PXIe-5667 (7 GHz).
                        - The IF Flatness step can take approximately 15 minutes to complete on the PXIe-5668.

                        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `PXI-5661 Calibration <https://www.ni.com/docs/en-US/bundle/pxi-5661-feature/page/self-calibration.html>`_

                        `PXIe-5663/5663E Calibration <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/self-calibration.html>`_

                        `PXIe-5665 Self-Calibration <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/self-calibration.html>`_

                        `PXIe-5667 Self-Calibration <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/self-calibration.html>`_

        Args:
            steps_to_omit (int): Specifies which calibration steps to skip as part of the self-calibration process. A value of 0 specifies all supported calibration steps are performed.

                                        ----

                                        To omit two or more calibration steps, specify a bitwise-OR combination of the following constants. For example, if you wanted to omit SelfCalibrationStep.AMPLITUDE_ACCURACY and SelfCalibrationStep.LO_SELF_CAL, you would pass the following string to the self_calibrate method: SelfCalibrationStep.AMPLITUDE_ACCURACY | SelfCalibrationStep.LO_SELF_CAL

                                        ----

                                        | Value                                          |  Description                                                                                                                                                                                                                     |
                                        |:------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | StepsToOmit.NONE             | No step is omitted during self-calibration.                                                                                                                                                                           |
                                        | SelfCalibrationStep.PRESELECTOR_ALIGNMENT | Not used by this method.                                                                                                                                                                                            |
                                        | SelfCalibrationStep.GAIN_REFERENCE        | Not used by this method.                                                                                                                                                                                            |
                                        | SelfCalibrationStep.IF_FLATNESS           | Not used by this method.                                                                                                                                                                                            |
                                        | SelfCalibrationStep.DIGITIZER_SELF_CAL    | Not used by this method.                                                                                                                                                                                            |
                                        | SelfCalibrationStep.LO_SELF_CAL           | Omits the Local Oscillator (LO) Self Cal step. If you omit this step and the is_self_cal_valid method indicates the calibration data for this step is invalid, the LO phase-locked loop (PLL) may fail to lock. |
                                        | SelfCalibrationStep.AMPLITUDE_ACCURACY    | Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy of the device is not adjusted.                                                                                                        |
                                        | SelfCalibrationStep.RESIDUAL_LO_POWER     | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.                                                                                                           |
                                        |SelfCalibrationStep.IMAGE_SUPPRESSION      | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image Performance is not adjusted.                                                                                                     |
                                        | SelfCalibrationStep.SYNTHESIZER_ALIGNMENT | Omits the Synthesizer Alignment step. If you omit this step, the LO PLL is not adjusted. This step is not valid for the PXIe-5820.                                                                                    |
                                        | SelfCalibrationStep.DC_OFFSET             | Omits the DC Offset step. This step applies only to the PXIe-5820.                                                                                                                                                    |

        '''
        self._interpreter.self_calibrate(steps_to_omit)

    @ivi_synchronized
    def self_calibrate_range(self, steps_to_omit, min_frequency, max_frequency, min_reference_level, max_reference_level):
        r'''self_calibrate_range

        Self-calibrates all configurations within the specified frequency and reference level limits.

                        Self-calibration range data is valid until you restart the system or call the clear_self_calibrate_range method.

                        NI recommends that no external signals are present on the RF In port while the calibration is taking place.

                        ----
                        **Note**
                        This method does not update self-calibration date and temperature.

                        ----

                        For best results, NI recommends that you perform a complete self-calibration without omitting any steps. However, if certain aspects of performance are less important for your application, you can omit that step for faster execution.

                        ----
                        **Note**
                        If there is an existing NI-RFSG session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this method runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSG Commit or niRFSG Initiate.

                        ----

                        ----
                        **Note**
                        If there is an existing NI-RFSG session open for the same PXIe-5644/5645/5646, it may remain open but cannot be used while this method runs.

                        ----

                        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

        Args:
            steps_to_omit (int): Specifies which calibration steps to skip as part of the self-calibration process. A value of 0 specifies all supported calibration steps are performed.

                                        ----

                                        To omit two or more calibration steps, specify a bitwise-OR combination of the following constants. For example, if you wanted to omit SelfCalibrationStep.AMPLITUDE_ACCURACY and SelfCalibrationStep.LO_SELF_CAL, you would pass the following string to the self_calibrate method: SelfCalibrationStep.AMPLITUDE_ACCURACY | SelfCalibrationStep.LO_SELF_CAL

                                        ----

                                        | Value                                          |  Description                                                                                                                                                                                                                     |
                                        |:------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | StepsToOmit.NONE             | No step is omitted during self-calibration.                                                                                                                                                                           |
                                        | SelfCalibrationStep.PRESELECTOR_ALIGNMENT | Not used by this method.                                                                                                                                                                                            |
                                        | SelfCalibrationStep.GAIN_REFERENCE        | Not used by this method.                                                                                                                                                                                            |
                                        | SelfCalibrationStep.IF_FLATNESS           | Not used by this method.                                                                                                                                                                                            |
                                        | SelfCalibrationStep.DIGITIZER_SELF_CAL    | Not used by this method.                                                                                                                                                                                            |
                                        | SelfCalibrationStep.LO_SELF_CAL           | Omits the Local Oscillator (LO) Self Cal step. If you omit this step and the is_self_cal_valid method indicates the calibration data for this step is invalid, the LO phase-locked loop (PLL) may fail to lock. |
                                        | SelfCalibrationStep.AMPLITUDE_ACCURACY    | Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy of the device is not adjusted.                                                                                                        |
                                        | SelfCalibrationStep.RESIDUAL_LO_POWER     | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.                                                                                                           |
                                        |SelfCalibrationStep.IMAGE_SUPPRESSION      | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image Performance is not adjusted.                                                                                                     |
                                        | SelfCalibrationStep.SYNTHESIZER_ALIGNMENT | Omits the Synthesizer Alignment step. If you omit this step, the LO PLL is not adjusted. This step is not valid for the PXIe-5820.                                                                                    |
                                        | SelfCalibrationStep.DC_OFFSET             | Omits the DC Offset step. This step applies only to the PXIe-5820.                                                                                                                                                    |

            min_frequency (float): Specifies the minimum RF frequency in Hz.

            max_frequency (float): Specifies the maximum RF frequency in Hz.

            min_reference_level (float): Specifies the minimum reference level in dBm.

            max_reference_level (float): Specifies the maximum reference level in dBm.

        '''
        self._interpreter.self_calibrate_range(steps_to_omit, min_frequency, max_frequency, min_reference_level, max_reference_level)

    @ivi_synchronized
    def self_test(self):
        r'''self_test

        Performs a self-test on the NI-RFSA device and returns the test result.

                        This method performs a simple series of tests verifying that the NI-RFSA device is powered on and responding.

                        ----
                        **Note**
                        This method calls the reset method, which resets the software state.

                        ----

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Running a Self-Test on an NI-RFSA Device <https://www.ni.com/docs/en-US/bundle/ni-rfsa-max/page/maxrfsa/mi_rf_self_test.html>`_

        Returns:
            test_result (int): Returns the value from the device self-test. A value of 0 means success. All other values indicate failure.

                                        You must pass a ViChar array with 1024 bytes or more to this parameter. Only the first 1024 bytes of the array are used.

            test_message (str): Returns the self-test response string from the NI-RFSA device.

        '''
        test_result, test_message = self._interpreter.self_test()
        return test_result, test_message

    @ivi_synchronized
    def send_software_edge_trigger(self, trigger, trigger_identifier):
        r'''send_software_edge_trigger

        Sends a trigger to the device when you use a software version of a supported trigger and the device is waiting for the trigger to be sent.

                        You can also use this method to override a hardware trigger.

                        This method returns an error in the following situations:

                        - You configure an invalid trigger.
                        - You set the **acquisitionType** to AcquisitionType.SPECTRUM using the configure_acquisition_type method.
                        - You have not previously called the initiate method.

                        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Software Trigger <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/software-edge-trigger.html>`_

                        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        Args:
            trigger (int): Specifies the software signal to send.

                                        %enum_table{trigger}

            trigger_identifier (str): Specifies a particular instance of a trigger. NI-RFSA does not currently support this parameter.

        '''
        self._interpreter.send_software_edge_trigger(trigger, trigger_identifier)

    @ivi_synchronized
    def set_cal_user_defined_info(self, info):
        r'''set_cal_user_defined_info

        Writes user-defined information into the onboard EEPROM.

                        This should be called in its own session or else the data may be overwritten by a commit.

                        **Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698

        Args:
            info (str): Specifies a string containing the user-defined information. This string can be up to 21 characters long.

        '''
        self._interpreter.set_cal_user_defined_info(info)

    @ivi_synchronized
    def set_user_data(self, identifier, data):
        r'''set_user_data

        TBD

        Args:
            identifier (str):

            data (array.array("b")):

        '''
        self._interpreter.set_user_data(identifier, data)

    @ivi_synchronized
    def unlock_session(self):
        r'''unlock_session

        Releases a lock obtained on an NI-RFSA device session by calling the lock_session method.

                        Refer to the lock_session method for additional information on session locks.

                        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

        Returns:
            caller_has_lock (bool): Keeps track of whether you obtain a lock and therefore need to unlock the session in complex methods. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to False. Pass the address of the same local variable to any other calls you make to this method or the unlock_session method in the same method.

                                        This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.

                                        The lock_session method and the unlock_session method each inspect the current value and take the actions shown in the following table.

                                        | Method             | Boolean Value | Action                                                                                               |
                                        |:---------------------|:--------------|:-----------------------------------------------------------------------------------------------------|
                                        | lock_session   | True       | The lock_session method does not lock the session again.                                     |
                                        |                      | False      | The lock_session method obtains the lock and sets the value of the parameter to True.     |
                                        | unlock_session | False      | The unlock_session method does not attempt to unlock the session.                            |
                                        |                      | True       | The unlock_session method releases the lock and sets the value of the parameter to False. |

                                        Thus, you can call the unlock_session method at the end of your method regardless of whether you actually have the lock.

        '''
        caller_has_lock = self._interpreter.unlock_session()
        return caller_has_lock

    @ivi_synchronized
    def self_test(self):
        '''self_test

        TBD
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None
