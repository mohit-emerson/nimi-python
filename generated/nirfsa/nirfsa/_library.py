# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nirfsa.errors as errors
import threading

from nirfsa._complextype import *  # noqa: F403
from nirfsa._visatype import *  # noqa: F403,H303

import nirfsa.waveform_info as waveform_info  # noqa: F401

import nirfsa.spectrum_info_type as spectrum_info_type  # noqa: F401

import nirfsa.coefficient_info_type as coefficient_info_type  # noqa: F401


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niRFSA_Abort_cfunc = None
        self.niRFSA_CalAdjustCalTonePower_cfunc = None
        self.niRFSA_CalAdjustDeviceGain_cfunc = None
        self.niRFSA_CalAdjustDownconverterGain_cfunc = None
        self.niRFSA_CalAdjustIfAttenuationCalibration_cfunc = None
        self.niRFSA_CalAdjustIfResponseCalibration_cfunc = None
        self.niRFSA_CalAdjustLoExportCalibration_cfunc = None
        self.niRFSA_CalAdjustRefLevelCalibration_cfunc = None
        self.niRFSA_CalSetTemperature_cfunc = None
        self.niRFSA_ChangeExtCalPassword_cfunc = None
        self.niRFSA_CheckAcquisitionStatus_cfunc = None
        self.niRFSA_ClearError_cfunc = None
        self.niRFSA_ClearSelfCalibrateRange_cfunc = None
        self.niRFSA_Close_cfunc = None
        self.niRFSA_CloseCalibrationStep_cfunc = None
        self.niRFSA_CloseExtCal_cfunc = None
        self.niRFSA_CloseExternalAlignment_cfunc = None
        self.niRFSA_CloseExternalAlignmentStep_cfunc = None
        self.niRFSA_Commit_cfunc = None
        self.niRFSA_ConfigureAcquisitionType_cfunc = None
        self.niRFSA_ConfigureDeembeddingTableInterpolationLinear_cfunc = None
        self.niRFSA_ConfigureDeembeddingTableInterpolationNearest_cfunc = None
        self.niRFSA_ConfigureDeembeddingTableInterpolationSpline_cfunc = None
        self.niRFSA_ConfigureDigitalEdgeAdvanceTrigger_cfunc = None
        self.niRFSA_ConfigureDigitalEdgeRefTrigger_cfunc = None
        self.niRFSA_ConfigureDigitalEdgeStartTrigger_cfunc = None
        self.niRFSA_ConfigureIqCarrierFrequency_cfunc = None
        self.niRFSA_ConfigureIqPowerEdgeRefTrigger_cfunc = None
        self.niRFSA_ConfigureIqRate_cfunc = None
        self.niRFSA_ConfigureNumberOfRecords_cfunc = None
        self.niRFSA_ConfigureNumberOfSamples_cfunc = None
        self.niRFSA_ConfigurePxiChassisClk10_cfunc = None
        self.niRFSA_ConfigureRefClock_cfunc = None
        self.niRFSA_ConfigureReferenceLevel_cfunc = None
        self.niRFSA_ConfigureResolutionBandwidth_cfunc = None
        self.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger_cfunc = None
        self.niRFSA_ConfigureSoftwareEdgeRefTrigger_cfunc = None
        self.niRFSA_ConfigureSoftwareEdgeStartTrigger_cfunc = None
        self.niRFSA_ConfigureSpectrumFrequencyCenterSpan_cfunc = None
        self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc = None
        self.niRFSA_CreateConfigurationList_cfunc = None
        self.niRFSA_CreateConfigurationListStep_cfunc = None
        self.niRFSA_CreateDeembeddingSparameterTableArray_cfunc = None
        self.niRFSA_CreateDeembeddingSparameterTableS2PFile_cfunc = None
        self.niRFSA_DeleteAllDeembeddingTables_cfunc = None
        self.niRFSA_DeleteConfigurationList_cfunc = None
        self.niRFSA_DeleteDeembeddingTable_cfunc = None
        self.niRFSA_Disable_cfunc = None
        self.niRFSA_DisableAdvanceTrigger_cfunc = None
        self.niRFSA_DisableRefTrigger_cfunc = None
        self.niRFSA_DisableStartTrigger_cfunc = None
        self.niRFSA_EnableSessionAccess_cfunc = None
        self.niRFSA_ErrorMessage_cfunc = None
        self.niRFSA_ErrorQuery_cfunc = None
        self.niRFSA_ExportSignal_cfunc = None
        self.niRFSA_ExtCalStoreBaselineForSelfCalibration_cfunc = None
        self.niRFSA_ExternalAlignmentAdjustPreselector_cfunc = None
        self.niRFSA_FetchIqMultiRecordComplexF32_cfunc = None
        self.niRFSA_FetchIqMultiRecordComplexF64_cfunc = None
        self.niRFSA_GetAttributeViBoolean_cfunc = None
        self.niRFSA_GetAttributeViInt32_cfunc = None
        self.niRFSA_GetAttributeViInt64_cfunc = None
        self.niRFSA_GetAttributeViReal64_cfunc = None
        self.niRFSA_GetAttributeViSession_cfunc = None
        self.niRFSA_GetAttributeViString_cfunc = None
        self.niRFSA_GetCalUserDefinedInfo_cfunc = None
        self.niRFSA_GetCalUserDefinedInfoMaxSize_cfunc = None
        self.niRFSA_GetDeembeddingSparameters_cfunc = None
        self.niRFSA_GetDeviceResponse_cfunc = None
        self.niRFSA_GetError_cfunc = None
        self.niRFSA_GetExtCalLastDateAndTime_cfunc = None
        self.niRFSA_GetExtCalLastTemp_cfunc = None
        self.niRFSA_GetExtCalRecommendedInterval_cfunc = None
        self.niRFSA_GetFetchBacklog_cfunc = None
        self.niRFSA_GetFrequencyResponse_cfunc = None
        self.niRFSA_GetGainReferenceCalBaseline_cfunc = None
        self.niRFSA_GetNormalizationCoefficients_cfunc = None
        self.niRFSA_GetNumberOfSpectralLines_cfunc = None
        self.niRFSA_GetRelayName_cfunc = None
        self.niRFSA_GetRelayOperationsCount_cfunc = None
        self.niRFSA_GetScalingCoefficients_cfunc = None
        self.niRFSA_GetSelfCalLastDateAndTime_cfunc = None
        self.niRFSA_GetSelfCalLastTemp_cfunc = None
        self.niRFSA_GetSpectralInfoForSmt_cfunc = None
        self.niRFSA_GetStreamEndpointHandle_cfunc = None
        self.niRFSA_GetTerminalName_cfunc = None
        self.niRFSA_GetUserData_cfunc = None
        self.niRFSA_Init_cfunc = None
        self.niRFSA_InitExtCal_cfunc = None
        self.niRFSA_InitWithOptions_cfunc = None
        self.niRFSA_InitializeCalibrationStep_cfunc = None
        self.niRFSA_InitializeExternalAlignment_cfunc = None
        self.niRFSA_InitializeExternalAlignmentStep_cfunc = None
        self.niRFSA_Initiate_cfunc = None
        self.niRFSA_InvalidateAllAttributes_cfunc = None
        self.niRFSA_IsSelfCalValid_cfunc = None
        self.niRFSA_LoadConfigurationsFromFile_cfunc = None
        self.niRFSA_LockSession_cfunc = None
        self.niRFSA_PerformThermalCorrection_cfunc = None
        self.niRFSA_ReadIqSingleRecordComplexF64_cfunc = None
        self.niRFSA_ReadPowerSpectrumF32_cfunc = None
        self.niRFSA_ReadPowerSpectrumF64_cfunc = None
        self.niRFSA_Reset_cfunc = None
        self.niRFSA_ResetAttribute_cfunc = None
        self.niRFSA_ResetDevice_cfunc = None
        self.niRFSA_ResetWithDefaults_cfunc = None
        self.niRFSA_ResetWithOptions_cfunc = None
        self.niRFSA_RevisionQuery_cfunc = None
        self.niRFSA_SaveConfigurationsToFile_cfunc = None
        self.niRFSA_SelfCal_cfunc = None
        self.niRFSA_SelfCalibrate_cfunc = None
        self.niRFSA_SelfCalibrateRange_cfunc = None
        self.niRFSA_SelfTest_cfunc = None
        self.niRFSA_SendSoftwareEdgeTrigger_cfunc = None
        self.niRFSA_SetAttributeViBoolean_cfunc = None
        self.niRFSA_SetAttributeViInt32_cfunc = None
        self.niRFSA_SetAttributeViInt64_cfunc = None
        self.niRFSA_SetAttributeViReal64_cfunc = None
        self.niRFSA_SetAttributeViSession_cfunc = None
        self.niRFSA_SetAttributeViString_cfunc = None
        self.niRFSA_SetCalUserDefinedInfo_cfunc = None
        self.niRFSA_SetUserData_cfunc = None
        self.niRFSA_UnlockSession_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niRFSA_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_Abort_cfunc is None:
                self.niRFSA_Abort_cfunc = self._get_library_function('niRFSA_Abort')
                self.niRFSA_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_Abort_cfunc(vi)

    def niRFSA_CalAdjustCalTonePower(self, vi, channel_list, measurement):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CalAdjustCalTonePower_cfunc is None:
                self.niRFSA_CalAdjustCalTonePower_cfunc = self._get_library_function('niRFSA_CalAdjustCalTonePower')
                self.niRFSA_CalAdjustCalTonePower_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_CalAdjustCalTonePower_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CalAdjustCalTonePower_cfunc(vi, channel_list, measurement)

    def niRFSA_CalAdjustDeviceGain(self, vi, channel_list, frequency, gain):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CalAdjustDeviceGain_cfunc is None:
                self.niRFSA_CalAdjustDeviceGain_cfunc = self._get_library_function('niRFSA_CalAdjustDeviceGain')
                self.niRFSA_CalAdjustDeviceGain_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niRFSA_CalAdjustDeviceGain_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CalAdjustDeviceGain_cfunc(vi, channel_list, frequency, gain)

    def niRFSA_CalAdjustDownconverterGain(self, vi, channel_list, frequency, gain):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CalAdjustDownconverterGain_cfunc is None:
                self.niRFSA_CalAdjustDownconverterGain_cfunc = self._get_library_function('niRFSA_CalAdjustDownconverterGain')
                self.niRFSA_CalAdjustDownconverterGain_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niRFSA_CalAdjustDownconverterGain_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CalAdjustDownconverterGain_cfunc(vi, channel_list, frequency, gain)

    def niRFSA_CalAdjustIfAttenuationCalibration(self, vi, channel_list, if_filter, number_of_attenuators, attenuator_settings, measurement):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CalAdjustIfAttenuationCalibration_cfunc is None:
                self.niRFSA_CalAdjustIfAttenuationCalibration_cfunc = self._get_library_function('niRFSA_CalAdjustIfAttenuationCalibration')
                self.niRFSA_CalAdjustIfAttenuationCalibration_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64), ViReal64]  # noqa: F405
                self.niRFSA_CalAdjustIfAttenuationCalibration_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CalAdjustIfAttenuationCalibration_cfunc(vi, channel_list, if_filter, number_of_attenuators, attenuator_settings, measurement)

    def niRFSA_CalAdjustIfResponseCalibration(self, vi, channel_list, if_filter, rf_frequency, band_width, number_of_measurements, measurements):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CalAdjustIfResponseCalibration_cfunc is None:
                self.niRFSA_CalAdjustIfResponseCalibration_cfunc = self._get_library_function('niRFSA_CalAdjustIfResponseCalibration')
                self.niRFSA_CalAdjustIfResponseCalibration_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSA_CalAdjustIfResponseCalibration_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CalAdjustIfResponseCalibration_cfunc(vi, channel_list, if_filter, rf_frequency, band_width, number_of_measurements, measurements)

    def niRFSA_CalAdjustLoExportCalibration(self, vi, channel_list, lo_number, number_of_frequency_points, frequency_points, lo_attenuation):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CalAdjustLoExportCalibration_cfunc is None:
                self.niRFSA_CalAdjustLoExportCalibration_cfunc = self._get_library_function('niRFSA_CalAdjustLoExportCalibration')
                self.niRFSA_CalAdjustLoExportCalibration_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSA_CalAdjustLoExportCalibration_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CalAdjustLoExportCalibration_cfunc(vi, channel_list, lo_number, number_of_frequency_points, frequency_points, lo_attenuation)

    def niRFSA_CalAdjustRefLevelCalibration(self, vi, channel_list, reference_level_data_type, rf_band, attenuator_table_number, frequency, measurement):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CalAdjustRefLevelCalibration_cfunc is None:
                self.niRFSA_CalAdjustRefLevelCalibration_cfunc = self._get_library_function('niRFSA_CalAdjustRefLevelCalibration')
                self.niRFSA_CalAdjustRefLevelCalibration_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niRFSA_CalAdjustRefLevelCalibration_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CalAdjustRefLevelCalibration_cfunc(vi, channel_list, reference_level_data_type, rf_band, attenuator_table_number, frequency, measurement)

    def niRFSA_CalSetTemperature(self, vi, channel_list, temperature):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CalSetTemperature_cfunc is None:
                self.niRFSA_CalSetTemperature_cfunc = self._get_library_function('niRFSA_CalSetTemperature')
                self.niRFSA_CalSetTemperature_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_CalSetTemperature_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CalSetTemperature_cfunc(vi, channel_list, temperature)

    def niRFSA_ChangeExtCalPassword(self, vi, old_password, new_password):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ChangeExtCalPassword_cfunc is None:
                self.niRFSA_ChangeExtCalPassword_cfunc = self._get_library_function('niRFSA_ChangeExtCalPassword')
                self.niRFSA_ChangeExtCalPassword_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_ChangeExtCalPassword_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ChangeExtCalPassword_cfunc(vi, old_password, new_password)

    def niRFSA_CheckAcquisitionStatus(self, vi, is_done):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CheckAcquisitionStatus_cfunc is None:
                self.niRFSA_CheckAcquisitionStatus_cfunc = self._get_library_function('niRFSA_CheckAcquisitionStatus')
                self.niRFSA_CheckAcquisitionStatus_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSA_CheckAcquisitionStatus_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CheckAcquisitionStatus_cfunc(vi, is_done)

    def niRFSA_ClearError(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ClearError_cfunc is None:
                self.niRFSA_ClearError_cfunc = self._get_library_function('niRFSA_ClearError')
                self.niRFSA_ClearError_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_ClearError_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ClearError_cfunc(vi)

    def niRFSA_ClearSelfCalibrateRange(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ClearSelfCalibrateRange_cfunc is None:
                self.niRFSA_ClearSelfCalibrateRange_cfunc = self._get_library_function('niRFSA_ClearSelfCalibrateRange')
                self.niRFSA_ClearSelfCalibrateRange_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_ClearSelfCalibrateRange_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ClearSelfCalibrateRange_cfunc(vi)

    def niRFSA_Close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_Close_cfunc is None:
                self.niRFSA_Close_cfunc = self._get_library_function('niRFSA_Close')
                self.niRFSA_Close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_Close_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_Close_cfunc(vi)

    def niRFSA_CloseCalibrationStep(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CloseCalibrationStep_cfunc is None:
                self.niRFSA_CloseCalibrationStep_cfunc = self._get_library_function('niRFSA_CloseCalibrationStep')
                self.niRFSA_CloseCalibrationStep_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_CloseCalibrationStep_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CloseCalibrationStep_cfunc(vi)

    def niRFSA_CloseExtCal(self, vi, action):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CloseExtCal_cfunc is None:
                self.niRFSA_CloseExtCal_cfunc = self._get_library_function('niRFSA_CloseExtCal')
                self.niRFSA_CloseExtCal_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niRFSA_CloseExtCal_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CloseExtCal_cfunc(vi, action)

    def niRFSA_CloseExternalAlignment(self, vi, action):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CloseExternalAlignment_cfunc is None:
                self.niRFSA_CloseExternalAlignment_cfunc = self._get_library_function('niRFSA_CloseExternalAlignment')
                self.niRFSA_CloseExternalAlignment_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niRFSA_CloseExternalAlignment_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CloseExternalAlignment_cfunc(vi, action)

    def niRFSA_CloseExternalAlignmentStep(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CloseExternalAlignmentStep_cfunc is None:
                self.niRFSA_CloseExternalAlignmentStep_cfunc = self._get_library_function('niRFSA_CloseExternalAlignmentStep')
                self.niRFSA_CloseExternalAlignmentStep_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_CloseExternalAlignmentStep_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CloseExternalAlignmentStep_cfunc(vi)

    def niRFSA_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_Commit_cfunc is None:
                self.niRFSA_Commit_cfunc = self._get_library_function('niRFSA_Commit')
                self.niRFSA_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_Commit_cfunc(vi)

    def niRFSA_ConfigureAcquisitionType(self, vi, acquisition_type):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureAcquisitionType_cfunc is None:
                self.niRFSA_ConfigureAcquisitionType_cfunc = self._get_library_function('niRFSA_ConfigureAcquisitionType')
                self.niRFSA_ConfigureAcquisitionType_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niRFSA_ConfigureAcquisitionType_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureAcquisitionType_cfunc(vi, acquisition_type)

    def niRFSA_ConfigureDeembeddingTableInterpolationLinear(self, vi, port, table_name, format):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureDeembeddingTableInterpolationLinear_cfunc is None:
                self.niRFSA_ConfigureDeembeddingTableInterpolationLinear_cfunc = self._get_library_function('niRFSA_ConfigureDeembeddingTableInterpolationLinear')
                self.niRFSA_ConfigureDeembeddingTableInterpolationLinear_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSA_ConfigureDeembeddingTableInterpolationLinear_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureDeembeddingTableInterpolationLinear_cfunc(vi, port, table_name, format)

    def niRFSA_ConfigureDeembeddingTableInterpolationNearest(self, vi, port, table_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureDeembeddingTableInterpolationNearest_cfunc is None:
                self.niRFSA_ConfigureDeembeddingTableInterpolationNearest_cfunc = self._get_library_function('niRFSA_ConfigureDeembeddingTableInterpolationNearest')
                self.niRFSA_ConfigureDeembeddingTableInterpolationNearest_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_ConfigureDeembeddingTableInterpolationNearest_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureDeembeddingTableInterpolationNearest_cfunc(vi, port, table_name)

    def niRFSA_ConfigureDeembeddingTableInterpolationSpline(self, vi, port, table_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureDeembeddingTableInterpolationSpline_cfunc is None:
                self.niRFSA_ConfigureDeembeddingTableInterpolationSpline_cfunc = self._get_library_function('niRFSA_ConfigureDeembeddingTableInterpolationSpline')
                self.niRFSA_ConfigureDeembeddingTableInterpolationSpline_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_ConfigureDeembeddingTableInterpolationSpline_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureDeembeddingTableInterpolationSpline_cfunc(vi, port, table_name)

    def niRFSA_ConfigureDigitalEdgeAdvanceTrigger(self, vi, source, edge):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureDigitalEdgeAdvanceTrigger_cfunc is None:
                self.niRFSA_ConfigureDigitalEdgeAdvanceTrigger_cfunc = self._get_library_function('niRFSA_ConfigureDigitalEdgeAdvanceTrigger')
                self.niRFSA_ConfigureDigitalEdgeAdvanceTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSA_ConfigureDigitalEdgeAdvanceTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureDigitalEdgeAdvanceTrigger_cfunc(vi, source, edge)

    def niRFSA_ConfigureDigitalEdgeRefTrigger(self, vi, source, edge, pretrigger_samples):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureDigitalEdgeRefTrigger_cfunc is None:
                self.niRFSA_ConfigureDigitalEdgeRefTrigger_cfunc = self._get_library_function('niRFSA_ConfigureDigitalEdgeRefTrigger')
                self.niRFSA_ConfigureDigitalEdgeRefTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt64]  # noqa: F405
                self.niRFSA_ConfigureDigitalEdgeRefTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureDigitalEdgeRefTrigger_cfunc(vi, source, edge, pretrigger_samples)

    def niRFSA_ConfigureDigitalEdgeStartTrigger(self, vi, source, edge):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureDigitalEdgeStartTrigger_cfunc is None:
                self.niRFSA_ConfigureDigitalEdgeStartTrigger_cfunc = self._get_library_function('niRFSA_ConfigureDigitalEdgeStartTrigger')
                self.niRFSA_ConfigureDigitalEdgeStartTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSA_ConfigureDigitalEdgeStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureDigitalEdgeStartTrigger_cfunc(vi, source, edge)

    def niRFSA_ConfigureIqCarrierFrequency(self, vi, channel_list, carrier_frequency):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureIqCarrierFrequency_cfunc is None:
                self.niRFSA_ConfigureIqCarrierFrequency_cfunc = self._get_library_function('niRFSA_ConfigureIqCarrierFrequency')
                self.niRFSA_ConfigureIqCarrierFrequency_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_ConfigureIqCarrierFrequency_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureIqCarrierFrequency_cfunc(vi, channel_list, carrier_frequency)

    def niRFSA_ConfigureIqPowerEdgeRefTrigger(self, vi, source, level, slope, pretrigger_samples):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureIqPowerEdgeRefTrigger_cfunc is None:
                self.niRFSA_ConfigureIqPowerEdgeRefTrigger_cfunc = self._get_library_function('niRFSA_ConfigureIqPowerEdgeRefTrigger')
                self.niRFSA_ConfigureIqPowerEdgeRefTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ViInt64]  # noqa: F405
                self.niRFSA_ConfigureIqPowerEdgeRefTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureIqPowerEdgeRefTrigger_cfunc(vi, source, level, slope, pretrigger_samples)

    def niRFSA_ConfigureIqRate(self, vi, channel_list, iq_rate):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureIqRate_cfunc is None:
                self.niRFSA_ConfigureIqRate_cfunc = self._get_library_function('niRFSA_ConfigureIqRate')
                self.niRFSA_ConfigureIqRate_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_ConfigureIqRate_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureIqRate_cfunc(vi, channel_list, iq_rate)

    def niRFSA_ConfigureNumberOfRecords(self, vi, channel_list, number_of_records_is_finite, number_of_records):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureNumberOfRecords_cfunc is None:
                self.niRFSA_ConfigureNumberOfRecords_cfunc = self._get_library_function('niRFSA_ConfigureNumberOfRecords')
                self.niRFSA_ConfigureNumberOfRecords_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean, ViInt64]  # noqa: F405
                self.niRFSA_ConfigureNumberOfRecords_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureNumberOfRecords_cfunc(vi, channel_list, number_of_records_is_finite, number_of_records)

    def niRFSA_ConfigureNumberOfSamples(self, vi, channel_list, number_of_samples_is_finite, samples_per_record):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureNumberOfSamples_cfunc is None:
                self.niRFSA_ConfigureNumberOfSamples_cfunc = self._get_library_function('niRFSA_ConfigureNumberOfSamples')
                self.niRFSA_ConfigureNumberOfSamples_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean, ViInt64]  # noqa: F405
                self.niRFSA_ConfigureNumberOfSamples_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureNumberOfSamples_cfunc(vi, channel_list, number_of_samples_is_finite, samples_per_record)

    def niRFSA_ConfigurePxiChassisClk10(self, vi, pxi_clk10_source):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigurePxiChassisClk10_cfunc is None:
                self.niRFSA_ConfigurePxiChassisClk10_cfunc = self._get_library_function('niRFSA_ConfigurePxiChassisClk10')
                self.niRFSA_ConfigurePxiChassisClk10_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_ConfigurePxiChassisClk10_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigurePxiChassisClk10_cfunc(vi, pxi_clk10_source)

    def niRFSA_ConfigureRefClock(self, vi, clock_source, ref_clock_rate):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureRefClock_cfunc is None:
                self.niRFSA_ConfigureRefClock_cfunc = self._get_library_function('niRFSA_ConfigureRefClock')
                self.niRFSA_ConfigureRefClock_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_ConfigureRefClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureRefClock_cfunc(vi, clock_source, ref_clock_rate)

    def niRFSA_ConfigureReferenceLevel(self, vi, channel_list, reference_level):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureReferenceLevel_cfunc is None:
                self.niRFSA_ConfigureReferenceLevel_cfunc = self._get_library_function('niRFSA_ConfigureReferenceLevel')
                self.niRFSA_ConfigureReferenceLevel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_ConfigureReferenceLevel_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureReferenceLevel_cfunc(vi, channel_list, reference_level)

    def niRFSA_ConfigureResolutionBandwidth(self, vi, channel_list, resolution_bandwidth):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureResolutionBandwidth_cfunc is None:
                self.niRFSA_ConfigureResolutionBandwidth_cfunc = self._get_library_function('niRFSA_ConfigureResolutionBandwidth')
                self.niRFSA_ConfigureResolutionBandwidth_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_ConfigureResolutionBandwidth_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureResolutionBandwidth_cfunc(vi, channel_list, resolution_bandwidth)

    def niRFSA_ConfigureSoftwareEdgeAdvanceTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger_cfunc is None:
                self.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger_cfunc = self._get_library_function('niRFSA_ConfigureSoftwareEdgeAdvanceTrigger')
                self.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger_cfunc(vi)

    def niRFSA_ConfigureSoftwareEdgeRefTrigger(self, vi, pretrigger_samples):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureSoftwareEdgeRefTrigger_cfunc is None:
                self.niRFSA_ConfigureSoftwareEdgeRefTrigger_cfunc = self._get_library_function('niRFSA_ConfigureSoftwareEdgeRefTrigger')
                self.niRFSA_ConfigureSoftwareEdgeRefTrigger_cfunc.argtypes = [ViSession, ViInt64]  # noqa: F405
                self.niRFSA_ConfigureSoftwareEdgeRefTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureSoftwareEdgeRefTrigger_cfunc(vi, pretrigger_samples)

    def niRFSA_ConfigureSoftwareEdgeStartTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureSoftwareEdgeStartTrigger_cfunc is None:
                self.niRFSA_ConfigureSoftwareEdgeStartTrigger_cfunc = self._get_library_function('niRFSA_ConfigureSoftwareEdgeStartTrigger')
                self.niRFSA_ConfigureSoftwareEdgeStartTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_ConfigureSoftwareEdgeStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureSoftwareEdgeStartTrigger_cfunc(vi)

    def niRFSA_ConfigureSpectrumFrequencyCenterSpan(self, vi, channel_list, center_frequency, span):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureSpectrumFrequencyCenterSpan_cfunc is None:
                self.niRFSA_ConfigureSpectrumFrequencyCenterSpan_cfunc = self._get_library_function('niRFSA_ConfigureSpectrumFrequencyCenterSpan')
                self.niRFSA_ConfigureSpectrumFrequencyCenterSpan_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niRFSA_ConfigureSpectrumFrequencyCenterSpan_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureSpectrumFrequencyCenterSpan_cfunc(vi, channel_list, center_frequency, span)

    def niRFSA_ConfigureSpectrumFrequencyStartStop(self, vi, channel_list, start_frequency, stop_frequency):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc is None:
                self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc = self._get_library_function('niRFSA_ConfigureSpectrumFrequencyStartStop')
                self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc(vi, channel_list, start_frequency, stop_frequency)

    def niRFSA_CreateConfigurationList(self, vi, list_name, number_of_list_attributes, list_attribute_i_ds, set_as_active_list):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CreateConfigurationList_cfunc is None:
                self.niRFSA_CreateConfigurationList_cfunc = self._get_library_function('niRFSA_CreateConfigurationList')
                self.niRFSA_CreateConfigurationList_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViAttr), ViBoolean]  # noqa: F405
                self.niRFSA_CreateConfigurationList_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CreateConfigurationList_cfunc(vi, list_name, number_of_list_attributes, list_attribute_i_ds, set_as_active_list)

    def niRFSA_CreateConfigurationListStep(self, vi, set_as_active_step):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CreateConfigurationListStep_cfunc is None:
                self.niRFSA_CreateConfigurationListStep_cfunc = self._get_library_function('niRFSA_CreateConfigurationListStep')
                self.niRFSA_CreateConfigurationListStep_cfunc.argtypes = [ViSession, ViBoolean]  # noqa: F405
                self.niRFSA_CreateConfigurationListStep_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CreateConfigurationListStep_cfunc(vi, set_as_active_step)

    def niRFSA_CreateDeembeddingSparameterTableArray(self, vi, port, table_name, frequencies, frequencies_size, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CreateDeembeddingSparameterTableArray_cfunc is None:
                self.niRFSA_CreateDeembeddingSparameterTableArray_cfunc = self._get_library_function('niRFSA_CreateDeembeddingSparameterTableArray')
                self.niRFSA_CreateDeembeddingSparameterTableArray_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(NIComplexNumber), ViInt32, ViInt32, ViInt32]  # noqa: F405
                self.niRFSA_CreateDeembeddingSparameterTableArray_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CreateDeembeddingSparameterTableArray_cfunc(vi, port, table_name, frequencies, frequencies_size, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation)

    def niRFSA_CreateDeembeddingSparameterTableS2PFile(self, vi, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CreateDeembeddingSparameterTableS2PFile_cfunc is None:
                self.niRFSA_CreateDeembeddingSparameterTableS2PFile_cfunc = self._get_library_function('niRFSA_CreateDeembeddingSparameterTableS2PFile')
                self.niRFSA_CreateDeembeddingSparameterTableS2PFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSA_CreateDeembeddingSparameterTableS2PFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CreateDeembeddingSparameterTableS2PFile_cfunc(vi, port, table_name, s2p_file_path, sparameter_orientation)

    def niRFSA_DeleteAllDeembeddingTables(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_DeleteAllDeembeddingTables_cfunc is None:
                self.niRFSA_DeleteAllDeembeddingTables_cfunc = self._get_library_function('niRFSA_DeleteAllDeembeddingTables')
                self.niRFSA_DeleteAllDeembeddingTables_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_DeleteAllDeembeddingTables_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_DeleteAllDeembeddingTables_cfunc(vi)

    def niRFSA_DeleteConfigurationList(self, vi, list_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_DeleteConfigurationList_cfunc is None:
                self.niRFSA_DeleteConfigurationList_cfunc = self._get_library_function('niRFSA_DeleteConfigurationList')
                self.niRFSA_DeleteConfigurationList_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_DeleteConfigurationList_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_DeleteConfigurationList_cfunc(vi, list_name)

    def niRFSA_DeleteDeembeddingTable(self, vi, port, table_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_DeleteDeembeddingTable_cfunc is None:
                self.niRFSA_DeleteDeembeddingTable_cfunc = self._get_library_function('niRFSA_DeleteDeembeddingTable')
                self.niRFSA_DeleteDeembeddingTable_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_DeleteDeembeddingTable_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_DeleteDeembeddingTable_cfunc(vi, port, table_name)

    def niRFSA_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_Disable_cfunc is None:
                self.niRFSA_Disable_cfunc = self._get_library_function('niRFSA_Disable')
                self.niRFSA_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_Disable_cfunc(vi)

    def niRFSA_DisableAdvanceTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_DisableAdvanceTrigger_cfunc is None:
                self.niRFSA_DisableAdvanceTrigger_cfunc = self._get_library_function('niRFSA_DisableAdvanceTrigger')
                self.niRFSA_DisableAdvanceTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_DisableAdvanceTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_DisableAdvanceTrigger_cfunc(vi)

    def niRFSA_DisableRefTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_DisableRefTrigger_cfunc is None:
                self.niRFSA_DisableRefTrigger_cfunc = self._get_library_function('niRFSA_DisableRefTrigger')
                self.niRFSA_DisableRefTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_DisableRefTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_DisableRefTrigger_cfunc(vi)

    def niRFSA_DisableStartTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_DisableStartTrigger_cfunc is None:
                self.niRFSA_DisableStartTrigger_cfunc = self._get_library_function('niRFSA_DisableStartTrigger')
                self.niRFSA_DisableStartTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_DisableStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_DisableStartTrigger_cfunc(vi)

    def niRFSA_EnableSessionAccess(self, vi, enable):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_EnableSessionAccess_cfunc is None:
                self.niRFSA_EnableSessionAccess_cfunc = self._get_library_function('niRFSA_EnableSessionAccess')
                self.niRFSA_EnableSessionAccess_cfunc.argtypes = [ViSession, ViBoolean]  # noqa: F405
                self.niRFSA_EnableSessionAccess_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_EnableSessionAccess_cfunc(vi, enable)

    def niRFSA_ErrorMessage(self, vi, status_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ErrorMessage_cfunc is None:
                self.niRFSA_ErrorMessage_cfunc = self._get_library_function('niRFSA_ErrorMessage')
                self.niRFSA_ErrorMessage_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_ErrorMessage_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ErrorMessage_cfunc(vi, status_code, error_message)

    def niRFSA_ErrorQuery(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ErrorQuery_cfunc is None:
                self.niRFSA_ErrorQuery_cfunc = self._get_library_function('niRFSA_ErrorQuery')
                self.niRFSA_ErrorQuery_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_ErrorQuery_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ErrorQuery_cfunc(vi, error_code, error_message)

    def niRFSA_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ExportSignal_cfunc is None:
                self.niRFSA_ExportSignal_cfunc = self._get_library_function('niRFSA_ExportSignal')
                self.niRFSA_ExportSignal_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_ExportSignal_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ExportSignal_cfunc(vi, signal, signal_identifier, output_terminal)

    def niRFSA_ExtCalStoreBaselineForSelfCalibration(self, vi, password, self_calibration_step):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ExtCalStoreBaselineForSelfCalibration_cfunc is None:
                self.niRFSA_ExtCalStoreBaselineForSelfCalibration_cfunc = self._get_library_function('niRFSA_ExtCalStoreBaselineForSelfCalibration')
                self.niRFSA_ExtCalStoreBaselineForSelfCalibration_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64]  # noqa: F405
                self.niRFSA_ExtCalStoreBaselineForSelfCalibration_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ExtCalStoreBaselineForSelfCalibration_cfunc(vi, password, self_calibration_step)

    def niRFSA_ExternalAlignmentAdjustPreselector(self, vi, number_of_coefficients, coefficients):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ExternalAlignmentAdjustPreselector_cfunc is None:
                self.niRFSA_ExternalAlignmentAdjustPreselector_cfunc = self._get_library_function('niRFSA_ExternalAlignmentAdjustPreselector')
                self.niRFSA_ExternalAlignmentAdjustPreselector_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSA_ExternalAlignmentAdjustPreselector_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ExternalAlignmentAdjustPreselector_cfunc(vi, number_of_coefficients, coefficients)

    def niRFSA_FetchIqMultiRecordComplexF32(self, vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, data, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_FetchIqMultiRecordComplexF32_cfunc is None:
                self.niRFSA_FetchIqMultiRecordComplexF32_cfunc = self._get_library_function('niRFSA_FetchIqMultiRecordComplexF32')
                self.niRFSA_FetchIqMultiRecordComplexF32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ViInt64, ViInt64, ViReal64, ctypes.POINTER(NIComplexNumberF32), ctypes.POINTER(waveform_info.struct_niRFSA_wfmInfo)]  # noqa: F405
                self.niRFSA_FetchIqMultiRecordComplexF32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_FetchIqMultiRecordComplexF32_cfunc(vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, data, wfm_info)

    def niRFSA_FetchIqMultiRecordComplexF64(self, vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, data, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_FetchIqMultiRecordComplexF64_cfunc is None:
                self.niRFSA_FetchIqMultiRecordComplexF64_cfunc = self._get_library_function('niRFSA_FetchIqMultiRecordComplexF64')
                self.niRFSA_FetchIqMultiRecordComplexF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ViInt64, ViInt64, ViReal64, ctypes.POINTER(NIComplexNumber), ctypes.POINTER(waveform_info.struct_niRFSA_wfmInfo)]  # noqa: F405
                self.niRFSA_FetchIqMultiRecordComplexF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_FetchIqMultiRecordComplexF64_cfunc(vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, data, wfm_info)

    def niRFSA_GetAttributeViBoolean(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetAttributeViBoolean_cfunc is None:
                self.niRFSA_GetAttributeViBoolean_cfunc = self._get_library_function('niRFSA_GetAttributeViBoolean')
                self.niRFSA_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSA_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_GetAttributeViInt32(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetAttributeViInt32_cfunc is None:
                self.niRFSA_GetAttributeViInt32_cfunc = self._get_library_function('niRFSA_GetAttributeViInt32')
                self.niRFSA_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_GetAttributeViInt64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetAttributeViInt64_cfunc is None:
                self.niRFSA_GetAttributeViInt64_cfunc = self._get_library_function('niRFSA_GetAttributeViInt64')
                self.niRFSA_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niRFSA_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetAttributeViInt64_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_GetAttributeViReal64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetAttributeViReal64_cfunc is None:
                self.niRFSA_GetAttributeViReal64_cfunc = self._get_library_function('niRFSA_GetAttributeViReal64')
                self.niRFSA_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSA_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_GetAttributeViSession(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetAttributeViSession_cfunc is None:
                self.niRFSA_GetAttributeViSession_cfunc = self._get_library_function('niRFSA_GetAttributeViSession')
                self.niRFSA_GetAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niRFSA_GetAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetAttributeViSession_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_GetAttributeViString(self, vi, channel_name, attribute_id, buf_size, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetAttributeViString_cfunc is None:
                self.niRFSA_GetAttributeViString_cfunc = self._get_library_function('niRFSA_GetAttributeViString')
                self.niRFSA_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetAttributeViString_cfunc(vi, channel_name, attribute_id, buf_size, value)

    def niRFSA_GetCalUserDefinedInfo(self, vi, info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetCalUserDefinedInfo_cfunc is None:
                self.niRFSA_GetCalUserDefinedInfo_cfunc = self._get_library_function('niRFSA_GetCalUserDefinedInfo')
                self.niRFSA_GetCalUserDefinedInfo_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_GetCalUserDefinedInfo_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetCalUserDefinedInfo_cfunc(vi, info)

    def niRFSA_GetCalUserDefinedInfoMaxSize(self, vi, info_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetCalUserDefinedInfoMaxSize_cfunc is None:
                self.niRFSA_GetCalUserDefinedInfoMaxSize_cfunc = self._get_library_function('niRFSA_GetCalUserDefinedInfoMaxSize')
                self.niRFSA_GetCalUserDefinedInfoMaxSize_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetCalUserDefinedInfoMaxSize_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetCalUserDefinedInfoMaxSize_cfunc(vi, info_size)

    def niRFSA_GetDeembeddingSparameters(self, vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetDeembeddingSparameters_cfunc is None:
                self.niRFSA_GetDeembeddingSparameters_cfunc = self._get_library_function('niRFSA_GetDeembeddingSparameters')
                self.niRFSA_GetDeembeddingSparameters_cfunc.argtypes = [ViSession, ctypes.POINTER(NIComplexNumber), ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetDeembeddingSparameters_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetDeembeddingSparameters_cfunc(vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports)

    def niRFSA_GetDeviceResponse(self, vi, channel_list, response_type, buffer_size, frequencies, magnitude_response, phase_response, number_of_frequencies):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetDeviceResponse_cfunc is None:
                self.niRFSA_GetDeviceResponse_cfunc = self._get_library_function('niRFSA_GetDeviceResponse')
                self.niRFSA_GetDeviceResponse_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetDeviceResponse_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetDeviceResponse_cfunc(vi, channel_list, response_type, buffer_size, frequencies, magnitude_response, phase_response, number_of_frequencies)

    def niRFSA_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetError_cfunc is None:
                self.niRFSA_GetError_cfunc = self._get_library_function('niRFSA_GetError')
                self.niRFSA_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetError_cfunc(vi, error_code, error_description_buffer_size, error_description)

    def niRFSA_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetExtCalLastDateAndTime_cfunc is None:
                self.niRFSA_GetExtCalLastDateAndTime_cfunc = self._get_library_function('niRFSA_GetExtCalLastDateAndTime')
                self.niRFSA_GetExtCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetExtCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetExtCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niRFSA_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetExtCalLastTemp_cfunc is None:
                self.niRFSA_GetExtCalLastTemp_cfunc = self._get_library_function('niRFSA_GetExtCalLastTemp')
                self.niRFSA_GetExtCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSA_GetExtCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetExtCalLastTemp_cfunc(vi, temperature)

    def niRFSA_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetExtCalRecommendedInterval_cfunc is None:
                self.niRFSA_GetExtCalRecommendedInterval_cfunc = self._get_library_function('niRFSA_GetExtCalRecommendedInterval')
                self.niRFSA_GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetExtCalRecommendedInterval_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetExtCalRecommendedInterval_cfunc(vi, months)

    def niRFSA_GetFetchBacklog(self, vi, channel_list, record_number, backlog):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetFetchBacklog_cfunc is None:
                self.niRFSA_GetFetchBacklog_cfunc = self._get_library_function('niRFSA_GetFetchBacklog')
                self.niRFSA_GetFetchBacklog_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niRFSA_GetFetchBacklog_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetFetchBacklog_cfunc(vi, channel_list, record_number, backlog)

    def niRFSA_GetFrequencyResponse(self, vi, channel_list, buffer_size, frequencies, magnitude_response, phase_response, number_of_frequencies):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetFrequencyResponse_cfunc is None:
                self.niRFSA_GetFrequencyResponse_cfunc = self._get_library_function('niRFSA_GetFrequencyResponse')
                self.niRFSA_GetFrequencyResponse_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetFrequencyResponse_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetFrequencyResponse_cfunc(vi, channel_list, buffer_size, frequencies, magnitude_response, phase_response, number_of_frequencies)

    def niRFSA_GetGainReferenceCalBaseline(self, vi, buffer_size, gain_reference_cal_constants, number_of_gain_reference_cal_constants):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetGainReferenceCalBaseline_cfunc is None:
                self.niRFSA_GetGainReferenceCalBaseline_cfunc = self._get_library_function('niRFSA_GetGainReferenceCalBaseline')
                self.niRFSA_GetGainReferenceCalBaseline_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetGainReferenceCalBaseline_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetGainReferenceCalBaseline_cfunc(vi, buffer_size, gain_reference_cal_constants, number_of_gain_reference_cal_constants)

    def niRFSA_GetNormalizationCoefficients(self, vi, channel_list, array_size, coefficient_info, number_of_coefficient_sets):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetNormalizationCoefficients_cfunc is None:
                self.niRFSA_GetNormalizationCoefficients_cfunc = self._get_library_function('niRFSA_GetNormalizationCoefficients')
                self.niRFSA_GetNormalizationCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(coefficient_info_type.struct_niRFSA_coefficientInfo), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetNormalizationCoefficients_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetNormalizationCoefficients_cfunc(vi, channel_list, array_size, coefficient_info, number_of_coefficient_sets)

    def niRFSA_GetNumberOfSpectralLines(self, vi, channel_list, number_of_spectral_lines):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetNumberOfSpectralLines_cfunc is None:
                self.niRFSA_GetNumberOfSpectralLines_cfunc = self._get_library_function('niRFSA_GetNumberOfSpectralLines')
                self.niRFSA_GetNumberOfSpectralLines_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetNumberOfSpectralLines_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetNumberOfSpectralLines_cfunc(vi, channel_list, number_of_spectral_lines)

    def niRFSA_GetRelayName(self, vi, channel_list, index, name, buffer_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetRelayName_cfunc is None:
                self.niRFSA_GetRelayName_cfunc = self._get_library_function('niRFSA_GetRelayName')
                self.niRFSA_GetRelayName_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSA_GetRelayName_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetRelayName_cfunc(vi, channel_list, index, name, buffer_size)

    def niRFSA_GetRelayOperationsCount(self, vi, channel_list, operations_count, buffer_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetRelayOperationsCount_cfunc is None:
                self.niRFSA_GetRelayOperationsCount_cfunc = self._get_library_function('niRFSA_GetRelayOperationsCount')
                self.niRFSA_GetRelayOperationsCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32), ViInt32]  # noqa: F405
                self.niRFSA_GetRelayOperationsCount_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetRelayOperationsCount_cfunc(vi, channel_list, operations_count, buffer_size)

    def niRFSA_GetScalingCoefficients(self, vi, channel_list, array_size, coefficient_info, number_of_coefficient_sets):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetScalingCoefficients_cfunc is None:
                self.niRFSA_GetScalingCoefficients_cfunc = self._get_library_function('niRFSA_GetScalingCoefficients')
                self.niRFSA_GetScalingCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(coefficient_info_type.struct_niRFSA_coefficientInfo), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetScalingCoefficients_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetScalingCoefficients_cfunc(vi, channel_list, array_size, coefficient_info, number_of_coefficient_sets)

    def niRFSA_GetSelfCalLastDateAndTime(self, vi, self_calibration_step, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetSelfCalLastDateAndTime_cfunc is None:
                self.niRFSA_GetSelfCalLastDateAndTime_cfunc = self._get_library_function('niRFSA_GetSelfCalLastDateAndTime')
                self.niRFSA_GetSelfCalLastDateAndTime_cfunc.argtypes = [ViSession, ViInt64, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetSelfCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetSelfCalLastDateAndTime_cfunc(vi, self_calibration_step, year, month, day, hour, minute)

    def niRFSA_GetSelfCalLastTemp(self, vi, self_calibration_step, temp):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetSelfCalLastTemp_cfunc is None:
                self.niRFSA_GetSelfCalLastTemp_cfunc = self._get_library_function('niRFSA_GetSelfCalLastTemp')
                self.niRFSA_GetSelfCalLastTemp_cfunc.argtypes = [ViSession, ViInt64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSA_GetSelfCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetSelfCalLastTemp_cfunc(vi, self_calibration_step, temp)

    def niRFSA_GetSpectralInfoForSmt(self, vi, spectrum_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetSpectralInfoForSmt_cfunc is None:
                self.niRFSA_GetSpectralInfoForSmt_cfunc = self._get_library_function('niRFSA_GetSpectralInfoForSmt')
                self.niRFSA_GetSpectralInfoForSmt_cfunc.argtypes = [ViSession, ctypes.POINTER(spectrum_info_type.struct_niRFSA_spectrumInfo)]  # noqa: F405
                self.niRFSA_GetSpectralInfoForSmt_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetSpectralInfoForSmt_cfunc(vi, spectrum_info)

    def niRFSA_GetStreamEndpointHandle(self, vi, stream_endpoint, writer_handle):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetStreamEndpointHandle_cfunc is None:
                self.niRFSA_GetStreamEndpointHandle_cfunc = self._get_library_function('niRFSA_GetStreamEndpointHandle')
                self.niRFSA_GetStreamEndpointHandle_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViUInt32)]  # noqa: F405
                self.niRFSA_GetStreamEndpointHandle_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetStreamEndpointHandle_cfunc(vi, stream_endpoint, writer_handle)

    def niRFSA_GetTerminalName(self, vi, signal, signal_identifier, buffer_size, terminal_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetTerminalName_cfunc is None:
                self.niRFSA_GetTerminalName_cfunc = self._get_library_function('niRFSA_GetTerminalName')
                self.niRFSA_GetTerminalName_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_GetTerminalName_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetTerminalName_cfunc(vi, signal, signal_identifier, buffer_size, terminal_name)

    def niRFSA_GetUserData(self, vi, identifier, buffer_size, data, actual_data_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetUserData_cfunc is None:
                self.niRFSA_GetUserData_cfunc = self._get_library_function('niRFSA_GetUserData')
                self.niRFSA_GetUserData_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt8), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetUserData_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetUserData_cfunc(vi, identifier, buffer_size, data, actual_data_size)

    def niRFSA_Init(self, resource_name, id_query, reset, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_Init_cfunc is None:
                self.niRFSA_Init_cfunc = self._get_library_function('niRFSA_Init')
                self.niRFSA_Init_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niRFSA_Init_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_Init_cfunc(resource_name, id_query, reset, vi)

    def niRFSA_InitExtCal(self, resource_name, password, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_InitExtCal_cfunc is None:
                self.niRFSA_InitExtCal_cfunc = self._get_library_function('niRFSA_InitExtCal')
                self.niRFSA_InitExtCal_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niRFSA_InitExtCal_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_InitExtCal_cfunc(resource_name, password, option_string, vi)

    def niRFSA_InitWithOptions(self, resource_name, id_query, reset, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_InitWithOptions_cfunc is None:
                self.niRFSA_InitWithOptions_cfunc = self._get_library_function('niRFSA_InitWithOptions')
                self.niRFSA_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niRFSA_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_InitWithOptions_cfunc(resource_name, id_query, reset, option_string, vi)

    def niRFSA_InitializeCalibrationStep(self, vi, calibration_step):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_InitializeCalibrationStep_cfunc is None:
                self.niRFSA_InitializeCalibrationStep_cfunc = self._get_library_function('niRFSA_InitializeCalibrationStep')
                self.niRFSA_InitializeCalibrationStep_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niRFSA_InitializeCalibrationStep_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_InitializeCalibrationStep_cfunc(vi, calibration_step)

    def niRFSA_InitializeExternalAlignment(self, resource_name, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_InitializeExternalAlignment_cfunc is None:
                self.niRFSA_InitializeExternalAlignment_cfunc = self._get_library_function('niRFSA_InitializeExternalAlignment')
                self.niRFSA_InitializeExternalAlignment_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niRFSA_InitializeExternalAlignment_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_InitializeExternalAlignment_cfunc(resource_name, option_string, vi)

    def niRFSA_InitializeExternalAlignmentStep(self, vi, external_alignment_step):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_InitializeExternalAlignmentStep_cfunc is None:
                self.niRFSA_InitializeExternalAlignmentStep_cfunc = self._get_library_function('niRFSA_InitializeExternalAlignmentStep')
                self.niRFSA_InitializeExternalAlignmentStep_cfunc.argtypes = [ViSession, ViInt64]  # noqa: F405
                self.niRFSA_InitializeExternalAlignmentStep_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_InitializeExternalAlignmentStep_cfunc(vi, external_alignment_step)

    def niRFSA_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_Initiate_cfunc is None:
                self.niRFSA_Initiate_cfunc = self._get_library_function('niRFSA_Initiate')
                self.niRFSA_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_Initiate_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_Initiate_cfunc(vi)

    def niRFSA_InvalidateAllAttributes(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_InvalidateAllAttributes_cfunc is None:
                self.niRFSA_InvalidateAllAttributes_cfunc = self._get_library_function('niRFSA_InvalidateAllAttributes')
                self.niRFSA_InvalidateAllAttributes_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_InvalidateAllAttributes_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_InvalidateAllAttributes_cfunc(vi)

    def niRFSA_IsSelfCalValid(self, vi, self_cal_valid, valid_steps):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_IsSelfCalValid_cfunc is None:
                self.niRFSA_IsSelfCalValid_cfunc = self._get_library_function('niRFSA_IsSelfCalValid')
                self.niRFSA_IsSelfCalValid_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niRFSA_IsSelfCalValid_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_IsSelfCalValid_cfunc(vi, self_cal_valid, valid_steps)

    def niRFSA_LoadConfigurationsFromFile(self, vi, channel_name, file_path):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_LoadConfigurationsFromFile_cfunc is None:
                self.niRFSA_LoadConfigurationsFromFile_cfunc = self._get_library_function('niRFSA_LoadConfigurationsFromFile')
                self.niRFSA_LoadConfigurationsFromFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_LoadConfigurationsFromFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_LoadConfigurationsFromFile_cfunc(vi, channel_name, file_path)

    def niRFSA_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_LockSession_cfunc is None:
                self.niRFSA_LockSession_cfunc = self._get_library_function('niRFSA_LockSession')
                self.niRFSA_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSA_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_LockSession_cfunc(vi, caller_has_lock)

    def niRFSA_PerformThermalCorrection(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_PerformThermalCorrection_cfunc is None:
                self.niRFSA_PerformThermalCorrection_cfunc = self._get_library_function('niRFSA_PerformThermalCorrection')
                self.niRFSA_PerformThermalCorrection_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_PerformThermalCorrection_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_PerformThermalCorrection_cfunc(vi)

    def niRFSA_ReadIqSingleRecordComplexF64(self, vi, channel_list, timeout, data, data_array_size, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ReadIqSingleRecordComplexF64_cfunc is None:
                self.niRFSA_ReadIqSingleRecordComplexF64_cfunc = self._get_library_function('niRFSA_ReadIqSingleRecordComplexF64')
                self.niRFSA_ReadIqSingleRecordComplexF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(NIComplexNumber), ViInt64, ctypes.POINTER(waveform_info.struct_niRFSA_wfmInfo)]  # noqa: F405
                self.niRFSA_ReadIqSingleRecordComplexF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ReadIqSingleRecordComplexF64_cfunc(vi, channel_list, timeout, data, data_array_size, wfm_info)

    def niRFSA_ReadPowerSpectrumF32(self, vi, channel_list, timeout, power_spectrum_data, data_array_size, spectrum_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ReadPowerSpectrumF32_cfunc is None:
                self.niRFSA_ReadPowerSpectrumF32_cfunc = self._get_library_function('niRFSA_ReadPowerSpectrumF32')
                self.niRFSA_ReadPowerSpectrumF32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal32), ViInt32, ctypes.POINTER(spectrum_info_type.struct_niRFSA_spectrumInfo)]  # noqa: F405
                self.niRFSA_ReadPowerSpectrumF32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ReadPowerSpectrumF32_cfunc(vi, channel_list, timeout, power_spectrum_data, data_array_size, spectrum_info)

    def niRFSA_ReadPowerSpectrumF64(self, vi, channel_list, timeout, power_spectrum_data, data_array_size, spectrum_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ReadPowerSpectrumF64_cfunc is None:
                self.niRFSA_ReadPowerSpectrumF64_cfunc = self._get_library_function('niRFSA_ReadPowerSpectrumF64')
                self.niRFSA_ReadPowerSpectrumF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(spectrum_info_type.struct_niRFSA_spectrumInfo)]  # noqa: F405
                self.niRFSA_ReadPowerSpectrumF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ReadPowerSpectrumF64_cfunc(vi, channel_list, timeout, power_spectrum_data, data_array_size, spectrum_info)

    def niRFSA_Reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_Reset_cfunc is None:
                self.niRFSA_Reset_cfunc = self._get_library_function('niRFSA_Reset')
                self.niRFSA_Reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_Reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_Reset_cfunc(vi)

    def niRFSA_ResetAttribute(self, vi, channel_name, attribute_id):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ResetAttribute_cfunc is None:
                self.niRFSA_ResetAttribute_cfunc = self._get_library_function('niRFSA_ResetAttribute')
                self.niRFSA_ResetAttribute_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr]  # noqa: F405
                self.niRFSA_ResetAttribute_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ResetAttribute_cfunc(vi, channel_name, attribute_id)

    def niRFSA_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ResetDevice_cfunc is None:
                self.niRFSA_ResetDevice_cfunc = self._get_library_function('niRFSA_ResetDevice')
                self.niRFSA_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ResetDevice_cfunc(vi)

    def niRFSA_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ResetWithDefaults_cfunc is None:
                self.niRFSA_ResetWithDefaults_cfunc = self._get_library_function('niRFSA_ResetWithDefaults')
                self.niRFSA_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ResetWithDefaults_cfunc(vi)

    def niRFSA_ResetWithOptions(self, vi, steps_to_omit):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ResetWithOptions_cfunc is None:
                self.niRFSA_ResetWithOptions_cfunc = self._get_library_function('niRFSA_ResetWithOptions')
                self.niRFSA_ResetWithOptions_cfunc.argtypes = [ViSession, ViUInt64]  # noqa: F405
                self.niRFSA_ResetWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ResetWithOptions_cfunc(vi, steps_to_omit)

    def niRFSA_RevisionQuery(self, vi, driver_rev, instr_rev):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_RevisionQuery_cfunc is None:
                self.niRFSA_RevisionQuery_cfunc = self._get_library_function('niRFSA_RevisionQuery')
                self.niRFSA_RevisionQuery_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_RevisionQuery_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_RevisionQuery_cfunc(vi, driver_rev, instr_rev)

    def niRFSA_SaveConfigurationsToFile(self, vi, channel_name, file_path):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SaveConfigurationsToFile_cfunc is None:
                self.niRFSA_SaveConfigurationsToFile_cfunc = self._get_library_function('niRFSA_SaveConfigurationsToFile')
                self.niRFSA_SaveConfigurationsToFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_SaveConfigurationsToFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SaveConfigurationsToFile_cfunc(vi, channel_name, file_path)

    def niRFSA_SelfCal(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SelfCal_cfunc is None:
                self.niRFSA_SelfCal_cfunc = self._get_library_function('niRFSA_SelfCal')
                self.niRFSA_SelfCal_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_SelfCal_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SelfCal_cfunc(vi)

    def niRFSA_SelfCalibrate(self, vi, steps_to_omit):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SelfCalibrate_cfunc is None:
                self.niRFSA_SelfCalibrate_cfunc = self._get_library_function('niRFSA_SelfCalibrate')
                self.niRFSA_SelfCalibrate_cfunc.argtypes = [ViSession, ViInt64]  # noqa: F405
                self.niRFSA_SelfCalibrate_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SelfCalibrate_cfunc(vi, steps_to_omit)

    def niRFSA_SelfCalibrateRange(self, vi, steps_to_omit, min_frequency, max_frequency, min_reference_level, max_reference_level):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SelfCalibrateRange_cfunc is None:
                self.niRFSA_SelfCalibrateRange_cfunc = self._get_library_function('niRFSA_SelfCalibrateRange')
                self.niRFSA_SelfCalibrateRange_cfunc.argtypes = [ViSession, ViInt64, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niRFSA_SelfCalibrateRange_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SelfCalibrateRange_cfunc(vi, steps_to_omit, min_frequency, max_frequency, min_reference_level, max_reference_level)

    def niRFSA_SelfTest(self, vi, test_result, test_message):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SelfTest_cfunc is None:
                self.niRFSA_SelfTest_cfunc = self._get_library_function('niRFSA_SelfTest')
                self.niRFSA_SelfTest_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_SelfTest_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SelfTest_cfunc(vi, test_result, test_message)

    def niRFSA_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SendSoftwareEdgeTrigger_cfunc is None:
                self.niRFSA_SendSoftwareEdgeTrigger_cfunc = self._get_library_function('niRFSA_SendSoftwareEdgeTrigger')
                self.niRFSA_SendSoftwareEdgeTrigger_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_SendSoftwareEdgeTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SendSoftwareEdgeTrigger_cfunc(vi, trigger, trigger_identifier)

    def niRFSA_SetAttributeViBoolean(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetAttributeViBoolean_cfunc is None:
                self.niRFSA_SetAttributeViBoolean_cfunc = self._get_library_function('niRFSA_SetAttributeViBoolean')
                self.niRFSA_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niRFSA_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_SetAttributeViInt32(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetAttributeViInt32_cfunc is None:
                self.niRFSA_SetAttributeViInt32_cfunc = self._get_library_function('niRFSA_SetAttributeViInt32')
                self.niRFSA_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niRFSA_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_SetAttributeViInt64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetAttributeViInt64_cfunc is None:
                self.niRFSA_SetAttributeViInt64_cfunc = self._get_library_function('niRFSA_SetAttributeViInt64')
                self.niRFSA_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niRFSA_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetAttributeViInt64_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_SetAttributeViReal64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetAttributeViReal64_cfunc is None:
                self.niRFSA_SetAttributeViReal64_cfunc = self._get_library_function('niRFSA_SetAttributeViReal64')
                self.niRFSA_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niRFSA_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_SetAttributeViSession(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetAttributeViSession_cfunc is None:
                self.niRFSA_SetAttributeViSession_cfunc = self._get_library_function('niRFSA_SetAttributeViSession')
                self.niRFSA_SetAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViSession]  # noqa: F405
                self.niRFSA_SetAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetAttributeViSession_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_SetAttributeViString(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetAttributeViString_cfunc is None:
                self.niRFSA_SetAttributeViString_cfunc = self._get_library_function('niRFSA_SetAttributeViString')
                self.niRFSA_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetAttributeViString_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_SetCalUserDefinedInfo(self, vi, info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetCalUserDefinedInfo_cfunc is None:
                self.niRFSA_SetCalUserDefinedInfo_cfunc = self._get_library_function('niRFSA_SetCalUserDefinedInfo')
                self.niRFSA_SetCalUserDefinedInfo_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_SetCalUserDefinedInfo_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetCalUserDefinedInfo_cfunc(vi, info)

    def niRFSA_SetUserData(self, vi, identifier, buffer_size, data):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetUserData_cfunc is None:
                self.niRFSA_SetUserData_cfunc = self._get_library_function('niRFSA_SetUserData')
                self.niRFSA_SetUserData_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niRFSA_SetUserData_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetUserData_cfunc(vi, identifier, buffer_size, data)

    def niRFSA_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_UnlockSession_cfunc is None:
                self.niRFSA_UnlockSession_cfunc = self._get_library_function('niRFSA_UnlockSession')
                self.niRFSA_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSA_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_UnlockSession_cfunc(vi, caller_has_lock)
