# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import nirfsa_pb2 as grpc_types
from . import nirfsa_pb2_grpc as nirfsa_grpc
from . import session_pb2 as session_grpc_types


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nirfsa_grpc.NiRFSAStub(grpc_options.grpc_channel)
        self.set_session_handle()

    def set_session_handle(self, value=session_grpc_types.Session()):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def _invoke(self, func, request, metadata=None):
        try:
            response = func(request, metadata=metadata)
            error_code = response.status
            error_message = ''
        except grpc.RpcError as rpc_error:
            error_code = None
            error_message = rpc_error.details()
            for entry in rpc_error.trailing_metadata() or []:
                if entry.key == 'ni-error':
                    value = entry.value if isinstance(entry.value, str) else entry.value.decode('utf-8')
                    try:
                        error_code = int(value)
                    except ValueError:
                        error_message += f'\nError status: {value}'

            grpc_error = rpc_error.code()
            if grpc_error == grpc.StatusCode.NOT_FOUND:
                raise errors.DriverTooOldError() from None
            elif grpc_error == grpc.StatusCode.INVALID_ARGUMENT:
                raise ValueError(error_message) from None
            elif grpc_error == grpc.StatusCode.UNAVAILABLE:
                error_message = 'Failed to connect to server'
            elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
                error_message = (
                    'This operation is not supported by the NI gRPC Device Server being used. Upgrade NI gRPC Device Server.'
                )

            if error_code is None:
                raise errors.RpcError(grpc_error, error_message) from None

        if error_code < 0:
            raise errors.DriverError(error_code, error_message)
        elif error_code > 0:
            if not error_message:
                try:
                    error_message = self.error_message(error_code)
                except errors.Error:
                    error_message = 'Failed to retrieve error description.'
            warnings.warn(errors.DriverWarning(error_code, error_message))
        return response

    def abort(self):  # noqa: N802
        self._invoke(
            self._client.Abort,
            grpc_types.AbortRequest(vi=self._vi),
        )

    def cal_adjust_cal_tone_power(self, channel_list, measurement):  # noqa: N802
        self._invoke(
            self._client.CalAdjustCalTonePower,
            grpc_types.CalAdjustCalTonePowerRequest(vi=self._vi, channel_list=channel_list, measurement=measurement),
        )

    def cal_adjust_device_gain(self, channel_list, frequency, gain):  # noqa: N802
        self._invoke(
            self._client.CalAdjustDeviceGain,
            grpc_types.CalAdjustDeviceGainRequest(vi=self._vi, channel_list=channel_list, frequency=frequency, gain=gain),
        )

    def cal_adjust_downconverter_gain(self, channel_list, frequency, gain):  # noqa: N802
        self._invoke(
            self._client.CalAdjustDownconverterGain,
            grpc_types.CalAdjustDownconverterGainRequest(vi=self._vi, channel_list=channel_list, frequency=frequency, gain=gain),
        )

    def cal_adjust_if_attenuation_calibration(self, channel_list, if_filter, number_of_attenuators, measurement):  # noqa: N802
        response = self._invoke(
            self._client.CalAdjustIfAttenuationCalibration,
            grpc_types.CalAdjustIfAttenuationCalibrationRequest(vi=self._vi, channel_list=channel_list, if_filter=if_filter, number_of_attenuators=number_of_attenuators, measurement=measurement),
        )
        return response.attenuator_settings

    def cal_adjust_if_response_calibration(self, channel_list, if_filter, rf_frequency, band_width, number_of_measurements):  # noqa: N802
        response = self._invoke(
            self._client.CalAdjustIfResponseCalibration,
            grpc_types.CalAdjustIfResponseCalibrationRequest(vi=self._vi, channel_list=channel_list, if_filter=if_filter, rf_frequency=rf_frequency, band_width=band_width, number_of_measurements=number_of_measurements),
        )
        return response.measurements

    def cal_adjust_lo_export_calibration(self, channel_list, lo_number, number_of_frequency_points):  # noqa: N802
        response = self._invoke(
            self._client.CalAdjustLoExportCalibration,
            grpc_types.CalAdjustLoExportCalibrationRequest(vi=self._vi, channel_list=channel_list, lo_number=lo_number, number_of_frequency_points=number_of_frequency_points),
        )
        return response.frequency_points, response.lo_attenuation

    def cal_adjust_ref_level_calibration(self, channel_list, reference_level_data_type, rf_band, attenuator_table_number, frequency, measurement):  # noqa: N802
        self._invoke(
            self._client.CalAdjustRefLevelCalibration,
            grpc_types.CalAdjustRefLevelCalibrationRequest(vi=self._vi, channel_list=channel_list, reference_level_data_type=reference_level_data_type, rf_band=rf_band, attenuator_table_number=attenuator_table_number, frequency=frequency, measurement=measurement),
        )

    def cal_set_temperature(self, channel_list, temperature):  # noqa: N802
        self._invoke(
            self._client.CalSetTemperature,
            grpc_types.CalSetTemperatureRequest(vi=self._vi, channel_list=channel_list, temperature=temperature),
        )

    def change_ext_cal_password(self, old_password, new_password):  # noqa: N802
        self._invoke(
            self._client.ChangeExtCalPassword,
            grpc_types.ChangeExtCalPasswordRequest(vi=self._vi, old_password=old_password, new_password=new_password),
        )

    def check_acquisition_status(self):  # noqa: N802
        response = self._invoke(
            self._client.CheckAcquisitionStatus,
            grpc_types.CheckAcquisitionStatusRequest(vi=self._vi),
        )
        return response.is_done

    def clear_error(self):  # noqa: N802
        self._invoke(
            self._client.ClearError,
            grpc_types.ClearErrorRequest(vi=self._vi),
        )

    def clear_self_calibrate_range(self):  # noqa: N802
        self._invoke(
            self._client.ClearSelfCalibrateRange,
            grpc_types.ClearSelfCalibrateRangeRequest(vi=self._vi),
        )

    def close(self):  # noqa: N802
        self._invoke(
            self._client.Close,
            grpc_types.CloseRequest(vi=self._vi),
        )

    def close_calibration_step(self):  # noqa: N802
        self._invoke(
            self._client.CloseCalibrationStep,
            grpc_types.CloseCalibrationStepRequest(vi=self._vi),
        )

    def close_ext_cal(self, action):  # noqa: N802
        self._invoke(
            self._client.CloseExtCal,
            grpc_types.CloseExtCalRequest(vi=self._vi, action=action),
        )

    def close_external_alignment(self, action):  # noqa: N802
        self._invoke(
            self._client.CloseExternalAlignment,
            grpc_types.CloseExternalAlignmentRequest(vi=self._vi, action=action),
        )

    def close_external_alignment_step(self):  # noqa: N802
        self._invoke(
            self._client.CloseExternalAlignmentStep,
            grpc_types.CloseExternalAlignmentStepRequest(vi=self._vi),
        )

    def commit(self):  # noqa: N802
        self._invoke(
            self._client.Commit,
            grpc_types.CommitRequest(vi=self._vi),
        )

    def configure_acquisition_type(self, acquisition_type):  # noqa: N802
        self._invoke(
            self._client.ConfigureAcquisitionType,
            grpc_types.ConfigureAcquisitionTypeRequest(vi=self._vi, acquisition_type=acquisition_type),
        )

    def configure_deembedding_table_interpolation_linear(self, port, table_name, format):  # noqa: N802
        self._invoke(
            self._client.ConfigureDeembeddingTableInterpolationLinear,
            grpc_types.ConfigureDeembeddingTableInterpolationLinearRequest(vi=self._vi, port=port, table_name=table_name, format=format),
        )

    def configure_deembedding_table_interpolation_nearest(self, port, table_name):  # noqa: N802
        self._invoke(
            self._client.ConfigureDeembeddingTableInterpolationNearest,
            grpc_types.ConfigureDeembeddingTableInterpolationNearestRequest(vi=self._vi, port=port, table_name=table_name),
        )

    def configure_deembedding_table_interpolation_spline(self, port, table_name):  # noqa: N802
        self._invoke(
            self._client.ConfigureDeembeddingTableInterpolationSpline,
            grpc_types.ConfigureDeembeddingTableInterpolationSplineRequest(vi=self._vi, port=port, table_name=table_name),
        )

    def configure_digital_edge_advance_trigger(self, source, edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureDigitalEdgeAdvanceTrigger,
            grpc_types.ConfigureDigitalEdgeAdvanceTriggerRequest(vi=self._vi, source=source, edge=edge),
        )

    def configure_digital_edge_ref_trigger(self, source, edge, pretrigger_samples):  # noqa: N802
        self._invoke(
            self._client.ConfigureDigitalEdgeRefTrigger,
            grpc_types.ConfigureDigitalEdgeRefTriggerRequest(vi=self._vi, source=source, edge=edge, pretrigger_samples=pretrigger_samples),
        )

    def configure_digital_edge_start_trigger(self, source, edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureDigitalEdgeStartTrigger,
            grpc_types.ConfigureDigitalEdgeStartTriggerRequest(vi=self._vi, source=source, edge=edge),
        )

    def configure_iq_carrier_frequency(self, channel_list, carrier_frequency):  # noqa: N802
        self._invoke(
            self._client.ConfigureIqCarrierFrequency,
            grpc_types.ConfigureIqCarrierFrequencyRequest(vi=self._vi, channel_list=channel_list, carrier_frequency=carrier_frequency),
        )

    def configure_iq_power_edge_ref_trigger(self, source, level, slope, pretrigger_samples):  # noqa: N802
        self._invoke(
            self._client.ConfigureIqPowerEdgeRefTrigger,
            grpc_types.ConfigureIqPowerEdgeRefTriggerRequest(vi=self._vi, source=source, level=level, slope=slope, pretrigger_samples=pretrigger_samples),
        )

    def configure_iq_rate(self, channel_list, iq_rate):  # noqa: N802
        self._invoke(
            self._client.ConfigureIqRate,
            grpc_types.ConfigureIqRateRequest(vi=self._vi, channel_list=channel_list, iq_rate=iq_rate),
        )

    def configure_number_of_records(self, channel_list, number_of_records_is_finite, number_of_records):  # noqa: N802
        self._invoke(
            self._client.ConfigureNumberOfRecords,
            grpc_types.ConfigureNumberOfRecordsRequest(vi=self._vi, channel_list=channel_list, number_of_records_is_finite=number_of_records_is_finite, number_of_records=number_of_records),
        )

    def configure_number_of_samples(self, channel_list, number_of_samples_is_finite, samples_per_record):  # noqa: N802
        self._invoke(
            self._client.ConfigureNumberOfSamples,
            grpc_types.ConfigureNumberOfSamplesRequest(vi=self._vi, channel_list=channel_list, number_of_samples_is_finite=number_of_samples_is_finite, samples_per_record=samples_per_record),
        )

    def configure_pxi_chassis_clk10(self, pxi_clk10_source):  # noqa: N802
        self._invoke(
            self._client.ConfigurePxiChassisClk10,
            grpc_types.ConfigurePxiChassisClk10Request(vi=self._vi, pxi_clk10_source=pxi_clk10_source),
        )

    def configure_ref_clock(self, clock_source, ref_clock_rate):  # noqa: N802
        self._invoke(
            self._client.ConfigureRefClock,
            grpc_types.ConfigureRefClockRequest(vi=self._vi, clock_source=clock_source, ref_clock_rate=ref_clock_rate),
        )

    def configure_reference_level(self, channel_list, reference_level):  # noqa: N802
        self._invoke(
            self._client.ConfigureReferenceLevel,
            grpc_types.ConfigureReferenceLevelRequest(vi=self._vi, channel_list=channel_list, reference_level=reference_level),
        )

    def configure_resolution_bandwidth(self, channel_list, resolution_bandwidth):  # noqa: N802
        self._invoke(
            self._client.ConfigureResolutionBandwidth,
            grpc_types.ConfigureResolutionBandwidthRequest(vi=self._vi, channel_list=channel_list, resolution_bandwidth=resolution_bandwidth),
        )

    def configure_software_edge_advance_trigger(self):  # noqa: N802
        self._invoke(
            self._client.ConfigureSoftwareEdgeAdvanceTrigger,
            grpc_types.ConfigureSoftwareEdgeAdvanceTriggerRequest(vi=self._vi),
        )

    def configure_software_edge_ref_trigger(self, pretrigger_samples):  # noqa: N802
        self._invoke(
            self._client.ConfigureSoftwareEdgeRefTrigger,
            grpc_types.ConfigureSoftwareEdgeRefTriggerRequest(vi=self._vi, pretrigger_samples=pretrigger_samples),
        )

    def configure_software_edge_start_trigger(self):  # noqa: N802
        self._invoke(
            self._client.ConfigureSoftwareEdgeStartTrigger,
            grpc_types.ConfigureSoftwareEdgeStartTriggerRequest(vi=self._vi),
        )

    def configure_spectrum_frequency_center_span(self, channel_list, center_frequency, span):  # noqa: N802
        self._invoke(
            self._client.ConfigureSpectrumFrequencyCenterSpan,
            grpc_types.ConfigureSpectrumFrequencyCenterSpanRequest(vi=self._vi, channel_list=channel_list, center_frequency=center_frequency, span=span),
        )

    def configure_spectrum_frequency_start_stop(self, channel_list, start_frequency, stop_frequency):  # noqa: N802
        self._invoke(
            self._client.ConfigureSpectrumFrequencyStartStop,
            grpc_types.ConfigureSpectrumFrequencyStartStopRequest(vi=self._vi, channel_list=channel_list, start_frequency=start_frequency, stop_frequency=stop_frequency),
        )

    def create_configuration_list(self, list_name, number_of_list_attributes, set_as_active_list):  # noqa: N802
        response = self._invoke(
            self._client.CreateConfigurationList,
            grpc_types.CreateConfigurationListRequest(vi=self._vi, list_name=list_name, number_of_list_attributes=number_of_list_attributes, set_as_active_list=set_as_active_list),
        )
        return response.list_attribute_i_ds

    def create_configuration_list_step(self, set_as_active_step):  # noqa: N802
        self._invoke(
            self._client.CreateConfigurationListStep,
            grpc_types.CreateConfigurationListStepRequest(vi=self._vi, set_as_active_step=set_as_active_step),
        )

    def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        self._invoke(
            self._client.CreateDeembeddingSparameterTableS2PFile,
            grpc_types.CreateDeembeddingSparameterTableS2PFileRequest(vi=self._vi, port=port, table_name=table_name, s2p_file_path=s2p_file_path, sparameter_orientation=sparameter_orientation),
        )

    def delete_all_deembedding_tables(self):  # noqa: N802
        self._invoke(
            self._client.DeleteAllDeembeddingTables,
            grpc_types.DeleteAllDeembeddingTablesRequest(vi=self._vi),
        )

    def delete_configuration_list(self, list_name):  # noqa: N802
        self._invoke(
            self._client.DeleteConfigurationList,
            grpc_types.DeleteConfigurationListRequest(vi=self._vi, list_name=list_name),
        )

    def delete_deembedding_table(self, port, table_name):  # noqa: N802
        self._invoke(
            self._client.DeleteDeembeddingTable,
            grpc_types.DeleteDeembeddingTableRequest(vi=self._vi, port=port, table_name=table_name),
        )

    def disable(self):  # noqa: N802
        self._invoke(
            self._client.Disable,
            grpc_types.DisableRequest(vi=self._vi),
        )

    def disable_advance_trigger(self):  # noqa: N802
        self._invoke(
            self._client.DisableAdvanceTrigger,
            grpc_types.DisableAdvanceTriggerRequest(vi=self._vi),
        )

    def disable_ref_trigger(self):  # noqa: N802
        self._invoke(
            self._client.DisableRefTrigger,
            grpc_types.DisableRefTriggerRequest(vi=self._vi),
        )

    def disable_start_trigger(self):  # noqa: N802
        self._invoke(
            self._client.DisableStartTrigger,
            grpc_types.DisableStartTriggerRequest(vi=self._vi),
        )

    def enable_session_access(self, enable):  # noqa: N802
        self._invoke(
            self._client.EnableSessionAccess,
            grpc_types.EnableSessionAccessRequest(vi=self._vi, enable=enable),
        )

    def error_message(self, status_code, error_message):  # noqa: N802
        self._invoke(
            self._client.ErrorMessage,
            grpc_types.ErrorMessageRequest(vi=self._vi, status_code=status_code, error_message=error_message),
        )

    def error_query(self):  # noqa: N802
        response = self._invoke(
            self._client.ErrorQuery,
            grpc_types.ErrorQueryRequest(vi=self._vi),
        )
        return response.error_code, response.error_message

    def export_signal(self, signal, signal_identifier, output_terminal):  # noqa: N802
        self._invoke(
            self._client.ExportSignal,
            grpc_types.ExportSignalRequest(vi=self._vi, signal=signal, signal_identifier=signal_identifier, output_terminal=output_terminal),
        )

    def ext_cal_store_baseline_for_self_calibration(self, password, self_calibration_step):  # noqa: N802
        self._invoke(
            self._client.ExtCalStoreBaselineForSelfCalibration,
            grpc_types.ExtCalStoreBaselineForSelfCalibrationRequest(vi=self._vi, password=password, self_calibration_step=self_calibration_step),
        )

    def external_alignment_adjust_preselector(self, coefficients):  # noqa: N802
        self._invoke(
            self._client.ExternalAlignmentAdjustPreselector,
            grpc_types.ExternalAlignmentAdjustPreselectorRequest(vi=self._vi, coefficients=coefficients),
        )

    def fetch_iq_multi_record_complex_f32(self, channel_list, starting_record, number_of_records, number_of_samples, timeout):  # noqa: N802
        response = self._invoke(
            self._client.FetchIqMultiRecordComplexF32,
            grpc_types.FetchIqMultiRecordComplexF32Request(vi=self._vi, channel_list=channel_list, starting_record=starting_record, number_of_records=number_of_records, number_of_samples=number_of_samples, timeout=timeout),
        )
        return ni_complex_number_f32(response.data), niRFSA_wfmInfo(response.wfm_info)

    def fetch_iq_multi_record_complex_f64(self, channel_list, starting_record, number_of_records, number_of_samples, timeout):  # noqa: N802
        response = self._invoke(
            self._client.FetchIqMultiRecordComplexF64,
            grpc_types.FetchIqMultiRecordComplexF64Request(vi=self._vi, channel_list=channel_list, starting_record=starting_record, number_of_records=number_of_records, number_of_samples=number_of_samples, timeout=timeout),
        )
        return ni_complex_number_f64(response.data), niRFSA_wfmInfo(response.wfm_info)

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_int64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt64,
            grpc_types.GetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_session(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViSession,
            grpc_types.GetAttributeViSessionRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.value

    def get_cal_user_defined_info(self):  # noqa: N802
        response = self._invoke(
            self._client.GetCalUserDefinedInfo,
            grpc_types.GetCalUserDefinedInfoRequest(vi=self._vi),
        )
        return response.info

    def get_cal_user_defined_info_max_size(self):  # noqa: N802
        response = self._invoke(
            self._client.GetCalUserDefinedInfoMaxSize,
            grpc_types.GetCalUserDefinedInfoMaxSizeRequest(vi=self._vi),
        )
        return response.info_size

    def get_deembedding_sparameters(self):
        import numpy as np
        response = self._invoke(
            self._client.GetDeembeddingSparameters,
            grpc_types.GetDeembeddingSparametersRequest(vi=self._vi),
        )
        number_of_ports = response.number_of_ports
        sparameters = np.array([c.real + 1j * c.imaginary for c in response.sparameters], dtype=np.complex128)
        sparameters = sparameters.reshape((number_of_ports, number_of_ports))
        return sparameters

    def get_device_response(self, channel_list, response_type, buffer_size):  # noqa: N802
        response = self._invoke(
            self._client.GetDeviceResponse,
            grpc_types.GetDeviceResponseRequest(vi=self._vi, channel_list=channel_list, response_type=response_type, buffer_size=buffer_size),
        )
        return response.frequencies, response.magnitude_response, response.phase_response, response.number_of_frequencies

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.error_description

    def get_ext_cal_last_date_and_time(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalLastDateAndTime,
            grpc_types.GetExtCalLastDateAndTimeRequest(vi=self._vi),
        )
        return response.year, response.month, response.day, response.hour, response.minute

    def get_ext_cal_last_temp(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalLastTemp,
            grpc_types.GetExtCalLastTempRequest(vi=self._vi),
        )
        return response.temperature

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalRecommendedInterval,
            grpc_types.GetExtCalRecommendedIntervalRequest(vi=self._vi),
        )
        return response.months

    def get_fetch_backlog(self, channel_list, record_number):  # noqa: N802
        response = self._invoke(
            self._client.GetFetchBacklog,
            grpc_types.GetFetchBacklogRequest(vi=self._vi, channel_list=channel_list, record_number=record_number),
        )
        return response.backlog

    def get_frequency_response(self, channel_list, buffer_size):  # noqa: N802
        response = self._invoke(
            self._client.GetFrequencyResponse,
            grpc_types.GetFrequencyResponseRequest(vi=self._vi, channel_list=channel_list, buffer_size=buffer_size),
        )
        return response.frequencies, response.magnitude_response, response.phase_response, response.number_of_frequencies

    def get_gain_reference_cal_baseline(self, buffer_size):  # noqa: N802
        response = self._invoke(
            self._client.GetGainReferenceCalBaseline,
            grpc_types.GetGainReferenceCalBaselineRequest(vi=self._vi, buffer_size=buffer_size),
        )
        return response.gain_reference_cal_constants, response.number_of_gain_reference_cal_constants

    def get_normalization_coefficients(self, channel_list):
        response = self._invoke(
            self._client.GetNormalizationCoefficients,
            grpc_types.GetNormalizationCoefficientsRequest(vi=self._vi, channel_list=channel_list),
        )
        return [{'offset': c.offset, 'gain': c.gain} for c in response.coefficient_info]

    def get_number_of_spectral_lines(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.GetNumberOfSpectralLines,
            grpc_types.GetNumberOfSpectralLinesRequest(vi=self._vi, channel_list=channel_list),
        )
        return response.number_of_spectral_lines

    def get_relay_name(self, channel_list, index):  # noqa: N802
        response = self._invoke(
            self._client.GetRelayName,
            grpc_types.GetRelayNameRequest(vi=self._vi, channel_list=channel_list, index=index),
        )
        return response.name

    def get_relay_operations_count(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.GetRelayOperationsCount,
            grpc_types.GetRelayOperationsCountRequest(vi=self._vi, channel_list=channel_list),
        )
        return response.operations_count

    def get_scaling_coefficients(self, channel_list):
        response = self._invoke(
            self._client.GetScalingCoefficients,
            grpc_types.GetScalingCoefficientsRequest(vi=self._vi, channel_list=channel_list),
        )
        return [{'offset': c.offset, 'gain': c.gain} for c in response.coefficient_info]

    def get_self_cal_last_date_and_time(self, self_calibration_step):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalLastDateAndTime,
            grpc_types.GetSelfCalLastDateAndTimeRequest(vi=self._vi, self_calibration_step=self_calibration_step),
        )
        return response.year, response.month, response.day, response.hour, response.minute

    def get_self_cal_last_temp(self, self_calibration_step):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalLastTemp,
            grpc_types.GetSelfCalLastTempRequest(vi=self._vi, self_calibration_step=self_calibration_step),
        )
        return response.temp

    def get_spectral_info_for_smt(self):  # noqa: N802
        response = self._invoke(
            self._client.GetSpectralInfoForSmt,
            grpc_types.GetSpectralInfoForSmtRequest(vi=self._vi),
        )
        return SmtSpectrumInfo(response.spectrum_info)

    def get_stream_endpoint_handle(self, stream_endpoint):  # noqa: N802
        response = self._invoke(
            self._client.GetStreamEndpointHandle,
            grpc_types.GetStreamEndpointHandleRequest(vi=self._vi, stream_endpoint=stream_endpoint),
        )
        return response.writer_handle

    def get_terminal_name(self, signal, signal_identifier):  # noqa: N802
        response = self._invoke(
            self._client.GetTerminalName,
            grpc_types.GetTerminalNameRequest(vi=self._vi, signal=signal, signal_identifier=signal_identifier),
        )
        return response.terminal_name

    def get_user_data(self, identifier, buffer_size):  # noqa: N802
        response = self._invoke(
            self._client.GetUserData,
            grpc_types.GetUserDataRequest(vi=self._vi, identifier=identifier, buffer_size=buffer_size),
        )
        return response.data, response.actual_data_size

    def init(self, resource_name, id_query, reset):  # noqa: N802
        response = self._invoke(
            self._client.Init,
            grpc_types.InitRequest(resource_name=resource_name, id_query=id_query, reset=reset),
        )
        return response.vi

    def init_ext_cal(self, resource_name, password, option_string):  # noqa: N802
        response = self._invoke(
            self._client.InitExtCal,
            grpc_types.InitExtCalRequest(resource_name=resource_name, password=password, option_string=option_string),
        )
        return response.vi

    def init_with_options(self, resource_name, id_query, reset, option_string):  # noqa: N802
        response = self._invoke(
            self._client.InitWithOptions,
            grpc_types.InitWithOptionsRequest(resource_name=resource_name, id_query=id_query, reset=reset, option_string=option_string),
        )
        return response.vi

    def initialize_calibration_step(self, calibration_step):  # noqa: N802
        self._invoke(
            self._client.InitializeCalibrationStep,
            grpc_types.InitializeCalibrationStepRequest(vi=self._vi, calibration_step=calibration_step),
        )

    def initialize_external_alignment(self, resource_name, option_string):  # noqa: N802
        response = self._invoke(
            self._client.InitializeExternalAlignment,
            grpc_types.InitializeExternalAlignmentRequest(resource_name=resource_name, option_string=option_string),
        )
        return response.vi

    def initialize_external_alignment_step(self, external_alignment_step):  # noqa: N802
        self._invoke(
            self._client.InitializeExternalAlignmentStep,
            grpc_types.InitializeExternalAlignmentStepRequest(vi=self._vi, external_alignment_step=external_alignment_step),
        )

    def initiate(self):  # noqa: N802
        self._invoke(
            self._client.Initiate,
            grpc_types.InitiateRequest(vi=self._vi),
        )

    def invalidate_all_attributes(self):  # noqa: N802
        self._invoke(
            self._client.InvalidateAllAttributes,
            grpc_types.InvalidateAllAttributesRequest(vi=self._vi),
        )

    def is_self_cal_valid(self):  # noqa: N802
        response = self._invoke(
            self._client.IsSelfCalValid,
            grpc_types.IsSelfCalValidRequest(vi=self._vi),
        )
        return response.self_cal_valid, response.valid_steps

    def load_configurations_from_file(self, channel_name, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadConfigurationsFromFile,
            grpc_types.LoadConfigurationsFromFileRequest(vi=self._vi, channel_name=channel_name, file_path=file_path),
        )

    def lock_session(self):  # noqa: N802
        response = self._invoke(
            self._client.LockSession,
            grpc_types.LockSessionRequest(vi=self._vi),
        )
        return response.caller_has_lock

    def perform_thermal_correction(self):  # noqa: N802
        self._invoke(
            self._client.PerformThermalCorrection,
            grpc_types.PerformThermalCorrectionRequest(vi=self._vi),
        )

    def read_iq_single_record_complex_f64(self, channel_list, timeout, data_array_size):  # noqa: N802
        response = self._invoke(
            self._client.ReadIqSingleRecordComplexF64,
            grpc_types.ReadIqSingleRecordComplexF64Request(vi=self._vi, channel_list=channel_list, timeout=timeout, data_array_size=data_array_size),
        )
        return ni_complex_number_f64(response.data), niRFSA_wfmInfo(response.wfm_info)

    def read_power_spectrum_f32(self, channel_list, timeout, data_array_size):  # noqa: N802
        response = self._invoke(
            self._client.ReadPowerSpectrumF32,
            grpc_types.ReadPowerSpectrumF32Request(vi=self._vi, channel_list=channel_list, timeout=timeout, data_array_size=data_array_size),
        )
        return response.power_spectrum_data, niRFSA_spectrumInfo(response.spectrum_info)

    def read_power_spectrum_f64(self, channel_list, timeout, data_array_size):  # noqa: N802
        response = self._invoke(
            self._client.ReadPowerSpectrumF64,
            grpc_types.ReadPowerSpectrumF64Request(vi=self._vi, channel_list=channel_list, timeout=timeout, data_array_size=data_array_size),
        )
        return response.power_spectrum_data, niRFSA_spectrumInfo(response.spectrum_info)

    def reset(self):  # noqa: N802
        self._invoke(
            self._client.Reset,
            grpc_types.ResetRequest(vi=self._vi),
        )

    def reset_attribute(self, channel_name, attribute_id):  # noqa: N802
        self._invoke(
            self._client.ResetAttribute,
            grpc_types.ResetAttributeRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )

    def reset_device(self):  # noqa: N802
        self._invoke(
            self._client.ResetDevice,
            grpc_types.ResetDeviceRequest(vi=self._vi),
        )

    def reset_with_defaults(self):  # noqa: N802
        self._invoke(
            self._client.ResetWithDefaults,
            grpc_types.ResetWithDefaultsRequest(vi=self._vi),
        )

    def reset_with_options(self, steps_to_omit):  # noqa: N802
        self._invoke(
            self._client.ResetWithOptions,
            grpc_types.ResetWithOptionsRequest(vi=self._vi, steps_to_omit=steps_to_omit),
        )

    def revision_query(self):  # noqa: N802
        response = self._invoke(
            self._client.RevisionQuery,
            grpc_types.RevisionQueryRequest(vi=self._vi),
        )
        return response.driver_rev, response.instr_rev

    def save_configurations_to_file(self, channel_name, file_path):  # noqa: N802
        self._invoke(
            self._client.SaveConfigurationsToFile,
            grpc_types.SaveConfigurationsToFileRequest(vi=self._vi, channel_name=channel_name, file_path=file_path),
        )

    def self_cal(self):  # noqa: N802
        self._invoke(
            self._client.SelfCal,
            grpc_types.SelfCalRequest(vi=self._vi),
        )

    def self_calibrate(self, steps_to_omit):  # noqa: N802
        self._invoke(
            self._client.SelfCalibrate,
            grpc_types.SelfCalibrateRequest(vi=self._vi, steps_to_omit=steps_to_omit),
        )

    def self_calibrate_range(self, steps_to_omit, min_frequency, max_frequency, min_reference_level, max_reference_level):  # noqa: N802
        self._invoke(
            self._client.SelfCalibrateRange,
            grpc_types.SelfCalibrateRangeRequest(vi=self._vi, steps_to_omit=steps_to_omit, min_frequency=min_frequency, max_frequency=max_frequency, min_reference_level=min_reference_level, max_reference_level=max_reference_level),
        )

    def self_test(self):  # noqa: N802
        response = self._invoke(
            self._client.SelfTest,
            grpc_types.SelfTestRequest(vi=self._vi),
        )
        return response.test_result, response.test_message

    def send_software_edge_trigger(self, trigger, trigger_identifier):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareEdgeTrigger,
            grpc_types.SendSoftwareEdgeTriggerRequest(vi=self._vi, trigger=trigger, trigger_identifier=trigger_identifier),
        )

    def set_attribute_vi_boolean(self, channel_name, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, value=value),
        )

    def set_attribute_vi_int32(self, channel_name, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, value_raw=value),
        )

    def set_attribute_vi_int64(self, channel_name, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt64,
            grpc_types.SetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, value_raw=value),
        )

    def set_attribute_vi_real64(self, channel_name, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, value_raw=value),
        )

    def set_attribute_vi_session(self, channel_name, attribute_id):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViSession,
            grpc_types.SetAttributeViSessionRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, value=self._vi),
        )

    def set_attribute_vi_string(self, channel_name, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, value_raw=value),
        )

    def set_cal_user_defined_info(self, info):  # noqa: N802
        self._invoke(
            self._client.SetCalUserDefinedInfo,
            grpc_types.SetCalUserDefinedInfoRequest(vi=self._vi, info=info),
        )

    def set_user_data(self, identifier, data):  # noqa: N802
        self._invoke(
            self._client.SetUserData,
            grpc_types.SetUserDataRequest(vi=self._vi, identifier=identifier, data=data),
        )

    def unlock_session(self):  # noqa: N802
        response = self._invoke(
            self._client.UnlockSession,
            grpc_types.UnlockSessionRequest(vi=self._vi),
        )
        return response.caller_has_lock
