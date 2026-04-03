# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import nirfsa._complextype as _complextype
import nirfsa._library_singleton as _library_singleton
import nirfsa._visatype as _visatype
import nirfsa.enums as enums  # noqa: F401
import nirfsa.errors as errors


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        if library_type in (_complextype.NIComplexI16, _complextype.NIComplexNumberF32, _complextype.NIComplexNumber):
            complex_dtype = numpy.dtype(library_type)
            if value.ndim > 1:
                # we create a flattened view of the multi-dimensional numpy array
                restructured_array_view = value.ravel().view(complex_dtype)
            else:
                restructured_array_view = value.view(complex_dtype)
            return restructured_array_view.ctypes.data_as(ctypes.POINTER(library_type))
        else:
            return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def _convert_to_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()
        # Initialize _vi to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self.set_session_handle()

    def set_session_handle(self, value=0):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            returned_error_code, error_string = self.get_error()
            if returned_error_code == error_code:
                return error_string
        except errors.Error:
            pass
        return "Failed to retrieve error description."

    def abort(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def cal_adjust_cal_tone_power(self, channel_list, measurement):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        measurement_ctype = _visatype.ViReal64(measurement)  # case S150
        error_code = self._library.niRFSA_CalAdjustCalTonePower(vi_ctype, channel_list_ctype, measurement_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def cal_adjust_device_gain(self, channel_list, frequency, gain):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        gain_ctype = _visatype.ViReal64(gain)  # case S150
        error_code = self._library.niRFSA_CalAdjustDeviceGain(vi_ctype, channel_list_ctype, frequency_ctype, gain_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def cal_adjust_downconverter_gain(self, channel_list, frequency, gain):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        gain_ctype = _visatype.ViReal64(gain)  # case S150
        error_code = self._library.niRFSA_CalAdjustDownconverterGain(vi_ctype, channel_list_ctype, frequency_ctype, gain_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def cal_adjust_if_attenuation_calibration(self, channel_list, if_filter, number_of_attenuators, measurement):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        if_filter_ctype = _visatype.ViInt32(if_filter)  # case S150
        number_of_attenuators_ctype = _visatype.ViInt32(number_of_attenuators)  # case S150
        attenuator_settings_ctype = _visatype.ViReal64()  # case S220
        measurement_ctype = _visatype.ViReal64(measurement)  # case S150
        error_code = self._library.niRFSA_CalAdjustIfAttenuationCalibration(vi_ctype, channel_list_ctype, if_filter_ctype, number_of_attenuators_ctype, None if attenuator_settings_ctype is None else (ctypes.pointer(attenuator_settings_ctype)), measurement_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attenuator_settings_ctype.value)

    def cal_adjust_if_response_calibration(self, channel_list, if_filter, rf_frequency, band_width, number_of_measurements):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        if_filter_ctype = _visatype.ViInt32(if_filter)  # case S150
        rf_frequency_ctype = _visatype.ViReal64(rf_frequency)  # case S150
        band_width_ctype = _visatype.ViReal64(band_width)  # case S150
        number_of_measurements_ctype = _visatype.ViInt32(number_of_measurements)  # case S150
        measurements_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSA_CalAdjustIfResponseCalibration(vi_ctype, channel_list_ctype, if_filter_ctype, rf_frequency_ctype, band_width_ctype, number_of_measurements_ctype, None if measurements_ctype is None else (ctypes.pointer(measurements_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(measurements_ctype.value)

    def cal_adjust_lo_export_calibration(self, channel_list, lo_number, number_of_frequency_points):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        lo_number_ctype = _visatype.ViInt32(lo_number)  # case S150
        number_of_frequency_points_ctype = _visatype.ViInt32(number_of_frequency_points)  # case S150
        frequency_points_ctype = _visatype.ViReal64()  # case S220
        lo_attenuation_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSA_CalAdjustLoExportCalibration(vi_ctype, channel_list_ctype, lo_number_ctype, number_of_frequency_points_ctype, None if frequency_points_ctype is None else (ctypes.pointer(frequency_points_ctype)), None if lo_attenuation_ctype is None else (ctypes.pointer(lo_attenuation_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(frequency_points_ctype.value), float(lo_attenuation_ctype.value)

    def cal_adjust_ref_level_calibration(self, channel_list, reference_level_data_type, rf_band, attenuator_table_number, frequency, measurement):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        reference_level_data_type_ctype = _visatype.ViInt32(reference_level_data_type)  # case S150
        rf_band_ctype = _visatype.ViInt32(rf_band)  # case S150
        attenuator_table_number_ctype = _visatype.ViInt32(attenuator_table_number)  # case S150
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        measurement_ctype = _visatype.ViReal64(measurement)  # case S150
        error_code = self._library.niRFSA_CalAdjustRefLevelCalibration(vi_ctype, channel_list_ctype, reference_level_data_type_ctype, rf_band_ctype, attenuator_table_number_ctype, frequency_ctype, measurement_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def cal_set_temperature(self, channel_list, temperature):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        temperature_ctype = _visatype.ViReal64(temperature)  # case S150
        error_code = self._library.niRFSA_CalSetTemperature(vi_ctype, channel_list_ctype, temperature_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def change_ext_cal_password(self, old_password, new_password):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        old_password_ctype = ctypes.create_string_buffer(old_password.encode(self._encoding))  # case C020
        new_password_ctype = ctypes.create_string_buffer(new_password.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_ChangeExtCalPassword(vi_ctype, old_password_ctype, new_password_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def check_acquisition_status(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        is_done_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSA_CheckAcquisitionStatus(vi_ctype, None if is_done_ctype is None else (ctypes.pointer(is_done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(is_done_ctype.value)

    def clear_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_ClearError(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_self_calibrate_range(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_ClearSelfCalibrateRange(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_Close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close_calibration_step(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_CloseCalibrationStep(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close_ext_cal(self, action):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        action_ctype = _visatype.ViInt32(action)  # case S150
        error_code = self._library.niRFSA_CloseExtCal(vi_ctype, action_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close_external_alignment(self, action):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        action_ctype = _visatype.ViInt32(action)  # case S150
        error_code = self._library.niRFSA_CloseExternalAlignment(vi_ctype, action_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close_external_alignment_step(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_CloseExternalAlignmentStep(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_acquisition_type(self, acquisition_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        acquisition_type_ctype = _visatype.ViInt32(acquisition_type)  # case S150
        error_code = self._library.niRFSA_ConfigureAcquisitionType(vi_ctype, acquisition_type_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_deembedding_table_interpolation_linear(self, port, table_name, format):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format)  # case S150
        error_code = self._library.niRFSA_ConfigureDeembeddingTableInterpolationLinear(vi_ctype, port_ctype, table_name_ctype, format_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_deembedding_table_interpolation_nearest(self, port, table_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_ConfigureDeembeddingTableInterpolationNearest(vi_ctype, port_ctype, table_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_deembedding_table_interpolation_spline(self, port, table_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_ConfigureDeembeddingTableInterpolationSpline(vi_ctype, port_ctype, table_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_advance_trigger(self, source, edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge)  # case S150
        error_code = self._library.niRFSA_ConfigureDigitalEdgeAdvanceTrigger(vi_ctype, source_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_ref_trigger(self, source, edge, pretrigger_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge)  # case S150
        pretrigger_samples_ctype = _visatype.ViInt64(pretrigger_samples)  # case S150
        error_code = self._library.niRFSA_ConfigureDigitalEdgeRefTrigger(vi_ctype, source_ctype, edge_ctype, pretrigger_samples_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_start_trigger(self, source, edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge)  # case S150
        error_code = self._library.niRFSA_ConfigureDigitalEdgeStartTrigger(vi_ctype, source_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_iq_carrier_frequency(self, channel_list, carrier_frequency):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        carrier_frequency_ctype = _visatype.ViReal64(carrier_frequency)  # case S150
        error_code = self._library.niRFSA_ConfigureIqCarrierFrequency(vi_ctype, channel_list_ctype, carrier_frequency_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_iq_power_edge_ref_trigger(self, source, level, slope, pretrigger_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        level_ctype = _visatype.ViReal64(level)  # case S150
        slope_ctype = _visatype.ViInt32(slope)  # case S150
        pretrigger_samples_ctype = _visatype.ViInt64(pretrigger_samples)  # case S150
        error_code = self._library.niRFSA_ConfigureIqPowerEdgeRefTrigger(vi_ctype, source_ctype, level_ctype, slope_ctype, pretrigger_samples_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_iq_rate(self, channel_list, iq_rate):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        iq_rate_ctype = _visatype.ViReal64(iq_rate)  # case S150
        error_code = self._library.niRFSA_ConfigureIqRate(vi_ctype, channel_list_ctype, iq_rate_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_number_of_records(self, channel_list, number_of_records_is_finite, number_of_records):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        number_of_records_is_finite_ctype = _visatype.ViBoolean(number_of_records_is_finite)  # case S150
        number_of_records_ctype = _visatype.ViInt64(number_of_records)  # case S150
        error_code = self._library.niRFSA_ConfigureNumberOfRecords(vi_ctype, channel_list_ctype, number_of_records_is_finite_ctype, number_of_records_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_number_of_samples(self, channel_list, number_of_samples_is_finite, samples_per_record):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        number_of_samples_is_finite_ctype = _visatype.ViBoolean(number_of_samples_is_finite)  # case S150
        samples_per_record_ctype = _visatype.ViInt64(samples_per_record)  # case S150
        error_code = self._library.niRFSA_ConfigureNumberOfSamples(vi_ctype, channel_list_ctype, number_of_samples_is_finite_ctype, samples_per_record_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_pxi_chassis_clk10(self, pxi_clk10_source):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pxi_clk10_source_ctype = ctypes.create_string_buffer(pxi_clk10_source.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_ConfigurePxiChassisClk10(vi_ctype, pxi_clk10_source_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_ref_clock(self, clock_source, ref_clock_rate):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        clock_source_ctype = ctypes.create_string_buffer(clock_source.encode(self._encoding))  # case C020
        ref_clock_rate_ctype = _visatype.ViReal64(ref_clock_rate)  # case S150
        error_code = self._library.niRFSA_ConfigureRefClock(vi_ctype, clock_source_ctype, ref_clock_rate_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_reference_level(self, channel_list, reference_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        reference_level_ctype = _visatype.ViReal64(reference_level)  # case S150
        error_code = self._library.niRFSA_ConfigureReferenceLevel(vi_ctype, channel_list_ctype, reference_level_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_resolution_bandwidth(self, channel_list, resolution_bandwidth):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        resolution_bandwidth_ctype = _visatype.ViReal64(resolution_bandwidth)  # case S150
        error_code = self._library.niRFSA_ConfigureResolutionBandwidth(vi_ctype, channel_list_ctype, resolution_bandwidth_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_software_edge_advance_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_software_edge_ref_trigger(self, pretrigger_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pretrigger_samples_ctype = _visatype.ViInt64(pretrigger_samples)  # case S150
        error_code = self._library.niRFSA_ConfigureSoftwareEdgeRefTrigger(vi_ctype, pretrigger_samples_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_software_edge_start_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_ConfigureSoftwareEdgeStartTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_spectrum_frequency_center_span(self, channel_list, center_frequency, span):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        center_frequency_ctype = _visatype.ViReal64(center_frequency)  # case S150
        span_ctype = _visatype.ViReal64(span)  # case S150
        error_code = self._library.niRFSA_ConfigureSpectrumFrequencyCenterSpan(vi_ctype, channel_list_ctype, center_frequency_ctype, span_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_spectrum_frequency_start_stop(self, channel_list, start_frequency, stop_frequency):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        start_frequency_ctype = _visatype.ViReal64(start_frequency)  # case S150
        stop_frequency_ctype = _visatype.ViReal64(stop_frequency)  # case S150
        error_code = self._library.niRFSA_ConfigureSpectrumFrequencyStartStop(vi_ctype, channel_list_ctype, start_frequency_ctype, stop_frequency_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_configuration_list(self, list_name, number_of_list_attributes, set_as_active_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        list_name_ctype = ctypes.create_string_buffer(list_name.encode(self._encoding))  # case C020
        number_of_list_attributes_ctype = _visatype.ViInt32(number_of_list_attributes)  # case S150
        list_attribute_i_ds_ctype = _visatype.ViAttr()  # case S220
        set_as_active_list_ctype = _visatype.ViBoolean(set_as_active_list)  # case S150
        error_code = self._library.niRFSA_CreateConfigurationList(vi_ctype, list_name_ctype, number_of_list_attributes_ctype, None if list_attribute_i_ds_ctype is None else (ctypes.pointer(list_attribute_i_ds_ctype)), set_as_active_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(list_attribute_i_ds_ctype.value)

    def create_configuration_list_step(self, set_as_active_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        set_as_active_step_ctype = _visatype.ViBoolean(set_as_active_step)  # case S150
        error_code = self._library.niRFSA_CreateConfigurationListStep(vi_ctype, set_as_active_step_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        frequencies_ctype = _get_ctypes_pointer_for_buffer(value=frequencies)  # case B510
        frequencies_size_ctype = _visatype.ViInt32(0 if frequencies is None else len(frequencies))  # case S160
        sparameter_table_ctype = _get_ctypes_pointer_for_buffer(value=sparameter_table, library_type=_complextype.NIComplexNumber)  # case B510
        sparameter_table_size_ctype = _visatype.ViInt32(0 if sparameter_table is None else sparameter_table.size)  # case S161
        number_of_ports_ctype = _visatype.ViInt32(number_of_ports)  # case S150
        sparameter_orientation_ctype = _visatype.ViInt32(sparameter_orientation)  # case S150
        error_code = self._library.niRFSA_CreateDeembeddingSparameterTableArray(vi_ctype, port_ctype, table_name_ctype, frequencies_ctype, frequencies_size_ctype, sparameter_table_ctype, sparameter_table_size_ctype, number_of_ports_ctype, sparameter_orientation_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        s2p_file_path_ctype = ctypes.create_string_buffer(s2p_file_path.encode(self._encoding))  # case C020
        sparameter_orientation_ctype = _visatype.ViInt32(sparameter_orientation)  # case S150
        error_code = self._library.niRFSA_CreateDeembeddingSparameterTableS2PFile(vi_ctype, port_ctype, table_name_ctype, s2p_file_path_ctype, sparameter_orientation_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_all_deembedding_tables(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_DeleteAllDeembeddingTables(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_configuration_list(self, list_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        list_name_ctype = ctypes.create_string_buffer(list_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_DeleteConfigurationList(vi_ctype, list_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_deembedding_table(self, port, table_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_DeleteDeembeddingTable(vi_ctype, port_ctype, table_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_advance_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_DisableAdvanceTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_ref_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_DisableRefTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_start_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_DisableStartTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enable_session_access(self, enable):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        enable_ctype = _visatype.ViBoolean(enable)  # case S150
        error_code = self._library.niRFSA_EnableSessionAccess(vi_ctype, enable_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, status_code, error_message):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        status_code_ctype = _visatype.ViStatus(status_code)  # case S150
        error_message_ctype = ctypes.create_string_buffer(error_message.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_ErrorMessage(vi_ctype, status_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_query(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViInt32()  # case S220
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niRFSA_ErrorQuery(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(error_code_ctype.value), error_message_ctype.value.decode(self._encoding)

    def export_signal(self, signal, signal_identifier, output_terminal):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        signal_ctype = _visatype.ViInt32(signal)  # case S150
        signal_identifier_ctype = ctypes.create_string_buffer(signal_identifier.encode(self._encoding))  # case C020
        output_terminal_ctype = ctypes.create_string_buffer(output_terminal.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_ExportSignal(vi_ctype, signal_ctype, signal_identifier_ctype, output_terminal_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def ext_cal_store_baseline_for_self_calibration(self, password, self_calibration_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        password_ctype = ctypes.create_string_buffer(password.encode(self._encoding))  # case C020
        self_calibration_step_ctype = _visatype.ViInt64(self_calibration_step)  # case S150
        error_code = self._library.niRFSA_ExtCalStoreBaselineForSelfCalibration(vi_ctype, password_ctype, self_calibration_step_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def external_alignment_adjust_preselector(self, coefficients):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_coefficients_ctype = _visatype.ViInt32(0 if coefficients is None else len(coefficients))  # case S160
        coefficients_array = _convert_to_array(value=coefficients, array_type="d")  # case B550
        coefficients_ctype = _get_ctypes_pointer_for_buffer(value=coefficients_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niRFSA_ExternalAlignmentAdjustPreselector(vi_ctype, number_of_coefficients_ctype, coefficients_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch_iq_multi_record_complex_f32(self, channel_list, starting_record, number_of_records, number_of_samples, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        starting_record_ctype = _visatype.ViInt64(starting_record)  # case S150
        number_of_records_ctype = _visatype.ViInt64(number_of_records)  # case S150
        number_of_samples_ctype = _visatype.ViInt64(number_of_samples)  # case S150
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        data_ctype = _visatype.ni_complex_number_f32()  # case S220
        wfm_info_ctype = _visatype.niRFSA_wfmInfo()  # case S220
        error_code = self._library.niRFSA_FetchIqMultiRecordComplexF32(vi_ctype, channel_list_ctype, starting_record_ctype, number_of_records_ctype, number_of_samples_ctype, timeout_ctype, None if data_ctype is None else (ctypes.pointer(data_ctype)), None if wfm_info_ctype is None else (ctypes.pointer(wfm_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return ni_complex_number_f32(data_ctype.value), niRFSA_wfmInfo(wfm_info_ctype.value)

    def fetch_iq_multi_record_complex_f64(self, channel_list, starting_record, number_of_records, number_of_samples, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        starting_record_ctype = _visatype.ViInt64(starting_record)  # case S150
        number_of_records_ctype = _visatype.ViInt64(number_of_records)  # case S150
        number_of_samples_ctype = _visatype.ViInt64(number_of_samples)  # case S150
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        data_ctype = _visatype.ni_complex_number_f64()  # case S220
        wfm_info_ctype = _visatype.niRFSA_wfmInfo()  # case S220
        error_code = self._library.niRFSA_FetchIqMultiRecordComplexF64(vi_ctype, channel_list_ctype, starting_record_ctype, number_of_records_ctype, number_of_samples_ctype, timeout_ctype, None if data_ctype is None else (ctypes.pointer(data_ctype)), None if wfm_info_ctype is None else (ctypes.pointer(wfm_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return ni_complex_number_f64(data_ctype.value), niRFSA_wfmInfo(wfm_info_ctype.value)

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSA_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_int64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niRFSA_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSA_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def get_attribute_vi_session(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niRFSA_GetAttributeViSession(vi_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buf_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        error_code = self._library.niRFSA_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buf_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buf_size_ctype.value)()  # case C060
        error_code = self._library.niRFSA_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(self._encoding)

    def get_cal_user_defined_info(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        info_ctype = (_visatype.ViChar * 22)()  # case C070
        error_code = self._library.niRFSA_GetCalUserDefinedInfo(vi_ctype, info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return info_array

    def get_cal_user_defined_info_max_size(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        info_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetCalUserDefinedInfoMaxSize(vi_ctype, None if info_size_ctype is None else (ctypes.pointer(info_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(info_size_ctype.value)

    def get_deembedding_sparameters(self):
        import numpy as np
        number_of_ports = self.get_deembedding_table_number_of_ports()
        sparameters_array_size = number_of_ports ** 2
        sparameters = np.full((number_of_ports, number_of_ports), 0 + 0j, dtype=np.complex128)
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sparameters_ctype = _get_ctypes_pointer_for_buffer(value=sparameters, library_type=_complextype.NIComplexNumber)  # case B510
        sparameters_array_size_ctype = _visatype.ViInt32(sparameters_array_size)  # case S150
        number_of_sparameters_ctype = _visatype.ViInt32()  # case S220
        number_of_ports_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetDeembeddingSparameters(vi_ctype, sparameters_ctype, sparameters_array_size_ctype, None if number_of_sparameters_ctype is None else (ctypes.pointer(number_of_sparameters_ctype)), None if number_of_ports_ctype is None else (ctypes.pointer(number_of_ports_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        sparameters = sparameters.reshape((int(number_of_ports_ctype.value), int(number_of_ports_ctype.value)))
        return sparameters

    def get_device_response(self, channel_list, response_type, buffer_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        response_type_ctype = _visatype.ViInt32(response_type)  # case S150
        buffer_size_ctype = _visatype.ViInt32(buffer_size)  # case S210
        frequencies_size = buffer_size  # case B600
        frequencies_array = array.array("d", [0]) * frequencies_size  # case B600
        frequencies_ctype = _get_ctypes_pointer_for_buffer(value=frequencies_array, library_type=_visatype.ViReal64)  # case B600
        magnitude_response_size = buffer_size  # case B600
        magnitude_response_array = array.array("d", [0]) * magnitude_response_size  # case B600
        magnitude_response_ctype = _get_ctypes_pointer_for_buffer(value=magnitude_response_array, library_type=_visatype.ViReal64)  # case B600
        phase_response_size = buffer_size  # case B600
        phase_response_array = array.array("d", [0]) * phase_response_size  # case B600
        phase_response_ctype = _get_ctypes_pointer_for_buffer(value=phase_response_array, library_type=_visatype.ViReal64)  # case B600
        number_of_frequencies_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetDeviceResponse(vi_ctype, channel_list_ctype, response_type_ctype, buffer_size_ctype, frequencies_ctype, magnitude_response_ctype, phase_response_ctype, None if number_of_frequencies_ctype is None else (ctypes.pointer(number_of_frequencies_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return frequencies_array, magnitude_response_array, phase_response_array, int(number_of_frequencies_ctype.value)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        error_code = self._library.niRFSA_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSA_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    def get_ext_cal_last_date_and_time(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetExtCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_ext_cal_last_temp(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSA_GetExtCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetExtCalRecommendedInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(months_ctype.value)

    def get_fetch_backlog(self, channel_list, record_number):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        record_number_ctype = _visatype.ViInt64(record_number)  # case S150
        backlog_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niRFSA_GetFetchBacklog(vi_ctype, channel_list_ctype, record_number_ctype, None if backlog_ctype is None else (ctypes.pointer(backlog_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(backlog_ctype.value)

    def get_frequency_response(self, channel_list, buffer_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(buffer_size)  # case S210
        frequencies_size = buffer_size  # case B600
        frequencies_array = array.array("d", [0]) * frequencies_size  # case B600
        frequencies_ctype = _get_ctypes_pointer_for_buffer(value=frequencies_array, library_type=_visatype.ViReal64)  # case B600
        magnitude_response_size = buffer_size  # case B600
        magnitude_response_array = array.array("d", [0]) * magnitude_response_size  # case B600
        magnitude_response_ctype = _get_ctypes_pointer_for_buffer(value=magnitude_response_array, library_type=_visatype.ViReal64)  # case B600
        phase_response_size = buffer_size  # case B600
        phase_response_array = array.array("d", [0]) * phase_response_size  # case B600
        phase_response_ctype = _get_ctypes_pointer_for_buffer(value=phase_response_array, library_type=_visatype.ViReal64)  # case B600
        number_of_frequencies_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetFrequencyResponse(vi_ctype, channel_list_ctype, buffer_size_ctype, frequencies_ctype, magnitude_response_ctype, phase_response_ctype, None if number_of_frequencies_ctype is None else (ctypes.pointer(number_of_frequencies_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return frequencies_array, magnitude_response_array, phase_response_array, int(number_of_frequencies_ctype.value)

    def get_gain_reference_cal_baseline(self, buffer_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        buffer_size_ctype = _visatype.ViInt32(buffer_size)  # case S210
        gain_reference_cal_constants_size = buffer_size  # case B600
        gain_reference_cal_constants_array = array.array("d", [0]) * gain_reference_cal_constants_size  # case B600
        gain_reference_cal_constants_ctype = _get_ctypes_pointer_for_buffer(value=gain_reference_cal_constants_array, library_type=_visatype.ViReal64)  # case B600
        number_of_gain_reference_cal_constants_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetGainReferenceCalBaseline(vi_ctype, buffer_size_ctype, gain_reference_cal_constants_ctype, None if number_of_gain_reference_cal_constants_ctype is None else (ctypes.pointer(number_of_gain_reference_cal_constants_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return gain_reference_cal_constants_array, int(number_of_gain_reference_cal_constants_ctype.value)

    def get_normalization_coefficients(self, channel_list):
        # First call with arraySize=0 to get number of coefficient sets
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        array_size_ctype = _visatype.ViInt32(0)  # case S150
        coefficient_info_ctype = None  # case B580
        number_of_coefficient_sets_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetNormalizationCoefficients(vi_ctype, channel_list_ctype, array_size_ctype, coefficient_info_ctype, None if number_of_coefficient_sets_ctype is None else (ctypes.pointer(number_of_coefficient_sets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        # Second call to get actual data
        array_size = number_of_coefficient_sets_ctype.value
        array_size_ctype = _visatype.ViInt32(array_size)  # case S150
        coefficient_info_ctype = (_complextype.niRFSA_coefficientInfo * array_size)()  # case B590
        error_code = self._library.niRFSA_GetNormalizationCoefficients(vi_ctype, channel_list_ctype, array_size_ctype, coefficient_info_ctype, None if number_of_coefficient_sets_ctype is None else (ctypes.pointer(number_of_coefficient_sets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [{'offset': c.offset, 'gain': c.gain} for c in coefficient_info_ctype]

    def get_number_of_spectral_lines(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        number_of_spectral_lines_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetNumberOfSpectralLines(vi_ctype, channel_list_ctype, None if number_of_spectral_lines_ctype is None else (ctypes.pointer(number_of_spectral_lines_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(number_of_spectral_lines_ctype.value)

    def get_relay_name(self, channel_list, index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        index_ctype = _visatype.ViInt32(index)  # case S150
        name_ctype = None  # case C050
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_code = self._library.niRFSA_GetRelayName(vi_ctype, channel_list_ctype, index_ctype, name_ctype, buffer_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSA_GetRelayName(vi_ctype, channel_list_ctype, index_ctype, name_ctype, buffer_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_array

    def get_relay_operations_count(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        operations_count_ctype = None  # case B580
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_code = self._library.niRFSA_GetRelayOperationsCount(vi_ctype, channel_list_ctype, operations_count_ctype, buffer_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        operations_count_size = buffer_size_ctype.value  # case B590
        operations_count_array = array.array("l", [0]) * operations_count_size  # case B590
        operations_count_ctype = _get_ctypes_pointer_for_buffer(value=operations_count_array, library_type=_visatype.ViInt32)  # case B590
        error_code = self._library.niRFSA_GetRelayOperationsCount(vi_ctype, channel_list_ctype, operations_count_ctype, buffer_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return operations_count_array

    def get_scaling_coefficients(self, channel_list):
        # First call with arraySize=0 to get number of coefficient sets
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        array_size_ctype = _visatype.ViInt32(0)  # case S150
        coefficient_info_ctype = None  # case B580
        number_of_coefficient_sets_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetScalingCoefficients(vi_ctype, channel_list_ctype, array_size_ctype, coefficient_info_ctype, None if number_of_coefficient_sets_ctype is None else (ctypes.pointer(number_of_coefficient_sets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        # Second call to get actual data
        array_size = number_of_coefficient_sets_ctype.value
        array_size_ctype = _visatype.ViInt32(array_size)  # case S150
        coefficient_info_ctype = (_complextype.niRFSA_coefficientInfo * array_size)()  # case B590
        error_code = self._library.niRFSA_GetScalingCoefficients(vi_ctype, channel_list_ctype, array_size_ctype, coefficient_info_ctype, None if number_of_coefficient_sets_ctype is None else (ctypes.pointer(number_of_coefficient_sets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [{'offset': c.offset, 'gain': c.gain} for c in coefficient_info_ctype]

    def get_self_cal_last_date_and_time(self, self_calibration_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_calibration_step_ctype = _visatype.ViInt64(self_calibration_step)  # case S150
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetSelfCalLastDateAndTime(vi_ctype, self_calibration_step_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_self_cal_last_temp(self, self_calibration_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_calibration_step_ctype = _visatype.ViInt64(self_calibration_step)  # case S150
        temp_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSA_GetSelfCalLastTemp(vi_ctype, self_calibration_step_ctype, None if temp_ctype is None else (ctypes.pointer(temp_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temp_ctype.value)

    def get_spectral_info_for_smt(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        spectrum_info_ctype = _visatype.SmtSpectrumInfo()  # case S220
        error_code = self._library.niRFSA_GetSpectralInfoForSmt(vi_ctype, None if spectrum_info_ctype is None else (ctypes.pointer(spectrum_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return SmtSpectrumInfo(spectrum_info_ctype.value)

    def get_stream_endpoint_handle(self, stream_endpoint):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        stream_endpoint_ctype = ctypes.create_string_buffer(stream_endpoint.encode(self._encoding))  # case C020
        writer_handle_ctype = _visatype.ViUInt32()  # case S220
        error_code = self._library.niRFSA_GetStreamEndpointHandle(vi_ctype, stream_endpoint_ctype, None if writer_handle_ctype is None else (ctypes.pointer(writer_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(writer_handle_ctype.value)

    def get_terminal_name(self, signal, signal_identifier):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        signal_ctype = _visatype.ViInt32(signal)  # case S150
        signal_identifier_ctype = ctypes.create_string_buffer(signal_identifier.encode(self._encoding))  # case C020
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        terminal_name_ctype = None  # case C050
        error_code = self._library.niRFSA_GetTerminalName(vi_ctype, signal_ctype, signal_identifier_ctype, buffer_size_ctype, terminal_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        terminal_name_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSA_GetTerminalName(vi_ctype, signal_ctype, signal_identifier_ctype, buffer_size_ctype, terminal_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return terminal_name_array

    def get_user_data(self, identifier, buffer_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        identifier_ctype = ctypes.create_string_buffer(identifier.encode(self._encoding))  # case C020
        buffer_size_ctype = _visatype.ViInt32(buffer_size)  # case S210
        data_size = buffer_size  # case B600
        data_array = array.array("b", [0]) * data_size  # case B600
        data_ctype = _get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViInt8)  # case B600
        actual_data_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetUserData(vi_ctype, identifier_ctype, buffer_size_ctype, data_ctype, None if actual_data_size_ctype is None else (ctypes.pointer(actual_data_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return data_array, int(actual_data_size_ctype.value)

    def init(self, resource_name, id_query, reset):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_ctype = _visatype.ViBoolean(reset)  # case S150
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niRFSA_Init(resource_name_ctype, id_query_ctype, reset_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def init_ext_cal(self, resource_name, password, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        password_ctype = ctypes.create_string_buffer(password.encode(self._encoding))  # case C020
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niRFSA_InitExtCal(resource_name_ctype, password_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def init_with_options(self, resource_name, id_query, reset, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_ctype = _visatype.ViBoolean(reset)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niRFSA_InitWithOptions(resource_name_ctype, id_query_ctype, reset_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def initialize_calibration_step(self, calibration_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        calibration_step_ctype = _visatype.ViInt32(calibration_step)  # case S150
        error_code = self._library.niRFSA_InitializeCalibrationStep(vi_ctype, calibration_step_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def initialize_external_alignment(self, resource_name, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niRFSA_InitializeExternalAlignment(resource_name_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def initialize_external_alignment_step(self, external_alignment_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        external_alignment_step_ctype = _visatype.ViInt64(external_alignment_step)  # case S150
        error_code = self._library.niRFSA_InitializeExternalAlignmentStep(vi_ctype, external_alignment_step_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def initiate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def invalidate_all_attributes(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_InvalidateAllAttributes(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_self_cal_valid(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_cal_valid_ctype = _visatype.ViBoolean()  # case S220
        valid_steps_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niRFSA_IsSelfCalValid(vi_ctype, None if self_cal_valid_ctype is None else (ctypes.pointer(self_cal_valid_ctype)), None if valid_steps_ctype is None else (ctypes.pointer(valid_steps_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_valid_ctype.value), int(valid_steps_ctype.value)

    def load_configurations_from_file(self, channel_name, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_LoadConfigurationsFromFile(vi_ctype, channel_name_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock_session(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSA_LockSession(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def perform_thermal_correction(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_PerformThermalCorrection(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read_iq_single_record_complex_f64(self, channel_list, timeout, data_array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        data_ctype = _visatype.ni_complex_number_f64()  # case S220
        data_array_size_ctype = _visatype.ViInt64(data_array_size)  # case S150
        wfm_info_ctype = _visatype.niRFSA_wfmInfo()  # case S220
        error_code = self._library.niRFSA_ReadIqSingleRecordComplexF64(vi_ctype, channel_list_ctype, timeout_ctype, None if data_ctype is None else (ctypes.pointer(data_ctype)), data_array_size_ctype, None if wfm_info_ctype is None else (ctypes.pointer(wfm_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return ni_complex_number_f64(data_ctype.value), niRFSA_wfmInfo(wfm_info_ctype.value)

    def read_power_spectrum_f32(self, channel_list, timeout, data_array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        power_spectrum_data_size = data_array_size  # case B600
        power_spectrum_data_array = array.array("f", [0]) * power_spectrum_data_size  # case B600
        power_spectrum_data_ctype = _get_ctypes_pointer_for_buffer(value=power_spectrum_data_array, library_type=_visatype.ViReal32)  # case B600
        data_array_size_ctype = _visatype.ViInt32(data_array_size)  # case S210
        spectrum_info_ctype = _visatype.niRFSA_spectrumInfo()  # case S220
        error_code = self._library.niRFSA_ReadPowerSpectrumF32(vi_ctype, channel_list_ctype, timeout_ctype, power_spectrum_data_ctype, data_array_size_ctype, None if spectrum_info_ctype is None else (ctypes.pointer(spectrum_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return power_spectrum_data_array, niRFSA_spectrumInfo(spectrum_info_ctype.value)

    def read_power_spectrum_f64(self, channel_list, timeout, data_array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        power_spectrum_data_size = data_array_size  # case B600
        power_spectrum_data_array = array.array("d", [0]) * power_spectrum_data_size  # case B600
        power_spectrum_data_ctype = _get_ctypes_pointer_for_buffer(value=power_spectrum_data_array, library_type=_visatype.ViReal64)  # case B600
        data_array_size_ctype = _visatype.ViInt32(data_array_size)  # case S210
        spectrum_info_ctype = _visatype.niRFSA_spectrumInfo()  # case S220
        error_code = self._library.niRFSA_ReadPowerSpectrumF64(vi_ctype, channel_list_ctype, timeout_ctype, power_spectrum_data_ctype, data_array_size_ctype, None if spectrum_info_ctype is None else (ctypes.pointer(spectrum_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return power_spectrum_data_array, niRFSA_spectrumInfo(spectrum_info_ctype.value)

    def reset(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_Reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_attribute(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        error_code = self._library.niRFSA_ResetAttribute(vi_ctype, channel_name_ctype, attribute_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_device(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_options(self, steps_to_omit):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        steps_to_omit_ctype = _visatype.ViUInt64(steps_to_omit)  # case S150
        error_code = self._library.niRFSA_ResetWithOptions(vi_ctype, steps_to_omit_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def revision_query(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        driver_rev_ctype = (_visatype.ViChar * 256)()  # case C070
        instr_rev_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niRFSA_RevisionQuery(vi_ctype, driver_rev_ctype, instr_rev_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return driver_rev_array, instr_rev_array

    def save_configurations_to_file(self, channel_name, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_SaveConfigurationsToFile(vi_ctype, channel_name_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_SelfCal(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_calibrate(self, steps_to_omit):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        steps_to_omit_ctype = _visatype.ViInt64(steps_to_omit)  # case S150
        error_code = self._library.niRFSA_SelfCalibrate(vi_ctype, steps_to_omit_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_calibrate_range(self, steps_to_omit, min_frequency, max_frequency, min_reference_level, max_reference_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        steps_to_omit_ctype = _visatype.ViInt64(steps_to_omit)  # case S150
        min_frequency_ctype = _visatype.ViReal64(min_frequency)  # case S150
        max_frequency_ctype = _visatype.ViReal64(max_frequency)  # case S150
        min_reference_level_ctype = _visatype.ViReal64(min_reference_level)  # case S150
        max_reference_level_ctype = _visatype.ViReal64(max_reference_level)  # case S150
        error_code = self._library.niRFSA_SelfCalibrateRange(vi_ctype, steps_to_omit_ctype, min_frequency_ctype, max_frequency_ctype, min_reference_level_ctype, max_reference_level_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        test_result_ctype = _visatype.ViInt16()  # case S220
        test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niRFSA_SelfTest(vi_ctype, None if test_result_ctype is None else (ctypes.pointer(test_result_ctype)), test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(test_result_ctype.value), test_message_array

    def send_software_edge_trigger(self, trigger, trigger_identifier):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger)  # case S150
        trigger_identifier_ctype = ctypes.create_string_buffer(trigger_identifier.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_identifier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_name, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niRFSA_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library.niRFSA_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int64(self, channel_name, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt64(value)  # case S150
        error_code = self._library.niRFSA_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        error_code = self._library.niRFSA_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_session(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_SetAttributeViSession(vi_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_cal_user_defined_info(self, info):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        info_ctype = ctypes.create_string_buffer(info.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_SetCalUserDefinedInfo(vi_ctype, info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_user_data(self, identifier, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        identifier_ctype = ctypes.create_string_buffer(identifier.encode(self._encoding))  # case C020
        buffer_size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_array = _convert_to_array(value=data, array_type="b")  # case B550
        data_ctype = _get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niRFSA_SetUserData(vi_ctype, identifier_ctype, buffer_size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock_session(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSA_UnlockSession(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)
