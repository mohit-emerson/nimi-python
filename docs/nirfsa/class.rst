.. py:module:: nirfsa

Session
=======

.. py:class:: Session(self, resource_name, id_query, reset, options={})

    

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

    



    :param resource_name:
        

        Specifies the resource name of the device to initialize.

                                For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.

                                Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.

        


    :type resource_name: str

    :param id_query:
        

        Specifies whether NI-RFSA performs an ID query. When you perform an ID query, NI-RFSA verifies the device you initialize is supported.

                                | Value               |  Description                                               |
                                |:--------------|:------------------------------------------------|
                                | True (Yes) | Perform an ID query. This value is the default. |
                                | False (No) | Do not perform an ID query.                     |

        


    :type id_query: bool

    :param reset:
        

        Specifies whether the NI-RFSA device is reset during the initialization procedure.

                                | Value              |  Description                                                   |
                                |:--------------|:----------------------------------------------------|
                                | True (Yes) | The device is reset.                                |
                                | False (No) | The device is not reset. This value is the default. |

        


    :type reset: bool

    :param options:
        

        Specifies the initial value of certain properties for the session. The
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


    :type options: str


Methods
=======

abort
-----

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: abort()

            Stops an acquisition previously started with the :py:meth:`nirfsa.Session._initiate` method or the :py:meth:`nirfsa.Session.read_power_spectrum_f64` method.

                            You can also use the :py:meth:`nirfsa.Session.abort` method to stop a self-calibration. Calling this method is optional, unless you want to stop an acquisition before it is complete or you are continuously acquiring data.

                            You can stop the following kinds of acquisitions:

                            - Triggered spectrum acquisitions that have not yet been triggered
                            - Multispan acquisitions in progress
                            - Average spectrum acquisitions in progress
                            - Single-record spectrum acquisitions in progress
                            - Streaming in progress

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            



cal_adjust_cal_tone_power
-------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: cal_adjust_cal_tone_power(measurement)

            Specifies the calibration tone power during calibration tone amplitude calibration.

                            You must call the :py:meth:`nirfsa.Session._initiate` method before calling this method.

                            **Supported Devices**: PXIe-5693

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].cal_adjust_cal_tone_power`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.cal_adjust_cal_tone_power`


            :param measurement:


                Specifies the calibration tone power, in dBm, for the current device setting.

                


            :type measurement: float

cal_adjust_device_gain
----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: cal_adjust_device_gain(frequency, gain)

            Records measured gain information that is gathered during the Reference Level Calibration step and IF Attenuation Calibration step.

                            This method internally queries the properties you set, and you must commit all properties appropriate for your device calibration procedure prior to calling this method. Refer to ni.com/manuals for the most recent version of the calibration procedure for your device.

                            Call this method immediately after a measurement is made and while the device under test (DUT) is still in the same state as it was during the measurement.

                            **Supported Devices**: PXIe-5693/5694/5698

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].cal_adjust_device_gain`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.cal_adjust_device_gain`


            :param frequency:


                Specifies the RF frequency, in Hz, of the measurement taken.

                


            :type frequency: float
            :param gain:


                Specifies the gain measurement, in dB.

                


            :type gain: float

cal_adjust_downconverter_gain
-----------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: cal_adjust_downconverter_gain(frequency, gain)

            Records measured gain information that is gathered during the Reference Level Calibration step and IF Attenuation Calibration step.

                            This method internally queries the properties you set, and you must set and commit the following properties prior to calling this method.

                            - :py:attr:`nirfsa.Session.cal_rf_electronic_attenuation_index` (This property is required only when the :py:attr:`nirfsa.Session.cal_rf_path_selection` property is set to :py:data:`~nirfsa.RfPathSel._1`.)
                            - :py:attr:`nirfsa.Session.cal_rf_mechanical_attenuation_index`
                            - :py:attr:`nirfsa.Session.cal_if_attenuation_table_selection`
                            - :py:attr:`nirfsa.Session.cal_if_attenuation_index`
                            - :py:attr:`nirfsa.Session.cal_if_filter_selection`
                            - :py:attr:`nirfsa.Session.channel_coupling`
                            - :py:attr:`nirfsa.Session.rf_preamp_enabled`

                            Call this method immediately after a measurement is made and while the device under test (DUT) is still in the same state as it was during the measurement.

                            **Supported Devices**: PXIe-5603/5605/5606

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].cal_adjust_downconverter_gain`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.cal_adjust_downconverter_gain`


            :param frequency:


                Specifies the RF frequency, in Hz, of the measurement taken.

                


            :type frequency: float
            :param gain:


                Specifies the gain measurement, in dB.

                


            :type gain: float

cal_adjust_if_attenuation_calibration
-------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: cal_adjust_if_attenuation_calibration(if_filter, number_of_attenuators, measurement)

            Specifies the IF attenuation settings.

                            **Supported Devices**: PXIe-5601, PXIe-5694

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].cal_adjust_if_attenuation_calibration`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.cal_adjust_if_attenuation_calibration`


            :param if_filter:


                Specifies the IF filter used by the downconverter.

                                        |Value                                     |Description                                             |
                                        |:------------------------------------|:--------------------------------------------|
                                        | :py:data:`~nirfsa.IFfilter._187_5_MHZ_NARROW` (1400)  | Uses the 187.5 MHz wide bandwidth filter.   |
                                        | :py:data:`~nirfsa.IFfilter._187_5_MHZ_NARROW` (1401) | Uses the 187.5 MHz narrow bandwidth filter. |
                                        | :py:data:`~nirfsa.IFfilter._53_MHZ` (1402)            | Uses the 53 MHz filter.                     |
                                        | :py:data:`~nirfsa.IFfilter.BYPASS` (1403)            | Bypasses the IF filter.                     |

                


            :type if_filter: int
            :param number_of_attenuators:


                Specifies the number of attenuators to use during the IF attenuation adjustment.

                


            :type number_of_attenuators: int
            :param measurement:


                Specifies the relevant measurement taken for the current configuration.

                


            :type measurement: float

            :rtype: float
            :return:


                    Specifies the IF attenuator settings for the measurement. The first element in the array corresponds with IF1, the next element corresponds to IF2, and so on.

                    



cal_adjust_if_response_calibration
----------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: cal_adjust_if_response_calibration(if_filter, rf_frequency, band_width, number_of_measurements)

            Specifies the IF response settings.

                            **Supported Devices**: PXIe-5601, PXIe-5694

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].cal_adjust_if_response_calibration`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.cal_adjust_if_response_calibration`


            :param if_filter:


                Specifies the IF filter used by the downconverter.

                                        |Value                                     |Description                                           |
                                        |:------------------------------------|:------------------------------------------|
                                        | :py:data:`~nirfsa.IFfilter._187_5_MHZ_NARROW` (1400)   | Uses the 187.5 MHz wide bandwidth path.   |
                                        | :py:data:`~nirfsa.IFfilter._187_5_MHZ_NARROW` (1401) | Uses the 187.5 MHz narrow bandwidth path. |
                                        | :py:data:`~nirfsa.IFfilter._53_MHZ` (1402)            | Uses the 53 MHz path.                     |
                                        | :py:data:`~nirfsa.IFfilter.BYPASS` (1403)            | Bypasses the IF path.                     |

                


            :type if_filter: int
            :param rf_frequency:


                Specifies the RF frequency, in Hz, used during the IF response adjustment.

                


            :type rf_frequency: float
            :param band_width:


                Specifies the bandwidth, in Hz, to use for the IF response adjustment.

                


            :type band_width: float
            :param number_of_measurements:


                Specifies the number of measurements to make.

                


            :type number_of_measurements: int

            :rtype: float
            :return:


                    Specifies the relevant measurements taken for each IF filter configuration, in dB.

                    



cal_adjust_lo_export_calibration
--------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: cal_adjust_lo_export_calibration(lo_number, number_of_frequency_points)

            LO export calibration measures the PXIe-5603/5605 LO output power level.

                            The LO output power measurements are taken from the PXIe-5653 module. In MIMO applications, when the LO is exported from one PXIe-5603/5605 module to another subsequent PXIe-5603/5605, an output power signal of approximately +7 dBm is expected on each LO connector (LO1, LO2, and LO3). This method records the LO attenuation that results in an output power of +7 dBm (or greater) on the three LO output terminals.

                            The PXIe-5665/5668 uses three LOs, but only LO1 is variable in frequency. This method accepts an array of frequencies and attenuations; however, for LO2 and LO3, this array must have only one element because these two LO sources operate only at one frequency. LO1 can have multiple values for specific frequencies.

                            **Supported Devices**: PXIe-5603/5605/5606

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].cal_adjust_lo_export_calibration`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.cal_adjust_lo_export_calibration`


            :param lo_number:


                Specifies the LO source to use for the LO export calibration.

                                        |Value                                   |Description                                                                    |
                                        |:----------------------------------|:-------------------------------------------------------------------|
                                        | :py:data:`~nirfsa.LoNumber.LO1`  (2200) | Selects LO1, which is the 3.2 GHz to 8.3 GHz variable signal path. |
                                        | :py:data:`~nirfsa.LoNumber.LO2` (2201) | Selects LO2, which is the 4 GHz signal path.                       |
                                        | :py:data:`~nirfsa.LoNumber.LO3`  (2202) | Selects LO3, which is the 800 MHz signal path.                     |

                


            :type lo_number: int
            :param number_of_frequency_points:


                Specifies the length of the **frequencies** and **:py:attr:`nirfsa.Session.LO_ATTENUATION`** arrays.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type number_of_frequency_points: int

            :rtype: tuple (frequency_points, lo_attenuation)

                WHERE

                frequency_points (float): 


                    Specifies frequencies for the LO output power measurement. The length of this array equals the **:py:attr:`nirfsa.Session.NUMBER_OF_FREQUENCY_POINTS`** parameter.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.


                lo_attenuation (float): 


                    Specifies the attenuation value of the corresponding frequency point that results in a +7 dBm output signal on the respective LO OUT connector. The length of this array equals the **:py:attr:`nirfsa.Session.NUMBER_OF_FREQUENCY_POINTS`** parameter.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.



cal_adjust_ref_level_calibration
--------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: cal_adjust_ref_level_calibration(reference_level_data_type, rf_band, attenuator_table_number, frequency, measurement)

            Writes the reference level calibration data settings to the driver.

                            **Supported Devices**: PXIe-5601

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].cal_adjust_ref_level_calibration`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.cal_adjust_ref_level_calibration`


            :param reference_level_data_type:


                Specifies whether the reference level calibration data being used is the default configuration data or the mechanical relay disabled configuration data.

                                        |Value                                                          |Description                                                                                                                                                           |
                                        |:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | :py:data:`~nirfsa.ReferenceLevelDataType.DEFAULT` (1800)                        | The data is the default configuration data.                                                                                                               |
                                        | :py:data:`~nirfsa.ReferenceLevelDataType.MECHANICAL_ATTENUATOR_DISABLED` (1801) | The data is the configuration data when the mechanical relay is disabled. Use this option to save uncalibrated measurements for more advanced operations. |

                


            :type reference_level_data_type: int
            :param rf_band:


                Specifies the RF band used during the reference level calibration.

                                        |Value                      |Description                             |
                                        |:---------------------|:----------------------------|
                                        | :py:data:`~nirfsa.RfPathSel._1` | The RF band 1 path is used. |
                                        | :py:data:`~nirfsa.RfPathSel._2`| The RF band 2 path is used. |
                                        | :py:data:`~nirfsa.RfPathSel._3` | The RF band 3 path is used. |
                                        | :py:data:`~nirfsa.RfPathSel._4` | The RF band 4 path is used. |

                


            :type rf_band: int
            :param attenuator_table_number:


                Specifies which attenuation table you are using. Valid values are 0 and 1.

                


            :type attenuator_table_number: int
            :param frequency:


                Specifies the frequency for the reference level adjustment.

                


            :type frequency: float
            :param measurement:


                Specifies the relevant measurement taken for the current configuration.

                


            :type measurement: float

cal_set_temperature
-------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: cal_set_temperature(temperature)

            Writes the calibration temperature to the driver.

                            **Supported Devices**: PXIe-5601

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].cal_set_temperature`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.cal_set_temperature`


            :param temperature:


                Specifies the calibration temperature, in degrees Celsius.

                


            :type temperature: float

change_ext_cal_password
-----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: change_ext_cal_password(old_password, new_password)

            Changes the password that is required to initialize an external calibration session.

                            **Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            



            :param old_password:


                Specifies the old (current) external calibration password.

                                        The maximum length of the password varies by device.

                


            :type old_password: str
            :param new_password:


                Specifies the new (desired) external calibration password.

                                        The maximum length of the password varies by device.

                


            :type new_password: str

check_acquisition_status
------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: check_acquisition_status()

            Checks the status of the acquisition.

                            Use this method to check for any errors that may occur during signal acquisition or to check whether the device has completed the acquisition operation.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/hardware-state-diagram.html>`_

            



            :rtype: bool
            :return:


                    Returns signal acquisition status.

                                            |Value          |Description                                     |
                                            |:---------|:------------------------------------|
                                            | True  | Signal acquisition is complete.     |
                                            | False | Signal acquisition is not complete. |

                    



clear_error
-----------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: clear_error()

            Clears the error information associated with the session.

                            If you pass VI_NULL for the :py:attr:`nirfsa.Session.VI` parameter, this method clears the error information for the current execution thread.

                            ----
                            **Note**
                            The :py:meth:`nirfsa.Session._get_error` method clears the error information after it is retrieved. A call to the :py:meth:`nirfsa.Session.clear_error` method is necessary only when a call to the :py:meth:`nirfsa.Session._get_error` method is not used to retrieve error information.

                            ----

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5840

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



clear_self_calibrate_range
--------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: clear_self_calibrate_range()

            Clears the data obtained from the :py:meth:`nirfsa.Session.self_calibrate_range` method.

                            **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

            



close
-----

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: close()

            Closes the session to the device.

                            If you close a session that has Soft Front Panel (SFP) session access enabled, any application connected to the shared device session is no longer usable. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about using SFP session access.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            

            .. note:: This method is not needed when using the session context manager



close_calibration_step
----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: close_calibration_step()

            Closes the current calibration step.

                            **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698

            



close_ext_cal
-------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: close_ext_cal(action)

            Closes an NI-RFSA external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM.

                            **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            



            :param action:


                Specifies how to use the calibration values from this session as the session is closed.

                                        |Value                           |Description                                                                         |
                                        |:--------------------------|:------------------------------------------------------------------------|
                                        | :py:data:`~nirfsa.Action.ABORT`  | The old calibration constants are kept, and the new ones are discarded. |
                                        | :py:data:`~nirfsa.Action.COMMIT` | The new calibration constants are stored in the EEPROM.                 |

                


            :type action: int

close_external_alignment
------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: close_external_alignment(action)

            Closes an NI-RFSA external alignment session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM.

                            **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

            



            :param action:


                Specifies how to use the alignment values from this session as the session is closed.

                                        |Value                           |Description                                                                       |
                                        |:--------------------------|:----------------------------------------------------------------------|
                                        | :py:data:`~nirfsa.Action.ABORT`  | The old alignment constants are kept, and the new ones are discarded. |
                                        |  :py:data:`~nirfsa.Action.COMMIT`| The new alignment constants are stored in the EEPROM.                 |

                


            :type action: int

close_external_alignment_step
-----------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: close_external_alignment_step()

            Closes an EEPROM-specific external alignment step.

                            **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

            



commit
------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: commit()

            Commits settings to hardware.

                            Calling this method is optional. Settings are automatically committed to hardware when you call the :py:meth:`nirfsa.Session._initiate` method, the :py:meth:`nirfsa.Session.read_iq_single_record_complex_f64` method, or the :py:meth:`nirfsa.Session.read_power_spectrum_f64` method.

                            ----
                            **Note**
                            This method does not wait for settling time, unlike the :py:meth:`nirfsa.Session._initiate` method.

                            ----

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/hardware-state-diagram.html>`_

            



configure_acquisition_type
--------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_acquisition_type(acquisition_type)

            Configures whether the session acquires I/Q data or computes a power spectrum over the specified frequency range.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

            



            :param acquisition_type:


                Configures the type of acquisition.

                                        | Value                    | Description                                                                       |
                                        |:--------------------|:-----------------------------------------------------------------------|
                                        | :py:data:`~nirfsa.AcquisitionType.IQ`       | Configures the driver for I/Q acquisitions. This value is the default. |
                                        | :py:data:`~nirfsa.AcquisitionType.SPECTRUM` | Configures the driver for spectrum acquisitions.                       |

                


            :type acquisition_type: int

configure_deembedding_table_interpolation_linear
------------------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_deembedding_table_interpolation_linear(port, table_name, format)

            Selects the linear interpolation method.

                            If the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

                            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table.

                


            :type table_name: str
            :param format:


                Specifies the format of parameters to interpolate.

                                        %enum_table{format}

                


            :type format: int

configure_deembedding_table_interpolation_nearest
-------------------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_deembedding_table_interpolation_nearest(port, table_name)

            Selects the nearest interpolation method.

                            NI-RFSA uses the parameters of the table nearest to the carrier frequency for de-embedding.

                            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table.

                


            :type table_name: str

configure_deembedding_table_interpolation_spline
------------------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_deembedding_table_interpolation_spline(port, table_name)

            Selects the spline interpolation method.

                            If the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

                            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table.

                


            :type table_name: str

configure_digital_edge_advance_trigger
--------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_digital_edge_advance_trigger(source, edge)

            Configures the device to wait for a digital edge Advance Trigger.

                            The Advance Trigger indicates where a new record begins.

                            ----
                            **Note**
                             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.configure_acquisition_type` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

                            ----

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



            :param source:


                Specifies the source of the digital edge for the Advance Trigger.

                                        | Value                                           | Description                                                                                                                                                                                                                |
                                        |:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PFI0_STR` ('PFI0')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                            |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PFI1_STR` ('PFI1')               | The trigger is received on PFI 1.                                                                                                                                                                              |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG0_STR` ('PXI_Trig0')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG1_STR` ('PXI_Trig1')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG2_STR` ('PXI_Trig2')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG3_STR` ('PXI_Trig3')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG4_STR` ('PXI_Trig4')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG5_STR` ('PXI_Trig5')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG6_STR` ('PXI_Trig6')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG7_STR` ('PXI_Trig7')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_STAR_STR` ('PXI_STAR')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                             |
                                        | :py:data:`~nirfsa.OutputTerm.PXIE_DSTARB` ('PXIE_DSTARB') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |
                                        | :py:data:`~nirfsa.OutputTerm.TIMER_EVENT` ('TimerEvent')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI0_STR` ('PFI0')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI1_STR`('PFI1')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI2_STR` ('PFI2')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI3_STR` ('PFI3')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI4_STR` ('PFI4')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI5_STR` ('PFI5')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI6_STR` ('PFI6')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI7_STR` ('PFI7')               | The trigger is received on PFI 7 of the DIO Terminal. |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source: str
            :param edge:


                Specifies the trigger edge to detect. The default value is :py:data:`~nirfsa.NIRFSA_VAL_RISING_EDGE`.

                                        | Value                              | Description                                |
                                        |:------------------------------|:--------------------------------|
                                        | :py:data:`~nirfsa.NIRFSA_VAL_RISING_EDGE` (900)  | NI-RFSA detects a rising edge.  |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_FALLING_EDGE` (901) | NI-RFSA detects a falling edge. |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type edge: int

configure_digital_edge_ref_trigger
----------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_digital_edge_ref_trigger(source, edge, pretrigger_samples)

            Configures the device to wait for a digital edge Reference Trigger to mark a reference point within the record.

                            You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

                            ----
                            **Note**
                             The PXIe-5644/5645/5646 does not support the NI-TClk API.

                            ----

                            ----
                            **Note**
                             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.configure_acquisition_type` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

                            ----

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



            :param source:


                Specifies the source of the digital edge for the Reference trigger.

                                        |Value                                            |Description                                                                                                                                                                                                                               |
                                        |:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PFI0_STR` ('PFI0')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                                           |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PFI1_STR` ('PFI1')               | The trigger is received on PFI 1.                                                                                                                                                                                             |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG0_STR` ('PXI_Trig0')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                                |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG1_STR` ('PXI_Trig1')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                                |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG2_STR` ('PXI_Trig2')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                                |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG3_STR` ('PXI_Trig3')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                                |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG4_STR` ('PXI_Trig4')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                                |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG5_STR` ('PXI_Trig5')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                                |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG6_STR` ('PXI_Trig6')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                                |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG7_STR` ('PXI_Trig7')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                                |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_STAR_STR` ('PXI_STAR')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                                            |
                                        | :py:data:`~nirfsa.OutputTerm.PXIE_DSTARB` ('PXIE_DSTARB') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |
                                        | :py:data:`~nirfsa.OutputTerm.TIMER_EVENT` ('TimerEvent')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI0_STR` ('PFI0')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI1_STR`('PFI1')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI2_STR` ('PFI2')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI3_STR` ('PFI3')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI4_STR` ('PFI4')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI5_STR` ('PFI5')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI6_STR` ('PFI6')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI7_STR` ('PFI7')               | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                          |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source: str
            :param edge:


                Specifies the trigger edge to detect. The default value is :py:data:`~nirfsa.NIRFSA_VAL_RISING_EDGE`.

                                        |Value                               |Description                                 |
                                        |:------------------------------|:--------------------------------|
                                        | :py:data:`~nirfsa.NIRFSA_VAL_RISING_EDGE` (900)  | NI-RFSA detects a rising edge.  |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_FALLING_EDGE` (901) | NI-RFSA detects a falling edge. |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type edge: int
            :param pretrigger_samples:


                Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.

                


            :type pretrigger_samples: int

configure_digital_edge_start_trigger
------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_digital_edge_start_trigger(source, edge)

            Configures the device to wait for a digital edge Start Trigger at the beginning of the acquisition.

                            You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

                            ----
                            **Note**
                             The PXIe-5644/5645/5646 does not support the NI-TClk API.

                            ----

                            ----
                            **Note**
                             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.configure_acquisition_type` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

                            ----

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



            :param source:


                Specifies the source of the digital edge for the Start Trigger.

                                        | Value                                           | Description                                                                                                                                                                                                               |
                                        |:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PFI0_STR` ('PFI0')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                            |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PFI1_STR` ('PFI1')               | The trigger is received on PFI 1.                                                                                                                                                                              |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG0_STR` ('PXI_Trig0')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG1_STR` ('PXI_Trig1')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG2_STR` ('PXI_Trig2')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG3_STR` ('PXI_Trig3')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG4_STR` ('PXI_Trig4')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG5_STR` ('PXI_Trig5')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG6_STR` ('PXI_Trig6')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG7_STR` ('PXI_Trig7')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                 |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_STAR_STR` ('PXI_STAR')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                             |
                                        | :py:data:`~nirfsa.OutputTerm.PXIE_DSTARB` ('PXIE_DSTARB') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |
                                        | :py:data:`~nirfsa.OutputTerm.TIMER_EVENT` ('TimerEvent')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI0_STR` ('PFI1')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI1_STR`('PFI2')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI2_STR` ('PFI3')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI3_STR` ('PFI4')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI4_STR` ('PFI5')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI5_STR` ('PFI6')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI6_STR` ('PFI7')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI7_STR` ('PFI8')               | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                          |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source: str
            :param edge:


                Specifies the trigger edge to detect. The default value is :py:data:`~nirfsa.NIRFSA_VAL_RISING_EDGE`.

                                        | Value                              | Description                                |
                                        |:------------------------------|:--------------------------------|
                                        | :py:data:`~nirfsa.NIRFSA_VAL_RISING_EDGE` (900)  | NI-RFSA detects a rising edge.  |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_FALLING_EDGE` (901) | NI-RFSA detects a falling edge. |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type edge: int

configure_iq_carrier_frequency
------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_iq_carrier_frequency(carrier_frequency)

            Configures the `carrier frequency <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/fund-carrierwave.html>`_ of the RF vector signal analyzer hardware for an I/Q acquisition.

                            The carrier frequency is the center frequency of the I/Q acquisition.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Carrier Wave <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/fund-carrierwave.html>`_

                            `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_iq_carrier_frequency`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_iq_carrier_frequency`


            :param carrier_frequency:


                Specifies the carrier frequency, in hertz (Hz), of the RF signal to acquire.

                                        The RF vector signal analyzer tunes to this frequency. NI-RFSA may coerce this value based on hardware settings and downconversion settings.

                                        NI-RFSA sets the :py:attr:`nirfsa.Session.iq_carrier_frequency` property to this value. Refer to the specifications document that shipped with your device for allowable frequency settings.

                


            :type carrier_frequency: float

configure_iq_power_edge_ref_trigger
-----------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_iq_power_edge_ref_trigger(source, level, slope, pretrigger_samples)

            Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

                            To trigger on burst signals, add a minimum quiet time, configured with the :py:attr:`nirfsa.Session.ref_trigger_minimum_quiet_time` property, to ensure the trigger does not occur in the middle of a burst if the acquisition starts while a burst is being generated. The quiet time should be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

                            You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

                            ----
                            **Note**
                             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.configure_acquisition_type` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

                            ----

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



            :param source:


                Specifies the source of the RF signal for the power edge Reference trigger. The only supported value is "0".

                


            :type source: str
            :param level:


                Specifies the threshold, in dBm, above or below which the device triggers.

                


            :type level: float
            :param slope:


                Specifies whether the device detects a positive or negative slope on the trigger signal. The default value is :py:data:`~nirfsa.RefTrigIqPwrEdgeSlope.RISING`.

                                        | Value                                | Description                                                |
                                        |:--------------------------------|:-------------------------------------------------|
                                        | :py:data:`~nirfsa.RefTrigIqPwrEdgeSlope.RISING` (1000)  | NI-RFSA detects a rising edge (positive slope).  |
                                        | :py:data:`~nirfsa.RefTrigIqPwrEdgeSlope.FALLING` (1001) | NI-RFSA detects a falling edge (negative slope). |

                


            :type slope: int
            :param pretrigger_samples:


                Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.

                


            :type pretrigger_samples: int

configure_iq_rate
-----------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_iq_rate(iq_rate)

            Specifies the I/Q rate for the acquisition.

                            The value is expressed in samples per second (S/s).

                            For the PXIe-5663/5663E/5665/5667/5668, when you set the :py:attr:`nirfsa.Session.digitizer_sample_clock_timebase_source` property to :py:data:`~nirfsa.NIRFSA_VAL_ONBOARD_CLOCK_STR`, the digitizer bandwidth is greater than or equal to the coerced **:py:attr:`nirfsa.Session.iq_rate`** times 0.8. Actual signal bandwidth is limited for all supported devices by the anti-aliasing filter. Further device-specific limitations are as follows.

                            ----
                            **Note**
                            For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect your measurements. Refer to the :py:attr:`nirfsa.Session.digitizer_dither_enabled` property for more information about dithering.

                            ----

                            - **PXI-5661** You should not need to configure an **:py:attr:`nirfsa.Session.iq_rate`** higher than 25 megasamples per second (MS/s) because the PXI-5600 RF downconverter bandwidth is 20 MHz. If you configure a higher I/Q rate, you may see aliasing effects at negative frequencies because the IF frequency of the PXI-5600 RF downconverter is 15 MHz.
                            - **PXIe-5663/5663E** Maximum allowed instantaneous bandwidth depends on the I/Q carrier frequency you use. Refer to the `PXIe-5601 RF downconverter overview <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/overview.3.html>`_  for more information about instantaneous bandwidth.
                            - **PXIe-5665** Actual signal bandwidth is limited by the preselector and the combination of the chosen IF filter and anti-aliasing filter. Maximum allowed instantaneous bandwidth is independent of the downconverter center frequency for frequencies less than 3.6 GHz. At frequencies greater than 3.6 GHz, if your device supports the preselector (YIG-tuned filter) and you have enabled it for your application, the maximum allowed instantaneous bandwidth is limited to the instantaneous bandwidth of the preselector. Refer to the *NI PXIe-5665 Specifications* for more information about instantaneous bandwidth limits.
                            - **PXIe-5667** Actual signal bandwidth is limited by the preselector and the combination of the chosen IF filter and anti-aliasing filter. Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the *NI PXIe-5667 Specifications* for more information about instantaneous bandwidth limits.
                            - **PXIe-5668** Actual signal bandwidth is limited by the FPGA image that is downloaded upon opening the session to the PXIe-5624 digitizer. Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the *PXIe-5668 Specifications* for more information about instantaneous bandwidth limits.
                            - **PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842** Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the specifications document for your device for more information about instantaneous bandwidth limits.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

            

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_iq_rate`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_iq_rate`


            :param iq_rate:


                Specifies the I/Q rate for the acquisition. The value is expressed in samples per second (S/s).

                


            :type iq_rate: float

configure_number_of_records
---------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_number_of_records(number_of_records_is_finite, number_of_records)

            Configures the number of records in a finite acquisition or configures the device to continuously acquire records.

                            You can only configure the device to acquire multiple records if you set the **:py:attr:`nirfsa.Session.number_of_records_is_finite`** parameter to True.

                            If you configure the device to continuously acquire samples, it continues acquiring data until you call the :py:meth:`nirfsa.Session.abort` method to abort the acquisition. The device stores data in onboard memory in a circular fashion. After the device fills the memory, it starts overwriting previously acquired data from the beginning of the memory buffer. Retrieve the samples as they are being acquired, using one of the niRFSA fetch I/Q methods, to avoid overwriting data before you retrieve it.

                            To acquire more records than will fit into the device memory without continuously acquiring records, set the **:py:attr:`nirfsa.Session.number_of_records_is_finite`** parameter in this method to True and the :py:attr:`nirfsa.Session.allow_more_records_than_memory` property to True.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_number_of_records`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_number_of_records`


            :param number_of_records_is_finite:


                Specifies whether to configure the device to acquire a finite number of records or to acquire records continuously. The default is True.

                                        | Value         | Description                                                                                                                                                                                                                |
                                        |:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | True  | The device acquires a finite number of records.                                                                                                                                                                 |
                                        | False | The NI-RFSA device acquires records continuously until you call the :py:meth:`nirfsa.Session.abort` method to abort the acquisition. |

                


            :type number_of_records_is_finite: bool
            :param number_of_records:


                Specifies the number of records to acquire if **:py:attr:`nirfsa.Session.number_of_records_is_finite`** is set to True.

                


            :type number_of_records: int

configure_number_of_samples
---------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_number_of_samples(number_of_samples_is_finite, samples_per_record)

            Configures the number of samples in a finite acquisition or configures the device to continuously acquire samples.

                            If you configure the device for finite acquisition, it acquires the specified number of samples and then stops the acquisition. You can configure the device to acquire multiple records using the :py:meth:`nirfsa.Session.configure_number_of_records` method. Each record contains the number of samples specified in this method.

                            If you configure the device to continuously acquire samples, it continues acquiring data until you call the :py:meth:`nirfsa.Session.abort` method to abort the acquisition. The device stores data in onboard memory in a circular fashion. After the device fills the memory, it starts overwriting previously acquired data from the beginning of the memory buffer. Retrieve the samples as they are being acquired, using one of the niRFSA fetch I/Q methods, to avoid overwriting data before you retrieve it.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_number_of_samples`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_number_of_samples`


            :param number_of_samples_is_finite:


                Specifies whether to configure the device to acquire a finite number of samples or to acquire samples continuously. The default is True.

                                        | Value         | Description                                                                                                                                                                                                        |
                                        |:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | True  | The device acquires a finite number of samples.                                                                                                                                                         |
                                        | False | The device acquires samples continuously until you call the :py:meth:`nirfsa.Session.abort` method to abort the acquisition. |

                


            :type number_of_samples_is_finite: bool
            :param samples_per_record:


                Specifies the number of samples per record if **:py:attr:`nirfsa.Session.number_of_samples_is_finite`** is set to True.

                


            :type samples_per_record: int

configure_pxi_chassis_clk10
---------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_pxi_chassis_clk10(pxi_clk10_source)

            Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane.

                            This option can be configured only when the PXI-5600 is installed in the Star Trigger Controller Slot, also known as the System Timing Slot, of the PXI chassis.

                            **Supported Devices**: PXI-5600 (external digitizer mode), PXI-5661

                            **Related Topics**

                            `System Reference Clock <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/system-reference-clock.html>`_

            



            :param pxi_clk10_source:


                Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. This option can only be configured when the PXI-5600 is in Slot 2 of the PXI chassis.

                                        | Value                                              | Description                                                                                                                                                                                                                                                |
                                        |:----------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | :py:data:`~nirfsa.NIRFSA_VAL_NONE_STR` ('None')                  | The device does not drive the PXI 10 MHz backplane Reference Clock.                                                                                                                                                                             |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_ONBOARD_CLOCK_STR` ('OnboardClock') | The device drives the PXI 10 MHz backplane Reference Clock with the PXI-5600 onboard clock. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O connector on the PXI-5600 front panel to use this option.                           |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_REF_IN_STR` ('RefIn')               | The device drives the PXI 10 MHz backplane Reference Clock with the reference source attached to the PXI-5600 REF IN connector. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O on the PXI-5600 front panel to use this option. |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type pxi_clk10_source: str

configure_ref_clock
-------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_ref_clock(clock_source, ref_clock_rate)

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

            



            :param clock_source:


                specifies the source of the Reference Clock signal.
                                        | Clock Source          | Description |
                                        |-----------------------|-------------|
                                        | **Onboard Clock (default)** | Uses the onboard Reference Clock as the clock source. <br/>**PXIe-5830/5831/5832**-<br>- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT. <br>- PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br/>**PXIe-5831 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. <br/>**PXIe-5841 with PXIe-5655**-<br>- Lock to PXIe-5655 onboard clock. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. <br/>**PXIe-5842**-<br>- Lock to PXIe-5655 onboard clock. Use cables as shown in the Getting Started Guide. |
                                        | **RefIn** | Uses the signal at the front panel REF IN connector. <br/>**PXIe-5830/5831/5832**-<br>- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT; lock external signal to PXIe-3621 REF IN. <br>- PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT; lock external signal to PXIe-3622 REF IN. <br>- PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT; lock external signal to PXIe-3623 REF IN. <br/>**PXIe-5831 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. <br>- Lock external signal to PXIe-5653 REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. <br>- Lock external signal to PXIe-5653 REF IN. <br/>**PXIe-5841 with PXIe-5655**-<br>- Lock to signal at REF IN on PXIe-5655. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. <br/>**PXIe-5842**-<br>- Lock to signal at REF IN on PXIe-5655. Use cables as shown in the Getting Started Guide. |
                                        | **PXI Clock** | Uses the PXI_CLK signal present on the PXI backplane. |
                                        | **PXI_ClkMaster** | Valid only for PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653. <br/>**PXIe-5831 with PXIe-5653**-<br>- NI-RFSG configures PXIe-5653 to export Reference Clock. <br>- Configures PXIe-5820 and PXIe-3622 to use PXI_Clk. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- NI-RFSG configures PXIe-5653 to export Reference Clock. <br>- Configures PXIe-5820 and PXIe-3623 to use PXI_Clk. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. |

                


            :type clock_source: str
            :param ref_clock_rate:


                specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. This parameter is only valid when the **ref clock source** parameter is set to **RefIn**. The default value is Auto (-1.0), which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. Refer to the Reference Clock Rate property for possible values.

                


            :type ref_clock_rate: float

configure_reference_level
-------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_reference_level(reference_level)

            Configures the reference level.

                            The reference level represents the maximum expected power of an input RF signal.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Improving Your Measurements <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/measurement_guidelines.html>`_

                            `Programming Attenuation-Related Properties and Properties Using NI-RFSA <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/programming-attenuation.html>`_

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_reference_level`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_reference_level`


            :param reference_level:


                Specifies the expected total power, in dBm, of the RF input signal.

                


            :type reference_level: float

configure_resolution_bandwidth
------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_resolution_bandwidth(resolution_bandwidth)

            Configures the resolution bandwidth of a spectrum acquisition.

                            The resolution bandwidth controls the width of the frequency bins in the power spectrum computed by NI-RFSA. A larger value for resolution bandwidth means the frequency bins are wider, so you get fewer bins, or spectral lines.

                            By default, the resolution bandwidth value corresponds to the 3 decibels (dB) bandwidth of the window type NI-RFSA uses to compute the spectrum. To directly specify the frequency bin width, set the :py:attr:`nirfsa.Session.resolution_bandwidth_type` property to :py:data:`~nirfsa.SpectrumResolutionBandwidthType.BIN_WIDTH`

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Resolution Bandwidth <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/resolution-bandwidth.html>`_

                            `Improving Your Measurements <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/measurement_guidelines.html>`_

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_resolution_bandwidth`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_resolution_bandwidth`


            :param resolution_bandwidth:


                Specifies the resolution bandwidth of a spectrum acquisition. The value is expressed in hertz (Hz). Configure the type of resolution bandwidth with the :py:attr:`nirfsa.Session.resolution_bandwidth_type` property.

                


            :type resolution_bandwidth: float

configure_software_edge_advance_trigger
---------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_software_edge_advance_trigger()

            Configures the device to wait for a software Advance Trigger.

                            The Advance Trigger indicates where a new record begins. The device waits until you call the :py:meth:`nirfsa.Session.send_software_edge_trigger` method to assert the trigger.

                            ----
                            **Note**
                             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.configure_acquisition_type` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

                            ----

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



configure_software_edge_ref_trigger
-----------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_software_edge_ref_trigger(pretrigger_samples)

            Configures the device to wait for a software Reference Trigger to mark a reference point within the record.

                            The device waits until you call the :py:meth:`nirfsa.Session.send_software_edge_trigger` method to assert the trigger.

                            You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

                            ----
                            **Note**
                             The PXIe-5644/5645/5646 does not support the NI-TClk API.

                            ----

                            ----
                            **Note**
                             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.configure_acquisition_type` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

                            ----

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



            :param pretrigger_samples:


                Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.

                


            :type pretrigger_samples: int

configure_software_edge_start_trigger
-------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_software_edge_start_trigger()

            Configures the device to wait for a software Start Trigger at the beginning of the acquisition.

                            The device waits until you call the :py:meth:`nirfsa.Session.send_software_edge_trigger` method to assert the trigger.

                            You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

                            ----
                            **Note**
                             The PXIe-5644/5645/5646 does not support the NI-TClk API.

                            ----

                            ----
                            **Note**
                             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.configure_acquisition_type` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

                            ----

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



configure_spectrum_frequency_center_span
----------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_spectrum_frequency_center_span(center_frequency, span)

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

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_spectrum_frequency_center_span`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_spectrum_frequency_center_span`


            :param center_frequency:


                Specifies the center frequency in a spectrum acquisition. The value is expressed in hertz (Hz). The NI-RFSA device you use determines the valid range. Refer to your device specifications document for more information about frequency range.

                


            :type center_frequency: float
            :param span:


                Specifies the span of a spectrum acquisition. The value is expressed in hertz (Hz).

                                        ----

                                        *Note* For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect your measurements. Refer to the :py:attr:`nirfsa.Session.digitizer_dither_enabled` property for more information about dithering.

                                        ----

                


            :type span: float

configure_spectrum_frequency_start_stop
---------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_spectrum_frequency_start_stop(start_frequency, stop_frequency)

            Configures the start and stop frequencies of a spectrum read by NI-RFSA.

                            ----
                            **Note**
                            If you configure the spectrum span (**:py:attr:`nirfsa.Session.STOP_FREQUENCY`**  **:py:attr:`nirfsa.Session.START_FREQUENCY`**) to a value larger than the instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you request.

                            ----

                            ----
                            **Note**
                             For the PXIe-5663/5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the bandwidths that correspond to each span are different (10 MHz and 20 MHz, respectively).

                            ----

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_spectrum_frequency_start_stop`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_spectrum_frequency_start_stop`


            :param start_frequency:


                Specifies the lower limit of a span of frequencies. This value is expressed in hertz (Hz).

                


            :type start_frequency: float
            :param stop_frequency:


                Specifies the upper limit of a span of frequencies. This value is expressed in hertz (Hz).

                


            :type stop_frequency: float

create_configuration_list
-------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: create_configuration_list(list_name, number_of_list_attributes, set_as_active_list)

            Creates an empty configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_.

                            After a configuration list is created, enable the list using the **setAsActiveList** parameter. Call the :py:meth:`nirfsa.Session.create_configuration_list_step` method to add steps to the active configuration list.

                            **Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

                            **Related Topics**

                            `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

            



            :param list_name:


                Specifies the name of the configuration list. This string may not contain spaces, special characters, or punctuation marks.

                


            :type list_name: str
            :param number_of_list_attributes:


                Specifies the number of configuration list properties to set.

                


            :type number_of_list_attributes: int
            :param set_as_active_list:


                Sets this list as the active configuration list when this parameter is set to True.

                


            :type set_as_active_list: bool

            :rtype: int
            :return:


                    Specifies the properties that you intend to change between configuration list steps. Calling the :py:meth:`nirfsa.Session.create_configuration_list` method allocates space for each of the configuration list properties. When you use an NI-RFSG Set property method to set one of the properties in the configuration list, that property is set for one of the configuration list steps. Use the :py:attr:`nirfsa.Session.active_configuration_list_step` property to specify which configuration list step to configure.

                                            You can include the following properties in your configuration list based on your device:

                                            | Property                                                                                              | PXIe-5663E | PXIe-5665 | PXIe-5667 | PXIe-5644/5646 | PXIe-5645 | PXIe-5820 | PXIe-5830/5831/5832 | PXIe-5840/5841 | PXIe-5841 with PXIe-5655 | PXIe-5842 |
                                            |:-------------------------------------------------------------------------------------------------------|:-----------|:----------|:----------|:----------------|:----------|:----------|:----------------------|:---------------|:--------------------------|:-----------|
                                            | :py:attr:`nirfsa.Session.channel_coupling`                                                                           |            |           | Supported |                |           |           |                      |                |                            |            |
                                            | :py:attr:`nirfsa.Session.device_instantaneous_bandwidth`                                                             | Supported  | Supported | Supported |                |           | Supported |                      | Supported      |                            | Supported  |
                                            | :py:attr:`nirfsa.Session.downconverter_center_frequency`                                                             |            |           |           |                | Supported | Supported |                      | Supported      | Supported                  | Supported  |
                                            | :py:attr:`nirfsa.Session.downconverter_frequency_offset`                                                      |            |           |           |                |           | Supported |                      |                |                            |            |
                                            | :py:attr:`nirfsa.Session.downconverter_preselector_enabled`                                                        | Supported  | Supported |           |                |           |           |                      | Supported      | Supported                  | Supported  |
                                            | :py:attr:`nirfsa.Session.external_gain`                                                                              |            |           |           |                |           |           |                      | Supported      | Supported                  | Supported  |
                                            | :py:attr:`nirfsa.Session.frequency_settling`                                                                         | Supported  | Supported | Supported | Supported       | Supported | Supported | Supported            | Supported      |                            |            |
                                            | :py:attr:`nirfsa.Session.if_filter_bandwidth`                                                                        |            |           | Supported | Supported       | Supported | Supported | Supported            |                |                            | Supported  |
                                            | :py:attr:`nirfsa.Session.if_output_power_level`                                                                      |            | Supported |           |                |           |           |                      | Supported      |                            |            |
                                            | :py:attr:`nirfsa.Session.if_output_power_level_offset`                                                               |            | Supported |           |                |           |           |                      | Supported      |                            |            |
                                            | :py:attr:`nirfsa.Session.iq_carrier_frequency`                                                                       |            | Supported |           |                |           |           |                      | Supported      |                            |            |
                                            | :py:attr:`nirfsa.Session.iq_in_port_carrier_frequency`                                                               |            | Supported |           |                |           |           |                      | Supported      |                            |            |
                                            | :py:attr:`nirfsa.Session.iq_in_port_vertical_range`                                                                  |            |           |           |                |           |           |                      |                | Supported                  | Supported  |
                                            | :py:attr:`nirfsa.Session.iq_power_edge_ref_trigger_level`                                                            |            |           |           |                | Supported | Supported |                      |                |                            |            |
                                            | :py:attr:`nirfsa.Session.lo_source`                                                                                  | Supported  | Supported | Supported | Supported       |           |           | Supported            | Supported      | Supported                  | Supported  |
                                            | :py:attr:`nirfsa.Session.if_output_power_level`                                                                                | Supported  | Supported | Supported |                | Supported | Supported | Supported            |                | Supported                  | Supported  |
                                            | :py:attr:`nirfsa.Session.low_frequency_bypass_enabled`                                                               |            |           |           |                |           |           | Supported            | Supported      | Supported                  | Supported  |
                                            | :py:attr:`nirfsa.Session.mechanical_attenuation`                                                                     |            |           |           |                | Supported | Supported | Supported            |                |                            |            |
                                            | :py:attr:`nirfsa.Session.mechanical_attenuator_enabled`                                                              |            |           |           |                |           |           |                      |                | Supported                  |            |
                                            | :py:attr:`nirfsa.Session.minimum_acpr`                                                                                  |            |           |           |                |           |           |                      |                | Supported                  |            |
                                            | :py:attr:`nirfsa.Session.notch_filter_enabled`                                                                       |            |           |           |                |           |           |                      | Supported      |                            | Supported  |
                                            | :py:attr:`nirfsa.Session.number_of_samples`                                                                          | Supported  | Supported | Supported |                | Supported | Supported | Supported            | Supported      | Supported                  | Supported  |
                                            | :py:attr:`nirfsa.Session.osp_data_scaling_factor`                                                                     | Supported  | Supported |           |                |           |           | Supported            |                |                            | Supported  |
                                            | :py:attr:`nirfsa.Session.reference_level`                                                                            |            |           |           |                |           |           |                      |                |                            | Supported  |
                                            | :py:attr:`nirfsa.Session.attenuation`                                                                                |            |           |           |                |           |           |                      |                |                            | Supported  |
                                            | :py:attr:`nirfsa.Session.rf_out_lo_export_enabled`                                                                   |            |           |           |                |           |           |                      |                | Supported                  | Supported  |
                                            | :py:attr:`nirfsa.Session.rf_preamp_enabled`                                                                          |            |           |           |                |           |           |                      |                | Supported                  | Supported  |
                                            | :py:attr:`nirfsa.Session.rf_preselector_filter`                                                                      |            |           |           |                |           |           |                      |                | Supported                  | Supported  |
                                            | :py:attr:`nirfsa.Session.selected_ports`                                                                              |            |           |           |                |           |           |                      |                | Supported                  | Supported  |
                                            | :py:attr:`nirfsa.Session.timer_event_interval`                                                                       |            |           |           |                |           |           |                      |                | Supported                  | Supported  |

                    



create_configuration_list_step
------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: create_configuration_list_step(set_as_active_step)

            Creates a new configuration list step in the configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_ specified by the :py:attr:`nirfsa.Session.active_configuration_list` property.

                            When you create a configuration list step, a new instance of each property specified by the configuration list properties is created. Configuration list properties are specified when a configuration list is created.

                            **Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

                            **Related Topics**

                            `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

            



            :param set_as_active_step:


                Sets this step as the active step for the active configuration list. The default value for this parameter is True.

                                        If you set this parameter to False, you can select the active configuration list step using the :py:attr:`nirfsa.Session.active_configuration_list_step` property.

                


            :type set_as_active_step: bool

create_deembedding_sparameter_table_s2p_file
--------------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: create_deembedding_sparameter_table_s2p_file(port, table_name, s2p_file_path, sparameter_orientation)

            Creates an S-parameter de-embedding table for the port based on the specified S2P file.

                            If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.

                            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_

                            `S-parameters <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html#GUID-0AD828DE-398A-45C6-ABBA-4208DEB7DE1B__GUID-67A69775-E4DB-4FA2-84FE-C05977ED4184>`_

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

                


            :type table_name: str
            :param s2p_file_path:


                Specifies the path to the S2P file that contains de-embedding information for the specified port.

                


            :type s2p_file_path: str
            :param sparameter_orientation:


                Specifies the orientation of the data in the S2P file relative to the port on the DUT port.

                                       %enum_table{sparameter orientation}

                


            :type sparameter_orientation: int

delete_all_deembedding_tables
-----------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: delete_all_deembedding_tables()

            Deletes all configured de-embedding tables for the session.

                            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

            



delete_configuration_list
-------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: delete_configuration_list(list_name)

            Deletes a previously created configuration list and all the configuration list steps in the `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_ configuration list.

                            When a configuration list step is deleted, all the instances of the properties associated with the configuration list step are also removed. When you delete the active configuration list, NI-RFSA automatically resets the :py:attr:`nirfsa.Session.active_configuration_list` property to "" (empty string), which indicates no list is active, and the :py:attr:`nirfsa.Session.active_configuration_list_step` property to 0.

                            **Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

                            **Related Topics**

                            `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

            



            :param list_name:


                Specifies the name of the configuration list. This string may not contain spaces, special characters, or punctuation marks.

                


            :type list_name: str

delete_deembedding_table
------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: delete_deembedding_table(port, table_name)

            Deletes the selected de-embedding table for a given port.

                            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table.

                


            :type table_name: str

disable
-------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: disable()

            TBD

            



disable_advance_trigger
-----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: disable_advance_trigger()

            Configures the device to not use an Advance Trigger.

                            This method is necessary only if you configured an Advance Trigger in the past and now want to disable it.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



disable_ref_trigger
-------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: disable_ref_trigger()

            Configures the device to not wait for a Reference Trigger to mark a reference point within a record.

                            This method is necessary only if you previously configured a Reference trigger in the past and now want to disable it.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5840/5841/5842/5860

                            **Related Topics**

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



disable_start_trigger
---------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: disable_start_trigger()

            Configures the device to not wait for a Start Trigger at the beginning of the acquisition.

                            This method is necessary only if you previously configured a Start Trigger in the past and now want to disable it.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



enable_session_access
---------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: enable_session_access(enable)

            Enables or disables SFP session access for the specified instrument.

                            SFP session access allows the NI-RFSA Soft Front Panel (SFP) to access a device with an existing open session and can help you debug your code. To enable session access, pass True to the **enabled** parameter. To disable session access, pass False to the **enabled** parameter.

                            Refer to `Configuring SFP Session Access using LabWindows/CVI or C <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/configuring_session_access_labwindows.html>`_ for more information about SFP session access.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842/5860

                            ----
                            **Note**
                            NI-RFSA does not support NI-TClk when driver session debugging is enabled.

                            ----

            



            :param enable:


                Enables or disables SFP session access for the specified device.

                                        | Value         | Description                         |
                                        |:---------|:-------------------------|
                                        | True  | Enables session access.  |
                                        | False | Disables session access. |

                


            :type enable: bool

error_message
-------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: error_message(status_code, error_message)

            Converts a status code returned by an NI-RFSA method into a user-readable string.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5840

            



            :param status_code:


                Passes the **status** parameter that is returned from any NI-RFSA method.

                


            :type status_code: int
            :param error_message:


                Returns the user-readable message string that corresponds to the status code you specify.

                                        You must pass a ViChar array with at least 256 bytes to this parameter.

                


            :type error_message: str

error_query
-----------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: error_query()

            Reads an error code and a message from the instrument error queue.

            



            :rtype: tuple (error_code, error_message)

                WHERE

                error_code (int): 


                    Passes the **status** parameter that is returned from any NI-RFSA method.

                    


                error_message (str): 


                    Returns the user-readable message string that corresponds to the error code.

                                            You must pass a ViChar array with at least 256 bytes to this parameter.

                    



export_signal
-------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: export_signal(signal, signal_identifier, output_terminal)

            Routes signals (triggers, clocks, and events) to the specified output terminal.

                            If you export a signal with this method and [commit](rfsacref.chm/cvi:py:meth:`nirfsa.Session.commit`.html) the session, the signal is routed to the output terminal you specify. If you then reconfigure the signal to have a different output terminal, the previous output terminal is tri-stated when the session is next committed. If you set the **:py:attr:`nirfsa.Session.OUTPUT_TERMINAL`** parameter to :py:data:`~nirfsa.NIRFSA_VAL_DO_NOT_EXPORT_STR` and commit, the previous output terminal is tristated.

                            Any signals, except for those exported over PXI trigger lines, that are exported within a session persist after the session closes to prevent signal glitches between sessions. PXI trigger lines are always set to tristate when a session is closed. If you wish to have the output terminal tristated when the session closes, change the **:py:attr:`nirfsa.Session.OUTPUT_TERMINAL`** for the exported signal to :py:data:`~nirfsa.NIRFSA_VAL_DO_NOT_EXPORT_STR`, and commit the session again before closing it.

                            You can also tristate all PFI lines by setting the **resetDevice** parameter in the :py:meth:`nirfsa.Session.init` method to True or by using the :py:meth:`nirfsa.Session.reset` method.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



            :param signal:


                Specifies the type of signal to route.

                                        %enum_table{signal}

                


            :type signal: int
            :param signal_identifier:


                Specifies the user-defined signal to route. Specify the signal you have implemented using FPGA extensions.

                


            :type signal_identifier: str
            :param output_terminal:


                Specifies the terminal where the signal will be exported. You can also choose not to export any signal. For the PXIe-5841 with PXIe-5655, the signal is exported to the terminal on the PXIe-5841.

                                        | Value                             | Description                                                                                                                                                                                                                                |
                                        |:-----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DO_NOT_EXPORT_STR` | The signal is not exported.                                                                                                                                                                                                     |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_CLK_OUT_STR`       | The signal is exported to the CLK OUT connector on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                       |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_REF_OUT_STR`       | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_REF_OUT2_STR`          | The signal is exported to the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                                  |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PFI0_STR`          | The signal is exported to the PFI 0 connector.                                                                                                                                                                                  |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PFI1_STR`          | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.                                                                                                                                                    |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG0_STR`     | The signal is exported to the PXI trigger line 0.                                                                                                                                                                               |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG1_STR`     | The signal is exported to the PXI trigger line 1.                                                                                                                                                                               |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG2_STR`     | The signal is exported to the PXI trigger line 2.                                                                                                                                                                               |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG3_STR`     | The signal is exported to the PXI trigger line 3.                                                                                                                                                                               |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG4_STR`     | The signal is exported to the PXI trigger line 4.                                                                                                                                                                               |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG5_STR`     | The signal is exported to the PXI trigger line 5.                                                                                                                                                                               |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG6_STR`     | The signal is exported to the PXI trigger line 6.                                                                                                                                                                               |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG7_STR`     | The signal is exported to the PXI trigger line 7.                                                                                                                                                                               |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_STAR_STR`      | The signal is exported to the PXI star trigger line.                                                                                                                                                                            |
                                        | :py:data:`~nirfsa.ExportOutputTerm.PXIE_DSTARC`   | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                                          |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI0_STR` ('PFI0') | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                                           |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI1_STR` ('PFI1') | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                                           |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI2_STR` ('PFI2') | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                                           |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI3_STR` ('PFI3') | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                                           |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI4_STR` ('PFI4') | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                                           |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI5_STR` ('PFI5') | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                                           |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI6_STR` ('PFI6') | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                                           |
                                        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI7_STR` ('PFI7') | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                                           |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type output_terminal: str

ext_cal_store_baseline_for_self_calibration
-------------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: ext_cal_store_baseline_for_self_calibration(password, self_calibration_step)

            Specifies the external calibration step to run and stores the associated constants in the device memory so that they can be compared with the computed constants at run time.

                            A password is required to run the method.

                            **Supported Devices**: PXIe-5603/5605/5606, PXIe-5665/5668

            



            :param password:


                Specifies the password for the calibration session. The initial password is factory configured to NI. :py:attr:`nirfsa.Session.PASSWORD` can be a maximum of ten alphanumeric characters.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type password: str
            :param self_calibration_step:


                Specifies the step for which constants are computed.

                                        %enum_table{self calibration step}

                


            :type self_calibration_step: int

external_alignment_adjust_preselector
-------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: external_alignment_adjust_preselector(coefficients)

            Stores the preselector alignment coefficients that NI-RFSA uses to compute the preselector-tuning DAC value whenever the preselector is enabled.

                            These coefficients are based on the desired center frequency for the preselector.

                            **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

            



            :param coefficients:


                Specifies the coefficients in the polynomial used to map the preselector center frequency to a preselector-tuning DAC value. Enter the coefficients in the array in order of highest order coefficient first (index 0) down to lowest order coefficient last.

                


            :type coefficients: array.array("d")

fetch_iq_multi_record_complex_f32
---------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: fetch_iq_multi_record_complex_f32(starting_record, number_of_records, number_of_samples, timeout)

            Fetches I/Q data from multiple records in an acquisition.

                            A fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.

                            This method is not necessary if you use the :py:meth:`nirfsa.Session.read_iq_single_record_complex_f64` method because the :py:meth:`nirfsa.Session.read_iq_single_record_complex_f64` method performs the fetch as part of the method.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].fetch_iq_multi_record_complex_f32`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.fetch_iq_multi_record_complex_f32`


            :param starting_record:


                Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.

                


            :type starting_record: int
            :param number_of_records:


                Specifies the number of records to fetch.

                


            :type number_of_records: int
            :param number_of_samples:


                Specifies the number of samples per record.

                


            :type number_of_samples: int
            :param timeout:


                **PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the method to complete before returning a timeout error.

                                        **PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.

                                        ----

                                        For all supported devices, a value of  specifies the method waits until all data is available. A value of 0 specifies the method immediately returns available data.

                                        ----

                


            :type timeout: float

            :rtype: tuple (data, wfm_info)

                WHERE

                data (NIComplexNumberF32): 


                    Returns the acquired waveform for each record fetched. The waveforms are written sequentially in the array. Allocate an array at least as large as **:py:attr:`nirfsa.Session.number_of_samples`** times **:py:attr:`nirfsa.Session.number_of_records`** for this parameter.

                    


                wfm_info (WaveformInfo): 


                    Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read. Each element of this array corresponds to a record.

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

                    



fetch_iq_multi_record_complex_f64
---------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: fetch_iq_multi_record_complex_f64(starting_record, number_of_records, number_of_samples, timeout)

            Fetches I/Q data from multiple records in an acquisition.

                            A fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.

                            This method is not necessary if you use the :py:meth:`nirfsa.Session.read_iq_single_record_complex_f64` method because the :py:meth:`nirfsa.Session.read_iq_single_record_complex_f64` method performs the fetch as part of the method.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].fetch_iq_multi_record_complex_f64`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.fetch_iq_multi_record_complex_f64`


            :param starting_record:


                Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.

                


            :type starting_record: int
            :param number_of_records:


                Specifies the number of records to fetch.

                


            :type number_of_records: int
            :param number_of_samples:


                Specifies the number of samples per record.

                


            :type number_of_samples: int
            :param timeout:


                **PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the method to complete before returning a timeout error.

                                        **PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.

                                        ----

                                        For all supported devices, a value of  specifies the method waits until all data is available. A value of 0 specifies the method immediately returns available data.

                                        ----

                


            :type timeout: float

            :rtype: tuple (data, wfm_info)

                WHERE

                data (NIComplexNumber): 


                    Returns the acquired waveform for each record fetched. The waveforms are written sequentially in the array. Allocate an array at least as large as **:py:attr:`nirfsa.Session.number_of_samples`** times **:py:attr:`nirfsa.Session.number_of_records`** for this parameter.

                    


                wfm_info (WaveformInfo): 


                    Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read. Each element of this array corresponds to a record.

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

                    



get_attribute_vi_boolean
------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_attribute_vi_boolean(attribute_id)

            Queries the value of a ViBoolean property.

                            You can use this low-level method to get the values of inherent IVI properties and instrument-specific properties.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_attribute_vi_boolean`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_attribute_vi_boolean`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int

            :rtype: bool
            :return:


                    Returns the current value of the property. Pass the address of a ViBoolean variable.

                    



get_attribute_vi_int32
----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_attribute_vi_int32(attribute_id)

            Queries the value of a ViInt32 property.

                            You can use this low-level method to get the values of inherent IVI properties and instrument-specific properties.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_attribute_vi_int32`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_attribute_vi_int32`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int

            :rtype: int
            :return:


                    Returns the current value of the property. Pass the address of a ViInt32 variable.

                    



get_attribute_vi_int64
----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_attribute_vi_int64(attribute_id)

            Queries the value of a ViInt64 property.

                            You can use this low-level method to get the values of inherent IVI properties and instrument-specific properties.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_attribute_vi_int64`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_attribute_vi_int64`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int

            :rtype: int
            :return:


                    Returns the current value of the property. Pass the address of a ViInt64 variable.

                    



get_attribute_vi_real64
-----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_attribute_vi_real64(attribute_id)

            Queries the value of a ViReal64 property.

                            You can use this low-level method to get the values of inherent IVI properties and instrument-specific properties.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_attribute_vi_real64`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_attribute_vi_real64`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int

            :rtype: float
            :return:


                    Returns the current value of the property. Pass the address of a ViReal64 variable.

                    



get_attribute_vi_session
------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_attribute_vi_session(attribute_id)

            Queries the value of a ViSession property.

                            You can use this low-level method to get the values of inherent IVI properties and instrument-specific properties.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_attribute_vi_session`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_attribute_vi_session`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int

            :rtype: int
            :return:


                    Returns the current value of the property. Pass the address of a ViSession variable.

                    



get_attribute_vi_string
-----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_attribute_vi_string(attribute_id)

            Queries the value of a ViString property.

                            You can use this low-level method to get the values of inherent IVI properties and instrument-specific properties.

                            You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **:py:attr:`nirfsa.Session.BUF_SIZE`** parameter. If the current value of the property, including the terminating NULL byte, is larger than the size you indicate in the **:py:attr:`nirfsa.Session.BUF_SIZE`** parameter, the method copies buffer size  1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the method places "123" into the buffer and returns 7.

                            If you want to call this method just to get the required buffer size, you can pass 0 for **:py:attr:`nirfsa.Session.BUF_SIZE`** and VI_NULL for the **attributeValue** buffer.

                            **Supported Devices:** PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_attribute_vi_string`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_attribute_vi_string`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int

            :rtype: str
            :return:


                    The buffer in which the method returns the current value of the property. The buffer must be of type ViChar and have at least as many bytes as indicated in **:py:attr:`nirfsa.Session.BUF_SIZE`**.

                                            If you specify 0 for the **:py:attr:`nirfsa.Session.BUF_SIZE`** parameter, you can pass VI_NULL for this parameter.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.



get_cal_user_defined_info
-------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_cal_user_defined_info()

            Returns user-defined information from the onboard EEPROM.

                            **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698

            



            :rtype: str
            :return:


                    Returns a string containing the user-defined information.

                    



get_cal_user_defined_info_max_size
----------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_cal_user_defined_info_max_size()

            Returns the number of characters of user-defined information that can be stored in the device onboard EEPROM.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

            



            :rtype: int
            :return:


                    Returns the number of characters of user-defined information that can be stored in the device onboard EEPROM. The maximum size of the user-defined information array is 21 characters.

                    



get_device_response
-------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_device_response(response_type, buffer_size)

            Returns the requested response type, based on current NI-RFSA settings.

                            The PXI-5661 and PXIe-5663/5663E/5665/5667/5668 automatically corrects for the IF and RF response when you set the :py:attr:`nirfsa.Session.digital_if_equalization_enabled` property to True. If you are using external digitizer mode, you can use information returned from this method to correct your measurement.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_device_response`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_device_response`


            :param response_type:


                Specifies the IF, RF, or combined (IF and RF) response of the downconverter or NI-RFSA device that NI-RFSA returns. The default value is :py:data:`~nirfsa.ResponseType.DOWNCONVERTER_IF`.

                                        %enum_table{response type}

                


            :type response_type: int
            :param buffer_size:


                Specifies the size of the array you specify for the :py:attr:`nirfsa.Session.FREQUENCIES`, **:py:attr:`nirfsa.Session.MAGNITUDE_RESPONSE`**, and **:py:attr:`nirfsa.Session.PHASE_RESPONSE`** parameters.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type buffer_size: int

            :rtype: tuple (frequencies, magnitude_response, phase_response, number_of_frequencies)

                WHERE

                frequencies (array.array("d")): 


                    Returns an array containing the frequencies, in hertz (Hz), that correspond to the response data.

                                            Pass VI_NULL if you do not want to use this parameter.

                    


                magnitude_response (array.array("d")): 


                    Returns an array containing the magnitude of the requested response, in decibels (dB). The magnitude response is normalized to the center frequency at each frequency in the :py:attr:`nirfsa.Session.FREQUENCIES` array.

                                            Pass VI_NULL if you do not want to use this parameter.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.


                phase_response (array.array("d")): 


                    Returns an array containing the phase of the requested response, in radians. The phase response is normalized to the center frequency at each frequency entry in the :py:attr:`nirfsa.Session.FREQUENCIES` array.

                                            Pass VI_NULL if you do not want to use this parameter. This array may contain zeros if the device does not contain a stored phase response in its calibration data.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.


                number_of_frequencies (int): 


                    Returns the required number of elements in the :py:attr:`nirfsa.Session.FREQUENCIES` array and the response arrays. If **:py:attr:`nirfsa.Session.BUFFER_SIZE`** is 0, this parameter returns the expected array size. The expected array size depends on which NI-RFSA device you use (PXI-5661, PXIe-5663/5663E/5665) and on the current settings (PXIe-5663/5663E/5665 only).

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.



get_ext_cal_last_date_and_time
------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_ext_cal_last_date_and_time()

            Returns the date and time of the last successful external calibration.

                            The time returned is 24-hour local time, and the date is returned as integer values. For example, if the device was calibrated at 2:30 PM on December 31, 2010, this method returns 14 for the :py:attr:`nirfsa.Session.HOUR` parameter, 30 for the :py:attr:`nirfsa.Session.MINUTE` parameter, 12 for the :py:attr:`nirfsa.Session.MONTH` parameter, 31 for the :py:attr:`nirfsa.Session.DAY` parameter, and 2010 for the :py:attr:`nirfsa.Session.YEAR` parameter.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :rtype: tuple (year, month, day, hour, minute)

                WHERE

                year (int): 


                    Returns the year of the last external calibration.

                    


                month (int): 


                    Returns the month of the last external calibration.

                    


                day (int): 


                    Returns the day of the last external calibration.

                    


                hour (int): 


                    Returns the hour of the last external calibration.

                    


                minute (int): 


                    Returns the minute of the last external calibration.

                    



get_ext_cal_last_temp
---------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_ext_cal_last_temp()

            Returns the temperature of the last successful external calibration.

                            The temperature is returned in degrees Celsius.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

            



            :rtype: float
            :return:


                    Returns the temperature, in degrees Celsius, of the last external calibration.

                    



get_ext_cal_recommended_interval
--------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_ext_cal_recommended_interval()

            Returns the recommended interval between external calibrations, in months.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            



            :rtype: int
            :return:


                    Returns the recommended maximum interval between external calibrations, in months.

                    



get_fetch_backlog
-----------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_fetch_backlog(record_number)

            Returns the number of points acquired that have not yet been fetched.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_fetch_backlog`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_fetch_backlog`


            :param record_number:


                Specifies the record from which to read the backlog. Record numbers are zero-based.

                


            :type record_number: int

            :rtype: int
            :return:


                    Returns the number of samples available to read for the requested record.

                    



get_frequency_response
----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_frequency_response(buffer_size)

            Returns the requested response type, based on current NI-RFSA settings. The PXI-5661 and PXIe-5663/5663E/5665/5667/5668 automatically corrects the IF and RF response when you set the Digital IF Equalization Enabled property to TRUE. If you are using external digitizer mode, you can use information returned from this VI to correct your measurement.

                            Refer to the *Factory Calibration* topic for your device for more information about frequency-response calibration.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_frequency_response`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_frequency_response`


            :param buffer_size:


                Specifies the size of the array you specify for the :py:attr:`nirfsa.Session.FREQUENCIES`, **:py:attr:`nirfsa.Session.MAGNITUDE_RESPONSE`**, and **:py:attr:`nirfsa.Session.PHASE_RESPONSE`** parameters.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type buffer_size: int

            :rtype: tuple (frequencies, magnitude_response, phase_response, number_of_frequencies)

                WHERE

                frequencies (array.array("d")): 


                    Returns an array containing the frequencies, in hertz (Hz), that correspond to the response data.

                                            Pass VI_NULL if you do not want to use this parameter.

                    


                magnitude_response (array.array("d")): 


                    Returns an array containing the magnitude of the requested response, in decibels (dB). The magnitude response is normalized to the center frequency at each frequency in the :py:attr:`nirfsa.Session.FREQUENCIES` array.

                                            Pass VI_NULL if you do not want to use this parameter.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.


                phase_response (array.array("d")): 


                    Returns an array containing the phase of the requested response, in radians. The phase response is normalized to the center frequency at each frequency entry in the :py:attr:`nirfsa.Session.FREQUENCIES` array.

                                            Pass VI_NULL if you do not want to use this parameter. This array may contain zeros if the device does not contain a stored phase response in its calibration data.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.


                number_of_frequencies (int): 


                    Returns the required number of elements in the :py:attr:`nirfsa.Session.FREQUENCIES` array and the response arrays. If **:py:attr:`nirfsa.Session.BUFFER_SIZE`** is 0, this parameter returns the expected array size. The expected array size depends on which NI-RFSA device you use (PXI-5661, PXIe-5663/5663E/5665) and on the current settings (PXIe-5663/5663E/5665 only).

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.



get_gain_reference_cal_baseline
-------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_gain_reference_cal_baseline(buffer_size)

            Returns the gain reference calibration constants.

                            **Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5668

            



            :param buffer_size:


                Specifies the buffer size.

                


            :type buffer_size: int

            :rtype: tuple (gain_reference_cal_constants, number_of_gain_reference_cal_constants)

                WHERE

                gain_reference_cal_constants (array.array("d")): 


                    Returns the gain reference calibration constants.

                    


                number_of_gain_reference_cal_constants (int): 


                    Specifies the number of elements in the **:py:attr:`nirfsa.Session.GAIN_REFERENCE_CAL_CONSTANTS`** array.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.



get_number_of_spectral_lines
----------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_number_of_spectral_lines()

            Returns the number of spectral lines that NI-RFSA computes with the current power spectrum configuration.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_number_of_spectral_lines`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_number_of_spectral_lines`


            :rtype: int
            :return:


                    Returns the value of the :py:attr:`nirfsa.Session.number_of_spectral_lines` property.

                    



get_relay_name
--------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_relay_name(index)

            Returns the name of a relay for your device.

                            When you call this method and pass a VI_NULL pointer to the :py:attr:`nirfsa.Session.NAME` parameter, **:py:attr:`nirfsa.Session.BUFFER_SIZE`** is populated with the size of name including the terminating NULL byte. When you call this method and specify a value for **:py:attr:`nirfsa.Session.BUFFER_SIZE`** that is greater than or equal to the name of relay, the :py:attr:`nirfsa.Session.NAME` parameter returns the appropriate value.

                            **Supported Devices**: PXIe-5603/5605/5606.

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_relay_name`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_relay_name`


            :param index:


                Specifies the index of the relay.

                


            :type index: int

            :rtype: str
            :return:


                    Specifies the relay name, when used as an input. You can select VI_NULL or a pointer to a ViInt32 array. VI_NULL is the default. When **:py:attr:`nirfsa.Session.BUFFER_SIZE`** is greater than or equal to the number of relays, :py:attr:`nirfsa.Session.NAME` returns the relay name.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.



get_relay_operations_count
--------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_relay_operations_count()

            Returns an array consisting of all the relay counts for your device.

                            When you call this method and pass a VI_NULL pointer to the **:py:attr:`nirfsa.Session.OPERATIONS_COUNT`** parameter, **:py:attr:`nirfsa.Session.BUFFER_SIZE`** is populated with the number of relays on the device. When you call this method and specify a value for **:py:attr:`nirfsa.Session.BUFFER_SIZE`** that is greater than or equal to the number of relays, the **:py:attr:`nirfsa.Session.OPERATIONS_COUNT`** parameter returns the appropriate value.

                            **Supported Devices**: PXIe-5603/5605/5606, PXIe-5698

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_relay_operations_count`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_relay_operations_count`


            :rtype: array.array("l")
            :return:


                    Specifies the operations count array, when used as an input. You can select VI_NULL or a pointer to a ViInt32 array. VI_NULL is the default. When **:py:attr:`nirfsa.Session.BUFFER_SIZE`** is greater than or equal to the number of relays, **:py:attr:`nirfsa.Session.OPERATIONS_COUNT`** returns the number of relay operations.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.



get_self_cal_last_date_and_time
-------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_self_cal_last_date_and_time(self_calibration_step)

            Returns the date and time of the last successful self-calibration.

                            The time returned is 24-hour local time, and the date is returned as integer values. For example, if the device was calibrated at 2:30 PM on December 31, 2010, this method returns 14 for the :py:attr:`nirfsa.Session.HOUR` parameter, 30 for the :py:attr:`nirfsa.Session.MINUTE` parameter, 12 for the :py:attr:`nirfsa.Session.MONTH` parameter, 31 for the :py:attr:`nirfsa.Session.DAY` parameter, and 2010 for the :py:attr:`nirfsa.Session.YEAR` parameter.

                            ----
                            **Note**
                            For the PXIe-5644/5645/5646, you must select :py:data:`~nirfsa.SelfCalibrationStep.IMAGE_SUPPRESSION` for the **:py:attr:`nirfsa.Session.SELF_CALIBRATION_STEP`** parameter.

                            ----

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :param self_calibration_step:


                Specifies the self-calibration step to query for the last successful self-calibration date and time data.

                                        %enum_table{self calibration step}

                


            :type self_calibration_step: int

            :rtype: tuple (year, month, day, hour, minute)

                WHERE

                year (int): 


                    Returns the year of the last external calibration.

                    


                month (int): 


                    Returns the month of the last external calibration.

                    


                day (int): 


                    Returns the day of the last external calibration.

                    


                hour (int): 


                    Returns the year of the last external calibration. It is expressed as an integer.

                    


                minute (int): 


                    Returns the minute of the last external calibration.

                    



get_self_cal_last_temp
----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_self_cal_last_temp(self_calibration_step)

            Returns the temperature, in degrees Celsius, at the last successful self-calibration.

                            ----
                            **Note**
                            For the PXIe-5644/5645/5646, you must select :py:data:`~nirfsa.SelfCalibrationStep.IMAGE_SUPPRESSION` for the **selfCalibrationStep** parameter.

                            ----

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860

            



            :param self_calibration_step:


                Specifies the self-calibration step to query for the last successful self-calibration date and time data.

                                        %enum_table{self calibration step}

                


            :type self_calibration_step: int

            :rtype: float
            :return:


                    Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

                    



get_spectral_info_for_smt
-------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_spectral_info_for_smt()

            Returns information about the power spectrum NI-RFSA computes.

                            ----
                            **Note**
                            The NI Spectral Measurements Toolkit (SMT) requires this information.

                            ----

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            



            :rtype: SpectrumInfoT
            :return:


                    Returns returns properties of the computed spectrum such as spectrum type, spectrum scale (linear or logarithmic), the window type the method used to compute the spectrum, window size, and FFT size. Pass this parameter to subsequent methods that contain the **:py:attr:`nirfsa.Session.SPECTRUM_INFO`** parameter.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.



get_stream_endpoint_handle
--------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_stream_endpoint_handle(stream_endpoint)

            Returns a writer endpoint handle that you can use with NI-P2P to configure a peer-to-peer stream with the digitizer as an endpoint.

                            **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Configuring An Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_

                            [Peer-to-Peer Streaming](nirfsa.chm/p2p-streaming.html)

                            [Configuring a Peer-to-Peer Stream](nirfsa.chm/configuring-p2p-stream.html)

            



            :param stream_endpoint:


                Specifies the name of the stream resources you want to use.

                


            :type stream_endpoint: str

            :rtype: int
            :return:


                    Returns the writer endpoint handle which you use with NI-P2P to create a stream with the digitizer as an endpoint.

                    



get_terminal_name
-----------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_terminal_name(signal, signal_identifier)

            Returns the fully qualified name of the signal being queried.

                            Signals can be triggers, clocks, or events.

                            You can pass the **:py:attr:`nirfsa.Session.TERMINAL_NAME`** parameter that is returned to the **source** parameter of a configure trigger method.

                            **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :param signal:


                Specifies the signal for which you want to query the terminal.

                                       %enum_table{signal}

                


            :type signal: int
            :param signal_identifier:


                Specifies a particular instance of a trigger. NI-RFSA does not support this parameter.

                


            :type signal_identifier: str

            :rtype: str
            :return:


                    Returns the fully qualified name of the signal being queried.

                    



get_user_data
-------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_user_data(identifier, buffer_size)

            TBD

            



            :param identifier:


                


            :type identifier: str
            :param buffer_size:


                


            :type buffer_size: int

            :rtype: tuple (data, actual_data_size)

                WHERE

                data (array.array("b")): 


                    


                actual_data_size (int): 


                    



init
----

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: init(resource_name, id_query, reset)

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

            



            :param resource_name:


                Specifies the resource name of the device to initialize.

                                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.

                                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.

                


            :type resource_name: str
            :param id_query:


                Specifies whether NI-RFSA performs an ID query. When you perform an ID query, NI-RFSA verifies the device you initialize is supported.

                                        | Value              | Description                                                |
                                        |:--------------|:------------------------------------------------|
                                        | True (Yes) | Perform an ID query. This value is the default. |
                                        | False (No) | Do not perform an ID query.                     |

                


            :type id_query: bool
            :param reset:


                Specifies whether the NI-RFSA device is reset during the initialization procedure.

                                        | Value              | Description                                                    |
                                        |:--------------|:----------------------------------------------------|
                                        | True (Yes) | The device is reset.                                |
                                        | False (No) | The device is not reset. This value is the default. |

                


            :type reset: bool

            :rtype: int
            :return:


                    Identifies your instrument session.

                    



init_ext_cal
------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: init_ext_cal(resource_name, password, option_string)

            Creates and initializes a special NI-RFSA external calibration session.

                            The ViSession returned is an NI-RFSA session that you can use to configure the device using normal properties and methods. However, NI-RFSA sets flags that allow you to program an external calibration procedure using the calibration properties and methods.

                            **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            



            :param resource_name:


                Specifies the resource name of the device to initialize.

                                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI ** topic of the *Measurement & Automation Explorer Help*.

                                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.

                


            :type resource_name: str
            :param password:


                Specifies the password for the calibration session. The initial password is factory configured to NI. :py:attr:`nirfsa.Session.PASSWORD` can have a maximum of ten alphanumeric characters.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type password: str
            :param option_string:


                Sets the initial value of certain options for the session.

                                        The following options are used in this parameter.

                                        - calAction:create Use this option when starting a calibration step for the first time.
                                        - calAction:append Use this option when appending data to existing calibration data.

                


            :type option_string: str

            :rtype: int
            :return:


                    Identifies your instrument session.

                    



init_with_options
-----------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: init_with_options(resource_name, id_query, reset, option_string)

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

            



            :param resource_name:


                Specifies the resource name of the device to initialize.

                                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.

                                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.

                


            :type resource_name: str
            :param id_query:


                Specifies whether NI-RFSA performs an ID query. When you perform an ID query, NI-RFSA verifies the device you initialize is supported.

                                        | Value               |  Description                                               |
                                        |:--------------|:------------------------------------------------|
                                        | True (Yes) | Perform an ID query. This value is the default. |
                                        | False (No) | Do not perform an ID query.                     |

                


            :type id_query: bool
            :param reset:


                Specifies whether the NI-RFSA device is reset during the initialization procedure.

                                        | Value              |  Description                                                   |
                                        |:--------------|:----------------------------------------------------|
                                        | True (Yes) | The device is reset.                                |
                                        | False (No) | The device is not reset. This value is the default. |

                


            :type reset: bool
            :param option_string:


                Sets the initial value of certain properties for the session. The properties shown in the following table are used in this parameter.

                                        | Name             | Property                                                                                                                                  |
                                        |:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
                                        | RangeCheck       | :py:attr:`nirfsa.Session.range_check`                         |
                                        | QueryInstrStatus | :py:attr:`nirfsa.Session.query_instrument_status` |
                                        | Cache            | :py:attr:`nirfsa.Session.cache`                                     |
                                        | RecordCoercions  | :py:attr:`nirfsa.Session.record_coercions`               |
                                        | DriverSetup      | :py:attr:`nirfsa.Session.driver_setup`                       |
                                        | Simulate         | :py:attr:`nirfsa.Session.simulate`                               |

                                        The format of this string is *AttributeName=Value*, where *AttributeName* is the name of the property and *Value* is the value to which the property will be set. For example, you can simulate the PXIe-5663 using the following strings:

                                        *Simulate=1, DriverSetup=Model:5663\E*.

                                        *Simulate=1, DriverSetup=Model:5601*; *Digitizer:5622; LO:5652; LOBoardType:PXIe*.

                                        To set multiple properties, separate their assignments with a comma.

                                        Refer to `Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_ for more information about the driver setup string.

                                        Note: To simulate a device using the PXIe-5622 25 MHz digitizer, set the *Digitizer* field to 5622_25MHz_DDC and the *Simulate* field to 1. You can set the *Digitizer* field to 5622_25MHz_DDC only when using the PXIe-5665.

                


            :type option_string: str

            :rtype: int
            :return:


                    Identifies your instrument session.

                    



initialize_calibration_step
---------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: initialize_calibration_step(calibration_step)

            Initializes an EEPROM-specific calibration step.

                            **Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698

            



            :param calibration_step:


                Specifies the calibration step to initialize.

                                       %enum_table{self calibration step}

                


            :type calibration_step: int

initialize_external_alignment
-----------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: initialize_external_alignment(resource_name, option_string)

            Creates and initializes a special NI-RFSA external alignment session.

                            The ViSession returned is an NI-RFSA session that you can use to configure the device using normal properties and methods. However, NI-RFSA sets flags that allow you to program an external alignment procedure using the external alignment properties and methods.

                            **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

            



            :param resource_name:


                Specifies the resource name of the device to initialize.
                                        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.

                                        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.

                


            :type resource_name: str
            :param option_string:


                Sets the initial value of certain properties for the session. The properties shown in the following table are used in this parameter.

                                        | Name             | Property                                                                                                                                        |
                                        |:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | RangeCheck       | :py:attr:`nirfsa.Session.range_check`                         |
                                        | QueryInstrStatus | :py:attr:`nirfsa.Session.query_instrument_status` |
                                        | Cache            | :py:attr:`nirfsa.Session.cache`                                     |
                                        | RecordCoercions  | :py:attr:`nirfsa.Session.record_coercions`               |
                                        | DriverSetup      | :py:attr:`nirfsa.Session.driver_setup`                       |
                                        | Simulate         | :py:attr:`nirfsa.Session.simulate`                               |

                                        The format of this string is "*AttributeName=Value*", where *AttributeName* is the name of the property and *Value* is the value to which the property will be set. To set multiple properties, separate their assignments with a comma.

                


            :type option_string: str

            :rtype: int
            :return:


                    Identifies your instrument session.

                    



initialize_external_alignment_step
----------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: initialize_external_alignment_step(external_alignment_step)

            Initializes an EEPROM-specific external alignment step.

                            **Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

            



            :param external_alignment_step:


                Specifies which external alignment step you want to initialize.

                                        | Value                                     | Description                                                                                                                                            |
                                        |:-------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
                                        | EXT ALIGNMENT PRESELECTOR | Initiates preselector alignment. This step generates coefficients to align the preselector across the frequency range of 3.6 GHz to 14 GHz. |

                


            :type external_alignment_step: int

initiate
--------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: initiate()

            Commits settings to hardware, waits for hardware settling, and starts an acquisition.

                            You can use this method in conjunction with one of the niRFSA fetch I/Q methods to retrieve acquired I/Q data, or you can use the :py:meth:`nirfsa.Session.read_iq_single_record_complex_f64` method to both initiate the acquisition and retrieve I/Q data at one time.

                            ----
                            **Note**
                            If you are using external digitizer mode, this method commits settings and waits for settling, but it does not start an acquisition. Notice that using the :py:meth:`nirfsa.Session.commit` method on its own commits settings to hardware, but the device does not wait for hardware settling.

                            ----

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

                            `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

                            `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/hardware-state-diagram.html>`_

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



invalidate_all_attributes
-------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: invalidate_all_attributes()

            TBD

            



is_self_cal_valid
-----------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: is_self_cal_valid()

            Indicates which calibration steps contain valid calibration data.

                            To omit steps with valid calibration data from self-calibration, you can pass the **:py:attr:`nirfsa.Session.VALID_STEPS`** parameter to the **stepsToOmit** parameter of the :py:meth:`nirfsa.Session.self_calibrate` method.

                            **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :rtype: tuple (self_cal_valid, valid_steps)

                WHERE

                self_cal_valid (bool): 


                    Returns True if all the calibration data is valid and False if any of the calibration data is invalid.

                    


                valid_steps (int): 


                    Returns valid steps.

                                            ----
                                            If two or more calibration steps are valid, this parameter returns a bitwise-OR combination of the calibration steps. For example, if both :py:data:`~nirfsa.SelfCalibrationStep.IF_FLATNESS` and :py:data:`~nirfsa.SelfCalibrationStep.LO_SELF_CAL` steps are valid, NI-RFSA returns the following string:

                                            :py:data:`~nirfsa.SelfCalibrationStep.IF_FLATNESS` |

                                            :py:data:`~nirfsa.SelfCalibrationStep.LO_SELF_CAL`

                                            ----

                                            %enum_table{self calibration step}

                    



load_configurations_from_file
-----------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: load_configurations_from_file(file_path)

            Loads the configurations from the specified file to the NI-RFSA driver session.

            The VI does an implicit reset before loading the configurations from the file.

            **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].load_configurations_from_file`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.load_configurations_from_file`


            :param file_path:


                Specifies the absolute path of the file from which the NI-RFSA loads the configurations.

                


            :type file_path: str

lock_session
------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: lock_session()

            Obtains a multithread lock on the instrument session.

                            Before doing so, this method waits until all other execution threads have released their locks on the instrument session.

                            Other threads might have obtained a lock on this session in the following ways:

                            - Your application already called this method.
                            - A call to NI-RFSA locked the session.

                            After the call to this method returns successfully, no other threads can access the instrument session until you call the :py:meth:`nirfsa.Session.unlock_session` method. Use the :py:meth:`nirfsa.Session.lock_session` method and the :py:meth:`nirfsa.Session.unlock_session` method around a sequence of calls to NI-RFSA methods if you require that the NI-RFSA device retain its settings through the end of the sequence.

                            You can safely make nested calls to the :py:meth:`nirfsa.Session.lock_session` method within the same thread. To completely unlock the session, balance each call to the :py:meth:`nirfsa.Session.lock_session` method with a call to the :py:meth:`nirfsa.Session.unlock_session` method. If, however, you use **:py:attr:`nirfsa.Session.CALLER_HAS_LOCK`** in all calls to the :py:meth:`nirfsa.Session.lock_session` method and the :py:meth:`nirfsa.Session.unlock_session` method within a method, the IVI Library locks the session only once within the method regardless of the number of calls you make to the :py:meth:`nirfsa.Session.lock_session` method. Locking the session only once allows you to call the :py:meth:`nirfsa.Session.unlock_session` method just once at the end of the method.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :rtype: bool
            :return:


                    Keeps track of whether you obtain a lock and therefore need to unlock the session in complex methods. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to False. Pass the address of the same local variable to any other calls you make to this method or the :py:meth:`nirfsa.Session.unlock_session` method in the same method.

                                            This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.

                                            The :py:meth:`nirfsa.Session.lock_session` method and the :py:meth:`nirfsa.Session.unlock_session` method each inspect the current value and take the actions shown in the following table.

                                            | Method             | Boolean Value | Action                                                                                               |
                                            |:---------------------|:--------------|:-----------------------------------------------------------------------------------------------------|
                                            | :py:meth:`nirfsa.Session.lock_session`   | True       | The :py:meth:`nirfsa.Session.lock_session` method does not lock the session again.                                     |
                                            |                      | False      | The :py:meth:`nirfsa.Session.lock_session` method obtains the lock and sets the value of the parameter to True.     |
                                            | :py:meth:`nirfsa.Session.unlock_session` | False      | The :py:meth:`nirfsa.Session.unlock_session` method does not attempt to unlock the session.                            |
                                            |                      | True       | The :py:meth:`nirfsa.Session.unlock_session` method releases the lock and sets the value of the parameter to False. |

                                            Thus, you can call the :py:meth:`nirfsa.Session.unlock_session` method at the end of your method regardless of whether you actually have the lock.

                    



perform_thermal_correction
--------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: perform_thermal_correction()

            Corrects for temperature variations while acquiring the same signal for an extended period of time in a continuous acquisition.

                            NI-RFSA internally acquires the temperature every time you initiate an acquisition. If you are performing a continuous acquisition, National Instruments recommends calling this method once every 10 minutes in a stable temperature environment to periodically update temperature calibration. If the ambient temperature varies, call this method more frequently.

                            ----
                            **Note**
                            You cannot call this method if your device is operating in `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_.

                            ----

                            Refer to the *Thermal Management* section for your device for more information about typical operating temperatures.

                            **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842

            



read_iq_single_record_complex_f64
---------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: read_iq_single_record_complex_f64(timeout, data_array_size)

            Initiates an acquisition and fetches a single I/Q data record.

                            Do not use this method if you have configured the device to continuously acquire data samples or to acquire multiple records.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].read_iq_single_record_complex_f64`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.read_iq_single_record_complex_f64`


            :param timeout:


                Specifies in seconds the time allotted for the method to complete before returning a timeout error. A value of  specifies the method waits until all data is available.

                


            :type timeout: float
            :param data_array_size:


                Specifies the size of the array for the :py:attr:`nirfsa.Session.DATA` parameter. The array needs to be at least as large as the number of samples configured in the :py:meth:`nirfsa.Session.configure_number_of_samples` method.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type data_array_size: int

            :rtype: tuple (data, wfm_info)

                WHERE

                data (NIComplexNumber): 


                    Returns the acquired waveform. Allocate an NIComplexNumber array at least as large as the number of samples configured in the :py:meth:`nirfsa.Session.configure_number_of_samples` method.

                    


                wfm_info (WaveformInfo): 


                    Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read.

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

                    



read_power_spectrum_f32
-----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: read_power_spectrum_f32(timeout, data_array_size)

            Initiates a spectrum acquisition and returns power spectrum data.

                            ----
                            **Note**
                             Under certain configurations, negative infinity is returned from this VI. If the Reference Level is very high and if the Signal Bandwidth is comparatively less, the ADC returns zero, which equates to negative infinity in dBm. This is expected behavior.

                            ----

                            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].read_power_spectrum_f32`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.read_power_spectrum_f32`


            :param timeout:


                Specifies the time, in seconds, allotted for the method to complete before returning a timeout error. A value of specifies the method waits until all data is available.

                


            :type timeout: float
            :param data_array_size:


                Specifies the size of the array that is returned by the **:py:attr:`nirfsa.Session.POWER_SPECTRUM_DATA`** parameter. Use the :py:meth:`nirfsa.Session.get_number_of_spectral_lines` method to obtain the array size to allocate. The array must be at least as large as the number of spectral lines that NI-RFSA computes for the power spectrum.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type data_array_size: int

            :rtype: tuple (power_spectrum_data, spectrum_info)

                WHERE

                power_spectrum_data (array.array("f")): 


                    Returns power spectrum data. Allocate an array as large as **:py:attr:`nirfsa.Session.DATA_ARRAY_SIZE`**.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.


                spectrum_info (SpectrumInfoT): 


                    Returns additional information about the **:py:attr:`nirfsa.Session.POWER_SPECTRUM_DATA`** array. This information includes the frequency, in hertz (Hz), corresponding to the first element in the array, the frequency increment, in Hz, between adjacent array elements, and the number of spectral lines the method returned.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.



read_power_spectrum_f64
-----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: read_power_spectrum_f64(timeout, data_array_size)

            Initiates a spectrum acquisition and returns power spectrum data.

                            ----
                            **Note**
                             Under certain configurations, negative infinity is returned from this VI. If the Reference Level is very high and if the Signal Bandwidth is comparatively less, the ADC returns zero, which equates to negative infinity in dBm. This is expected behavior.

                            ----

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].read_power_spectrum_f64`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.read_power_spectrum_f64`


            :param timeout:


                Specifies the time, in seconds, allotted for the method to complete before returning a timeout error. A value of specifies the method waits until all data is available.

                


            :type timeout: float
            :param data_array_size:


                Specifies the size of the array that is returned by the **:py:attr:`nirfsa.Session.POWER_SPECTRUM_DATA`** parameter. Use the :py:meth:`nirfsa.Session.get_number_of_spectral_lines` method to obtain the array size to allocate. The array must be at least as large as the number of spectral lines that NI-RFSA computes for the power spectrum.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type data_array_size: int

            :rtype: tuple (power_spectrum_data, spectrum_info)

                WHERE

                power_spectrum_data (array.array("d")): 


                    Returns power spectrum data. Allocate an array as large as **:py:attr:`nirfsa.Session.DATA_ARRAY_SIZE`**.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.


                spectrum_info (SpectrumInfoT): 


                    Returns additional information about the **:py:attr:`nirfsa.Session.POWER_SPECTRUM_DATA`** array. This information includes the frequency, in hertz (Hz), corresponding to the first element in the array, the frequency increment, in Hz, between adjacent array elements, and the number of spectral lines the method returned.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.



reset
-----

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: reset()

            Resets all properties to default values, deletes all de-embedding tables, and stops the export of all external signals and events.

                            For the PXI-5600, this method does not reset the PXI Clock signal that is driven by devices installed in the Trigger Controller Slot, also known as the System Timing Slot.

                            This method resets all configured routes for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 in NI-RFSA and NI-RFSG. To avoid resetting routes on the device that are in use by NI-RFSG sessions, NI recommends using the :py:meth:`nirfsa.Session.reset_with_options` method, with **stepsToOmit** set to :py:data:`~nirfsa.StepsToOmit.ROUTES`.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

                            `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

            



reset_attribute
---------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: reset_attribute(attribute_id)

            Resets the property to its default value.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].reset_attribute`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.reset_attribute`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int

reset_device
------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: reset_device()

            Performs a hard reset on the device.

                            A hard reset consists of the following actions:

                            - Signal acquisition is stopped.
                            - All routes are released.
                            - External bidirectional terminals are tristated.
                            - FPGAs are reset.
                            - Hardware is configured to its default state.
                            - All session properties are reset to their default states.

                            During a device reset, routes of signals between this and other devices are released, regardless of which device created the route. For example, a trigger signal exported to a PXI trigger line that is used by another device is no longer exported.

                            On the PXI-5600, if you are driving the PXI_CLK10 line, you continue to drive the clock even after a device reset. To stop driving the PXI_CLK10 line, use the :py:meth:`nirfsa.Session.configure_pxi_chassis_clk10` method and set the **pxiClk10Source** parameter to :py:data:`~nirfsa.NIRFSA_VAL_NONE_STR` or set the :py:attr:`nirfsa.Session.pxi_chassis_clk10_source` property to :py:data:`~nirfsa.NIRFSA_VAL_NONE_STR`.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

            

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



reset_with_defaults
-------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: reset_with_defaults()

            TBD

            



reset_with_options
------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: reset_with_options(steps_to_omit)

            Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes.

                            For the PXI-5600, this method does not reset the PXI Clock signal that is driven by devices installed in the Star Trigger Controller Slot, also known as the System Timing Slot.

                            By default, this method resets all properties to their default values, deletes all de-embedding tables, aborts generation, clears all routes, and resets session properties to initial values. You can specify steps to omit using the steps to omit parameter. For example, if you specify :py:data:`~nirfsa.StepsToOmit.ROUTES` for the **:py:attr:`nirfsa.Session.STEPS_TO_OMIT`** parameter, this method does not release signal routes during the reset process.

                            When routes of signals between two devices are released, they are released regardless of which device created the route.

                            To avoid resetting routes on PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSG sessions, NI recommends using this method instead of :py:meth:`nirfsa.Session.reset`, with **:py:attr:`nirfsa.Session.STEPS_TO_OMIT`** set to :py:data:`~nirfsa.StepsToOmit.ROUTES`.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

                            `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :param steps_to_omit:


                Specifies a list of steps to skip during the reset process. The default value is :py:data:`~nirfsa.StepsToOmit.NONE`, which specifies that no step is omitted during reset.

                                        %enum_table{steps to omit}


                                        Note::py:data:`~nirfsa.StepsToOmit.ROUTES` is not supported in external calibration or alignment sessions.


                                        Note::py:data:`~nirfsa.StepsToOmit.ROUTES` is not supported for the PXI-5600/5661.

                


            :type steps_to_omit: int

revision_query
--------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: revision_query()

            Returns the revision numbers of the NI-RFSA instrument driver.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            



            :rtype: tuple (driver_rev, instr_rev)

                WHERE

                driver_rev (str): 


                    Returns the instrument driver software revision numbers in the form of a string. The value of the :py:attr:`nirfsa.Session.specific_driver_revision` property is returned.

                                            You must pass a ViChar array with 256 bytes or more to this parameter.

                    


                instr_rev (str): 


                    Returns the instrument firmware revision numbers in the form of a string. The value of the :py:attr:`nirfsa.Session.instrument_firmware_revision` property is returned.

                                            You must pass a ViChar array with 256 bytes or more to this parameter.

                    



save_configurations_to_file
---------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: save_configurations_to_file(file_path)

            Saves the configurations of the session to the specified file.

            **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].save_configurations_to_file`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.save_configurations_to_file`


            :param file_path:


                Specifies the absolute path of the file to which the NI-RFSA saves the configurations.

                


            :type file_path: str

self_cal
--------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: self_cal()

            TBD

            



self_calibrate
--------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: self_calibrate(steps_to_omit)

            Self-calibrates the NI-RFSA device and associated modules that support self-calibration.

                            If self-calibration is performed successfully, the new calibration constants are stored immediately in the self-calibration area of the module EEPROM. Refer to the specifications document for your device for more information about how often to self-calibrate.

                            For best results, NI recommends that you perform a complete self-calibration without omitting any steps. However, if the :py:meth:`nirfsa.Session.is_self_cal_valid` method indicates that the calibration data for a specific step is still valid, you can omit that step for faster execution.

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

            



            :param steps_to_omit:


                Specifies which calibration steps to skip as part of the self-calibration process. A value of 0 specifies all supported calibration steps are performed.

                                        ----

                                        To omit two or more calibration steps, specify a bitwise-OR combination of the following constants. For example, if you wanted to omit :py:data:`~nirfsa.SelfCalibrationStep.AMPLITUDE_ACCURACY` and :py:data:`~nirfsa.SelfCalibrationStep.LO_SELF_CAL`, you would pass the following string to the :py:meth:`nirfsa.Session.self_calibrate` method: :py:data:`~nirfsa.SelfCalibrationStep.AMPLITUDE_ACCURACY` | :py:data:`~nirfsa.SelfCalibrationStep.LO_SELF_CAL`

                                        ----

                                        | Value                                          |  Description                                                                                                                                                                                                                     |
                                        |:------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | :py:data:`~nirfsa.StepsToOmit.NONE`             | No step is omitted during self-calibration.                                                                                                                                                                           |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.PRESELECTOR_ALIGNMENT` | Not used by this method.                                                                                                                                                                                            |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.GAIN_REFERENCE`        | Not used by this method.                                                                                                                                                                                            |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.IF_FLATNESS`           | Not used by this method.                                                                                                                                                                                            |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.DIGITIZER_SELF_CAL`    | Not used by this method.                                                                                                                                                                                            |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.LO_SELF_CAL`           | Omits the Local Oscillator (LO) Self Cal step. If you omit this step and the :py:meth:`nirfsa.Session.is_self_cal_valid` method indicates the calibration data for this step is invalid, the LO phase-locked loop (PLL) may fail to lock. |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.AMPLITUDE_ACCURACY`    | Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy of the device is not adjusted.                                                                                                        |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.RESIDUAL_LO_POWER`     | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.                                                                                                           |
                                        |:py:data:`~nirfsa.SelfCalibrationStep.IMAGE_SUPPRESSION`      | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image Performance is not adjusted.                                                                                                     |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.SYNTHESIZER_ALIGNMENT` | Omits the Synthesizer Alignment step. If you omit this step, the LO PLL is not adjusted. This step is not valid for the PXIe-5820.                                                                                    |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.DC_OFFSET`             | Omits the DC Offset step. This step applies only to the PXIe-5820.                                                                                                                                                    |

                


            :type steps_to_omit: int

self_calibrate_range
--------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: self_calibrate_range(steps_to_omit, min_frequency, max_frequency, min_reference_level, max_reference_level)

            Self-calibrates all configurations within the specified frequency and reference level limits.

                            Self-calibration range data is valid until you restart the system or call the :py:meth:`nirfsa.Session.clear_self_calibrate_range` method.

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

            



            :param steps_to_omit:


                Specifies which calibration steps to skip as part of the self-calibration process. A value of 0 specifies all supported calibration steps are performed.

                                        ----

                                        To omit two or more calibration steps, specify a bitwise-OR combination of the following constants. For example, if you wanted to omit :py:data:`~nirfsa.SelfCalibrationStep.AMPLITUDE_ACCURACY` and :py:data:`~nirfsa.SelfCalibrationStep.LO_SELF_CAL`, you would pass the following string to the :py:meth:`nirfsa.Session.self_calibrate` method: :py:data:`~nirfsa.SelfCalibrationStep.AMPLITUDE_ACCURACY` | :py:data:`~nirfsa.SelfCalibrationStep.LO_SELF_CAL`

                                        ----

                                        | Value                                          |  Description                                                                                                                                                                                                                     |
                                        |:------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                        | :py:data:`~nirfsa.StepsToOmit.NONE`             | No step is omitted during self-calibration.                                                                                                                                                                           |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.PRESELECTOR_ALIGNMENT` | Not used by this method.                                                                                                                                                                                            |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.GAIN_REFERENCE`        | Not used by this method.                                                                                                                                                                                            |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.IF_FLATNESS`           | Not used by this method.                                                                                                                                                                                            |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.DIGITIZER_SELF_CAL`    | Not used by this method.                                                                                                                                                                                            |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.LO_SELF_CAL`           | Omits the Local Oscillator (LO) Self Cal step. If you omit this step and the :py:meth:`nirfsa.Session.is_self_cal_valid` method indicates the calibration data for this step is invalid, the LO phase-locked loop (PLL) may fail to lock. |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.AMPLITUDE_ACCURACY`    | Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy of the device is not adjusted.                                                                                                        |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.RESIDUAL_LO_POWER`     | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.                                                                                                           |
                                        |:py:data:`~nirfsa.SelfCalibrationStep.IMAGE_SUPPRESSION`      | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image Performance is not adjusted.                                                                                                     |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.SYNTHESIZER_ALIGNMENT` | Omits the Synthesizer Alignment step. If you omit this step, the LO PLL is not adjusted. This step is not valid for the PXIe-5820.                                                                                    |
                                        | :py:data:`~nirfsa.SelfCalibrationStep.DC_OFFSET`             | Omits the DC Offset step. This step applies only to the PXIe-5820.                                                                                                                                                    |

                


            :type steps_to_omit: int
            :param min_frequency:


                Specifies the minimum RF frequency in Hz.

                


            :type min_frequency: float
            :param max_frequency:


                Specifies the maximum RF frequency in Hz.

                


            :type max_frequency: float
            :param min_reference_level:


                Specifies the minimum reference level in dBm.

                


            :type min_reference_level: float
            :param max_reference_level:


                Specifies the maximum reference level in dBm.

                


            :type max_reference_level: float

self_test
---------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: self_test()

            TBD

            



send_software_edge_trigger
--------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: send_software_edge_trigger(trigger, trigger_identifier)

            Sends a trigger to the device when you use a software version of a supported trigger and the device is waiting for the trigger to be sent.

                            You can also use this method to override a hardware trigger.

                            This method returns an error in the following situations:

                            - You configure an invalid trigger.
                            - You set the **acquisitionType** to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.configure_acquisition_type` method.
                            - You have not previously called the :py:meth:`nirfsa.Session._initiate` method.

                            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                            **Related Topics**

                            `Software Trigger <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/software-edge-trigger.html>`_

                            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



            :param trigger:


                Specifies the software signal to send.

                                        %enum_table{trigger}

                


            :type trigger: int
            :param trigger_identifier:


                Specifies a particular instance of a trigger. NI-RFSA does not currently support this parameter.

                


            :type trigger_identifier: str

set_attribute_vi_boolean
------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: set_attribute_vi_boolean(attribute_id, value)

            Sets the value of a ViBoolean property.

                            Use this low-level method to set the values of inherent IVI properties and instrument-specific properties.

                            NI-RFSA contains high-level methods that set most of the instrument properties. NI recommends you use the high-level methods as much as possible. High-level methods handle order dependencies and multithread locking for you.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].set_attribute_vi_boolean`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.set_attribute_vi_boolean`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int
            :param value:


                Pass the value to which you want to set the property.

                                        ----

                                        Some of the values might not be valid depending on the current state of the instrument session.

                                        ----

                


            :type value: bool

set_attribute_vi_int32
----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: set_attribute_vi_int32(attribute_id, value)

            Sets the value of a ViInt32 property.

                            Use this low-level method to set the values of inherent IVI properties and instrument-specific properties.

                            NI-RFSA contains high-level methods that set most of the instrument properties. NI recommends you use the high-level methods as much as possible. High-level methods handle order dependencies and multithread locking for you.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].set_attribute_vi_int32`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.set_attribute_vi_int32`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int
            :param value:


                Pass the value to which you want to set the property.

                                        ----

                                        Some of the values might not be valid depending on the current state of the instrument session.

                                        ----

                


            :type value: int

set_attribute_vi_int64
----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: set_attribute_vi_int64(attribute_id, value)

            Sets the value of a ViInt64 property.

                            Use this low-level method to set the values of inherent IVI properties and instrument-specific properties.

                            NI-RFSA contains high-level methods that set most of the instrument properties. NI recommends you use the high-level methods as much as possible. High-level methods handle order dependencies and multithread locking for you.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].set_attribute_vi_int64`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.set_attribute_vi_int64`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int
            :param value:


                Pass the value to which you want to set the property.

                                        ----

                                        Some of the values might not be valid depending on the current state of the instrument session.

                                        ----

                


            :type value: int

set_attribute_vi_real64
-----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: set_attribute_vi_real64(attribute_id, value)

            Sets the value of a ViReal64 property.

                            Use this low-level method to set the values of inherent IVI properties, and instrument-specific properties.

                            NI-RFSA contains high-level methods that set most of the instrument properties. NI recommends you use the high-level methods as much as possible. High-level methods handle order dependencies and multithread-locking for you.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].set_attribute_vi_real64`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.set_attribute_vi_real64`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int
            :param value:


                Pass the value to which you want to set the property.

                                        ----

                                        Some of the values might not be valid depending on the current state of the instrument session.

                                        ----

                


            :type value: float

set_attribute_vi_session
------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: set_attribute_vi_session(attribute_id)

            Sets the value of a ViSession property.

                            Use this low-level method to set the values of inherent IVI properties and instrument-specific properties.

                            NI-RFSA contains high-level methods that set most of the instrument properties. NI recommends you use the high-level methods as much as possible. High-level methods handle order dependencies and multithread locking for you.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].set_attribute_vi_session`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.set_attribute_vi_session`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int

set_attribute_vi_string
-----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: set_attribute_vi_string(attribute_id, value)

            Sets the value of a ViString property.

                            Use this low-level method to set the values of inherent IVI properties and instrument-specific properties.

                            NI-RFSA contains high-level methods that set most of the instrument properties. NI recommends you use the high-level methods as much as possible. High-level methods handle order dependencies and multithread locking for you.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].set_attribute_vi_string`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.set_attribute_vi_string`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int
            :param value:


                Pass the value to which you want to set the property.

                                        ----

                                        Some of the values might not be valid depending on the current state of the instrument session.

                                        ----

                


            :type value: str

set_cal_user_defined_info
-------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: set_cal_user_defined_info(info)

            Writes user-defined information into the onboard EEPROM.

                            This should be called in its own session or else the data may be overwritten by a commit.

                            **Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698

            



            :param info:


                Specifies a string containing the user-defined information. This string can be up to 21 characters long.

                


            :type info: str

set_user_data
-------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: set_user_data(identifier, data)

            TBD

            



            :param identifier:


                


            :type identifier: str
            :param data:


                


            :type data: array.array("b")

unlock_session
--------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: unlock_session()

            Releases a lock obtained on an NI-RFSA device session by calling the :py:meth:`nirfsa.Session.lock_session` method.

                            Refer to the :py:meth:`nirfsa.Session.lock_session` method for additional information on session locks.

                            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

            



            :rtype: bool
            :return:


                    Keeps track of whether you obtain a lock and therefore need to unlock the session in complex methods. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to False. Pass the address of the same local variable to any other calls you make to this method or the :py:meth:`nirfsa.Session.unlock_session` method in the same method.

                                            This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.

                                            The :py:meth:`nirfsa.Session.lock_session` method and the :py:meth:`nirfsa.Session.unlock_session` method each inspect the current value and take the actions shown in the following table.

                                            | Method             | Boolean Value | Action                                                                                               |
                                            |:---------------------|:--------------|:-----------------------------------------------------------------------------------------------------|
                                            | :py:meth:`nirfsa.Session.lock_session`   | True       | The :py:meth:`nirfsa.Session.lock_session` method does not lock the session again.                                     |
                                            |                      | False      | The :py:meth:`nirfsa.Session.lock_session` method obtains the lock and sets the value of the parameter to True.     |
                                            | :py:meth:`nirfsa.Session.unlock_session` | False      | The :py:meth:`nirfsa.Session.unlock_session` method does not attempt to unlock the session.                            |
                                            |                      | True       | The :py:meth:`nirfsa.Session.unlock_session` method releases the lock and sets the value of the parameter to False. |

                                            Thus, you can call the :py:meth:`nirfsa.Session.unlock_session` method at the end of your method regardless of whether you actually have the lock.

                    




Properties
==========

_5665_preselector_tuning_dac_value
----------------------------------

    .. py:attribute:: _5665_preselector_tuning_dac_value

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **External Alignment:NI 5665/5668R:Preselector Tuning DAC Value**
                - C Attribute: **NIRFSA_ATTR_5665_PRESELECTOR_TUNING_DAC_VALUE**

absolute_delay
--------------

    .. py:attribute:: absolute_delay

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:Absolute Delay**
                - C Attribute: **NIRFSA_ATTR_ABSOLUTE_DELAY**

acquisition_type
----------------

    .. py:attribute:: acquisition_type

        Configures the session to either acquire I/Q data or to compute a power spectrum over the specified frequency range.

        **Defined Values:**

        %enum_table{acquisition type}

        **Default Value**: :py:data:`~nirfsa.AcquisitionType.IQ`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_acquisition_type`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.AcquisitionType |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition Type**
                - C Attribute: **NIRFSA_ATTR_ACQUISITION_TYPE**

active_configuration_list
-------------------------

    .. py:attribute:: active_configuration_list

        Specifies the configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_ to make active for configuration or initiation.

        Activating a list makes all properties in the list reflect the value of the properties that correspond to the set specified by the :py:attr:`nirfsa.Session.active_configuration_list` and the :py:attr:`nirfsa.Session.active_configuration_list_step` properties.

        Set this property to an empty string to disable RF list mode.

        **Default Value**: "" (empty string) for devices that support RF list mode. For all other devices, the default value is N/A.

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

        **Related Topics**

        `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.create_configuration_list`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration List:Active List**
                - C Attribute: **NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST**

active_configuration_list_step
------------------------------

    .. py:attribute:: active_configuration_list_step

        Specifies the step in the configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_ to make active for configuration or initiation.

        Activating a list makes all properties in the list reflect the value of the properties that correspond to the set specified by the :py:attr:`nirfsa.Session.active_configuration_list` and the :py:attr:`nirfsa.Session.active_configuration_list_step` properties.

        **Default Value**: 0 for devices that support RF list mode. For all other devices, the default value is N/A.

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

        **Related Topics**

        `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.create_configuration_list_step`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration List:Active Step**
                - C Attribute: **NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP**

advance_trigger_terminal_name
-----------------------------

    .. py:attribute:: advance_trigger_terminal_name

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

        - :py:meth:`nirfsa.Session.get_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Advance:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_ADVANCE_TRIGGER_TERMINAL_NAME**

advance_trigger_type
--------------------

    .. py:attribute:: advance_trigger_type

        Specifies whether you want the Advance Trigger to be a digital edge or software trigger.

        ----
        **Note**
        Set this property to :py:data:`~nirfsa.AdvanceTrigType.NONE` if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` or if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.configure_acquisition_type` method.

        ----

        **Defined Values:**

        %enum_table{advance trig type}

        **Default Value**: :py:data:`~nirfsa.AdvanceTrigType.NONE`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.AdvanceTrigType |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Advance:Type**
                - C Attribute: **NIRFSA_ATTR_ADVANCE_TRIGGER_TYPE**

allow_more_records_than_memory
------------------------------

    .. py:attribute:: allow_more_records_than_memory

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:IQ:Allow More Records Than Memory**
                - C Attribute: **NIRFSA_ATTR_ALLOW_MORE_RECORDS_THAN_MEMORY**

allow_out_of_specification_user_settings
----------------------------------------

    .. py:attribute:: allow_out_of_specification_user_settings

        Enables or disables warnings and errors when you set frequency, power, or bandwidth values beyond the limits of the NI-RFSA device specifications.

        When you set this property to :py:data:`~nirfsa.EnableAttrVals.ENABLED`, the driver does not report out-of-specification warnings and errors.

        **Defined Values:**

        %enum_table{enable attr vals}

        **Default Value**: :py:data:`~nirfsa.EnableAttrVals.DISABLED`

        **Supported Devices:** PXIe-5820/5830/5831/5840/5841/5842/5860



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Advanced:Allow Out Of Specification User Settings**
                - C Attribute: **NIRFSA_ATTR_ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS**

amplitude_settling
------------------

    .. py:attribute:: amplitude_settling

        Configures the amplitude settling accuracy in decibels.

        NI-RFSA waits until the RF power settles within the specified accuracy level after calling the :py:meth:`nirfsa.Session._initiate` method.

        Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.

        **Units**: dB

        **Default Value:** 0.5

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Amplitude Settling**
                - C Attribute: **NIRFSA_ATTR_AMPLITUDE_SETTLING**

arm_ref_trigger_type
--------------------

    .. py:attribute:: arm_ref_trigger_type

        Specifies whether you want the Arm Reference Trigger to be a digital edge or software trigger.

        ----
        **Note**
        The PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841 only support :py:data:`~nirfsa.ArmRefTrigType.NONE`.

        ----

        ----
        **Note**
        Set this property to :py:data:`~nirfsa.ArmRefTrigType.NONE` if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` or if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.configure_acquisition_type` method.

        ----

        **Defined Values:**

        %enum_table{arm ref trig type}

        **Default Value**: :py:data:`~nirfsa.ArmRefTrigType.NONE`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842/5860



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.ArmRefTrigType |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Arm Ref:Type**
                - C Attribute: **NIRFSA_ATTR_ARM_REF_TRIGGER_TYPE**

assoc_aux_switch_gain_uid
-------------------------

    .. py:attribute:: assoc_aux_switch_gain_uid

        

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIRFSA_ATTR_ASSOC_AUX_SWITCH_GAIN_UID**

attenuation
-----------

    .. py:attribute:: attenuation

        Specifies the nominal attenuation setting, in dB, for all attenuators before the first mixer in the RF signal chain.

        If you do not set this property, NI-RFSA automatically chooses an attenuation setting based on the reference level you configure. The valid values for this property depend on the device configuration.

        **PXI-5600/5661**: You can change the attenuation value to modify the amount of noise and distortion. Higher attenuation levels increase the noise level while decreasing distortion; lower attenuation levels decrease the noise level while increasing distortion.

        **PXIe-5601/5663/5663E**: You can change the attenuation value and the value of the :py:attr:`nirfsa.Session.if_attenuation` property to modify the amount of noise and distortion. Higher attenuation levels increase the noise level while decreasing distortion; lower attenuation levels decrease the noise level while increasing distortion.

        **PXIe-5603/5605/5606/5665/5668**: You can set multiple properties to modify the attenuation values for the device. Refer to `PXIe-5665 RF Attenuation and Signal Levels <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/attenuation-and-signal-levels.html>`_ for more information about configuring attenuation.

        **PXIe-5667**: This property specifies the nominal attenuation setting for all attenuators before the first RF mixer in the input signal path. This property is read-only when the :py:attr:`nirfsa.Session.low_frequency_bypass_enabled` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`.

        **PXIe-5693**: This property is read-only and returns the nominal RF attenuation of the PXIe-5693.

        **Units**: dB

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:RF Attenuation (dB)**
                - C Attribute: **NIRFSA_ATTR_ATTENUATION**

available_paths
---------------

    .. py:attribute:: available_paths

        Returns a comma separated list of the configurable paths available for use based on your instrument configuration.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Available Paths**
                - C Attribute: **NIRFSA_ATTR_AVAILABLE_PATHS**

available_ports
---------------

    .. py:attribute:: available_ports

        Returns a comma-separated list of the available ports for use based on your instrument configuration.

        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Available Ports**
                - C Attribute: **NIRFSA_ATTR_AVAILABLE_PORTS**

cache
-----

    .. py:attribute:: cache

        Specifies whether to cache the value of properties.

        If you set this property to True, NI-RFSA tracks the current NI-RFSA device settings and avoids sending redundant commands to the device.

        NI-RFSA can always cache or never cache particular properties, regardless of the setting of this property.

        Use the :py:meth:`nirfsa.Session.init_with_options` method to override the default value.

        **Defined Values:**

        |Value          | Description                      |
        |:---------|:---------------------|
        | True  | Caching is enabled.  |
        | False | Caching is disabled. |

        **Default Value**: True

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Cache**
                - C Attribute: **NIRFSA_ATTR_CACHE**

calibration_correction_100_mhz_filter
-------------------------------------

    .. py:attribute:: calibration_correction_100_mhz_filter

        Specifies the internal gain self-calibration correction for the 100 MHz IF filter path.

        The value you specify using this property overrides any previously-set value.

        **Units**: dB

        **Default Value**: 0

        **Supported Devices**: PXIe-5606

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Self Calibration:NI 5665/5668R:Calibration Correction for 100 MHz Filter**
                - C Attribute: **NIRFSA_ATTR_CALIBRATION_CORRECTION_100_MHZ_FILTER**

calibration_correction_300_khz_filter
-------------------------------------

    .. py:attribute:: calibration_correction_300_khz_filter

        Specifies the internal gain self-calibration correction for the 300 kHz IF filter path.

        The value you specify using this property overrides any previously-set value.

        **Units**: dB

        **Default Value**: 0

        **Supported Devices**: PXIe-5603/5605/5606

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Self Calibration:NI 5665/5668R:Calibration Correction for 300 kHz Filter**
                - C Attribute: **NIRFSA_ATTR_CALIBRATION_CORRECTION_300_KHZ_FILTER**

calibration_correction_320_mhz_filter
-------------------------------------

    .. py:attribute:: calibration_correction_320_mhz_filter

        Specifies the internal gain self-calibration correction for the 320 MHz IF filter path.

        The value you specify using this property overrides any previously-set value.

        **Units**: dB

        **Default Value**: 0

        **Supported Devices**: PXIe-5606

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Self Calibration:NI 5665/5668R:Calibration Correction for 320 MHz Filter**
                - C Attribute: **NIRFSA_ATTR_CALIBRATION_CORRECTION_320_MHZ_FILTER**

calibration_correction_5_mhz_filter
-----------------------------------

    .. py:attribute:: calibration_correction_5_mhz_filter

        Specifies the internal gain self-calibration correction for the 5 MHz IF filter path.

        The value you specify using this property overrides any previously-set value.

        **Units**: dB

        **Default Value**: 0

        **Supported Devices**: PXIe-5603/5605/5606

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Self Calibration:NI 5665/5668R:Calibration Correction for 5 MHz Filter**
                - C Attribute: **NIRFSA_ATTR_CALIBRATION_CORRECTION_5_MHZ_FILTER**

calibration_correction_765_mhz_filter
-------------------------------------

    .. py:attribute:: calibration_correction_765_mhz_filter

        Specifies the internal gain self-calibration correction for the 765 MHz IF filter path.

        The value you specify using this property overrides any previously-set value.

        **Units**: dB

        **Default Value**: 0

        **Supported Devices**: PXIe-5606

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Self Calibration:NI 5665/5668R:Calibration Correction for 765 MHz Filter**
                - C Attribute: **NIRFSA_ATTR_CALIBRATION_CORRECTION_765_MHZ_FILTER**

calibration_correction_through_filter
-------------------------------------

    .. py:attribute:: calibration_correction_through_filter

        Specifies the internal gain self-calibration correction for the IF filter through path.

        The value you specify using this property overrides any previously-set value.

        **Units**: dB

        **Default Value**: 0

        **Supported Devices**: PXIe-5603/5605

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Self Calibration:NI 5665/5668R:Calibration Correction for Through Filter**
                - C Attribute: **NIRFSA_ATTR_CALIBRATION_CORRECTION_THROUGH_FILTER**

cal_digitizer_id
----------------

    .. py:attribute:: cal_digitizer_id

        Returns the currently associated digitizer ID.

        Allows the use of self calibration data when configured in external digitizer mode.

        **Default Value**: "" (empty string) in external digitizer mode

        **Supported Devices**: PXIe-5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Self Calibration:Digitizer ID**
                - C Attribute: **NIRFSA_ATTR_CAL_DIGITIZER_ID**

cal_if_attenuation_index
------------------------

    .. py:attribute:: cal_if_attenuation_index

        Specifies the IF attenuation index from a table of valid settings.

        To select a correct attenuation table, set this property in conjunction with the :py:attr:`nirfsa.Session.cal_if_filter_selection` property. This property is valid only during a calibration session.

        **Valid Values**: 0 to 25

        **Default Value**: 0

        **Supported Devices:** PXIe-5694

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:IF Attenuation Table Index**
                - C Attribute: **NIRFSA_ATTR_CAL_IF_ATTENUATION_INDEX**

cal_if_attenuation_table_selection
----------------------------------

    .. py:attribute:: cal_if_attenuation_table_selection

        Specifies the IF attenuation table to be used for external calibration.

        This property is valid only in a calibration session.

        **Defined Values**:

        %enum_table{i fatten table sel}

        **Default Value**: :py:data:`~nirfsa.IFattenTableSel.STANDARD`

        **Supported Devices**: PXIe-5603/5605

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.IFattenTableSel |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:IF Attenuation Table Selection**
                - C Attribute: **NIRFSA_ATTR_CAL_IF_ATTENUATION_TABLE_SELECTION**

cal_if_attenuation_table_size
-----------------------------

    .. py:attribute:: cal_if_attenuation_table_size

        Returns the size of the selected IF attenuation table.

        **Valid Values**: 0-132

        **Default Value**: 0

        **Supported Devices**: PXIe-5606

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:IF Attenuation Table Size**
                - C Attribute: **NIRFSA_ATTR_CAL_IF_ATTENUATION_TABLE_SIZE**

cal_if_filter_selection
-----------------------

    .. py:attribute:: cal_if_filter_selection

        Specifies the IF filter path during calibration.

        The property is valid only during a calibration session.

        **Defined Values:**

        %enum_table{i ffilter sel}

        **Default Value**: :py:data:`~nirfsa.IFfilterSel._4`

        **Supported Devices**: PXIe-5694

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.IFfilterSel |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:IF Filter Selection**
                - C Attribute: **NIRFSA_ATTR_CAL_IF_FILTER_SELECTION**

cal_lo1_attenuation
-------------------

    .. py:attribute:: cal_lo1_attenuation

        Specifies the LO1 attenuation, in dB, during a calibration session.

        This property is valid only during a calibration session.

        **Valid Values and Default Values**:

        | Device         | Valid Values | Default Value |
        |:---------------|:-------------|:--------------|
        | PXIe-5603/5605 | 0 to 15.5    | 15.5          |
        | PXIe-5606      | 0 to 31      | 31            |

        **Supported Devices**: PXIe-5603/5605/5606

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:LO1 Attenuation**
                - C Attribute: **NIRFSA_ATTR_CAL_LO1_ATTENUATION**

cal_lo2_attenuation
-------------------

    .. py:attribute:: cal_lo2_attenuation

        Specifies the LO2 attenuation, in dB, during a calibration session.

        This property is valid only during a calibration session.

        **Valid Values and Default Values**:

        | Device         | Valid Values | Default Value |
        |:---------------|:-------------|:--------------|
        | PXIe-5603/5605 | 0 to 15.5    | 15.5          |
        | PXIe-5606      | 0 to 31      | 31            |

        **Supported Devices**: PXIe-5603/5605/5606

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:LO2 Attenuation**
                - C Attribute: **NIRFSA_ATTR_CAL_LO2_ATTENUATION**

cal_lo3_attenuation
-------------------

    .. py:attribute:: cal_lo3_attenuation

        Specifies the LO3 attenuation, in dB, during a calibration session. This property is valid only during a calibration session.

        **Valid Values and Default Values**:

        | Device         | Valid Values | Default Value |
        |:---------------|:-------------|:--------------|
        | PXIe-5603/5605 | 0 to 15.5    | 15.5          |
        | PXIe-5606      | 0 to 31      | 31            |

        **Supported Devices**: PXIe-5603/5605/5606

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:LO3 Attenuation**
                - C Attribute: **NIRFSA_ATTR_CAL_LO3_ATTENUATION**

cal_lo_path_selection
---------------------

    .. py:attribute:: cal_lo_path_selection

        Selects the LO signal path used during calibration.

        During noncalibration sessions, NI-RFSA implicitly derives the LO signal path from the center frequency. During calibration sessions, you must explicitly specify the LO signal path. This property is valid only during a calibration session.

        **Defined Values:**

        %enum_table{lo path sel}

        **Default Value**: :py:data:`~nirfsa.LoPathSel._1`

        **Supported Devices**: PXIe-5603/5605/5606

        The following table lists the characteristics of this property.

            +-----------------------+-----------------+
            | Characteristic        | Value           |
            +=======================+=================+
            | Datatype              | enums.LoPathSel |
            +-----------------------+-----------------+
            | Permissions           | read-write      |
            +-----------------------+-----------------+
            | Repeated Capabilities | None            |
            +-----------------------+-----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:LO Path Selection**
                - C Attribute: **NIRFSA_ATTR_CAL_LO_PATH_SELECTION**

cal_rf_electronic_attenuation_index
-----------------------------------

    .. py:attribute:: cal_rf_electronic_attenuation_index

        Selects the value of RF electronic attenuation from a table of valid configurations.

        This property is valid only during a calibration session and when you set the :py:attr:`nirfsa.Session.cal_rf_path_selection` property to :py:data:`~nirfsa.RfPathSel._1`.

        **Default Value**: N/A

        **Supported Devices:** PXIe-5603/5605/5606

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:RF Electronic Attenuation Table Index**
                - C Attribute: **NIRFSA_ATTR_CAL_RF_ELECTRONIC_ATTENUATION_INDEX**

cal_rf_lowband_signal_conditioning_path_selection
-------------------------------------------------

    .. py:attribute:: cal_rf_lowband_signal_conditioning_path_selection

        Specifies the RF lowband signal conditioning path.

        **Valid Values**:

        :py:data:`~nirfsa.RfLbSigCondPathSel._1`

        :py:data:`~nirfsa.RfLbSigCondPathSel._2`

        **Default Value**: :py:data:`~nirfsa.RfLbSigCondPathSel._1`

        **Supported Devices**: PXIe-5606

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.RfLbSigCondPathSel |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | None                     |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:RF Lowband Signal Conditioning Path Selection**
                - C Attribute: **NIRFSA_ATTR_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_SELECTION**

cal_rf_mechanical_attenuation_index
-----------------------------------

    .. py:attribute:: cal_rf_mechanical_attenuation_index

        Selects the value of the RF mechanical attenuation configuration from a table of valid configurations.

        This property is valid only during a calibration session.

        **Default Values**:

        **PXIe-5603/5605**: 3

        **PXIe-5606**: 2

        **Supported Devices:** PXIe-5603/5605/5606

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:RF Mechanical Attenuation Table Index**
                - C Attribute: **NIRFSA_ATTR_CAL_RF_MECHANICAL_ATTENUATION_INDEX**

cal_rf_path_selection
---------------------

    .. py:attribute:: cal_rf_path_selection

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
        | :py:data:`~nirfsa.RfPathSel._1` (1700)    | Specifies to use RF band 1. | PXIe-5601/5603/5605/5606 |
        | :py:data:`~nirfsa.RfPathSel._2` (1701)    | Specifies to use RF band 2. | PXIe-5601/5605/5606      |
        | :py:data:`~nirfsa.RfPathSel._3` (1702)    | Specifies to use RF band 3. | PXIe-5601                |
        | :py:data:`~nirfsa.RfPathSel._4` (1703)    | Specifies to use RF band 4. | PXIe-5601                |

        **Default Values**:

        **PXIe-5603/5605 (low band)/5606**: :py:data:`~nirfsa.RfPathSel._1`

        **PXIe-5601/5605 (high band)**: :py:data:`~nirfsa.RfPathSel._2`

        **Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5698

        The following table lists the characteristics of this property.

            +-----------------------+-----------------+
            | Characteristic        | Value           |
            +=======================+=================+
            | Datatype              | enums.RfPathSel |
            +-----------------------+-----------------+
            | Permissions           | read-write      |
            +-----------------------+-----------------+
            | Repeated Capabilities | None            |
            +-----------------------+-----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:RF Path Selection**
                - C Attribute: **NIRFSA_ATTR_CAL_RF_PATH_SELECTION**

cal_tone_power_referred_to_rf_in
--------------------------------

    .. py:attribute:: cal_tone_power_referred_to_rf_in

        Returns the power of a virtual signal connected to the RF IN connector on the PXIe-5693 front panel when the calibration tone is enabled.

        You can enable a calibration tone for the PXIe-5693 by setting the :py:attr:`nirfsa.Session.rf_conditioning_cal_tone_mode` property to :py:data:`~nirfsa.NIRFSA_VAL_CAL_TONE_LOWBAND_RF` or :py:data:`~nirfsa.NIRFSA_VAL_CAL_TONE_HIGHBAND_RF`.

        **Units**: dBm

        **Default Value**: N/A

        **Supported Devices**: PXIe-5693



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:NI 5693:Cal Tone Power Referred to RF IN**
                - C Attribute: **NIRFSA_ATTR_CAL_TONE_POWER_REFERRED_TO_RF_IN**

cal_tone_step_attenuation
-------------------------

    .. py:attribute:: cal_tone_step_attenuation

        Specifies the step attenuator to engage in the calibration tone path.

        **Units**: dB

        **Valid Values**: 2.00, 10.00

        **Default Value**: 2.00 dB

        **Supported Devices**: PXIe-5693

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5665/5668R:Cal Tone Step Attenuation**
                - C Attribute: **NIRFSA_ATTR_CAL_TONE_STEP_ATTENUATION**

center_frequency
----------------

    .. py:attribute:: center_frequency

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Center Frequency**
                - C Attribute: **NIRFSA_ATTR_CENTER_FREQUENCY**

channel_coupling
----------------

    .. py:attribute:: channel_coupling

        Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter.

        ----
        **Note**
        For the PXIe-5605/5606/5665/5667/5668, this property must be set to :py:data:`~nirfsa.ChannelCoupling.AC` when the DC block is present and set to :py:data:`~nirfsa.ChannelCoupling.DC` when the DC block is not present to ensure device specifications are met and proper calibration data is used. For more information about removing or attaching the DC block, refer to the `PXIe-5665 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/block-diagram.2.html>`_, the `PXIe-5605 Front Panel and LEDs <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/pinout.4.html>`_, the `PXIe-5667 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/block-diagram.html>`_, or the `PXIe-5668 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/block-diagram.html>`_ topics in this help file.

        ----

        **Valid Values**:

        **PXIe-5603/5665 (3.6 GHz)**: :py:data:`~nirfsa.ChannelCoupling.AC`, :py:data:`~nirfsa.ChannelCoupling.DC`

        **PXIe-5605/5665 (14 GHz)**: :py:data:`~nirfsa.ChannelCoupling.AC`, :py:data:`~nirfsa.ChannelCoupling.DC`

        **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low-frequency bypass path**: :py:data:`~nirfsa.ChannelCoupling.AC`, :py:data:`~nirfsa.ChannelCoupling.DC`

        **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**: :py:data:`~nirfsa.ChannelCoupling.AC`

        **PXIe-5667 (7 GHz)**: :py:data:`~nirfsa.ChannelCoupling.AC`

        **PXIe-5606/5668**: :py:data:`~nirfsa.ChannelCoupling.AC`, :py:data:`~nirfsa.ChannelCoupling.DC`

        **Defined Values**:

        %enum_table{channel coupling}

        **Default Value**: :py:data:`~nirfsa.ChannelCoupling.AC`

        **Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.ChannelCoupling |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:NI 5665/5667/5668R:Channel Coupling**
                - C Attribute: **NIRFSA_ATTR_CHANNEL_COUPLING**

common_mode
-----------

    .. py:attribute:: common_mode

        Specifies the common-mode level presented at each differential input terminal.

        Common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT).

        **Units**: volts

        **Default Value**: 0 V

        **Supported Devices**: PXIe-5820

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ In Port:Common Mode Level**
                - C Attribute: **NIRFSA_ATTR_COMMON_MODE**

configuration_list_step_in_progress
-----------------------------------

    .. py:attribute:: configuration_list_step_in_progress

        Returns the configuration list step that is currently programmed to the hardware.

        The list is zero-indexed. You can query this property only when a list is executed.

        **PXIe-5663E/5665/5667**: This property can be read only when a configuration list is running.

        **PXIe-5644/5645/5646**: This property always returns 0 when the configuration list is not running.

        **PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters**: If a configuration list is not running, this property returns the last step of a configuration list that is programmed to the hardware. If the device was last initiated without an active configuration list, this property returns 0.

        **Default Value**: N/A

        **Supported Devices:**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

        **Related Topics**

        `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration List:Step In Progress**
                - C Attribute: **NIRFSA_ATTR_CONFIGURATION_LIST_STEP_IN_PROGRESS**

contiguous_multirecord
----------------------

    .. py:attribute:: contiguous_multirecord

        This property is not for customer use.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:IQ:Advanced:Contiguous Multirecord**
                - C Attribute: **NIRFSA_ATTR_CONTIGUOUS_MULTIRECORD**

created_session_channel
-----------------------

    .. py:attribute:: created_session_channel

        

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIRFSA_ATTR_CREATED_SESSION_CHANNEL**

data_transfer_block_size
------------------------

    .. py:attribute:: data_transfer_block_size

        Specifies the maximum number of samples to transfer at one time from the device to host memory.

        Increasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may increase the amount of page-locked memory required from the system.

        **Default Values**:

        **PXIe-5668**: 0x2,000,000

        **All Other Devices**: 0x400,000

        **Supported Devices:**: PXI-5661, PXIe-5663/5663E/5665/5667/5668

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Fetch:Data Transfer:Data Transfer Block Size**
                - C Attribute: **NIRFSA_ATTR_DATA_TRANSFER_BLOCK_SIZE**

data_transfer_maximum_bandwidth
-------------------------------

    .. py:attribute:: data_transfer_maximum_bandwidth

        Specifies the maximum bandwidth that the device can consume.

        ----
        **Note**
        The NI device limits itself to transfer fewer bytes per second on the PCI Express bus than the value you specify for this property.

        ----

        **Default Value**: N/A

        **Supported Devices:**: PXI-5661, PXIe-5663/5663E/5665

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Fetch:Data Transfer:Data Transfer Maximum Bandwidth**
                - C Attribute: **NIRFSA_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH**

ddc_ref_trigger_override
------------------------

    .. py:attribute:: ddc_ref_trigger_override

        This property is not for customer use.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Advanced:DDC Reference Trigger Override**
                - C Attribute: **NIRFSA_ATTR_DDC_REF_TRIGGER_OVERRIDE**

decimation_delay
----------------

    .. py:attribute:: decimation_delay

        Specifies the sub-sample delay, in seconds, to apply to the acquired signal.

        To set this property, the NI-RFSA device must be in the Configuration state.

        **Valid Values:** -4.16 ns to +4.16 ns

        **Default Value**: 0

        **Supported Devices:** PXIe-5644/5645/5646

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:Decimation Delay**
                - C Attribute: **NIRFSA_ATTR_DECIMATION_DELAY**

deembedding_compensation_gain
-----------------------------

    .. py:attribute:: deembedding_compensation_gain

        Returns the de-embedding gain applied to compensate for the mismatch on the specified port. Use the Active Channel property to specify the name of the port to configure for de-embedding.

        If de-embedding is enabled, NI-RFSA uses the returned compensation gain to remove the effects of the external network between the instrument and the DUT.

        **Supported Devices**: PXIe-5830/5831/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **De-embedding:Compensation Gain**
                - C Attribute: **NIRFSA_ATTR_DEEMBEDDING_COMPENSATION_GAIN**

deembedding_selected_table
--------------------------

    .. py:attribute:: deembedding_selected_table

        Selects the de-embedding table to apply to the measurements on the specified port.

        To use this property, you must use the channelName parameter of the :py:meth:`nirfsa.Session.set_attribute_vi_string` method to specify the name of the port to configure for de-embedding.

        If de-embedding is enabled, NI-RFSA uses the specified table to remove the effects of the external network between the instrument and the DUT.

        Use the :py:meth:`nirfsa.Session._create_deembedding_sparameter_table_array` method to create tables.

        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **De-embedding:Selected Table**
                - C Attribute: **NIRFSA_ATTR_DEEMBEDDING_SELECTED_TABLE**

deembedding_type
----------------

    .. py:attribute:: deembedding_type

        Specifies the type of de-embedding to apply to measurements on the specified port.

        To use this property, you must use the channelName parameter of the :py:meth:`nirfsa.Session.set_attribute_vi_int32` method to specify the name of the port to configure for de-embedding.

        If you set this property to :py:data:`~nirfsa.DeembeddingTypeAttrVals.SCALAR` or :py:data:`~nirfsa.DeembeddingTypeAttrVals.VECTOR`, NI-RFSA adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT.

        **Defined Values:**

        %enum_table{deembedding type attr vals}

        **Default Value**: :py:data:`~nirfsa.DeembeddingTypeAttrVals.SCALAR`

        **Valid Values for PXIe-5830/5832/5840/5841/5842/5860** : :py:data:`~nirfsa.DeembeddingTypeAttrVals.SCALAR` or  :py:data:`~nirfsa.DeembeddingTypeAttrVals.NONE`

        **Valid Values for PXIe-5831:** :py:data:`~nirfsa.DeembeddingTypeAttrVals.VECTOR`, :py:data:`~nirfsa.DeembeddingTypeAttrVals.SCALAR`, or :py:data:`~nirfsa.DeembeddingTypeAttrVals.NONE`. :py:data:`~nirfsa.DeembeddingTypeAttrVals.VECTOR` is only supported for TRX Ports in a Semiconductor Test System (STS).

        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------+
            | Characteristic        | Value                         |
            +=======================+===============================+
            | Datatype              | enums.DeembeddingTypeAttrVals |
            +-----------------------+-------------------------------+
            | Permissions           | read-write                    |
            +-----------------------+-------------------------------+
            | Repeated Capabilities | None                          |
            +-----------------------+-------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **De-embedding:Type**
                - C Attribute: **NIRFSA_ATTR_DEEMBEDDING_TYPE**

device_configuration_temperature
--------------------------------

    .. py:attribute:: device_configuration_temperature

        Specifies the temperature, in degrees Celsius, that NI-RFSA uses to calculate the device configuration settings.

        ----
        **Note**
        For most applications, you can choose not to set this property, so NI-RFSA uses the device temperature to calculate best attenuation settings. Set this property only if you want NI-RFSA to maintain the same device configuration settings from acquisition to acquisition, independent of device temperature changes.

        ----

        **PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: This property is read-only.

        **Units**: degrees Celsius

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Device Configuration Temperature (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_DEVICE_CONFIGURATION_TEMPERATURE**

device_instantaneous_bandwidth
------------------------------

    .. py:attribute:: device_instantaneous_bandwidth

        Specifies the instantaneous bandwidth of the device in hertz (Hz).

        The instantaneous bandwidth is the effective real-time bandwidth of the signal path for your configuration.

        Specify the maximum instantaneous bandwidth needed for your measurement. NI-RFSA coerces the actual IF filter to use based on other measurement constraints such as the :py:attr:`nirfsa.Session.if_filter_bandwidth` property and the :py:attr:`nirfsa.Session.digital_if_equalization_enabled` property.

        To change the value that NI-RFSA uses for the maximum size of multispan acquisition subspans, use the :py:attr:`nirfsa.Session.fft_width` property.

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Device Instantaneous Bandwidth (Hz)**
                - C Attribute: **NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH**

device_temperature
------------------

    .. py:attribute:: device_temperature

        Returns the current temperature, in degrees Celsius, of the module.

        **PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860**: If you query this property during RF list mode, list steps may take longer to complete during list execution.

        **PXIe-5830/5831/5832**: To use this property, you must first set the channelName parameter of the :py:meth:`nirfsa.Session.set_attribute_vi_real64` method to using the appropriate string for your instrument configuration. Setting the :py:meth:`nirfsa.Session.set_attribute_vi_real64` property is not required for the PXIe-3621/3622. Refer to the following table to determine which strings are valid for your configuration.

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

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Device Temperature (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_DEVICE_TEMPERATURE**

digital_edge_advance_trigger_source
-----------------------------------

    .. py:attribute:: digital_edge_advance_trigger_source

        Specifies the source terminal for the Advance Trigger.

        This property is used only when the :py:attr:`nirfsa.Session.advance_trigger_type` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`.

        **Defined Values:**

        %enum_table{output term}

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_digital_edge_ref_trigger`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Advance:Digital Edge:Source**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_SOURCE**

digital_edge_arm_ref_trigger_source
-----------------------------------

    .. py:attribute:: digital_edge_arm_ref_trigger_source

        Specifies the source terminal for the digital edge Arm Reference Trigger.

        This property is used only when the :py:attr:`nirfsa.Session.arm_ref_trigger_type` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`.

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



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Arm Ref:Digital Edge:Source**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_ARM_REF_TRIGGER_SOURCE**

digital_edge_configuration_list_step_trigger_source
---------------------------------------------------

    .. py:attribute:: digital_edge_configuration_list_step_trigger_source

        Configures the list trigger source.

        The default value is the :py:data:`~nirfsa.Signal.END_OF_RECORD_EVENT`. When the value is :py:data:`~nirfsa.Signal.END_OF_RECORD_EVENT`, this will signal the instrument to reconfigure from configuration N to configuration N + 1 after the End Of Record Event, and before the Ready For Advance Event. If you configure this property to any other value, the instrument reconfiguration will occur whenever the specified trigger is asserted, which may be decoupled from the acquisition state machine. Therefore, if you trigger a reconfiguration during a record acquisition, you may see transient data in the record, which should be discarded by the application. NI recommends you to use this property only in case of streaming.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Configuration List Step:Digital Edge:Source**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE**

digital_edge_ref_trigger_edge
-----------------------------

    .. py:attribute:: digital_edge_ref_trigger_edge

        Specifies the active edge for the Reference Trigger.

        This property is used only when the :py:attr:`nirfsa.Session.ref_trigger_type` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`.

        **Defined Values:**

        %enum_table{ref trig dig edge edge}

        **Default Value**: :py:data:`~nirfsa.RefTrigDigEdgeEdge.RISING`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_digital_edge_ref_trigger`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.RefTrigDigEdgeEdge |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | None                     |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Digital Edge:Edge**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_REF_TRIGGER_EDGE**

digital_edge_ref_trigger_source
-------------------------------

    .. py:attribute:: digital_edge_ref_trigger_source

        Specifies the source terminal for the digital edge Reference Trigger.

        This property is used only when the :py:attr:`nirfsa.Session.ref_trigger_type` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`.

        **Defined Values:**

        %enum_table{output term}

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Digital Edge:Source**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE**

digital_edge_start_trigger_edge
-------------------------------

    .. py:attribute:: digital_edge_start_trigger_edge

        Specifies the active edge for the Start Trigger.

        This property is used only when the :py:attr:`nirfsa.Session.start_trigger_type` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`.

        **Defined and Valid Values:**

        | Value                         | Description                                           | Valid For                           |
        |:------------------------------|:------------------------------------------------------|:------------------------------------|
        | :py:data:`~nirfsa.StartTrigDigEdgeEdge.RISING` (900)  | The trigger asserts on the rising edge of the signal. | PXI-5661, PXIe-5663/5663E/5665/5668 |
        | :py:data:`~nirfsa.StartTrigDigEdgeEdge.FALLING` (901) | The trigger asserts on the falling edge of the signal | PXIe-5668                           |

        **Default Value**: :py:data:`~nirfsa.StartTrigDigEdgeEdge.RISING`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_digital_edge_start_trigger`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.StartTrigDigEdgeEdge |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Digital Edge:Edge**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

digital_edge_start_trigger_source
---------------------------------

    .. py:attribute:: digital_edge_start_trigger_source

        Specifies the source terminal for the Start Trigger.

        This property is used only when the :py:attr:`nirfsa.Session.start_trigger_type` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`.

        **Defined Values**:

        %enum_table{output term}

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_digital_edge_start_trigger`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Digital Edge:Source**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE**

digital_gain
------------

    .. py:attribute:: digital_gain

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Digital Gain (dB)**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_GAIN**

digital_if_equalization_enabled
-------------------------------

    .. py:attribute:: digital_if_equalization_enabled

        Enables use of the digital equalization filter for the RF downconverter.

        **PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: The only valid value for this property is True.

        ----
        **Note**
        For PXIe-5665/5667 devices, digital IF equalization is supported only with a 150 MHz clock. You cannot set this property to True if the :py:attr:`nirfsa.Session.digitizer_sample_clock_timebase_source` property is set to :py:data:`~nirfsa.DigitizerSampClkTimebaseSrc.LO_REF_CLK`.

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Digital IF Equalization Enabled**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_IF_EQUALIZATION_ENABLED**

digitizer_dither_enabled
------------------------

    .. py:attribute:: digitizer_dither_enabled

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
        For the PXIe-5820/5830/5831/5832/5840/5841/5842, only :py:data:`~nirfsa.EnableAttrVals.ENABLED` is supported.

        ----

        **Default Value**: :py:data:`~nirfsa.EnableAttrVals.ENABLED`

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Digitizer Dither Enabled**
                - C Attribute: **NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED**

digitizer_sample_clock_rate
---------------------------

    .. py:attribute:: digitizer_sample_clock_rate

        Returns the actual frequency, in hertz (Hz), of the digitizer Sample Clock.

        **Units**: hertz (Hz)

        **Supported Devices**: PXIe-5668

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Digitizer Sample Clock Rate**
                - C Attribute: **NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_RATE**

digitizer_sample_clock_timebase_rate
------------------------------------

    .. py:attribute:: digitizer_sample_clock_timebase_rate

        Specifies the frequency, in hertz (Hz), of the external clock used as the timebase source if you set the :py:attr:`nirfsa.Session.digitizer_sample_clock_timebase_source` property to an external source, such as :py:data:`~nirfsa.NIRFSA_VAL_CLK_IN_STR`, :py:data:`~nirfsa.DigitizerSampClkTimebaseSrc.LO_REF_CLK`, or :py:data:`~nirfsa.DigitizerSampClkTimebaseSrc.DOWNCONVERTER_LO2_OUT`

        **PXI-5661**If this property is set to a value less than 60 MHz, signals at frequencies just above the 20 MHz passband of the downconverter may be aliased back into the passband. This aliasing occurs because the IF frequency of the downconverter is 15 MHz, and the upper end of the passband is 25 MHz. At sampling rates below 60 MHz, the Nyquist frequency is close to the end of the passband and creates aliases that are not filtered effectively by the downconverter.

        **Units**: hertz (Hz)

        **Valid and Default Values**:

        | Device                    | Valid Values            | Default Value |
        |:--------------------------|:------------------------|:--------------|
        | PXI-5661                  | Any frequency 226552.5 MHz | 100 MHz       |
        | PXIe-5663/5663E/5665/5667 | 150 MHz                 | 150 MHz       |
        | PXIe-5668                 | 2 GHz                   | 2 GHz         |

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Digitizer Sample Clock Timebase Rate**
                - C Attribute: **NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_RATE**

digitizer_sample_clock_timebase_source
--------------------------------------

    .. py:attribute:: digitizer_sample_clock_timebase_source

        Specifies the source of the Sample Clock timebase, which is the timebase used to control waveform sampling.

        **Defined Values:**

        %enum_table{digitizer samp clk timebase src}

        **Default Value**: :py:data:`~nirfsa.DigitizerSampClkTimebaseSrc.ONBOARD_CLOCK`

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------------+
            | Characteristic        | Value                             |
            +=======================+===================================+
            | Datatype              | enums.DigitizerSampClkTimebaseSrc |
            +-----------------------+-----------------------------------+
            | Permissions           | read-write                        |
            +-----------------------+-----------------------------------+
            | Repeated Capabilities | None                              |
            +-----------------------+-----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Digitizer Sample Clock Timebase Source**
                - C Attribute: **NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE**

digitizer_temperature
---------------------

    .. py:attribute:: digitizer_temperature

        Returns the current temperature, in degrees Celsius, of the digitizer module.

        **PXIe-5820/5840/5841/5842**: If you query this property during RF list mode, list steps may take longer to complete during list execution.

        **Default Value**: N/A

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Digitizer Temperature (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_DIGITIZER_TEMPERATURE**

digitizer_vertical_range
------------------------

    .. py:attribute:: digitizer_vertical_range

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Digitizer Vertical Range**
                - C Attribute: **NIRFSA_ATTR_DIGITIZER_VERTICAL_RANGE**

done_event_terminal_name
------------------------

    .. py:attribute:: done_event_terminal_name

        Returns the fully qualified signal name as a string.

        **Default Values**:

        **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>DoneEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

        **PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>DoneEvent</i>, where *ModuleName* is the name of your device in MAX.

        **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>DoneEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

        **All other devices**: /<i>DigitizerName</i>/<i>DoneEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.get_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Done:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_DONE_EVENT_TERMINAL_NAME**

downconverter_cal_tone_frequency
--------------------------------

    .. py:attribute:: downconverter_cal_tone_frequency

        Specifies the frequency of the RF downconverter calibration tone, in hertz (Hz).

        **Valid Values**

        **PXIe-5603/5605**: 134 MHz to 13.2 GHz

        **PXIe-5606**: 34.5 MHz to 4 GHz

        **Default Value**: 612.5 MHz

        **Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Self Calibration:NI 5665/5667/5668R:Downconverter Cal Tone Frequency**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_CAL_TONE_FREQUENCY**

downconverter_cal_tone_mode
---------------------------

    .. py:attribute:: downconverter_cal_tone_mode

        Specifies the location in a signal path where an RF downconverter calibration tone is injected or whether the tone is disabled.

        Refer to `PXIe-5665 Theory of Operation <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/block-diagram.2.html>`_, `PXIe-5667 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/block-diagram.html>`_, or `PXIe-5668 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/block-diagram.html>`_ for more information about signal paths for your device.

        **Defined and Valid Values:**

        | Value                                          | Description                                                                                | Valid For           |
        |:-----------------------------------------------|:-------------------------------------------------------------------------------------------|:--------------------|
        |  :py:data:`~nirfsa.CalToneMode.DISABLED` (2700)            | Disables the calibration tone for the associated signal path.                              | PXIe-5603/5605/5606 |
        | :py:data:`~nirfsa.CalToneMode.CAL_TONE_LOWBAND_RF` (2701)          | Injects the calibration tone into the low band RF signal path.                             | PXIe-5603/5605/5606 |
        | :py:data:`~nirfsa.CalToneMode.CAL_TONE_HIGHBAND_RF` (2702)         | Injects the calibration tone into the high band RF signal path.                            | PXIe-5605/5606      |
        | :py:data:`~nirfsa.CalToneMode.CAL_TONE_HIGHBAND_IF` (2703)         | Injects the calibration tone into the high band IF signal path.                            | PXIe-5605           |
        | :py:data:`~nirfsa.CalToneMode.CAL_TONE_LOWBAND_RF_WITHOUT_ALC` (2704) | Injects the calibration tone into the low band RF signal path, bypassing the ALC.          | PXIe-5606           |
        | :py:data:`~nirfsa.CalToneMode.CAL_TONE_COMB_GENERATOR` (2705)      | Injects the calibration tone into the high band RF signal path through the Comb Generator. | PXIe-5606           |

        **Default Value**:  :py:data:`~nirfsa.CalToneMode.DISABLED`

        **Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.CalToneMode |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Self Calibration:NI 5665/5667/5668R:Downconverter Cal Tone Mode**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_CAL_TONE_MODE**

downconverter_center_frequency
------------------------------

    .. py:attribute:: downconverter_center_frequency

        Enables in-band retuning and specifies the current frequency, in hertz (Hz), of the RF downconverter.

        If you set this property, any measurements outside the instantaneous bandwidth of the device are invalid. To disable in-band retuning, reset the property or call the :py:meth:`nirfsa.Session.reset_device` method.

        After you set this property, the downconverter is locked to that frequency until the value is changed or the property is reset. Locking the downconverter to a fixed value allows frequencies within the instantaneous bandwidth of the downconverter to be measured with minimal overhead, decreasing tuning time.

        **Valid Values**: Any supported tuning frequency of the device

        **PXIe-5820**: The only valid value for this property is 0 Hz.

        **Default Value**:

        **PXIe-5694**: The default value for the PXIe-5694 is 193.6 MHz unless you set the :py:attr:`nirfsa.Session.signal_conditioning_enabled` property to  :py:data:`~nirfsa.SignalConditioningEnabled.BYPASSED`, in which case the default value is 187.5 MHz.

        **All other devices**: The carrier frequency or spectrum center frequency. NI-RFSA sets this property to the default value based on the value of the :py:attr:`nirfsa.Session.acquisition_type` property.

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Advanced:Downconverter Center Frequency**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY**

downconverter_frequency_offset
------------------------------

    .. py:attribute:: downconverter_frequency_offset

        Specifies an offset from the I/Q carrier frequency for the downconverter.

        If you set this property, any measurements outside the instantaneous bandwidth of the device are invalid. After you set this property, the RF downconverter is locked to that frequency offset until the value is changed or the property is reset.

        **Valid Values:**

        **PXIe-5646:**: -100 MHz to +100 MHz

        **PXIe-5830/5831/5832/5840/5841:**: -500 MHz to +500 MHz

        **All other devices:**: -42 MHz to +42 MHz

        **Default Values:**: For spectrum acquisition types the driver automatically calculates the default to avoid residual LO power. For I/Q acquisition types the default is 0 Hz. If the center frequency is set to a non-multiple of the :py:attr:`nirfsa.Session.lo_frequency_step_size` property, the :py:attr:`nirfsa.Session.downconverter_frequency_offset` property is set to compensate for the difference.

        **Supported Devices:**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

        **Related Topics**

        `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-selection.html>`_

        `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-selection.html>`_

        `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-selection.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Acquisition:Advanced:Downconverter Frequency Offset**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET**

downconverter_frequency_offset_mode
-----------------------------------

    .. py:attribute:: downconverter_frequency_offset_mode

        Specifies whether to allow NI-RFSA to select the downconveter frequency offset.

        You can either set an offset yourself or let NI-RFSA select one for you.

        Placing the downconverter center frequency outside the bandwidth of your input signal can help avoid issues such as LO leakage.

        To set an offset yourself, set this property to :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.AUTOMATIC` or :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.USER_DEFINED`, and set either the :py:attr:`nirfsa.Session.downconverter_center_frequency` or the :py:attr:`nirfsa.Session.downconverter_frequency_offset` properties.

        To allow NI-RFSA to automatically select the downconverter frequency offset, set this property to :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.AUTOMATIC` or :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.ENABLED` and configure the :py:attr:`nirfsa.Session.signal_bandwidth` property to describe your expected input signal. The signal bandwidth must be no greater than half the specified value of the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property, minus a device-specific guard band. Do not set the :py:attr:`nirfsa.Session.downconverter_center_frequency` or :py:attr:`nirfsa.Session.downconverter_frequency_offset` properties. If all conditions are met, NI-RFSA places the downconverter center frequency outside the signal bandwidth. Set this property to :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.ENABLED` if you want to receive an error any time NI-RFSA is unable to apply automatic offset.

        When you set an offset yourself or do not use an offset, the reference frequency for gain is near the downconverter center frequency, and :py:attr:`nirfsa.Session.downconverter_frequency_offset_mode` returns :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.USER_DEFINED`. When NI-RFSA automatically sets an offset, the reference frequency for gain is the :py:attr:`nirfsa.Session.iq_carrier_frequency`, and :py:attr:`nirfsa.Session.downconverter_frequency_offset_mode` returns :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.ENABLED`. Refer to the specifications document for your device for more information about gain, flatness, and reference frequencies.

        ----
        **Note**
        Below 120 MHz, the PXIe-5841 does not use an LO and :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.ENABLED` is unavailable. Refer to the *PXIe-5841 Automatic Frequency Offset* topic for more information about using an automatic offset with an external LO.

        ----

        **Defined Values:**

        %enum_table{downconverter frequency offset mode}

        **Default Value:** :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.AUTOMATIC`

        **Supported Devices**: PXIe-5830/5831/5832/5841/5842

        **Related Topics**

        `PXIe-5830 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/automatic-frequency-offset.html>`_

        `PXIe-5831/5832 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/automatic-frequency-offset.html>`_

        `PXIe-5841 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/automatic-frequency-offset.html>`_



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------------+
            | Characteristic        | Value                                  |
            +=======================+========================================+
            | Datatype              | enums.DownconverterFrequencyOffsetMode |
            +-----------------------+----------------------------------------+
            | Permissions           | read-write                             |
            +-----------------------+----------------------------------------+
            | Repeated Capabilities | None                                   |
            +-----------------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Advanced:Downconverter Frequency Offset Mode**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE**

downconverter_gain
------------------

    .. py:attribute:: downconverter_gain

        Returns the net signal gain for the NI-RFSA device at the current NI-RFSA settings and temperature.

        NI-RFSA scales the acquired I/Q and spectrum data from the digitizer using the value of this property.

        For a vector signal analyzer (VSA), the system is defined as the RF downconverter and all interfaces between the RF IN connector on the RF downconverter front panel and the IF IN connector on the digitizer front panel. For a spectrum monitoring receiver, the system is defined as the RF preselector, RF downconverter, and IF conditioning modules including all interfaces between the RF IN connector on the RF preselector module front panel and the IF IN connector on the digitizer front panel.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Downconverter Gain (dB)**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_GAIN**

downconverter_loop_bandwidth
----------------------------

    .. py:attribute:: downconverter_loop_bandwidth

        Configures the loop bandwidth of the RF downconverter tuning PLLs.

        To set this property, the NI-RFSA device must be in the Configuration state.

        **PXI-5600/5661** : For signal bandwidths greater than 10 MHz, :py:data:`~nirfsa.DownconverterLoopBandwidth.WIDE` is the only value supported for this property.

        **PXIe-5601/5663/5663E** : The PXIe-5601 does not support the :py:data:`~nirfsa.DownconverterLoopBandwidth.MEDIUM` value. This property is not supported if you are using an external LO.

        **PXIe-5830/5831/5832/5840/5841/5842** : The PXIe-5840/5841/5842 supports only :py:data:`~nirfsa.DownconverterLoopBandwidth.MEDIUM` for this property. This property is not supported if you are using an external LO.

        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsa.Session.set_attribute_vi_int32` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

        **Defined Values:**

        %enum_table{downconverter loop bandwidth}

        **Default Values**:

        **PXI-5600** : :py:data:`~nirfsa.DownconverterLoopBandwidth.WIDE`

        **PXIe-5601** : :py:data:`~nirfsa.DownconverterLoopBandwidth.NARROW`

        **PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842** : :py:data:`~nirfsa.DownconverterLoopBandwidth.MEDIUM`

        **Supported Devices**: PXI-5600, PXIe-5601 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E, PXIe-5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.DownconverterLoopBandwidth |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | None                             |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Downconverter Loop Bandwidth**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_LOOP_BANDWIDTH**

downconverter_preselector_enabled
---------------------------------

    .. py:attribute:: downconverter_preselector_enabled

        Specifies whether the tunable preselector is enabled on the downconverter.

        ----
        **Note**
        All devices support setting this property to :py:data:`~nirfsa.EnablePreselector.DISABLED` or :py:data:`~nirfsa.EnablePreselector.ENABLED_WHEN_IN_SIGNAL_PATH`. Only devices with a preselector support setting this property to :py:data:`~nirfsa.EnablePreselector.ENABLED`.

        ----

        **Defined Values:**

        %enum_table{enable preselector}

        **Default Value**: :py:data:`~nirfsa.EnablePreselector.DISABLED` if the device has no preselector. :py:data:`~nirfsa.EnablePreselector.ENABLED_WHEN_IN_SIGNAL_PATH` if the device has a preselector.

        **Supported Devices:** PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------+
            | Characteristic        | Value                   |
            +=======================+=========================+
            | Datatype              | enums.EnablePreselector |
            +-----------------------+-------------------------+
            | Permissions           | read-write              |
            +-----------------------+-------------------------+
            | Repeated Capabilities | None                    |
            +-----------------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Downconverter Preselector Enabled**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED**

driver_setup
------------

    .. py:attribute:: driver_setup

        The Driver Setup string returns the initial values for properties that are specific to NI-RFSA.

        The Driver Setup string uses the following format:

        DriverSetup= <i>Tag</i>:<i>Value</i>

        *Tag* is the name of the Driver Setup string property. *Value* is the value set to the property. If multiple properties are set, their assignments are separated with a semicolon.

        This property only returns the Driver Setup string that has already been defined. Refer to `Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_ for more information about configuring the Driver Setup string. Refer to the :py:meth:`nirfsa.Session.init_with_options` method for additional information about using the **option string** parameter.

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Driver Setup**
                - C Attribute: **NIRFSA_ATTR_DRIVER_SETUP**

enable_fractional_resampling
----------------------------

    .. py:attribute:: enable_fractional_resampling

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Fractional Resample Enabled**
                - C Attribute: **NIRFSA_ATTR_ENABLE_FRACTIONAL_RESAMPLING**

end_of_record_event_terminal_name
---------------------------------

    .. py:attribute:: end_of_record_event_terminal_name

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

        - :py:meth:`nirfsa.Session.get_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:End Of Record:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_END_OF_RECORD_EVENT_TERMINAL_NAME**

exported_advance_trigger_output_terminal
----------------------------------------

    .. py:attribute:: exported_advance_trigger_output_terminal

        Specifies the destination terminal for the exported Advance Trigger.

        **Defined Values:**

        %enum_table{export output term}

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.export_signal`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.ExportOutputTerm |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Advance:Export:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL**

exported_digitizer_sample_clock_output_terminal
-----------------------------------------------

    .. py:attribute:: exported_digitizer_sample_clock_output_terminal

        Specifies the terminal at which to export the Digitizer Sample Clock.

        **Valid Values**:
        %enum_table{digitizer samp clk exported term}

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5668

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------------+
            | Characteristic        | Value                              |
            +=======================+====================================+
            | Datatype              | enums.DigitizerSampClkExportedTerm |
            +-----------------------+------------------------------------+
            | Permissions           | read-write                         |
            +-----------------------+------------------------------------+
            | Repeated Capabilities | None                               |
            +-----------------------+------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Digitizer Sample Clock Exported Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_DIGITIZER_SAMPLE_CLOCK_OUTPUT_TERMINAL**

exported_done_event_output_terminal
-----------------------------------

    .. py:attribute:: exported_done_event_output_terminal

        Specifies the destination terminal for the Done Event.

        **Defined Values:**

        %enum_table{export output term}

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.export_signal`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.ExportOutputTerm |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Done:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL**

exported_end_of_record_event_output_terminal
--------------------------------------------

    .. py:attribute:: exported_end_of_record_event_output_terminal

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

        - :py:meth:`nirfsa.Session.export_signal`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.ExportOutputTerm |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:End Of Record:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_END_OF_RECORD_EVENT_OUTPUT_TERMINAL**

exported_ready_for_advance_event_output_terminal
------------------------------------------------

    .. py:attribute:: exported_ready_for_advance_event_output_terminal

        Specifies the destination terminal for the Ready for Advance Event.

        | Value                                           | Description                                                                                                                                                                   |
        |:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | :py:data:`~nirfsa.ExportOutputTerm.DO_NOT_EXPORT` ("")          | The signal is not exported.                                                                                                                                        |
        | :py:data:`~nirfsa.ExportOutputTerm.CLK_OUT` ("ClkOut")          | The signal is exported to the CLK OUT connector on the PXIe-5622/5624 front panel.                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.REF_OUT` ("RefOut")          | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652 and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841. |
        | :py:data:`~nirfsa.ExportOutputTerm.REF_OUT2` ("RefOut2")        | The signal is exported to the REF OUT2 terminal on the LO. This connector exists on only the PXIe-5652.                                                            |
        | :py:data:`~nirfsa.ExportOutputTerm.PFI0` ("PFI0")               | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.                                    |
        | :py:data:`~nirfsa.ExportOutputTerm.PFI1` ("PFI1")               | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.                                                                                       |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG0` ("PXI_Trig0")     | The signal is exported to the PXI trigger line 0.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG1` ("PXI_Trig1")     | The signal is exported to the PXI trigger line 1.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG2` ("PXI_Trig2")     | The signal is exported to the PXI trigger line 2.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG3` ("PXI_Trig3")     | The signal is exported to the PXI trigger line 3.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG4` ("PXI_Trig4")     | The signal is exported to the PXI trigger line 4.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG5` ("PXI_Trig5")     | The signal is exported to the PXI trigger line 5.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG6` ("PXI_Trig6")     | The signal is exported to the PXI trigger line 6.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG7` ("PXI_Trig7")     | The signal is exported to the PXI trigger line 7.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_STAR` ("PXI_Star")       | The signal is exported to the PXI star trigger line.                                                                                                               |
        | :py:data:`~nirfsa.ExportOutputTerm.PXIE_DSTARC` ("PXIe_DStarC") | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                      |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI0` ("DIO/PFI0")           | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI1`("DIO/PFI1")           | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI2` ("DIO/PFI2")           | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI3` ("DIO/PFI3")           | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI4` ("DIO/PFI4")           | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI5` ("DIO/PFI5")           | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI6` ("DIO/PFI6")           | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI7` ("DIO/PFI7")           | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                 |

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.export_signal`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.ExportOutputTerm |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Advance:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL**

exported_ready_for_ref_event_output_terminal
--------------------------------------------

    .. py:attribute:: exported_ready_for_ref_event_output_terminal

        Specifies the destination terminal for the Ready for Reference Event.

        | Value                                           | Description                                                                                                                                                                   |
        |:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | :py:data:`~nirfsa.ExportOutputTerm.DO_NOT_EXPORT` ("")          | The signal is not exported.                                                                                                                                        |
        | :py:data:`~nirfsa.ExportOutputTerm.CLK_OUT` ("ClkOut")          | The signal is exported to the CLK OUT connector on the PXIe-5622/5624 front panel.                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.REF_OUT` ("RefOut")          | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652 and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841. |
        | :py:data:`~nirfsa.ExportOutputTerm.REF_OUT2` ("RefOut2")        | The signal is exported to the REF OUT2 terminal on the LO. This connector exists on only the PXIe-5652.                                                            |
        | :py:data:`~nirfsa.ExportOutputTerm.PFI0` ("PFI0")               | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.                                    |
        | :py:data:`~nirfsa.ExportOutputTerm.PFI1` ("PFI1")               | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.                                                                                       |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG0` ("PXI_Trig0")     | The signal is exported to the PXI trigger line 0.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG1` ("PXI_Trig1")     | The signal is exported to the PXI trigger line 1.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG2` ("PXI_Trig2")     | The signal is exported to the PXI trigger line 2.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG3` ("PXI_Trig3")     | The signal is exported to the PXI trigger line 3.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG4` ("PXI_Trig4")     | The signal is exported to the PXI trigger line 4.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG5` ("PXI_Trig5")     | The signal is exported to the PXI trigger line 5.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG6` ("PXI_Trig6")     | The signal is exported to the PXI trigger line 6.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG7` ("PXI_Trig7")     | The signal is exported to the PXI trigger line 7.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_STAR` ("PXI_Star")       | The signal is exported to the PXI star trigger line.                                                                                                               |
        | :py:data:`~nirfsa.ExportOutputTerm.PXIE_DSTARC` ("PXIe_DStarC") | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                      |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI0` ("DIO/PFI0")           | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI1`("DIO/PFI1")           | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI2` ("DIO/PFI2")           | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI3` ("DIO/PFI3")           | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI4` ("DIO/PFI4")           | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI5` ("DIO/PFI5")           | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI6` ("DIO/PFI6")           | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI7` ("DIO/PFI7")           | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                 |

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.export_signal`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.ExportOutputTerm |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Ref:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_READY_FOR_REF_EVENT_OUTPUT_TERMINAL**

exported_ready_for_start_event_output_terminal
----------------------------------------------

    .. py:attribute:: exported_ready_for_start_event_output_terminal

        Specifies the destination terminal for the Ready for Start Event.

        | Value                                           | Description                                                                                                                                                                   |
        |:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | :py:data:`~nirfsa.ExportOutputTerm.DO_NOT_EXPORT` ("")          | The signal is not exported.                                                                                                                                        |
        | :py:data:`~nirfsa.ExportOutputTerm.CLK_OUT` ("ClkOut")          | The signal is exported to the CLK OUT connector on the PXIe-5622/5624 front panel.                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.REF_OUT` ("RefOut")          | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652 and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841. |
        | :py:data:`~nirfsa.ExportOutputTerm.REF_OUT2` ("RefOut2")        | The signal is exported to the REF OUT2 terminal on the LO. This connector exists only on the PXIe-5652.                                                            |
        | :py:data:`~nirfsa.ExportOutputTerm.PFI0` ("PFI0")               | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.                                    |
        | :py:data:`~nirfsa.ExportOutputTerm.PFI1` ("PFI1")               | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.                                                                                       |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG0` ("PXI_Trig0")     | The signal is exported to the PXI trigger line 0.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG1` ("PXI_Trig1")     | The signal is exported to the PXI trigger line 1.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG2` ("PXI_Trig2")     | The signal is exported to the PXI trigger line 2.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG3` ("PXI_Trig3")     | The signal is exported to the PXI trigger line 3.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG4` ("PXI_Trig4")     | The signal is exported to the PXI trigger line 4.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG5` ("PXI_Trig5")     | The signal is exported to the PXI trigger line 5.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG6` ("PXI_Trig6")     | The signal is exported to the PXI trigger line 6.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_TRIG7` ("PXI_Trig7")     | The signal is exported to the PXI trigger line 7.                                                                                                                  |
        | :py:data:`~nirfsa.ExportOutputTerm.PXI_STAR` ("PXI_Star")       | The signal is exported to the PXI star trigger line.                                                                                                               |
        | :py:data:`~nirfsa.ExportOutputTerm.PXIE_DSTARC` ("PXIe_DStarC") | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                      |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI0` ("DIO/PFI0")           | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI1`("DIO/PFI1")           | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI2` ("DIO/PFI2")           | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI3` ("DIO/PFI3")           | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI4` ("DIO/PFI4")           | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI5` ("DIO/PFI5")           | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI6` ("DIO/PFI6")           | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                 |
        | :py:data:`~nirfsa.ExportOutputTerm.DIO_PFI7` ("DIO/PFI7")           | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                 |

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.export_signal`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.ExportOutputTerm |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Start:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_READY_FOR_START_EVENT_OUTPUT_TERMINAL**

exported_ref_clock_output_terminal
----------------------------------

    .. py:attribute:: exported_ref_clock_output_terminal

        Specifies a comma-separated list of the terminals at which to export the Reference Clock.

        **Defined Values:**

        %enum_table{ref clk exported term}

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.export_signal`

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.RefClkExportedTerm |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | None                     |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Ref Clock Exported Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL**

exported_ref_clock_rate
-----------------------

    .. py:attribute:: exported_ref_clock_rate

        Specifies the Reference Clock Rate, in Hz, of the signal sent to the Ref Clock Exported Terminal.

        **Default Value**: 10 MHz

        **Valid Values**:

        PXIe-5820/5830/5831/5832/5840/5841: 10 MHz

        PXIe-5842: 10 MHz, 100 MHz, 1 GHz

        PXIe-5860: 10 MHz, 100 MHz

        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.ReferenceClockExportedRate |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | None                             |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Ref Clock Exported Rate:Ref Clock Exported Rate**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_REF_CLOCK_RATE**

exported_ref_trigger_output_terminal
------------------------------------

    .. py:attribute:: exported_ref_trigger_output_terminal

        Specifies the destination terminal for the exported Reference Trigger.

        **Defined Values:**

        %enum_table{export output term}

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.export_signal`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.ExportOutputTerm |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Export:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL**

exported_start_trigger_output_terminal
--------------------------------------

    .. py:attribute:: exported_start_trigger_output_terminal

        Specifies the destination terminal for the exported Start Trigger.

        **Defined Values:**

        %enum_table{export output term}

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.export_signal`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.ExportOutputTerm |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Export:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

external_gain
-------------

    .. py:attribute:: external_gain

        Specifies the gain, in dB, of a switch (or cable) connected before the RF IN connector of an NI-RFSA system.

        When you set this property, NI-RFSA calculates appropriate attenuator settings based on the value of this property and the value of the :py:attr:`nirfsa.Session.reference_level` property. In this case, NI-RFSA interprets the reference level as the maximum expected power level of the signal at the input of the external gain device. For more information about attenuation, refer to the *Attenuation and Signal Levels* topic for your device in the *NI RF Vector Signal Analyzers Help*.

        ----
        **Note**
        For the PXIe-5820, this property specifies the gain, in dB, of a switch (or cable) connected before the IQ IN connector.

        ----

        ----
        **Note**
        For the PXIe-5645, this property is ignored if you are using the I/Q ports.

        ----

        With this property set, NI-RFSA reads the :py:attr:`nirfsa.Session.iq_power_edge_ref_trigger_level` property value as the power level at the input of the external gain device at which the NI-RFSA device should trigger.

        Negative values indicate attenuation.

        **Valid Values**: INF to +INF

        **Units**: dB

        **Default Value**: 0

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:External Gain (dB)**
                - C Attribute: **NIRFSA_ATTR_EXTERNAL_GAIN**

fetch_offset
------------

    .. py:attribute:: fetch_offset

        Specifies the offset relative to the position specified by the :py:attr:`nirfsa.Session.fetch_relative_to` property from which to start fetching data.

        Offset can be a positive or negative value.

        **Default Value**: 0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Fetch:Fetch Offset**
                - C Attribute: **NIRFSA_ATTR_FETCH_OFFSET**

fetch_relative_to
-----------------

    .. py:attribute:: fetch_relative_to

        Specifies the reference location within the acquired record from which to begin fetching.

        **Defined Values:**

        %enum_table{fetch relative to}

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.FetchRelativeTo |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Fetch:Fetch Relative To**
                - C Attribute: **NIRFSA_ATTR_FETCH_RELATIVE_TO**

fft_size
--------

    .. py:attribute:: fft_size

        Returns the size of the fast Fourier transform (FFT).

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:FFT Size**
                - C Attribute: **NIRFSA_ATTR_FFT_SIZE**

fft_width
---------

    .. py:attribute:: fft_width

        Specifies the FFT width of the device.

        The FFT width is the effective bandwidth of the signal path during each signal acquisition.

        ----
        **Note**
        The maximum FFT width when using the PXIe-5622 is constrained to 50 MHz or 25 MHz, depending on the digitizer option you purchased. The maximum FFT width when using thing PXIe-5624 is constrained to 400 MHz or 765 MHz, depending on the digitizer configuration.

        ----

        ----
        **Note**
        You can use the :py:attr:`nirfsa.Session.fft_width` property with in-band retuning. For more information about in-band retuning, refer to the :py:attr:`nirfsa.Session.downconverter_center_frequency` property.

        ----

        NI-RFSA treats the *device instantaneous bandwidth* as the effective real-time bandwidth of the signal path. The *span* specifies the frequency range of the computed spectrum. An RF vector signal analyzer can acquire a bandwidth only within the device instantaneous bandwidth frequency. If the span you choose is greater than the device instantaneous bandwidth, NI-RFSA obtains multiple acquisitions and combines them into a single spectrum. By specifying the FFT width, you can control the specific bandwidth obtained in each signal acquisition. If you read the :py:attr:`nirfsa.Session.fft_width` property without setting it, NI-RFSA returns the value of the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property.

        **Valid Values**:

        The lower limit for all FFT width supported devices using the PXIe-5622 IF digitizer is 7.325 kHz. The lower limit for all FFT width supported devices using the PXIe-5624 IF digitizer is 400 MHz or 800 MHz, depending on the FPGA image that is downloaded upon opening the session to the PXIe-5624 IF digitizer.

        **PXIe-5663/5663E**: The FFT width upper limit for the PXIe-5663/5663E depends on the downconverter center frequency and on the module revision of the PXIe-5601 as illustrated in the following table. Refer to the `Identifying Module Revision <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/identifying-module-revision.html>`_ topic for more information about determining which revision of the PXIe-5601 RF downconverter you have installed.

        | Downconverter Center Frequency                                                                                                                                                              | PXIe-5601 Instantaneous Bandwidth | FFT Width Upper Limit                                          |
        |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------|:---------------------------------------------------------------|
        | 10 MHz to <120 MHz                                                                                                                                                                         | 10 MHz                            | 10 MHz (Revision E), 20 MHz< sup >* < /sup> (Revision G or later) |
        | 120 MHz to <330 MHz                                                                                                                                                                        | 20 MHz                            | 20 MHz (Revision E), 30 MHz< sup > * < /sup> (Revision G or later) |
        | 330 MHz to <6.6 GHz                                                                                                                                                                        | 50 MHz                            | 50 MHz                                                         |
        | <sup > * < / sup >National Instruments does not guarantee device specifications if you set the :py:attr:`nirfsa.Session.fft_width` property greater than the warranted instantaneous bandwidth specification. |                                   |                                                                |

        **PXIe-5665/5667/5668**: The upper limit of the FFT width is the maximum device instantaneous bandwidth.

        ----
        **Note**

        ----

        ----
        **Note**
        At frequencies greater than 3.6 GHz, the PXIe-5605 provides a typical bandwidth of 47 MHz at   dB with the preselector enabled. The :py:attr:`nirfsa.Session.fft_width` property can override the typical bandwidth of the PXIe-5605 up to 57 MHz using an external digitizer and up to 50 MHz or 25 MHz depending on the PXIe-5622 digitizer option you purchased. The increase in bandwidth results in faster signal acquisitions, but amplitude accuracy is decreased for spectrum acquisitions, and magnitude and phase accuracy is decreased for I/Q acquisitions. National Instruments does not guarantee device specifications if you set the :py:attr:`nirfsa.Session.fft_width` property greater than the warranted instantaneous bandwidth specification.

        ----

        ----
        **Note**
        When using the PXIe-5606, the 765 MHz IF filter is only available at center frequencies of 3.6 GHz and above.

        ----

        **Default Value**: N/A

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:FFT Width**
                - C Attribute: **NIRFSA_ATTR_FFT_WIDTH**

fft_window_shape_factor
-----------------------

    .. py:attribute:: fft_window_shape_factor

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

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:FFT Window Shape Factor**
                - C Attribute: **NIRFSA_ATTR_FFT_WINDOW_SHAPE_FACTOR**

fft_window_size
---------------

    .. py:attribute:: fft_window_size

        Returns the size of the window used in the fast Fourier transform (FFT), in terms of the number of samples in the window.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:FFT Window Size**
                - C Attribute: **NIRFSA_ATTR_FFT_WINDOW_SIZE**

fft_window_type
---------------

    .. py:attribute:: fft_window_type

        Specifies the time-domain window type.

        **Defined Values:**

        %enum_table{spectrum ff twindow type}

        **Default Values**:

        **PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: :py:data:`~nirfsa.SpectrumFfTwindowType._7_TERM_BLACKMAN_HARRIS`

        **PXIe-5667**: :py:data:`~nirfsa.SpectrumFfTwindowType._4_TERM_BLACKMAN_HARRIS`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Resolution Bandwidth <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/resolution-bandwidth.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.SpectrumFfTwindowType |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:FFT Window Type**
                - C Attribute: **NIRFSA_ATTR_FFT_WINDOW_TYPE**

fixed_group_delay_across_ports
------------------------------

    .. py:attribute:: fixed_group_delay_across_ports

        Specifies a comma-separated list of ports for which to fix the group delay.

        **Valid Values**:

        PXIe-5831/5832: rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel.

        **Default Value**:

        PXIe-5831/5832: (empty string), which specifies that the group delay will not be fixed for any port.

        **Supported Devices**: PXIe-5831/5832

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Fixed Group Delay Across Ports**
                - C Attribute: **NIRFSA_ATTR_FIXED_GROUP_DELAY_ACROSS_PORTS**

fpga_bitfile_path
-----------------

    .. py:attribute:: fpga_bitfile_path

        Returns a string containing the path to the location of the current NI-RFSA instrument driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device.

        You can specify the bitfile location using the Driver Setup string in the **optionString** parameter of the :py:meth:`nirfsa.Session.init_with_options` method.

        NI-RFSA instrument driver FPGA extensions enable you to use pre-compiled FPGA bitfiles to customize the behavior of the device FPGA while maintaining the functionality of the NI-RFSA instrument driver.

        Refer to `NI-RFSA Instrument Driver FPGA Extensions <https://www.ni.com/docs/en-US/bundle/ni-rf-vst/page/rfsa-rfsg-instrument-driver-fpga-extensions.html>`_ for more information about using NI-RFSA instrument driver FPGA extensions for NI devices.

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:FPGA Bitfile Path**
                - C Attribute: **NIRFSA_ATTR_FPGA_BITFILE_PATH**

fpga_target_name
----------------

    .. py:attribute:: fpga_target_name

        Returns a string containing the name of the FPGA target being used.

        This name can be used with the RIO open session to open a reference to the FPGA.

        This property is channel dependent if multiple targets are supported.

        **Supported Devices:** PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:FPGA Target Name**
                - C Attribute: **NIRFSA_ATTR_FPGA_TARGET_NAME**

fpga_temperature
----------------

    .. py:attribute:: fpga_temperature

        Returns the current temperature, in degrees Celsius, of the FPGA.

        ----
        **Note**
        If you query this property during RF list mode, list steps may take longer to complete during list execution.

        ----

        **Units**: degrees Celcius

        **Default Value**: N/A

        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:FPGA Temperature (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_FPGA_TEMPERATURE**

frequency_settling
------------------

    .. py:attribute:: frequency_settling

        Specifies the value used for local oscillator (LO) frequency settling.

        The units and interpretation for this scalar value are specified using the :py:attr:`nirfsa.Session.frequency_settling_units` property. This property is not supported if you are using an external LO.

        The valid values for this property depend on the :py:attr:`nirfsa.Session.frequency_settling_units` property.

        | Device | :py:data:`~nirfsa.FrequencySettlingUnits.SECONDS_AFTER_LOCK` | :py:data:`~nirfsa.FrequencySettlingUnits.SECONDS_AFTER_IO` | %enum_value{frequency settling units.fsu
        ppm} |
        |:-------|:----------------------------------|:--------------------------------|:------------------|
        | PXIe-5663/5663E | 2 microseconds<sup>1</sup> to 80 milliseconds, resolution of approximately 2 microseconds | 0 microseconds to 80 milliseconds<sup>2</sup>, resolution of 1 microsecond | 1.0, 0.1, 0.01 |
        | PXIe-5665/5667/5668 | 4 microseconds to 80 milliseconds, resolution of approximately 4 microseconds | 0 microseconds to 80 milliseconds<sup>2</sup>, resolution of 1 microsecond | 1.0, 0.1, 0.01, 0.001 |
        | PXIe-5644/5645/5646 | 1 microsecond<sup>1</sup> to 65 milliseconds, resolution of 1 microsecond | 1 microsecond<sup>1</sup> to 65 milliseconds, resolution of 1 microsecond | 1.0, 0.1, 0.01 |
        | PXIe-5830/5831/5832/5840/5841/5842 | 1 microsecond<sup>1</sup> to 10 seconds, resolution of 1 microsecond | 0 microseconds to 10 seconds, resolution of 1 microsecond | 1.0 to 0.01 |
        | PXIe-5831/5832 with PXIe-5653 (using PXIe-3622 LO)<sup>3</sup> | 1 microsecond<sup>1</sup> to 10 seconds, resolution of 1 microsecond | 0 microseconds to 10 seconds, resolution of 1 microsecond | 1.0 to 0.01 |
        | PXIe-5831/5832 with PXIe-5653 (using PXIe-5653 LO)<sup>3</sup> | 4 microseconds to 80 milliseconds, resolution of approximately 4 microseconds | 0 microseconds to 80 milliseconds, resolution of 1 microsecond | 1.0 to 0.01 |

        **Notes:**
        1. If the frequency settling units property is set to :py:data:`~nirfsa.FrequencySettlingUnits.SECONDS_AFTER_LOCK` and the downconverter loop bandwidth property is set to narrow, NI recommends a minimum settling time of 128 microseconds to ensure that the phase-locked loop (PLL) lock stabilizes. If the downconverter loop bandwidth is set to wide, NI recommends a minimum settling time of 16 microseconds.
        2. When in RF list mode, the valid values for :py:data:`~nirfsa.FrequencySettlingUnits.SECONDS_AFTER_IO` are 0 microseconds to 50 milliseconds.
        3. The valid values for this configuration depend on the module used as the LO source. Refer to the lo source property for more information.

        **Default Value**: 0.1

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Frequency Settling**
                - C Attribute: **NIRFSA_ATTR_FREQUENCY_SETTLING**

frequency_settling_units
------------------------

    .. py:attribute:: frequency_settling_units

        Specifies the delay duration units and interpretation for LO settling.

        Specify the actual settling value using the :py:attr:`nirfsa.Session.frequency_settling` property. This property is not supported if you are using an external LO.

        **Defined Values:**

        %enum_table{frequency settling units}

        **Default Value**: :py:data:`~nirfsa.FrequencySettlingUnits.PPM`

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------+
            | Characteristic        | Value                        |
            +=======================+==============================+
            | Datatype              | enums.FrequencySettlingUnits |
            +-----------------------+------------------------------+
            | Permissions           | read-write                   |
            +-----------------------+------------------------------+
            | Repeated Capabilities | None                         |
            +-----------------------+------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Frequency Settling Units**
                - C Attribute: **NIRFSA_ATTR_FREQUENCY_SETTLING_UNITS**

host_dma_buffer_size
--------------------

    .. py:attribute:: host_dma_buffer_size

        Specifies the size of the DMA buffer in computer memory, in bytes.

        To set this property, the NI-RFSA device must be in the Configuration state.

        A sufficiently large host DMA buffer improves performance by allowing large fetches to be transferred more efficiently.

        **Default Value:** 8 MB

        **Supported Devices**: PXI-5820/5830/5831/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Fetch:Data Transfer:Host DMA Buffer Size**
                - C Attribute: **NIRFSA_ATTR_HOST_DMA_BUFFER_SIZE**

if1_atten_value
---------------

    .. py:attribute:: if1_atten_value

        Specifies the IF1 attenuation, in dB. The device IF1 attenuator is set to this nominal value.

        Use this property, along with the :py:attr:`nirfsa.Session.if2_atten_value` property, when you set the :py:attr:`nirfsa.Session.if_filter` property to :py:data:`~nirfsa.IFfilter.BYPASS`.

        **Valid Values**: 0 to 15

        **Units**: dB

        **Default Value**: N/A

        **Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:NI 5663:IF1 Attenuation (dB)**
                - C Attribute: **NIRFSA_ATTR_IF1_ATTEN_VALUE**

if2_atten_value
---------------

    .. py:attribute:: if2_atten_value

        Specifies the IF2 attenuation, in dB. The device IF2 attenuator is set to this nominal value.

        Use this property, along with the :py:attr:`nirfsa.Session.if1_atten_value` property, when you set the :py:attr:`nirfsa.Session.if_filter` property to :py:data:`~nirfsa.IFfilter.BYPASS`.

        **Valid Values**: 0 to 15

        **Units**: dB

        **Default Value**: N/A

        **Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:NI 5663:IF2 Attenuation (dB)**
                - C Attribute: **NIRFSA_ATTR_IF2_ATTEN_VALUE**

if_attenuation
--------------

    .. py:attribute:: if_attenuation

        Configures the device attenuation to a value that has the actual calibrated IF attenuation closest to the desired value.

        **Valid Values**: 0 to 30

        **Default Value**: N/A

        **Supported Devices**: PXIe-5601/5603/5605 (external digitizer mode), PXIe-5663/5663E/5665/5667, PXIe-5693

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:NI 5663:IF Attenuation (dB)**
                - C Attribute: **NIRFSA_ATTR_IF_ATTENUATION**

if_conditioning_down_conversion_enabled
---------------------------------------

    .. py:attribute:: if_conditioning_down_conversion_enabled

        Specifies whether downconversion to 21.4 MHz is enabled for the IF conditioning module.

        The IF output frequency is 21.4 MHz when you enable this property, and it is 193.6 MHz when you disable this property.

        ----
        **Note**
        If you set the :py:attr:`nirfsa.Session.signal_conditioning_enabled` property to :py:data:`~nirfsa.SignalConditioningEnabled.BYPASSED`, you cannot set the :py:attr:`nirfsa.Session.if_conditioning_down_conversion_enabled` property to :py:data:`~nirfsa.EnableAttrVals.ENABLED`.

        ----

        ----
        **Note**
        For the PXI-5661, PXIe-5663/5663E/5665, the only valid value for this property is :py:data:`~nirfsa.EnableAttrVals.DISABLED`.

        ----

        **Defined Values:**

        %enum_table{enable attr vals}

        **Default Values**: :py:data:`~nirfsa.EnableAttrVals.DISABLED`

        **Supported Devices**: PXIe-5667, PXIe-5694



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:IF Conditioning Downconversion Enabled**
                - C Attribute: **NIRFSA_ATTR_IF_CONDITIONING_DOWN_CONVERSION_ENABLED**

if_conditioning_temperature
---------------------------

    .. py:attribute:: if_conditioning_temperature

        Returns the current temperature, in degrees Celsius, of the IF conditioning module associated with the NI-RFSA device.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5667

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:IF Conditioning Temperature (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_IF_CONDITIONING_TEMPERATURE**

if_filter
---------

    .. py:attribute:: if_filter

        Specifies the desired IF filter path, regardless of the RF band chosen by NI-RFSA.

        **Defined Values:**

        %enum_table{i ffilter}

        **Default Value**: N/A

        **Supported Devices**: PXIe-5601

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | enums.IFfilter |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | None           |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:NI 5663:IF Filter**
                - C Attribute: **NIRFSA_ATTR_IF_FILTER**

if_filter_bandwidth
-------------------

    .. py:attribute:: if_filter_bandwidth

        Specifies the IF filter path bandwidth for your device configuration.

        ----
        **Note**
        For composite devices, such as the PXIe-5665/5667/5668, the IF filter path bandwidth includes all IF filters across the component modules of a composite device.

        ----

        NI-RFSA uses this property in conjunction with the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property and the :py:attr:`nirfsa.Session.digital_if_equalization_enabled` property to determine the settings for your measurement. NI-RFSA selects the next highest available filter based on the value you specify. The following table lists the IF filters available for NI devices. You may specify a higher value than your device instantaneous bandwidth if your measurement requires it, but specifying a lower value returns an error.

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
        To set this property to values greater than 20 MHz, you must set the :py:attr:`nirfsa.Session.signal_conditioning_enabled` property to :py:data:`~nirfsa.SignalConditioningEnabled.BYPASSED`

        ----

        **Default Values:** For spectrum acquisition types the default is greater than or equal to the :py:attr:`nirfsa.Session.spectrum_span` property. NI-RFSA chooses the default value of the :py:attr:`nirfsa.Session.if_filter_bandwidth` property to correspond to the appropriate IF filter. For I/Q acquisition types NI-RFSA chooses the default value corresponding to the widest IF filter possible for your equipment setup.

        **Supported Devices**: PXIe-5603/5605/5606, PXIe-5665/5667/5668, PXIe-5694

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:IF Filter Bandwidth**
                - C Attribute: **NIRFSA_ATTR_IF_FILTER_BANDWIDTH**

if_output_frequency
-------------------

    .. py:attribute:: if_output_frequency

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

        Additionally, if you use the :py:attr:`nirfsa.Session.downconverter_center_frequency` and :py:attr:`nirfsa.Session.lo_frequency` properties to program the downconverter, the IF output frequency could vary from the nominal value. NI-RFSA adjusts the acquired spectrum or I/Q data for the difference between nominal and actual IF output frequency. If you use an external digitizer with a RF downconverter, use this property to specify the actual IF output frequency.

        **Default Value**: N/A

        **Supported Devices**:PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Advanced:IF Output Frequency**
                - C Attribute: **NIRFSA_ATTR_IF_OUTPUT_FREQUENCY**

if_output_power_level
---------------------

    .. py:attribute:: if_output_power_level

        Specifies the level of the IF signal leaving the system, in dBm.

        Use this property to increase or decrease the nominal IF signal output level to achieve better measurement results.

        If you set the :py:attr:`nirfsa.Session.if_output_power_level` and :py:attr:`nirfsa.Session.if_output_power_level_offset` properties at the same time, NI-RFSA returns an error.

        ----
        **Note**
        If you set the :py:attr:`nirfsa.Session.if_output_power_level` property to a value less than 201310 dBm, the IF output power level may be higher than the value you request. Read the value of this property to determine the configured IF output power level.

        ----

        ----
        **Note**
        The value of this property is limited by the amount of IF attenuation that the downconverter can apply, the :py:attr:`nirfsa.Session.reference_level` property, the :py:attr:`nirfsa.Session.downconverter_center_frequency` property, and the :py:attr:`nirfsa.Session.center_frequency` property or :py:attr:`nirfsa.Session.iq_carrier_frequency` property, depending on your acquisition type.

        ----

        **Units**: dBm

        **Default Value**:

        **PXIe-5667**: -2 dBm

        **PXIe-5668**: -1 dBm

        **All other devices**:   dBm

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:IF Output Power Level (dBm)**
                - C Attribute: **NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL**

if_output_power_level_offset
----------------------------

    .. py:attribute:: if_output_power_level_offset

        Specifies the number of dB by which to adjust the default IF output power level.

        This property does not depend on absolute IF output power levels, so you can use it to adjust the IF output power level on all NI-RFSA devices without knowing the exact default value. Use this property to increase or decrease the nominal output level to achieve better measurement results. The default value for the offset is 0 dB.

        If you set the :py:attr:`nirfsa.Session.if_output_power_level` and :py:attr:`nirfsa.Session.if_output_power_level_offset` properties at the same time, NI-RFSA returns an error.

        **Units**: dB

        **Default Value**: 0

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:IF Output Power Level Offset (dB)**
                - C Attribute: **NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET**

input_isolation_enabled
-----------------------

    .. py:attribute:: input_isolation_enabled

        Specifies whether input isolation is enabled.

        Enabling this property isolates the input signal at the RF IN connector on the RF downconverter from the rest of the RF downconverter signal path. Disabling this property reintegrates the input signal into the RF downconverter signal path.

        ----
        **Note**
        If you enable input isolation for your device, the device impedance is changed from the characteristic 50  impedance. A change in the device impedance may also cause a VSWR value higher than the device specifications.

        ----

        For the PXIe-5830/5831/5832, input isolation is supported for all available ports for your hardware configuration.

        **Defined Values:**

        %enum_table{enable attr vals}

        **Default Value**: :py:data:`~nirfsa.EnableAttrVals.DISABLED`, if the device configuration is supported.

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5693, PXIe-5820/5830/5831/5832/5840/5841



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Input Isolation Enabled**
                - C Attribute: **NIRFSA_ATTR_INPUT_ISOLATION_ENABLED**

input_port
----------

    .. py:attribute:: input_port

        Specifies the connector(s) to use to acquire the signal.

        To set this property, the NI-RFSA device must be in the Configuration state.

        **Defined Values:**

        %enum_table{input port}

        **Default Values**:

        **PXIe-5820**: :py:data:`~nirfsa.InputPort.IQ_IN`

        **All other devices**: :py:data:`~nirfsa.InputPort.RF_IN`

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------------+
            | Characteristic        | Value           |
            +=======================+=================+
            | Datatype              | enums.InputPort |
            +-----------------------+-----------------+
            | Permissions           | read-write      |
            +-----------------------+-----------------+
            | Repeated Capabilities | None            |
            +-----------------------+-----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:Input Port**
                - C Attribute: **NIRFSA_ATTR_INPUT_PORT**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        Returns a string that contains the firmware revision information for the NI-RFSA downconverter for the composite device you are currently using.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        ----
        **Note**
        PXIe-5820/5830/5831/5832/5840/5841/5842/5860 devices will return "No revision information available." To retrieve the firmware revision, use MAX, Hardware Configuration Utility, or NI System Configuration API.

        ----

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Firmware Revision**
                - C Attribute: **NIRFSA_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        Returns a string that contains the name of the manufacturer for the NI-RFSA device you are currently using.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Manufacturer**
                - C Attribute: **NIRFSA_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        Returns a string that contains the model number or name of the NI-RFSA device that you are currently using.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Model**
                - C Attribute: **NIRFSA_ATTR_INSTRUMENT_MODEL**

interchange_check
-----------------

    .. py:attribute:: interchange_check

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Interchange Check**
                - C Attribute: **NIRFSA_ATTR_INTERCHANGE_CHECK**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        Indicates the resource name NI-RFSA uses to identify the physical device.

        If you initialize NI-RFSA with a logical name, this property contains the resource name that corresponds to the entry in the IVI Configuration Utility.

        If you initialize NI-RFSA with the resource name, this property contains that value.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Resource Descriptor**
                - C Attribute: **NIRFSA_ATTR_IO_RESOURCE_DESCRIPTOR**

iq_analog_edge_ref_trigger_hysteresis
-------------------------------------

    .. py:attribute:: iq_analog_edge_ref_trigger_hysteresis

        Specifies the size of the hysteresis window on either side of the trigger level.

        The device triggers when the signal passes through the threshold you specify with the :py:attr:`nirfsa.Session.iq_analog_edge_ref_trigger_level` property, has the slope you specify with the :py:attr:`nirfsa.Session.iq_analog_edge_ref_trigger_slope` property, and passes through the hysteresis window that you specify with this property. This property affects the device operation only when the :py:attr:`nirfsa.Session.ref_trigger_type` property is set to :py:data:`~nirfsa.RefTrigType.IQ_ANALOG_EDGE`.

        **Valid Values:** 0 to (Voltage Range/2 + Trigger Level) for Rising Slope. 0 to (Voltage Range/2 -Trigger Level) for Falling Slope. These values limit the hysteresis to the entire voltage range that is below the trigger level for Rising Slope or that is above the trigger level for Falling Slope.

        **Default Value:** The default is calculated by the driver as (Range x 0.025).

        **Supported Devices:** PXIe-5644/5645R

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Ref:IQ Analog Edge:Hysteresis**
                - C Attribute: **NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_HYSTERESIS**

iq_analog_edge_ref_trigger_level
--------------------------------

    .. py:attribute:: iq_analog_edge_ref_trigger_level

        Specifies the analog level, in volts, at which the device triggers.

        The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property affects the device operation only when the :py:attr:`nirfsa.Session.ref_trigger_type` property is set to :py:data:`~nirfsa.RefTrigType.IQ_ANALOG_EDGE`.

        **Default Value:** 0 V

        **Supported Devices:** PXIe-5644/5645

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Ref:IQ Analog Edge:Level**
                - C Attribute: **NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_LEVEL**

iq_analog_edge_ref_trigger_slope
--------------------------------

    .. py:attribute:: iq_analog_edge_ref_trigger_slope

        Specifies whether the device asserts the trigger when the voltage level is rising or falling.

        When you set the :py:attr:`nirfsa.Session.ref_trigger_type` property to :py:data:`~nirfsa.RefTrigType.IQ_ANALOG_EDGE`, the device asserts the trigger when the signal level exceeds the specified level with the slope you specify. This property affects the device operation only when the :py:attr:`nirfsa.Session.ref_trigger_type` property is set to :py:data:`~nirfsa.RefTrigType.IQ_ANALOG_EDGE`.

        **Defined Values:**

        %enum_table{ref trig iq pwr edge slope}

        **Default Value**: :py:data:`~nirfsa.RefTrigIqPwrEdgeSlope.RISING`

        **Supported Devices:** PXIe-5644/5645

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.RefTrigIqPwrEdgeSlope |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Ref:IQ Analog Edge:Slope**
                - C Attribute: **NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_SLOPE**

iq_analog_edge_ref_trigger_source
---------------------------------

    .. py:attribute:: iq_analog_edge_ref_trigger_source

        Specifies the channel from which the device monitors the trigger.

        Use a value of "I" to monitor the I channel. Use a value of "Q" to monitor the Q channel. Use a value of "I,Q" to monitor both I and Q channels. This property affects the device operation only when the :py:attr:`nirfsa.Session.ref_trigger_type` property is set to :py:data:`~nirfsa.RefTrigType.IQ_ANALOG_EDGE`.

        **Valid Values:** "I", "Q", "I,Q", "Q,I"

        **Default Value:** "I"

        **Supported Devices:** PXIe-5644/5645

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Ref:IQ Analog Edge:Source**
                - C Attribute: **NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_SOURCE**

iq_carrier_frequency
--------------------

    .. py:attribute:: iq_carrier_frequency

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

        - :py:meth:`nirfsa.Session.configure_iq_carrier_frequency`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:IQ:IQ Carrier Frequency**
                - C Attribute: **NIRFSA_ATTR_IQ_CARRIER_FREQUENCY**

iq_in_port_carrier_frequency
----------------------------

    .. py:attribute:: iq_in_port_carrier_frequency

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ In Port:Carrier Frequency**
                - C Attribute: **NIRFSA_ATTR_IQ_IN_PORT_CARRIER_FREQUENCY**

iq_in_port_temperature
----------------------

    .. py:attribute:: iq_in_port_temperature

        Returns the temperature of the I/Q IN circuitry on the device.

        **Units:** degrees C

        **Supported Devices:** PXIe-5645, PXIe-5820

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ In Port:Temperature (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_IQ_IN_PORT_TEMPERATURE**

iq_in_port_terminal_configuration
---------------------------------

    .. py:attribute:: iq_in_port_terminal_configuration

        Configures the terminal configuration of the I/Q port.

        To use this property, you must use the channelName parameter of the :py:meth:`nirfsa.Session.set_attribute_vi_int32` method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

        ----
        **Note**
        For the PXIe-5645, this property is ignored if you are using the RF ports.

        ----

        **PXIe-5820**: The only valid value for this property is :py:data:`~nirfsa.IqInPortTermCfg.DIFFERENTIAL`.

        **Defined Values:**

        %enum_table{iq in port term cfg}

        **Default Value**: :py:data:`~nirfsa.IqInPortTermCfg.DIFFERENTIAL`

        **Supported Devices:** PXIe-5645, PXIe-5820

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.IqInPortTermCfg |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ In Port:Terminal Configuration**
                - C Attribute: **NIRFSA_ATTR_IQ_IN_PORT_TERMINAL_CONFIGURATION**

iq_in_port_vertical_range
-------------------------

    .. py:attribute:: iq_in_port_vertical_range

        Specifies the voltage range for the I/Q terminals.

        To use this property, you must use the channelName parameter of the :py:meth:`nirfsa.Session.set_attribute_vi_real64` method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ In Port:Vertical Range**
                - C Attribute: **NIRFSA_ATTR_IQ_IN_PORT_VERTICAL_RANGE**

iq_power_edge_ref_trigger_level
-------------------------------

    .. py:attribute:: iq_power_edge_ref_trigger_level

        Specifies the power level, in dBm, at which the device triggers.

        The device asserts the trigger when the signal crosses the level specified by the value of this property, taking into consideration the specified slope. If you are using external gain, refer to the :py:attr:`nirfsa.Session.external_gain` property for more information about how this property affects the I/Q power edge trigger level.

        **Default Value**: 0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_iq_power_edge_ref_trigger`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:IQ Power Edge:Level**
                - C Attribute: **NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_LEVEL**

iq_power_edge_ref_trigger_slope
-------------------------------

    .. py:attribute:: iq_power_edge_ref_trigger_slope

        Specifies whether the device asserts the trigger when the signal power is rising or falling.

        When you set the :py:attr:`nirfsa.Session.ref_trigger_type` property to :py:data:`~nirfsa.RefTrigType.IQ_POWER_EDGE`, the device asserts the trigger when the signal power exceeds the specified level with the slope you specify.

        **Defined Values:**

        %enum_table{ref trig iq pwr edge slope}

        **Default Value**: :py:data:`~nirfsa.RefTrigIqPwrEdgeSlope.RISING`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_iq_power_edge_ref_trigger`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.RefTrigIqPwrEdgeSlope |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:IQ Power Edge:Slope**
                - C Attribute: **NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_SLOPE**

iq_power_edge_ref_trigger_source
--------------------------------

    .. py:attribute:: iq_power_edge_ref_trigger_source

        Specifies the channel from which the device monitors the trigger.

        NI-RFSA currently supports only 0 as the value of this property.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_iq_power_edge_ref_trigger`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:IQ Power Edge:Source**
                - C Attribute: **NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_SOURCE**

iq_rate
-------

    .. py:attribute:: iq_rate

        Specifies the I/Q rate for the acquisition.

        The value is expressed in samples per second (S/s).

        Refer to the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property for more information about device specific instantaneous bandwidth limits. You can also refer to the *NI PXIe-5665 Specifications* for more information about instantaneous bandwidth device specifications.

        ----
        **Note**
        For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. At I/Q rates above 50 MS/s, the dither noise can affect phase coherency performance and leak into the lower frequencies and the upper frequencies of the IF passband. Refer to the :py:attr:`nirfsa.Session.digitizer_dither_enabled` property for more information about dithering.

        For the PXIe-5663/5663E/5665/5667, when you set the :py:attr:`nirfsa.Session.digitizer_sample_clock_timebase_source` property to :py:data:`~nirfsa.NIRFSA_VAL_ONBOARD_CLOCK_STR`, the downconverter instantaneous bandwidth is greater than or equal to the coerced I/Q rate times 0.8. For the PXIe-5665, the actual signal bandwidth is further limited by the combination of the chosen IF filter and anti-aliasing filter.

        ----

        **PXI-5661**: You should not need to configure an I/Q rate higher than 25 megasamples per second (MS/s) because the PXI-5600 RF downconverter bandwidth is 20 MHz. If you configure a higher I/Q rate, you may see aliasing effects at negative frequencies because the IF frequency of the PXI-5600 is 15 MHz.

        **PXIe-5663/5663E**: Your maximum allowed instantaneous bandwidth depends on the I/Q carrier frequency you use. Refer to the `PXIe-5601 RF downconverter overview <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/overview.3.html>`_ for more information about instantaneous bandwidth.

        **PXIe-5665**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency if you have enabled the preselector (YIG-tuned filter).

        **PXIe-5667**: Your maximum allowed instantaneous bandwidth depends on the selected [RF preselector filter](:py:attr:`nirfsa.Session.rf_preselector_filter`.html) and whether the preselector on the [RF downconverter](:py:attr:`nirfsa.Session.PRESELECTOR_ENABLED`.html) is enabled.

        **PXIe-5668**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use and whether or not you enable the highpass filter or preselector (YIG-tuned filter).

        **Units**: S/s

        **Default Values:**

        **PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality**: 5 GS/s only.

        **All Other Devices**: 1 MS/s

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_iq_rate`



        .. note:: One or more of the referenced properties are not in the Python API for this driver.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:IQ:IQ Rate (S/s)**
                - C Attribute: **NIRFSA_ATTR_IQ_RATE**

lo2_export_enabled
------------------

    .. py:attribute:: lo2_export_enabled

        Specifies whether to enable the LO2 OUT terminal on the installed devices.

        Set this property to TRUE to export the 4 GHz LO signal from the device LO2 IN terminal to the LO2 OUT terminal.

        You can also export the LO2 signal by setting the :py:attr:`nirfsa.Session.lo_export_enabled` property and the :py:attr:`nirfsa.Session.digitizer_sample_clock_timebase_source` property.

        **Defined Values:**

        |          |                                |
        |:---------|:-------------------------------|
        | True  | Enables the LO2 OUT terminal.  |
        | False | Disables the LO2 OUT terminal. |

        **Default Value:** False

        **Supported Devices:** PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5668

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:LO2 Export Enabled**
                - C Attribute: **NIRFSA_ATTR_LO2_EXPORT_ENABLED**

load_configurations_from_file_reset_options
-------------------------------------------

    .. py:attribute:: load_configurations_from_file_reset_options

        Specifies the configurations to skip to reset while loading configurations from a file.

        **Default Value:**  :py:data:`~nirfsa.NIRFSA_VAL_SKIP_NONE`
        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +---------------------------------------------------------------------+--------------------------------------------------+
        | Value                                                               | Description                                      |
        +=====================================================================+==================================================+
        | :py:data:`~nirfsa.LoadConfigurationResetOptions.NONE`               | NI-RFSA resets all configurations.               |
        +---------------------------------------------------------------------+--------------------------------------------------+
        | :py:data:`~nirfsa.LoadConfigurationResetOptions.DEEMBEDDING_TABLES` | NI-RFSA skips resetting the de-embedding tables. |
        +---------------------------------------------------------------------+--------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------+
            | Characteristic        | Value                               |
            +=======================+=====================================+
            | Datatype              | enums.LoadConfigurationResetOptions |
            +-----------------------+-------------------------------------+
            | Permissions           | read-write                          |
            +-----------------------+-------------------------------------+
            | Repeated Capabilities | None                                |
            +-----------------------+-------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Load Configurations:Reset Options**
                - C Attribute: **NIRFSA_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS**

logical_name
------------

    .. py:attribute:: logical_name

        Contains the logical name you specified when opening the current IVI session.

        You may pass a logical name to the :py:meth:`nirfsa.Session.init` method or the :py:meth:`nirfsa.Session.init_with_options` method. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a driver session section in the IVI Configuration file. The driver session section specifies a physical device and initial user options.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
                - C Attribute: **NIRFSA_ATTR_LOGICAL_NAME**

low_frequency_bypass_enabled
----------------------------

    .. py:attribute:: low_frequency_bypass_enabled

        Specifies whether to use the low-frequency bypass path for the incoming RF signal.

        |                            |                                         |
        |:---------------------------|:----------------------------------------|
        | :py:data:`~nirfsa.EnableAttrVals.DISABLED` (1900) | Disables the low-frequency bypass path. |
        | :py:data:`~nirfsa.EnableAttrVals.ENABLED` (1901)  | Enables the low-frequency bypass path.  |

        **Default Value**: :py:data:`~nirfsa.EnableAttrVals.DISABLED`

        **Supported Devices**: PXIe-5693, PXIe-5667



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Low Frequency Bypass Enabled**
                - C Attribute: **NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED**

lo_export_enabled
-----------------

    .. py:attribute:: lo_export_enabled

        Specifies whether to enable the LO OUT terminals on the installed devices.

        **PXIe-5601**: The only valid value for this property is True.

        **PXIe-5603/5605/5606**: If you want to daisy-chain multiple devices together using the same LO source, set this property to TRUE to export the LO input signals on the LO1 IN, LO2 IN, and LO3 IN terminals to LO1 OUT, LO2 OUT, and LO3 OUT, respectively.

        **PXIe-5694**: You can enable this property only if you set the :py:attr:`nirfsa.Session.lo_source` property to :py:data:`~nirfsa.LoSourceVals.LO_IN`, or if you set the :py:attr:`nirfsa.Session.lo_source` property to :py:data:`~nirfsa.LoSourceVals.ONBOARD` and the :py:attr:`nirfsa.Session.if_conditioning_down_conversion_enabled` property to :py:data:`~nirfsa.NIRFSA_VAL_ENABLED`.

        **PXIe-5830/5831**: To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsa.Session.set_attribute_vi_boolean` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

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



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:LO Export Enabled**
                - C Attribute: **NIRFSA_ATTR_LO_EXPORT_ENABLED**

lo_frequency
------------

    .. py:attribute:: lo_frequency

        Specifies the LO signal frequency for the configured center frequency.

        If you are using the NI RF vector signal analyzer with an external LO, use this property to specify the LO frequency that the external LO source passes into the LO IN or LO1 IN connector on the RF downconverter front panel. If you are using an external LO, reading the value of this property after configuring the rest of the parameters returns the LO frequency needed by the device.

        Set this property to the actual LO frequency because NI-RFSA corrects for any difference between expected and actual LO frequencies.

        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsa.Session.set_attribute_vi_real64` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

        **Default Values**:

        **PXIe-5694**: 215 MHz

        **All other devices**: 0

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842

        **Related Topics**

        `PXIe-5830 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-configuration.html>`_

        `PXIe-5831/5832 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-configuration.html>`_

        `PXIe-5841 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-configuration.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:LO Frequency**
                - C Attribute: **NIRFSA_ATTR_LO_FREQUENCY**

lo_frequency_step_size
----------------------

    .. py:attribute:: lo_frequency_step_size

        Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL).

        You can only tune the LO frequency by multiples of the :py:attr:`nirfsa.Session.lo_frequency_step_size` property. For the PXIe-5644/5645/5646 and PXIe-5840/5841, the LO frequency can therefore be offset from the requested center frequency by as much as half of the :py:attr:`nirfsa.Session.lo_frequency_step_size` property. This offset is corrected by digitally frequency shifting the :py:attr:`nirfsa.Session.lo_frequency` property to the value requested in either the :py:attr:`nirfsa.Session.iq_carrier_frequency` property or the :py:attr:`nirfsa.Session.center_frequency` property.

        ----
        **Note**
        For the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653, this property is ignored if the PXIe-5653 is used as the LO source.

        ----

        The valid values for this property depend on the :py:attr:`nirfsa.Session.lo_pll_fractional_mode_enabled` property.

        **PXIe-5644/5645/5646**: If the :py:attr:`nirfsa.Session.lo_pll_fractional_mode_enabled` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`, the specified value is coerced to the closest valid value.

        **PXIe-5840/5841/5842**: If the :py:attr:`nirfsa.Session.lo_pll_fractional_mode_enabled` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.

        | :py:attr:`nirfsa.Session.lo_pll_fractional_mode_enabled` | PXIe-5644/5645 | PXIe-5646 | PXIe-5840/5841 | PXIe-5830/5831/5832 | PXIe-5841 w/PXIe-5655 |
        |-------------------------------|-----------------|------------|----------------|---------------------|-----------------------------------|
        | :py:data:`~nirfsa.NIRFSA_VAL_ENABLED` | 50 kHz to 24 MHz | 50 kHz to 25 MHz | 50 kHz to 100 MHz | LO1: 8 Hz to 400 MHz<br>LO2: 4 kHz to 400 MHz | 1 nHz to 50 MHz |
        | :py:data:`~nirfsa.NIRFSA_VAL_DISABLED` | 4 MHz, 5 MHz, 6 MHz, 12 MHz, 24 MHz | 2 MHz, 5 MHz, 10 MHz, 25 MHz | 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, 100 MHz | LO1: --<br>LO2: -- | 1 nHz to 50 MHz |

        * Values up to 100 MHz are coerced to 50 MHz.

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



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO Frequency Step Size (Hz)**
                - C Attribute: **NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE**

lo_injection_side
-----------------

    .. py:attribute:: lo_injection_side

        Specifies the LO injection side.

        **PXIe-5601/5663/5663E**: For frequencies below 517.5 MHz or above 6.4125 GHz, the LO injection side is fixed and NI-RFSA returns an error if you specify the incorrect value. If you do not configure this property, NI-RFSA selects the default LO injection side based on the downconverter center frequency. Reset this property to return to automatic behavior.

        **PXIe-5603/5605/5665 (3.6 GHz)/5667 (3.6 GHz)**: Setting this property to :py:data:`~nirfsa.LoInjection.LOW` is not supported for this device.

        **PXIe-5605/5665 (14 GHz)/5667 (7 GHz)**: Setting this property to :py:data:`~nirfsa.LoInjection.LOW` is supported for this device for frequencies greater than 4 GHz, but this configuration is not calibrated, and device specifications are not guaranteed.

        **PXIe-5606/5668**: Setting this property to :py:data:`~nirfsa.LoInjection.LOW` is supported for certain frequencies in high band, varying by final IF frequency. This configuration is not calibrated and device specifications are not guaranteed.

        **Defined Values:**

        %enum_table{lo injection}

        **Default Values**:

        **PXIe-5601 (external digitizer mode), PXIe-5663/5663E (frequencies < 3.0 GHz)**: :py:data:`~nirfsa.LoInjection.HIGH`

        **PXIe-5601 (external digitizer mode), PXIe-5663/5663E (frequencies  3.0 GHz)**: :py:data:`~nirfsa.LoInjection.LOW`

        **PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668**: :py:data:`~nirfsa.LoInjection.HIGH`

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.LoInjection |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:LO Injection Side**
                - C Attribute: **NIRFSA_ATTR_LO_INJECTION_SIDE**

lo_in_power
-----------

    .. py:attribute:: lo_in_power

        Returns the power level, in dBm, expected at the LO IN terminal when the :py:attr:`nirfsa.Session.lo_source` property is set to :py:data:`~nirfsa.LoSourceVals.LO_IN`.

        ----
        **Note**
        For the PXIe-5644/5645/5646, this property is always read-only.

        ----

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO In Power (dBm)**
                - C Attribute: **NIRFSA_ATTR_LO_IN_POWER**

lo_out_export_configure_from_rfsg
---------------------------------

    .. py:attribute:: lo_out_export_configure_from_rfsg

        Specifies whether to allow NI-RFSG to control the NI-RFSA LO out export.

        Set this property to :py:data:`~nirfsa.EnableAttrVals.ENABLED` to allow NI-RFSG to control the LO out export. Use the NIRFSG ATTR RF IN LO EXPORT ENABLED property to control the NI-RFSA LO out export from NI-RFSG.

        **Defined Values:**

        %enum_table{enable attr vals}

        **Default Value:** :py:data:`~nirfsa.EnableAttrVals.DISABLED`

        **Supported Devices**: PXIe-5840/5841/5842



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:LO Out Export Configure From RFSG**
                - C Attribute: **NIRFSA_ATTR_LO_OUT_EXPORT_CONFIGURE_FROM_RFSG**

lo_out_power
------------

    .. py:attribute:: lo_out_power

        Specifies the power level, in dBm, of the signal at the LO OUT terminal when the :py:attr:`nirfsa.Session.lo_export_enabled` property is set to True.

        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsa.Session.set_attribute_vi_real64` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

        **Units:** dBm

        **Supported Devices:** PXIe-5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO Out Power (dBm)**
                - C Attribute: **NIRFSA_ATTR_LO_OUT_POWER**

lo_pll_fractional_mode_enabled
------------------------------

    .. py:attribute:: lo_pll_fractional_mode_enabled

        Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL).

        Fractional mode gives a finer frequency step resolution, but it may result in non harmonic spurs. Refer to the device specifications for your device for more information about fractional mode and non harmonic spurs.

        ----
        **Note**
        The :py:attr:`nirfsa.Session.lo_pll_fractional_mode_enabled` property is applicable only when using the internal LO.

        ----

        ----
        **Note**
        For the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653, this property is ignored if the PXIe-5653 is used as the LO source. For the PXIe-5841 with PXIe-5655, this property is ignored if the PXIe-5655 is used as the LO source.

        ----

        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsa.Session.set_attribute_vi_int32` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

        **Defined Values:**

        %enum_table{enable attr vals}

        **Default Value**: :py:data:`~nirfsa.EnableAttrVals.ENABLED`

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO PLL Fractional Mode Enabled**
                - C Attribute: **NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED**

lo_source
---------

    .. py:attribute:: lo_source

        Specifies the LO signal source used to downconvert the RF input signal.

                        If no signal downconversion is required, this property is ignored. If this property is set to "" (empty string), NI-RFSA uses the internal LO source.

                        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsa.Session.set_attribute_vi_string` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

                        ----
                        **Note**
                        For the PXIe-5841 with PXIe-5655, RF list mode is not supported when this property is set to :py:data:`~nirfsa.LoSourceVals.LO_SOURCE_SG_SA_SHARED`.

                        ----

                        **Defined Values:**
                        %enum_table{lo source vals}

                        **Default Value**: :py:data:`~nirfsa.LoSourceVals.ONBOARD` ("Onboard")

                        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842

                        **Related Topics**
                        `PXIe-5830 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/lo-sharing-using-rfsa-rfsg.html>`_
                        `PXIe-5831/5832 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/lo-sharing-using-rfsa-rfsg.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+--------------------+
            | Characteristic        | Value              |
            +=======================+====================+
            | Datatype              | enums.LoSourceVals |
            +-----------------------+--------------------+
            | Permissions           | read-write         |
            +-----------------------+--------------------+
            | Repeated Capabilities | None               |
            +-----------------------+--------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:LO Source**
                - C Attribute: **NIRFSA_ATTR_LO_SOURCE**

lo_temperature
--------------

    .. py:attribute:: lo_temperature

        Returns the current temperature, in degrees Celsius, of the LO module.

        **PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode) PXI-5661, PXIe-5663/5663E/5665/5667/5668** This property is not supported if you are using an external LO.

        **PXIe-5840/5841/5842**: If you query this property during RF list mode, list steps may take longer to complete during list execution.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode) PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:LO Temperature (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_LO_TEMPERATURE**

lo_vco_frequency_step_size
--------------------------

    .. py:attribute:: lo_vco_frequency_step_size

        Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal.

        ----
        **Note**
        Do not set this property with the :py:attr:`nirfsa.Session.lo_frequency_step_size` property.

        ----

        **Valid Values**:

        LO1: 1 Hz to 50 MHz

        LO2: 1 Hz to 100 MHz

        **Default Values**: 1 MHz

        **Supported Devices**: PXIe-5830/5831/5832

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO VCO Frequency Step Size (Hz)**
                - C Attribute: **NIRFSA_ATTR_LO_VCO_FREQUENCY_STEP_SIZE**

lo_yig_main_coil_drive
----------------------

    .. py:attribute:: lo_yig_main_coil_drive

        Adjusts the dynamics of the current driving the YIG main coil.

        ----
        **Note**
        Setting this property to :py:data:`~nirfsa.LoYigMainCoilDrive.FAST` allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise. This property is not supported if you are using an external LO.

        ----

        **Defined Values:**

        %enum_table{lo yig main coil drive}

        **Default Value**: :py:data:`~nirfsa.LoYigMainCoilDrive.NORMAL`

        **Supported Devices:** PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.LoYigMainCoilDrive |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | None                     |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:LO YIG Main Coil Drive**
                - C Attribute: **NIRFSA_ATTR_LO_YIG_MAIN_COIL_DRIVE**

max_device_instantaneous_bandwidth
----------------------------------

    .. py:attribute:: max_device_instantaneous_bandwidth

        Returns the maximum instantaneous bandwidth of the device.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Max Device Instantaneous Bandwidth**
                - C Attribute: **NIRFSA_ATTR_MAX_DEVICE_INSTANTANEOUS_BANDWIDTH**

max_fundamental_silo_frequency
------------------------------

    .. py:attribute:: max_fundamental_silo_frequency

        

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIRFSA_ATTR_MAX_FUNDAMENTAL_SILO_FREQUENCY**

max_iq_rate
-----------

    .. py:attribute:: max_iq_rate

        Returns the maximum I/Q rate.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Max IQ Rate**
                - C Attribute: **NIRFSA_ATTR_MAX_IQ_RATE**

mechanical_attenuation
----------------------

    .. py:attribute:: mechanical_attenuation

        Specifies the level of mechanical attenuation for the RF path, in dB.

        **PXIe-5667**: This property is read-only when the :py:attr:`nirfsa.Session.low_frequency_bypass_enabled` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`.

        **PXIe-5668with PXIe-5698**: This property is read-only when the :py:attr:`nirfsa.Session.rf_preamp_enabled` property is set to :py:data:`~nirfsa.EnableRfPreamp.ENABLED`.

        **Units**: dB

        **Valid Values:**

        **PXIe-5601/5663/5663E**: 0, 16

        **PXIe-5603/5665 (3.6 GHz)**: 0, 10, 20, 30

        **PXIe-5605/5665 (14 GHz), PXIe-5606/5668**: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75

        **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 0, 10, 20, 30

        **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**: 0

        **PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75

        **PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector filter path**: 0

        **PXIe-5668 with PXIe-5698 with the** :py:attr:`nirfsa.Session.rf_preamp_enabled` property set to :py:data:`~nirfsa.EnableRfPreamp.ENABLED`: 5

        **Default Value**: N/A

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Mechanical Attenuation (dB)**
                - C Attribute: **NIRFSA_ATTR_MECHANICAL_ATTENUATION**

mechanical_attenuator_enabled
-----------------------------

    .. py:attribute:: mechanical_attenuator_enabled

        Specifies whether the mechanical attenuator is enabled.

        Set this property to :py:data:`~nirfsa.EnableAttrVals.ENABLED` to allow NI-RFSA to use the mechanical attenuator.

        Disabling this attenuator can improve device performance. Refer to `PXIe-5663/5663E Programming Attenuation <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/programming-attenuation.html>`_ for more information about the attenuators.

        **Defined Values:**

        %enum_table{enable attr vals}

        **Default Value**: :py:data:`~nirfsa.EnableAttrVals.ENABLED`

        **Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:NI 5663:Mechanical Attenuator Enabled**
                - C Attribute: **NIRFSA_ATTR_MECHANICAL_ATTENUATOR_ENABLED**

memory_size
-----------

    .. py:attribute:: memory_size

        Returns the digitizer onboard memory size, in bytes.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Memory Size**
                - C Attribute: **NIRFSA_ATTR_MEMORY_SIZE**

minimum_acpr
------------

    .. py:attribute:: minimum_acpr

        Specifies the minimum adjacent channel power ratio (ACPR), in dB, relative to the main channel reference level.

        This property configures NI-RFSA to optimize downconverter gain to measure a lower-power adjacent channel, adding gain only after filtering the main channel. The gain NI-RFSA applies is always less than or equal to the ACPR value you specify.

        ----
        **Note**
        For the PXIe-5665 (3.6 GHz), this property is supported only if you set the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth`, :py:attr:`nirfsa.Session.spectrum_span`, or :py:attr:`nirfsa.Session.if_filter_bandwidth` property to a value less than 300 kHz. For the PXIe-5665 (14 GHz), this property is supported for :py:attr:`nirfsa.Session.device_instantaneous_bandwidth`, :py:attr:`nirfsa.Session.spectrum_span`, or :py:attr:`nirfsa.Session.if_filter_bandwidth` property values less than 300 kHz by using the 300 kHz IF filter, and it is supported for values between 300 kHz and 5 MHz by using the 5 MHz IF filter.

        ----

        ----
        **Note**
        NI-RFSA coerces this property to zero for the PXI-5600, PXIe-5601 and the PXIe-5667. For all other devices, read the coerced value of this property to determine the actual amount of gain applied.

        ----

        ----
        **Note**
        For the PXIe-5668, this property alters the :py:attr:`nirfsa.Session.if_output_power_level` property. This property will not affect the :py:attr:`nirfsa.Session.reference_level` property.

        ----

        **Default Value**: 0

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Minimum Adjacent Channel Power Ratio (dB)**
                - C Attribute: **NIRFSA_ATTR_MINIMUM_ACPR**

minimum_reconfig_time
---------------------

    .. py:attribute:: minimum_reconfig_time

        This property is not for customer use.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration List:Advanced:Minimum Reconfiguration Time**
                - C Attribute: **NIRFSA_ATTR_MINIMUM_RECONFIG_TIME**

min_fundamental_silo_frequency
------------------------------

    .. py:attribute:: min_fundamental_silo_frequency

        

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIRFSA_ATTR_MIN_FUNDAMENTAL_SILO_FREQUENCY**

mixer_level
-----------

    .. py:attribute:: mixer_level

        Specifies the mixer level, in dBm.

        The mixer level represents the attenuation value to apply to the input RF signal as it reaches the first mixer in the signal chain. If you do not set this property, NI-RFSA automatically selects an optimal mixer level value based on the reference level. The valid values for this property depend on your device configuration.

        If you set the :py:attr:`nirfsa.Session.mixer_level` and :py:attr:`nirfsa.Session.mixer_level_offset` properties at the same time, NI-RFSA returns an error.

        **PXIe-5601/5663/5663E**: This property is read-only.

        **PXIe-5667**: This property is read-only when the :py:attr:`nirfsa.Session.low_frequency_bypass_enabled` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`.

        **Units**: dBm

        **Default Values**:

        **PXI-5600/5661**: -30

        **PXIe-5603/5605/5665/5667/5668**: -10

        **All other devices**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Mixer Level (dBm)**
                - C Attribute: **NIRFSA_ATTR_MIXER_LEVEL**

mixer_level_offset
------------------

    .. py:attribute:: mixer_level_offset

        Specifies the number of dB by which to adjust the device mixer level.

        The default value is 0, which specifies device settings that are the best compromise between distortion and noise. Specifying a positive value for this property configures the device for moderate distortion and low noise, and specifying a negative value results in low distortion and higher noise.

        You cannot set the :py:attr:`nirfsa.Session.mixer_level` and :py:attr:`nirfsa.Session.mixer_level_offset` properties at the same time.

        **PXIe-5667**: This property is read-only when the :py:attr:`nirfsa.Session.low_frequency_bypass_enabled` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`.

        **Units**: dB

        **Default Value**: 0

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Mixer Level Offset (dB)**
                - C Attribute: **NIRFSA_ATTR_MIXER_LEVEL_OFFSET**

module_power_consumption
------------------------

    .. py:attribute:: module_power_consumption

        Returns the module power consumption.

        ----
        **Note**
        If you query this property during RF list mode, list steps may take longer to complete during list execution.

        ----

        **Units**: watts

        **Default Value**: N/A

        **Supported Devices:**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Module Power Consumption (W)**
                - C Attribute: **NIRFSA_ATTR_MODULE_POWER_CONSUMPTION**

module_revision
---------------

    .. py:attribute:: module_revision

        Returns the revision of the RF downconverter module.

        ----
        **Note**
        For the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5840/5841, this property returns the revision of the VST module. For the PXIe-5830/5831/5832, this property returns the revision of the PXIe-3621/3622

        ----

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Module Revision**
                - C Attribute: **NIRFSA_ATTR_MODULE_REVISION**

noise_source_power_enabled
--------------------------

    .. py:attribute:: noise_source_power_enabled

        Enables the 28 V DC source on the device front panel.

        **PXIe-5668 with PXIe-5698**: When this property is set to :py:data:`~nirfsa.EnableAttrVals.ENABLED`, the PXIe-5698 noise source is used instead of the PXIe-5668 noise source.

        **Units**: dB

        **Default Value**: :py:data:`~nirfsa.EnableAttrVals.DISABLED`

        **Supported Devices**: PXIe-5606, PXIe-5668, PXIe-5698



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:5606:Noise Source Power Enabled**
                - C Attribute: **NIRFSA_ATTR_NOISE_SOURCE_POWER_ENABLED**

notch_filter_enabled
--------------------

    .. py:attribute:: notch_filter_enabled

        Specifies whether the notch filter is enabled on the RF conditioning module.

        ----
        **Note**
        The PXI-5661 and PXIe-5663/5663E/5665 only support setting this property to :py:data:`~nirfsa.NotchFilterEnabled.DISABLED`.

        ----

        **Defined Values**:

        %enum_table{notch filter enabled}

        **Default Value**: :py:data:`~nirfsa.NotchFilterEnabled.DISABLED`

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5693

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.NotchFilterEnabled |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | None                     |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Notch Filter Enabled**
                - C Attribute: **NIRFSA_ATTR_NOTCH_FILTER_ENABLED**

number_of_records
-----------------

    .. py:attribute:: number_of_records

        Specifies the number of records to acquire if the :py:attr:`nirfsa.Session.number_of_records_is_finite` property is set to True.

        **Default Value**: 1

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_number_of_records`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:IQ:Number Of Records**
                - C Attribute: **NIRFSA_ATTR_NUMBER_OF_RECORDS**

number_of_records_is_finite
---------------------------

    .. py:attribute:: number_of_records_is_finite

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

        - :py:meth:`nirfsa.Session.configure_number_of_records`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:IQ:Number Of Records Is Finite**
                - C Attribute: **NIRFSA_ATTR_NUMBER_OF_RECORDS_IS_FINITE**

number_of_samples
-----------------

    .. py:attribute:: number_of_samples

        Specifies the number of samples to acquire.

        This property is valid only if the :py:attr:`nirfsa.Session.number_of_samples_is_finite` property is set to True.

        **Default Value**: 1,000

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_number_of_samples`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:IQ:Number Of Samples**
                - C Attribute: **NIRFSA_ATTR_NUMBER_OF_SAMPLES**

number_of_samples_is_finite
---------------------------

    .. py:attribute:: number_of_samples_is_finite

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

        - :py:meth:`nirfsa.Session.configure_number_of_samples`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:IQ:Number Of Samples Is Finite**
                - C Attribute: **NIRFSA_ATTR_NUMBER_OF_SAMPLES_IS_FINITE**

number_of_spectral_lines
------------------------

    .. py:attribute:: number_of_spectral_lines

        Specifies the number of spectral lines expected with the current power spectrum configuration.

        If you do not configure this property, NI-RFSA selects an appropriate value based on the :py:attr:`nirfsa.Session.resolution_bandwidth` property. If you configure this property, NI-RFSA coerces the :py:attr:`nirfsa.Session.resolution_bandwidth` value based on the number of spectral lines requested and the value of the :py:attr:`nirfsa.Session.spectrum_span` property.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Number Of Spectral Lines**
                - C Attribute: **NIRFSA_ATTR_NUMBER_OF_SPECTRAL_LINES**

osp_data_scaling_factor
-----------------------

    .. py:attribute:: osp_data_scaling_factor

        Specifies the scaling factor applied to the time-domain voltage data in the IF digitizer.

        Use this property to maximize the dynamic range of the digitizer by increasing the maximum IF power the digitizer can measure without creating OSP overflows.

        Because of the device amplitude response, some wide-band signals normally attenuated by the downconverter go through the IF digitizer without causing an ADC overflow. During IF equalization, these wide-band digitizer input signals may become amplified. These amplified input signal values overflow the available numeric range used in the signal processing algorithm.

        You can use this property when OSP calculations would generate an overflow while applying digital filters to the data. The OSP module in the digitizer multiplies the time-domain signal amplitude, in volts, by the specified property value before further onboard processing. Set this property to a value less than 1 to avoid OSP overflow for near full-scale IF signals and to use the maximum dynamic range of the digitizer. NI-RFSA compensates for the specified OSP data scaling factor to ensure that the correct scaled data, in absolute levels, is always returned regardless of the value of this property.

        **Valid Values:**: 0.25 to 1.0

        **Default Values:**

        **PXI-5661, PXIe-5663/5663E/5665 (3.6 GHz)/5667 (3.6 GHz)/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: 1.0

        **PXIe-5665 (14 GHz)/5667 (7 GHz)**: 0.8

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:OSP Data Scaling Factor**
                - C Attribute: **NIRFSA_ATTR_OSP_DATA_SCALING_FACTOR**

overflow_error_reporting
------------------------

    .. py:attribute:: overflow_error_reporting

        Configures error reporting for ADC and onboard signal processing overflows.

        Overflows lead to clipping of the waveform.

        **Defined Values:**

        %enum_table{overflow error reporting}

        **Default Value**: :py:data:`~nirfsa.OverflowErrorReporting.WARNING`

        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------+
            | Characteristic        | Value                        |
            +=======================+==============================+
            | Datatype              | enums.OverflowErrorReporting |
            +-----------------------+------------------------------+
            | Permissions           | read-write                   |
            +-----------------------+------------------------------+
            | Repeated Capabilities | None                         |
            +-----------------------+------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Overflow Error Reporting**
                - C Attribute: **NIRFSA_ATTR_OVERFLOW_ERROR_REPORTING**

p2p_enabled
-----------

    .. py:attribute:: p2p_enabled

        Specifies whether peer-to-peer streaming is enabled for the active stream endpoint.

        This property is `endpoint based <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/configuring-peer-to-peer-endpoint-ni-rfsa.html>`_.

        **Defined Values:**

        | Value                | Description                    |
        |:----------------|:--------------------|
        | True (1900)  | Enables streaming.  |
        | False (1901) | Disables streaming. |

        **Default Value**: False

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Enabled**
                - C Attribute: **NIRFSA_ATTR_P2P_ENABLED**

p2p_endpoint_overflow
---------------------

    .. py:attribute:: p2p_endpoint_overflow

        Indicates whether the endpoint has overflowed.

        An overflow condition occurs when data is written to the endpoint faster than it can be streamed from it. During an overflow, data in the endpoint begins to be overwritten. Reset the device or close the session to reset the overflow condition.

        **Defined Values:**

        | Value         | Description                                               |
        |:---------|:-----------------------------------------------|
        | True  | The endpoint has overflowed.                   |
        | False | You can write additional data to the endpoint. |

        **Default Value**: False

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Endpoint Overflow**
                - C Attribute: **NIRFSA_ATTR_P2P_ENDPOINT_OVERFLOW**

p2p_endpoint_size
-----------------

    .. py:attribute:: p2p_endpoint_size

        Returns the size, in samples, of the peer-to-peer endpoint.

        **Default Value**: 0

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Endpoint Size**
                - C Attribute: **NIRFSA_ATTR_P2P_ENDPOINT_SIZE**

p2p_fifo_endpoint_count
-----------------------

    .. py:attribute:: p2p_fifo_endpoint_count

        Returns the number of peer-to-peer streams supported by the device.

        **Default Value**: 0

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:FIFO Endpoint Count**
                - C Attribute: **NIRFSA_ATTR_P2P_FIFO_ENDPOINT_COUNT**

p2p_most_samples_available_in_endpoint
--------------------------------------

    .. py:attribute:: p2p_most_samples_available_in_endpoint

        Returns the largest number of complex samples available in the peer-to-peer endpoint since this property was last read.

        **Default Value**: 0

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Most Samples in P2P Endpoint**
                - C Attribute: **NIRFSA_ATTR_P2P_MOST_SAMPLES_AVAILABLE_IN_ENDPOINT**

p2p_onboard_memory_enabled
--------------------------

    .. py:attribute:: p2p_onboard_memory_enabled

        Specifies whether a limit is placed on the number of records and the size of the records by the size of the device onboard memory.

        When a peer-to-peer stream is enabled and onboard memory is disabled, any fetch calls result in an error.

        **Default Value**: False

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Onboard Memory Enabled**
                - C Attribute: **NIRFSA_ATTR_P2P_ONBOARD_MEMORY_ENABLED**

p2p_samples_available_in_endpoint
---------------------------------

    .. py:attribute:: p2p_samples_available_in_endpoint

        Returns the current number of complex samples available in the peer-to-peer endpoint.

        ----
        **Note**
        The complex samples are composed of two 16-bit words with the I data as the LSB.

        ----

        **Default Value**: 0

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Samples in P2P Endpoint**
                - C Attribute: **NIRFSA_ATTR_P2P_SAMPLES_AVAILABLE_IN_ENDPOINT**

p2p_samples_transferred
-----------------------

    .. py:attribute:: p2p_samples_transferred

        Returns the number of complex samples transferred through the peer-to-peer stream endpoint since the endpoint was last reset.

        **Default Value**: 0

        **Supported Devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Samples Transferred**
                - C Attribute: **NIRFSA_ATTR_P2P_SAMPLES_TRANSFERRED**

phase_offset
------------

    .. py:attribute:: phase_offset

        Specifies the offset to apply to the initial I and Q phases.

        **Valid Values**: 0 to 180

        **Default Value**: 0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:IQ:Phase Offset**
                - C Attribute: **NIRFSA_ATTR_PHASE_OFFSET**

power_spectrum_units
--------------------

    .. py:attribute:: power_spectrum_units

        Specifies the units of the power spectrum.

        **Defined Values:**

        %enum_table{spectrum units}

        **Default Value**: :py:data:`~nirfsa.SpectrumUnits.DBM`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | enums.SpectrumUnits |
            +-----------------------+---------------------+
            | Permissions           | read-write          |
            +-----------------------+---------------------+
            | Repeated Capabilities | None                |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Power Spectrum Units**
                - C Attribute: **NIRFSA_ATTR_POWER_SPECTRUM_UNITS**

preselector_present
-------------------

    .. py:attribute:: preselector_present

        Returns whether a preselector is available on the RF downconverter module.

        **Defined Values:**

        | Value         | Description                                                  |
        |:---------|:--------------------------------------------------|
        | True  | A preselector is available on the downconverter.  |
        | False | No preselector is available on the downconverter. |

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Preselector Present**
                - C Attribute: **NIRFSA_ATTR_PRESELECTOR_PRESENT**

pxi_chassis_clk10_source
------------------------

    .. py:attribute:: pxi_chassis_clk10_source

        Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane.

        This option can be configured only when the PXI-5600 is installed in Slot 2 of the PXI chassis.

        **Defined Values:**

        %enum_table{pxi chassis clk10 src}

        **Default Value**: N/A

        **Supported Devices**: PXI-5600 (external digitizer mode), PXI-5661

        **Related Topics**

        [System Reference Clock](nirfsa.chm/system-reference-clock.html)

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_pxi_chassis_clk10`

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.PxiChassisClk10Src |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | None                     |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:PXI Chassis Clk10 Source**
                - C Attribute: **NIRFSA_ATTR_PXI_CHASSIS_CLK10_SOURCE**

query_instrument_status
-----------------------

    .. py:attribute:: query_instrument_status

        Specifies whether NI-RFSA queries the NI-RFSA device status after each operation.

        Querying the device status is useful for debugging. After you validate your program, you can set this property to False to disable status checking and maximize performance.

        NI-RFSA can choose to ignore status checking for particular properties regardless of the setting of this property.

        ----
        **Note**
        Use the :py:meth:`nirfsa.Session.init_with_options` method to override this value.

        ----

        **Defined Values:**

        | Value         | Description                                                               |
        |:---------|:---------------------------------------------------------------|
        | True  | NI-RFSA queries the device status after each operation.        |
        | False | NI-RFSA does not query the device status after each operation. |

        **Default Value**: False

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Query Instrument Status**
                - C Attribute: **NIRFSA_ATTR_QUERY_INSTRUMENT_STATUS**

range_check
-----------

    .. py:attribute:: range_check

        Specifies whether to validate property values and method parameters.

        If enabled, NI-RFSA validates the parameter values that you pass to NI-RFSA methods. Range checking parameters is very useful for debugging. After you validate your program, you can set this property to False to disable range checking and maximize performance.

        ----
        **Note**
        Use the :py:meth:`nirfsa.Session.init_with_options` method to override this value.

        ----

        **Defined Values:**

        | Value         | Description                                                                    |
        |:---------|:--------------------------------------------------------------------|
        | True  | NI-RFSA validates property values and method parameters.         |
        | False | NI-RFSA does not validate property values and method parameters. |

        **Default Value**: True

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Range Check**
                - C Attribute: **NIRFSA_ATTR_RANGE_CHECK**

ready_for_advance_event_terminal_name
-------------------------------------

    .. py:attribute:: ready_for_advance_event_terminal_name

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

        - :py:meth:`nirfsa.Session.get_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Advance:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME**

ready_for_ref_event_terminal_name
---------------------------------

    .. py:attribute:: ready_for_ref_event_terminal_name

        Returns the fully qualified signal name as a string.

        **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>ReadyForReferenceEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

        **PXIe-5820/5840/5841/5842**: /<i>ModuleName/<i>ai/0/<i>ReadyForReferenceEvent</i>, where *ModuleName* is the name of your device in MAX.

        **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>ReadyForReferenceEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

        **All other devices**: /<i>DigitizerName</i>/<i>ReadyForReferenceEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.get_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Ref:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_READY_FOR_REF_EVENT_TERMINAL_NAME**

ready_for_start_event_terminal_name
-----------------------------------

    .. py:attribute:: ready_for_start_event_terminal_name

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

        - :py:meth:`nirfsa.Session.get_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Start:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_READY_FOR_START_EVENT_TERMINAL_NAME**

records_done
------------

    .. py:attribute:: records_done

        Returns the number of records the RF vector signal analyzer has acquired.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Fetch:Records Done**
                - C Attribute: **NIRFSA_ATTR_RECORDS_DONE**

record_coercions
----------------

    .. py:attribute:: record_coercions

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Record Value Coercions**
                - C Attribute: **NIRFSA_ATTR_RECORD_COERCIONS**

reference_level
---------------

    .. py:attribute:: reference_level

        Specifies the reference level, in dBm.

        The reference level represents the maximum expected power of an RF input signal.

        ----
        **Note**
        For the PXIe-5645, this property is ignored if you are using the I/Q ports.

        ----

        Refer to the :py:attr:`nirfsa.Session.external_gain` property for more information about how configuring an external gain and a reference level affect attenuation.

        **Default Value**: 0

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Improving Your Measurements <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/measurement_guidelines.html>`_

        `Programming Attenuation-Related Properties and Properties Using NI-RFSA <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/programming-attenuation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_reference_level`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Reference Level (dBm)**
                - C Attribute: **NIRFSA_ATTR_REFERENCE_LEVEL**

reference_level_headroom
------------------------

    .. py:attribute:: reference_level_headroom

        Specifies the margin NI-RFSA adds to the :py:attr:`nirfsa.Session.reference_level` property.

        The margin helps to avoid clipping and overflow warnings if the input signal exceeds the configured reference level.

        NI-RFSA configures the input gain to avoid clipping and associated overflow warnings as long as the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or have already included margin in the reference level, you may be able to improve the signal-to-noise ratio by reducing the reference level headroom.

        **Units**: dB

        **Default Value**:

        **PXIe-5830/5831/5832/5841/5842/5860**: 1 dB

        **PXIe-5840**: 0 dB

        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Reference Level Headroom (dB)**
                - C Attribute: **NIRFSA_ATTR_REFERENCE_LEVEL_HEADROOM**

ref_clock_rate
--------------

    .. py:attribute:: ref_clock_rate

        Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector.

        This property is only valid when the :py:attr:`nirfsa.Session.ref_clock_source` property is set to :py:data:`~nirfsa.NIRFSA_VAL_CLK_IN_STR`,:py:data:`~nirfsa.NIRFSA_VAL_REF_IN_STR` , or :py:data:`~nirfsa.RefClockSrc.REF_IN_2`.

        **Valid Values**:

        **PXIe-5644/5645/5646, PXIe-5601/5663/5663E, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841**: 10 MHz

        **PXIe-5603/5605/5665/5667/5668**: 5 MHz to 100 MHz, in increments of 1 MHz

        **PXIe-5841 with PXIe-5655, PXIe-5842**: 10 MHz, 100 MHz, 270 MHz, and 3.84 MHz  *y*, where *y* is 4, 8, 16, 24, 25, or 32.

        **PXIe-5860**: 10 MHz, 100 MHz

        **Default Value**: 10 MHz

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_ref_clock`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Ref Clock Rate**
                - C Attribute: **NIRFSA_ATTR_REF_CLOCK_RATE**

ref_clock_source
----------------

    .. py:attribute:: ref_clock_source

        Specifies the Reference Clock source.

        ----
        **Note**
        For the PXIe-5694, if your application requires an external LO source, set this property to :py:data:`~nirfsa.RefClockSrc.NONE`.

        ----

        **Defined Values:**

        %enum_table{ref clock src}

        **Default Values**:

        **PXIe-5694**: :py:data:`~nirfsa.RefClockSrc.REF_IN`

        **All other devices**: :py:data:`~nirfsa.RefClockSrc.ONBOARD_CLOCK`

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_ref_clock`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.RefClockSrc |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Ref Clock Source**
                - C Attribute: **NIRFSA_ATTR_REF_CLOCK_SOURCE**

ref_to_ref_trigger_holdoff
--------------------------

    .. py:attribute:: ref_to_ref_trigger_holdoff

        Specifies the minimum time, in seconds, that must elapse between Reference Triggers of two records.

        The device does not recognize the Reference Trigger of the next record before this minimum time elapses.

        **Units:**: seconds

        **Default Value**: 0

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Advanced:Ref To Ref Trigger Holdoff (s)**
                - C Attribute: **NIRFSA_ATTR_REF_TO_REF_TRIGGER_HOLDOFF**

ref_trigger_delay
-----------------

    .. py:attribute:: ref_trigger_delay

        Specifies the trigger delay time, in seconds.

        The trigger delay time is the length of time the IF digitizer waits after it receives the trigger before it asserts the Reference Event.

        **Units:**: seconds

        **Default Value**: 0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Advanced:Ref Trigger Delay (s)**
                - C Attribute: **NIRFSA_ATTR_REF_TRIGGER_DELAY**

ref_trigger_minimum_quiet_time
------------------------------

    .. py:attribute:: ref_trigger_minimum_quiet_time

        Specifies a time duration, in seconds, for which the signal must be quiet before the device arms the trigger.

        The signal is quiet when it is below the trigger level if the trigger slope, specified by the :py:attr:`nirfsa.Session.iq_power_edge_ref_trigger_slope` property, is set to :py:data:`~nirfsa.RefTrigIqPwrEdgeSlope.RISING` or when it is above the trigger level if the trigger slope is set to :py:data:`~nirfsa.RefTrigIqPwrEdgeSlope.FALLING`.

        By default, this value is set to 0, which means the device does not wait for a quiet time before arming the trigger. This property is useful to trigger the acquisition on signals containing repeated bursts, but for which each burst may have large changes in signal power within itself. By configuring the minimum quiet time to the time between bursts, you can ensure that the trigger occurs at the beginning of a burst rather than at the signal power change within a burst.

        **Default Value**: 0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Minimum Quiet Time**
                - C Attribute: **NIRFSA_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME**

ref_trigger_osp_delay_enabled
-----------------------------

    .. py:attribute:: ref_trigger_osp_delay_enabled

        Specifies whether the digitizer OSP block delays Reference Triggers, along with the data samples, moving through the OSP block or if the Reference Triggers bypass the OSP block and are processed immediately.

        Enabling this property requires the following equipment configurations:

        - All digitizers being used must be the same model and hardware revision.
        - All digitizers must use the same firmware.
        - All digitizers must be configured with the same I/Q rate.
        - All devices must use the same signal path.

        **PXIe-5663/5663E**: Read the value of the :py:attr:`nirfsa.Session.if_filter` property to determine the IF filters used by the PXIe-5663/5663E.

        **PXIe-5665/5667/5668**:Refer to the device-specific information in the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property to determine the IF filters used by the PXIe-5665/5667/5668. If you set the :py:attr:`nirfsa.Session.fft_width` property, refer to the device-specific information for this property and the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property to determine the IF filters used. For frequencies less than 3.6 GHz, set the :py:attr:`nirfsa.Session.rf_preamp_enabled` to the same value for all devices.

        **PXIe-5665 14 GHz**: Set the :py:attr:`nirfsa.Session.downconverter_preselector_enabled` to the same value for all devices.

        If the I/Q rate is set programmatically for I/Q acquisitions, the following properties should be identical for the best device synchronization:

        - :py:attr:`nirfsa.Session.digital_if_equalization_enabled`
        - :py:attr:`nirfsa.Session.spectrum_osp_sampling_ratio`

        For spectrum acquisitions, the following properties should be identical for the best device synchronization:

        - :py:attr:`nirfsa.Session.spectrum_span`
        - :py:attr:`nirfsa.Session.resolution_bandwidth_type`
        - :py:attr:`nirfsa.Session.digital_if_equalization_enabled`
        - :py:attr:`nirfsa.Session.spectrum_osp_sampling_ratio`

        For more information about the digitizer OSP block and Reference Triggers, refer to the following topics in the *NI High-Speed Digitizers Help*:

        - NI 5622 Onboard Signal Processing (OSP)
        - NI 5142 Onboard Signal Processing (OSP)
        - NI PXIe-5622 Trigger Sources
        - NI PXI-5142 Trigger Sources
        - NI PXIe-5622 Block Diagram
        - NI PXI-5142 Trigger Sources

        **Defined Values:**

        %enum_table{enable attr vals}

        **Default Value**: :py:data:`~nirfsa.EnableAttrVals.ENABLED`

        **Supported Devices**:PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Advanced:OSP Delay Enabled**
                - C Attribute: **NIRFSA_ATTR_REF_TRIGGER_OSP_DELAY_ENABLED**

ref_trigger_pretrigger_samples
------------------------------

    .. py:attribute:: ref_trigger_pretrigger_samples

        Specifies the number of pretrigger samples the samples acquired before the Reference Trigger is received to be acquired per record.

        **Default Value**: 0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_digital_edge_ref_trigger`
        - :py:meth:`nirfsa.Session.configure_software_edge_ref_trigger`
        - :py:meth:`nirfsa.Session.configure_iq_power_edge_ref_trigger`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Pretrigger Samples**
                - C Attribute: **NIRFSA_ATTR_REF_TRIGGER_PRETRIGGER_SAMPLES**

ref_trigger_terminal_name
-------------------------

    .. py:attribute:: ref_trigger_terminal_name

        Returns the fully qualified signal name as a string.

        **Default Values**:

        **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>RefTrigger</i>, where *BasebandModule* is the name of your baseband module of your device in MAX.

        **PXIe-5820/5840/5841/5842**: /<i>ModuleName/<i>ai</i>/0/<i>RefTrigger</i>, where *ModuleName* is the name of your device in MAX.

        **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>RefTrigger</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

        **All other devices**: /<i>DigitizerName</i>/<i>RefTrigger</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.get_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_REF_TRIGGER_TERMINAL_NAME**

ref_trigger_type
----------------

    .. py:attribute:: ref_trigger_type

        Specifies whether you want the Reference Trigger to be a digital edge, I/Q power edge, or software trigger.

        **Defined Values:**

        %enum_table{ref trig type}

        **Default Value**: :py:data:`~nirfsa.RefTrigType.NONE`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.RefTrigType |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Type**
                - C Attribute: **NIRFSA_ATTR_REF_TRIGGER_TYPE**

resolution_bandwidth
--------------------

    .. py:attribute:: resolution_bandwidth

        Specifies the resolution along the x-axis of the spectrum.

        NI-RFSA uses the resolution bandwidth value to determine the acquisition size. If specified, the :py:attr:`nirfsa.Session.number_of_spectral_lines` property value overrides this value.

        **Units**: hertz (Hz)

        **Default Value**: 100 kHz

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_resolution_bandwidth`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Resolution Bandwidth (Hz)**
                - C Attribute: **NIRFSA_ATTR_RESOLUTION_BANDWIDTH**

resolution_bandwidth_type
-------------------------

    .. py:attribute:: resolution_bandwidth_type

        Specifies how the :py:attr:`nirfsa.Session.resolution_bandwidth` property is expressed.

        **Defined Values:**

        %enum_table{spectrum resolution bandwidth type}

        **Default Value**: :py:data:`~nirfsa.SpectrumResolutionBandwidthType._3DB`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------------+
            | Characteristic        | Value                                 |
            +=======================+=======================================+
            | Datatype              | enums.SpectrumResolutionBandwidthType |
            +-----------------------+---------------------------------------+
            | Permissions           | read-write                            |
            +-----------------------+---------------------------------------+
            | Repeated Capabilities | None                                  |
            +-----------------------+---------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Resolution Bandwidth Type**
                - C Attribute: **NIRFSA_ATTR_RESOLUTION_BANDWIDTH_TYPE**

rf_attenuation_index
--------------------

    .. py:attribute:: rf_attenuation_index

        Specifies the value of the RF attenuation from a table of valid configurations.

        This property is valid only during a calibration session and when you set the :py:attr:`nirfsa.Session.low_frequency_bypass_enabled` property to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`.

        **Valid Values**: 0 to 64

        **Default Value**: N/A

        **Supported Devices**: PXIe-5693



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Factory Calibration:NI 5693:RF Attenuation Index**
                - C Attribute: **NIRFSA_ATTR_RF_ATTENUATION_INDEX**

rf_attenuation_step_size
------------------------

    .. py:attribute:: rf_attenuation_step_size

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:RF Attenuation Step Size (dB)**
                - C Attribute: **NIRFSA_ATTR_RF_ATTENUATION_STEP_SIZE**

rf_attenuation_table
--------------------

    .. py:attribute:: rf_attenuation_table

        Specifies which RF attenuator table to use.

        **Valid Values**: 0 to 1

        **Default Value**: N/A

        **Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:NI 5663:RF Attenuation Table**
                - C Attribute: **NIRFSA_ATTR_RF_ATTENUATION_TABLE**

rf_conditioning_cal_tone_frequency
----------------------------------

    .. py:attribute:: rf_conditioning_cal_tone_frequency

        Specifies the frequency of the RF conditioning calibration tone, in hertz (Hz).

        **Valid Values**: 34.5 MHz to 7.5 GHz

        **Default Value**: 1.0 GHz

        **Supported Devices**: PXIe-5667, PXIe-5693/5698

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Self Calibration:RF Conditioning Cal Tone Frequency**
                - C Attribute: **NIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_FREQUENCY**

rf_conditioning_cal_tone_mode
-----------------------------

    .. py:attribute:: rf_conditioning_cal_tone_mode

        Specifies the location in a signal path where an RF conditioning calibration tone is injected or whether the tone is disabled.

        **Defined Values:**

        %enum_table{conditioning cal tone mode}

        **Default Value**: :py:data:`~nirfsa.ConditioningCalToneMode.DISABLED`

        **Supported Devices**: PXIe-5667, PXIe-5693/5698



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------+
            | Characteristic        | Value                         |
            +=======================+===============================+
            | Datatype              | enums.ConditioningCalToneMode |
            +-----------------------+-------------------------------+
            | Permissions           | read-write                    |
            +-----------------------+-------------------------------+
            | Repeated Capabilities | None                          |
            +-----------------------+-------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Self Calibration:RF Conditioning Cal Tone Mode**
                - C Attribute: **NIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_MODE**

rf_conditioning_temperature
---------------------------

    .. py:attribute:: rf_conditioning_temperature

        Returns the current temperature, in degrees Celsius, of the RF conditioning module associated with the NI-RFSA device.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5667

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:RF Conditioning Temperature (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_RF_CONDITIONING_TEMPERATURE**

rf_high_pass_filtering
----------------------

    .. py:attribute:: rf_high_pass_filtering

        Specifies the maximum corner frequency of the highpass filter in the RF signal path.

        The device uses the highest frequency highpass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables highpass filtering.

        For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this property returns the value you specified rather than a coerced value if multiple highpass filters are used during the acquisition.

        The PXIe-5606 features highpass filters at 1.35 GHz and 2.2 GHz.

        **Valid Values**: 0 to 26.5

        **Default Value**: 0

        **Supported Devices**: PXIe-5606, PXIe-5668

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:RF Highpass Filtering**
                - C Attribute: **NIRFSA_ATTR_RF_HIGH_PASS_FILTERING**

rf_out_lo_export_enabled
------------------------

    .. py:attribute:: rf_out_lo_export_enabled

        Specifies whether to enable the RF OUT LO OUT terminal on the PXIe-5840/5841.

        When this property is enabled, if the :py:attr:`nirfsa.Session.lo_source` property is set to :py:data:`~nirfsa.LoSourceVals.LO_IN` and you do not set the :py:attr:`nirfsa.Session.lo_frequency` or :py:attr:`nirfsa.Session.downconverter_center_frequency` properties, NI-RFSA rounds the LO frequency to approximately an LO step size as if the source was :py:data:`~nirfsa.LoSourceVals.ONBOARD`. This ensures that when you configure NI-RFSA and NI-RFSG with compatible settings that result in the same LO frequency, the rounding also is compatible.

        **Defined Values:**

        %enum_table{enable unspecified attr vals}

        **Default Value:**: :py:data:`~nirfsa.EnableUnspecifiedAttrVals.UNSPECIFIED`

        **Supported Devices**: PXIe-5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.EnableUnspecifiedAttrVals |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | None                            |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:RF Out LO Export Enabled**
                - C Attribute: **NIRFSA_ATTR_RF_OUT_LO_EXPORT_ENABLED**

rf_preamp_enabled
-----------------

    .. py:attribute:: rf_preamp_enabled

        Specifies whether the RF preamplifier is enabled in the system.

        **PXIe-5667, PXIe-5644/5645/5646, PXIe-5830/5831/5840/5841/5842**: The  :py:data:`~nirfsa.EnableRfPreamp.AUTOMATIC` value enables the RF preamplifier based on the value of the :py:attr:`nirfsa.Session.reference_level` property and the center frequency. Except on the PXIe-5830/5831/5832, NI-RFSA coerces this property from :py:data:`~nirfsa.EnableRfPreamp.AUTOMATIC` to the selected value.

        ----
        **Note**
        For the PXIe-5840/5841, the automatically selected value may not be optimal for all measurements. At some reference levels, :py:data:`~nirfsa.EnableRfPreamp.ENABLED` may improve the noise floor while :py:data:`~nirfsa.EnableRfPreamp.DISABLED` may improve distortion.

        ----

        **PXIe-5667**: The :py:data:`~nirfsa.EnableRfPreamp.AUTOMATIC` value is supported only when the :py:attr:`nirfsa.Session.low_frequency_bypass_enabled` property is set to :py:data:`~nirfsa.EnableRfPreamp.DISABLED`. If the reference level is greater than -25 dBm, NI-RFSA disables the preamplifier. If the reference level is less than or equal to -25 dBm, NI-RFSA sets the :py:attr:`nirfsa.Session.rf_preamp_enabled` property to :py:data:`~nirfsa.EnableRfPreamp.ENABLED_WHEN_IN_SIGNAL_PATH`.

        **PXIe-5668 with PXIe-5698**: If you set this property to :py:attr:`nirfsa.Session.rf_preamp_enabled`, only the preamplifier on the PXIe-5698 is used, and the preamplifier on the PXIe-5668 remains disabled.

        **Defined Values:**

        %enum_table{enable rf preamp}

        **Default Value**:

        **PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842**: :py:data:`~nirfsa.EnableRfPreamp.AUTOMATIC`

        **All other devices**: :py:data:`~nirfsa.EnableRfPreamp.DISABLED`

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5698, PXIe-5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableRfPreamp |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Preamp Enabled**
                - C Attribute: **NIRFSA_ATTR_RF_PREAMP_ENABLED**

rf_preamp_present
-----------------

    .. py:attribute:: rf_preamp_present

        Returns whether an RF preamplifier is available on the RF downconverter module.

        **Defined Values:**

        | Value         | Description                                                     |
        |:---------|:-----------------------------------------------------|
        | True  | The device has an enabled RF preamplifier available. |
        | False | The device has no RF preamplifier available.         |

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:RF Preamp Present**
                - C Attribute: **NIRFSA_ATTR_RF_PREAMP_PRESENT**

rf_preselector_filter
---------------------

    .. py:attribute:: rf_preselector_filter

        Specifies the RF preselector filter to use.

        ----
        **Note**
        You can write to this property when using only the PXIe-5693 as a stand-alone device.

        ----

        **Defined Values**:

        %enum_table{rf preselector filter}

        **Default Values**:

        **PXIe-5667, PXIe-5693**: :py:data:`~nirfsa.RfPreselectorFilter._9`

        **PXIe-5665**: :py:data:`~nirfsa.RfPreselectorFilter.NONE`

        **Supported Devices**: PXIe-5665/5667, PXIe-5693

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | enums.RfPreselectorFilter |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | None                      |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:RF Preselector Filter**
                - C Attribute: **NIRFSA_ATTR_RF_PRESELECTOR_FILTER**

selected_path
-------------

    .. py:attribute:: selected_path

        Specifies which path to configure to acquire a signal.

        **Default Value**: "" (empty string)

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Selected Path**
                - C Attribute: **NIRFSA_ATTR_SELECTED_PATH**

selected_ports
--------------

    .. py:attribute:: selected_ports

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

        :py:attr:`nirfsa.Session.available_ports`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Selected Ports**
                - C Attribute: **NIRFSA_ATTR_SELECTED_PORTS**

serial_number
-------------

    .. py:attribute:: serial_number

        Returns the serial number of the RF downconverter module.

        ----
        **Note**
        For the PXIe-5644/5645/5646 and PXIe-5820/5840/5841, this property returns the serial number of the VST module. For the PXIe-5830/5831/5832, this property returns the serial number of the PXIe-3621/3622.

        ----

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Serial Number**
                - C Attribute: **NIRFSA_ATTR_SERIAL_NUMBER**

signal_bandwidth
----------------

    .. py:attribute:: signal_bandwidth

        Specifies the bandwidth of the input signal around the :py:attr:`nirfsa.Session.iq_carrier_frequency`.

        This value must be less than or equal to (0.8 7 [I/Q rate](:py:attr:`nirfsa.Session.iq_rate`.html)).

        NI-RFSA defines *signal bandwidth* as twice the maximum I/Q signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the signal bandwidth is simply the baseband signal's minimum frequency subtracted from its maximum frequency, or *f* < sub>max</sub> - *f*< sub>min</sub>.

        If you do not set this property, NI-RFSA uses the maximum available signal bandwidth. Depending on your device settings, setting this property enables certain optimizations. Based on the specified signal bandwidth, NI-RFSA decides the minimum equalized bandwidth and equalizer gain.

        ----
        **Note**
        You must set this property to enable the :py:attr:`nirfsa.Session.downconverter_frequency_offset_mode` property.

        ----

        Ensure you set the signal bandwidth wide enough to encompass all significant anticipated input power. In cases where NI-RFSA optimizes the input gain based on the signal bandwidth, significant input power outside the signal bandwidth can lead to clipping and associated overflow warnings if you do not have enough margin in your [reference level.](:py:attr:`nirfsa.Session.reference_level`.html)

        **Units**: Hz

        **Default Value**: 0 Hz

        **Supported Devices:**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-selection.html>`_

        `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-selection.html>`_

        `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-selection.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:IQ:Signal Bandwidth (Hz)**
                - C Attribute: **NIRFSA_ATTR_SIGNAL_BANDWIDTH**

signal_conditioning_enabled
---------------------------

    .. py:attribute:: signal_conditioning_enabled

        Specifies whether all signal conditioning is enabled on the PXIe-5694.

        ----
        **Note**
        If you set this property to :py:data:`~nirfsa.SignalConditioningEnabled.BYPASSED`, NI-RFSA bypasses all signal conditioning, prevents any signal downconversion, and fixes the values for :py:attr:`nirfsa.Session.downconverter_gain` property, the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property, and the :py:attr:`nirfsa.Session.if_filter_bandwidth` property.

        ----

        **Defined Values:**

        %enum_table{signal conditioning enabled}

        **Default Value**: :py:data:`~nirfsa.SignalConditioningEnabled.ENABLED`

        **Supported Devices**: PXIe-5694

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.SignalConditioningEnabled |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | None                            |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:NI 5694:Signal Conditioning Enabled**
                - C Attribute: **NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED**

simulate
--------

    .. py:attribute:: simulate

        Specifies whether NI-RFSA simulates I/O operations. This property is useful for debugging applications without using hardware. After a session is opened, you cannot change the simulation state. Use the :py:meth:`nirfsa.Session.init_with_options` method to enable simulation.

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

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
                - C Attribute: **NIRFSA_ATTR_SIMULATE**

smooth_spectrum_enabled
-----------------------

    .. py:attribute:: smooth_spectrum_enabled

        Specifies that an optimized IF filtering selection is made at different spectrum frequency ranges during spectrum acquisition.

        The IF filter used depends on the configured RF center frequency, as shown in the following table.

        | Center Frequency    | IF Filter |
        |:--------------------|:----------|
        | 0 Hz and <80 MHz | 300 kHz   |
        | 0 MHz             | 50 MHz    |

        ----
        **Note**
        Setting this property to **Enabled** prevents you from setting :py:attr:`nirfsa.Session.if_filter_bandwidth` or :py:attr:`nirfsa.Session.device_instantaneous_bandwidth`.

        ----

        **Defined Values:**

        %enum_table{enable attr vals}

        **Default Value**: :py:data:`~nirfsa.EnableAttrVals.DISABLED`

        **Supported Devices**: PXIe-5665/5668



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Smooth Spectrum Enabled**
                - C Attribute: **NIRFSA_ATTR_SMOOTH_SPECTRUM_ENABLED**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        Returns a string that contains a brief description of NI-RFSA.

        This property returns

        RF Signal Analyzer Instrument Driver.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Description**
                - C Attribute: **NIRFSA_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_prefix
----------------------

    .. py:attribute:: specific_driver_prefix

        Returns a string that contains the prefix for NI-RFSA. The name of each user-callable method in NI-RFSA starts with this prefix.

        This property returns

        niRFSA.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Prefix**
                - C Attribute: **NIRFSA_ATTR_SPECIFIC_DRIVER_PREFIX**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        Returns a string that contains additional version information about NI-RFSA.

        For example, NI-RFSA can return

        Driver: NI-RFSA 2.6, Compiler: MSVC 7.10, Components: IVI Engine 4.00, VISA-Spec 4.00 as the value of this property.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Revision**
                - C Attribute: **NIRFSA_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        Returns a string that contains the name of the vendor that supplies NI-RFSA.

        This property returns

        National Instruments.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Vendor**
                - C Attribute: **NIRFSA_ATTR_SPECIFIC_DRIVER_VENDOR**

spectrum_averaging_mode
-----------------------

    .. py:attribute:: spectrum_averaging_mode

        Specifies the averaging mode for the spectrum acquisition.

        **Defined Values:**

        %enum_table{spectrum averaging mode}

        **Default Value**: :py:data:`~nirfsa.SpectrumAveragingMode.NO`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.SpectrumAveragingMode |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Averaging Mode**
                - C Attribute: **NIRFSA_ATTR_SPECTRUM_AVERAGING_MODE**

spectrum_number_of_averages
---------------------------

    .. py:attribute:: spectrum_number_of_averages

        Specifies the number of acquisitions to average.

        The averaging process returns the final result after the number of averages is complete.

        **Default Value**: 10

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Number Of Averages**
                - C Attribute: **NIRFSA_ATTR_SPECTRUM_NUMBER_OF_AVERAGES**

spectrum_osp_sampling_ratio
---------------------------

    .. py:attribute:: spectrum_osp_sampling_ratio

        Specifies the oversampling ratio used by the digitizer onboard signal processing (OSP) when you are in spectrum acquisition mode. This property allows you to acquire a larger bandwidth in hardware and reduce that bandwidth in software, decreasing the possibility of hardware data path overflows.

        **PXIe-5644/5645/5646**: The only valid value for this property is 1.

        **Default Value**: 1.0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Spectrum OSP Sampling Ratio**
                - C Attribute: **NIRFSA_ATTR_SPECTRUM_OSP_SAMPLING_RATIO**

spectrum_span
-------------

    .. py:attribute:: spectrum_span

        Specifies the frequency range of the computed spectrum in hertz (Hz).

        For example, if you specify a center frequency of 1 GHz and a span of 100 MHz, the spectrum ranges from 950 MHz to 1,050 MHz after zoom processing. This value may be coerced based on hardware settings and RF downconverter specifications.

        NI-RFSA performs multispan acquisitions by dividing the total requested span into equally sized subspans based on the device instantaneous bandwidth at the range of frequencies you specify. NI-RFSA combines these subspans to yield a multispan acquisition. You can use the :py:attr:`nirfsa.Session.fft_width` property to improve amplitude accuracy and avoid unwanted effects such as filter roll-off and spurs across the span you select.

        ----
        **Note**
        If you configure the spectrum span to a value larger than the hardware instantaneous bandwidth, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you requested.

        ----

        ----
        **Note**
        For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect measurements. Refer to the :py:attr:`nirfsa.Session.digitizer_dither_enabled` property for more information about dithering.

        ----

        **PXIe-5663/5663E**: NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the instantaneous bandwidth for frequencies above 120 MHz is different than instantaneous bandwidth for frequencies less than 120 MHz, which are 20 MHz and 10 MHz respectively.

        **PXIe-5665 (14 GHz)/5667 (7 GHz)**: If you enable the downconverter preselector filter, the device instantaneous bandwidth is only a typical specification.

        **Default Value**: 10 MHz

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_spectrum_frequency_center_span`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Span**
                - C Attribute: **NIRFSA_ATTR_SPECTRUM_SPAN**

start_to_ref_trigger_holdoff
----------------------------

    .. py:attribute:: start_to_ref_trigger_holdoff

        Specifies the minimum time, in seconds, that must elapse after the Start Trigger is received before the device recognizes a Reference Trigger.

        **Units:** seconds

        **Default Value**: 0

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Advanced:Start To Ref Trigger Holdoff (s)**
                - C Attribute: **NIRFSA_ATTR_START_TO_REF_TRIGGER_HOLDOFF**

start_trigger_delay
-------------------

    .. py:attribute:: start_trigger_delay

        This property is not for customer use.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Advanced:Start Trigger Delay**
                - C Attribute: **NIRFSA_ATTR_START_TRIGGER_DELAY**

start_trigger_terminal_name
---------------------------

    .. py:attribute:: start_trigger_terminal_name

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

        - :py:meth:`nirfsa.Session.get_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_START_TRIGGER_TERMINAL_NAME**

start_trigger_type
------------------

    .. py:attribute:: start_trigger_type

        Specifies whether you want the Start Trigger to be a digital edge or software trigger.

        ----
        **Note**
        Set this property to :py:data:`~nirfsa.StartTrigType.NONE` if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` or if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the [cvi:py:meth:`nirfsa.Session.configure_acquisition_type`](cvi:py:meth:`nirfsa.Session.configure_acquisition_type`.html) method.

        ----

        **Defined Values:**

        %enum_table{start trig type}

        **Default Value**: :py:data:`~nirfsa.StartTrigType.NONE`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | enums.StartTrigType |
            +-----------------------+---------------------+
            | Permissions           | read-write          |
            +-----------------------+---------------------+
            | Repeated Capabilities | None                |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Type**
                - C Attribute: **NIRFSA_ATTR_START_TRIGGER_TYPE**

step_gain_enabled
-----------------

    .. py:attribute:: step_gain_enabled

        Specifies whether to enable the step gain amplifier.

        **Defined Values:**

        %enum_table{step gain enabled}

        **Default Value**: :py:data:`~nirfsa.StepGainEnabled.DISABLED`

        **Supported Devices**: PXIe-5694

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.StepGainEnabled |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:NI 5694:Step Gain Enabled**
                - C Attribute: **NIRFSA_ATTR_STEP_GAIN_ENABLED**

subspan_overlap
---------------

    .. py:attribute:: subspan_overlap

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Subspan Overlap**
                - C Attribute: **NIRFSA_ATTR_SUBSPAN_OVERLAP**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        Returns a comma-separated list of supported devices.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NIRFSA_ATTR_SUPPORTED_INSTRUMENT_MODELS**

sync_advance_trigger_dist_line
------------------------------

    .. py:attribute:: sync_advance_trigger_dist_line

        Specifies which external trigger line distributes the synchronized Advance Trigger signal.

        When synchronizing the Advance Trigger, configure all devices to use the same Advance Trigger distribution line.

        Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

        **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

        **Default Value**: "" (empty string)

        **Supported Devices:** PXIe-5644/5645/5646

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Advance Trigger Dist Line**
                - C Attribute: **NIRFSA_ATTR_SYNC_ADVANCE_TRIGGER_DIST_LINE**

sync_advance_trigger_master
---------------------------

    .. py:attribute:: sync_advance_trigger_master

        Specifies whether the device is the master for synchronizing the shared Advance Trigger between multiple devices.

        The master device distributes the synchronized Advance Trigger to all devices in the system through the Advance Trigger distribution line.

        When synchronizing the Advance Trigger, one device must always be designated as the master. When the device is configured as a master, it actively drives the Advance Trigger distribution line. When the device is configured as a slave, set the :py:attr:`nirfsa.Session.advance_trigger_type` property to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`, and the :py:attr:`nirfsa.Session.digital_edge_advance_trigger_source` property to NIRFSA VAL SYNC ADVANCE TRIGGER STR.

        Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

        **Defined Values:**

        | Value         | Description                                                                           |
        |:---------|:---------------------------------------------------------------------------|
        | True  | The device is the master device for synchronizing the Advance Trigger.     |
        | False | The device is not the master device for synchronizing the Advance Trigger. |

        **Default Value**: False

        **Supported Devices:** PXIe-5644/5645/5646



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Advance Trigger Master**
                - C Attribute: **NIRFSA_ATTR_SYNC_ADVANCE_TRIGGER_MASTER**

sync_ref_trigger_delay_enabled
------------------------------

    .. py:attribute:: sync_ref_trigger_delay_enabled

        Specifies whether the Reference Trigger is delayed with the data.

        Set this property to :py:data:`~nirfsa.EnableAttrVals.DISABLED` when the :py:attr:`nirfsa.Session.ref_trigger_type` property is set to :py:data:`~nirfsa.RefTrigType.IQ_POWER_EDGE` or :py:data:`~nirfsa.RefTrigType.IQ_ANALOG_EDGE`.

        Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

        **Defined Values:**

        %enum_table{enable attr vals}

        **Default Value**: :py:data:`~nirfsa.EnableAttrVals.DISABLED`

        **Supported Devices:** PXIe-5644/5645/5646



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableAttrVals |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Ref Trigger Delay Enabled**
                - C Attribute: **NIRFSA_ATTR_SYNC_REF_TRIGGER_DELAY_ENABLED**

sync_ref_trigger_dist_line
--------------------------

    .. py:attribute:: sync_ref_trigger_dist_line

        Specifies which external trigger line distributes the synchronized Reference Trigger signal.

        When synchronizing the Reference Trigger, configure all devices to use the same Reference Trigger distribution line.

        Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

        **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

        **Default Value**: "" (empty string)

        **Supported Devices:** PXIe-5644/5645/5646

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Ref Trigger Dist Line**
                - C Attribute: **NIRFSA_ATTR_SYNC_REF_TRIGGER_DIST_LINE**

sync_ref_trigger_master
-----------------------

    .. py:attribute:: sync_ref_trigger_master

        Specifies whether the device is the master for synchronizing the shared Reference Trigger between multiple devices.

        The master device distributes the synchronized Reference Trigger to all devices in the system through the Reference Trigger distribution line.

        When synchronizing the Reference Trigger, one device must always be designated as the master. When the device is configured as a master, it actively drives the Reference Trigger distribution line. When the device is configured as a slave, set the :py:attr:`nirfsa.Session.ref_trigger_type` property to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`, and the :py:attr:`nirfsa.Session.digital_edge_ref_trigger_source` property to NIRFSA VAL SYNC REF TRIGGER STR.

        Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

        **Defined Values:**

        |Value          | Description                                                                       |
        |:---------|:-----------------------------------------------------------------------|
        | True  | The device is the master device for synchronizing the Ref Trigger.     |
        | False | The device is not the master device for synchronizing the Ref Trigger. |

        **Default Value**: False

        **Supported Devices:** PXIe-5644/5645/5646



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Ref Trigger Master**
                - C Attribute: **NIRFSA_ATTR_SYNC_REF_TRIGGER_MASTER**

sync_sample_clock_dist_line
---------------------------

    .. py:attribute:: sync_sample_clock_dist_line

        Specifies which external trigger line distributes the Sample Clock sync signal.

        When synchronizing the Sample Clock, configure all devices to use the same Sample Clock distribution line.

        Refer to `Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/pxie-5644-feature/page/synchronization-rfsa-g.html>`_ for more information about PXIe-5646 device synchronization.

        **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

        **Default Value:** "" (empty string)

        **Supported Devices:** PXIe-5646

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Sample Clock Dist Line**
                - C Attribute: **NIRFSA_ATTR_SYNC_SAMPLE_CLOCK_DIST_LINE**

sync_sample_clock_master
------------------------

    .. py:attribute:: sync_sample_clock_master

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

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Sample Clock Master**
                - C Attribute: **NIRFSA_ATTR_SYNC_SAMPLE_CLOCK_MASTER**

sync_start_trigger_dist_line
----------------------------

    .. py:attribute:: sync_start_trigger_dist_line

        Specifies which external trigger line distributes the synchronized Start Trigger signal.

        When synchronizing the Start Trigger, configure all devices to use the same Start Trigger distribution line.

        Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

        **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Start Trigger Dist Line**
                - C Attribute: **NIRFSA_ATTR_SYNC_START_TRIGGER_DIST_LINE**

sync_start_trigger_master
-------------------------

    .. py:attribute:: sync_start_trigger_master

        Specifies whether the device is the master for synchronizing the shared Start Trigger between multiple devices.

        The master device distributes the synchronized Start Trigger to all devices in the system through the Start Trigger distribution line.

        When synchronizing the Start Trigger, one device must always be designated as the master. When the device is configured as a master, it actively drives the Start Trigger distribution line. When the device is configured as a slave, set the :py:attr:`nirfsa.Session.start_trigger_type` property to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`, and the :py:attr:`nirfsa.Session.digital_edge_start_trigger_source` property to NIRFSA VAL SYNC START TRIGGER STR.

        Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

        **Defined Values:**

        |Value          | Description                                                                         |
        |:---------|:-------------------------------------------------------------------------|
        | True  | The device is the master device for synchronizing the Start Trigger.     |
        | False | The device is not the master device for synchronizing the Start Trigger. |

        **Default Value**: False

        **Supported Devices:** PXIe-5644/5645/5646



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Start Trigger Master**
                - C Attribute: **NIRFSA_ATTR_SYNC_START_TRIGGER_MASTER**

temperature_read_interval
-------------------------

    .. py:attribute:: temperature_read_interval

        Indicates the minimum time between temperature sensor readings in seconds.

        When you call the :py:meth:`nirfsa.Session.read_power_spectrum_f64` method, the :py:meth:`nirfsa.Session.read_iq_single_record_complex_f64` method, or the :py:meth:`nirfsa.Session._initiate` method, NI-RFSA checks whether at least the amount of time specified by this property has elapsed before reading the hardware temperature.

        ----
        **Note**
        NI-RFSA ignores this property if you call the :py:meth:`nirfsa.Session.perform_thermal_correction` method or read the :py:attr:`nirfsa.Session.downconverter_gain` property.

        ----

        **Default Value**: 30 seconds

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Temperature Read Interval**
                - C Attribute: **NIRFSA_ATTR_TEMPERATURE_READ_INTERVAL**

thermal_correction_headroom_range
---------------------------------

    .. py:attribute:: thermal_correction_headroom_range

        Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the :py:attr:`nirfsa.Session.device_temperature` property.

        For example, if this property is set to 5.0, and the device is self-calibrated at 35 C, then you can expect to run the device from 30 C to 40 C with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance and ADC or DSP overflows.

        **Units:** degrees Celsius (C)

        **Default Value**:

        **PXIe-5830/5831/5832/5842/5860**: 5

        **PXIe-5840/5841**: 10

        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Thermal Correction Headroom Range (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_THERMAL_CORRECTION_HEADROOM_RANGE**

thermal_correction_temperature_resolution
-----------------------------------------

    .. py:attribute:: thermal_correction_temperature_resolution

        Specifies the temperature change required before NI-RFSA recalculates the thermal correction settings when entering the Running state.

        **Units:** degrees Celsius (C)

        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Default Values**:

        **PXIe-5830/5831/5832/5842/5860**: 0.2

        **PXIe-5840/5841**: 1.0

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Thermal Correction Temperature Resolution (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION**

timer_event_interval
--------------------

    .. py:attribute:: timer_event_interval

        Specifies the time, in seconds, that the timer counts before generating a Timer Event.

        After the timer reaches zero, it automatically restarts.

        ----
        **Note**
        For the PXIe-5820/5830/5831/5832/5840/5841/5842 and the PXIe-5842 with S-parameters, this property must be set for the timer to start. If you do not set this property, the timer is disabled.

        ----

        **Units**: seconds

        **Default Value**: 0.01

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration List:Timer Event Interval**
                - C Attribute: **NIRFSA_ATTR_TIMER_EVENT_INTERVAL**

timer_start_source
------------------

    .. py:attribute:: timer_start_source

        This property is not for customer use.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration List:Advanced:Timer Start Source**
                - C Attribute: **NIRFSA_ATTR_TIMER_START_SOURCE**

user_source_pulse_width
-----------------------

    .. py:attribute:: user_source_pulse_width

        Specifies the pulse width for the User Source.

        Use the :py:attr:`nirfsa.Session.user_source_pulse_width_units` property to set the units for the pulse width.

        **Default Value**: 200E(-9)

        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:User Source:Pulse Width**
                - C Attribute: **NIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH**

user_source_pulse_width_units
-----------------------------

    .. py:attribute:: user_source_pulse_width_units

        Specifies the pulse width units for the User Source.

        When the value is :py:data:`~nirfsa.UserSourcePulseWidthUnits.SECONDS`, it is assumed that the clock rate of the signal is the data clock. Use :py:data:`~nirfsa.UserSourcePulseWidthUnits.CLOCK_PERIODS` if the user source clock rate is anything else.

        **Defined Values:**

        %enum_table{user source pulse width units}

        **Default Value**: :py:data:`~nirfsa.UserSourcePulseWidthUnits.SECONDS`

        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.UserSourcePulseWidthUnits |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | None                            |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:User Source:Pulse Width Units**
                - C Attribute: **NIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH_UNITS**


NI-TClk Support
===============

    .. py:attribute:: tclk

        This is used to get and set NI-TClk attributes on the session.

        .. seealso:: See :py:class:`nitclk.SessionReference` for a complete list of attributes.


.. contents:: Session
