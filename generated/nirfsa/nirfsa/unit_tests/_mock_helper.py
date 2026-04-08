# -*- coding: utf-8 -*-
# This file was generated
import sys  # noqa: F401   - Not all mock_helpers will need this


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['Abort'] = {}
        self._defaults['Abort']['return'] = 0
        self._defaults['CalAdjustCalTonePower'] = {}
        self._defaults['CalAdjustCalTonePower']['return'] = 0
        self._defaults['CalAdjustDeviceGain'] = {}
        self._defaults['CalAdjustDeviceGain']['return'] = 0
        self._defaults['CalAdjustDownconverterGain'] = {}
        self._defaults['CalAdjustDownconverterGain']['return'] = 0
        self._defaults['CalAdjustIfAttenuationCalibration'] = {}
        self._defaults['CalAdjustIfAttenuationCalibration']['return'] = 0
        self._defaults['CalAdjustIfAttenuationCalibration']['attenuatorSettings'] = None
        self._defaults['CalAdjustIfResponseCalibration'] = {}
        self._defaults['CalAdjustIfResponseCalibration']['return'] = 0
        self._defaults['CalAdjustIfResponseCalibration']['measurements'] = None
        self._defaults['CalAdjustLoExportCalibration'] = {}
        self._defaults['CalAdjustLoExportCalibration']['return'] = 0
        self._defaults['CalAdjustLoExportCalibration']['frequencyPoints'] = None
        self._defaults['CalAdjustLoExportCalibration']['loAttenuation'] = None
        self._defaults['CalAdjustRefLevelCalibration'] = {}
        self._defaults['CalAdjustRefLevelCalibration']['return'] = 0
        self._defaults['CalSetTemperature'] = {}
        self._defaults['CalSetTemperature']['return'] = 0
        self._defaults['ChangeExtCalPassword'] = {}
        self._defaults['ChangeExtCalPassword']['return'] = 0
        self._defaults['CheckAcquisitionStatus'] = {}
        self._defaults['CheckAcquisitionStatus']['return'] = 0
        self._defaults['CheckAcquisitionStatus']['isDone'] = None
        self._defaults['ClearError'] = {}
        self._defaults['ClearError']['return'] = 0
        self._defaults['ClearSelfCalibrateRange'] = {}
        self._defaults['ClearSelfCalibrateRange']['return'] = 0
        self._defaults['Close'] = {}
        self._defaults['Close']['return'] = 0
        self._defaults['CloseCalibrationStep'] = {}
        self._defaults['CloseCalibrationStep']['return'] = 0
        self._defaults['CloseExtCal'] = {}
        self._defaults['CloseExtCal']['return'] = 0
        self._defaults['CloseExternalAlignment'] = {}
        self._defaults['CloseExternalAlignment']['return'] = 0
        self._defaults['CloseExternalAlignmentStep'] = {}
        self._defaults['CloseExternalAlignmentStep']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureAcquisitionType'] = {}
        self._defaults['ConfigureAcquisitionType']['return'] = 0
        self._defaults['ConfigureDeembeddingTableInterpolationLinear'] = {}
        self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return'] = 0
        self._defaults['ConfigureDeembeddingTableInterpolationNearest'] = {}
        self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return'] = 0
        self._defaults['ConfigureDeembeddingTableInterpolationSpline'] = {}
        self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return'] = 0
        self._defaults['ConfigureDigitalEdgeAdvanceTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeAdvanceTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeRefTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeRefTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeStartTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] = 0
        self._defaults['ConfigureIqCarrierFrequency'] = {}
        self._defaults['ConfigureIqCarrierFrequency']['return'] = 0
        self._defaults['ConfigureIqPowerEdgeRefTrigger'] = {}
        self._defaults['ConfigureIqPowerEdgeRefTrigger']['return'] = 0
        self._defaults['ConfigureIqRate'] = {}
        self._defaults['ConfigureIqRate']['return'] = 0
        self._defaults['ConfigureNumberOfRecords'] = {}
        self._defaults['ConfigureNumberOfRecords']['return'] = 0
        self._defaults['ConfigureNumberOfSamples'] = {}
        self._defaults['ConfigureNumberOfSamples']['return'] = 0
        self._defaults['ConfigurePxiChassisClk10'] = {}
        self._defaults['ConfigurePxiChassisClk10']['return'] = 0
        self._defaults['ConfigureRefClock'] = {}
        self._defaults['ConfigureRefClock']['return'] = 0
        self._defaults['ConfigureReferenceLevel'] = {}
        self._defaults['ConfigureReferenceLevel']['return'] = 0
        self._defaults['ConfigureResolutionBandwidth'] = {}
        self._defaults['ConfigureResolutionBandwidth']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeAdvanceTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeAdvanceTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeRefTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeRefTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeStartTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeStartTrigger']['return'] = 0
        self._defaults['ConfigureSpectrumFrequencyCenterSpan'] = {}
        self._defaults['ConfigureSpectrumFrequencyCenterSpan']['return'] = 0
        self._defaults['ConfigureSpectrumFrequencyStartStop'] = {}
        self._defaults['ConfigureSpectrumFrequencyStartStop']['return'] = 0
        self._defaults['CreateConfigurationList'] = {}
        self._defaults['CreateConfigurationList']['return'] = 0
        self._defaults['CreateConfigurationList']['listAttributeIDs'] = None
        self._defaults['CreateConfigurationListStep'] = {}
        self._defaults['CreateConfigurationListStep']['return'] = 0
        self._defaults['CreateDeembeddingSparameterTableArray'] = {}
        self._defaults['CreateDeembeddingSparameterTableArray']['return'] = 0
        self._defaults['CreateDeembeddingSparameterTableS2PFile'] = {}
        self._defaults['CreateDeembeddingSparameterTableS2PFile']['return'] = 0
        self._defaults['DeleteAllDeembeddingTables'] = {}
        self._defaults['DeleteAllDeembeddingTables']['return'] = 0
        self._defaults['DeleteConfigurationList'] = {}
        self._defaults['DeleteConfigurationList']['return'] = 0
        self._defaults['DeleteDeembeddingTable'] = {}
        self._defaults['DeleteDeembeddingTable']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['DisableAdvanceTrigger'] = {}
        self._defaults['DisableAdvanceTrigger']['return'] = 0
        self._defaults['DisableRefTrigger'] = {}
        self._defaults['DisableRefTrigger']['return'] = 0
        self._defaults['DisableStartTrigger'] = {}
        self._defaults['DisableStartTrigger']['return'] = 0
        self._defaults['EnableSessionAccess'] = {}
        self._defaults['EnableSessionAccess']['return'] = 0
        self._defaults['ErrorMessage'] = {}
        self._defaults['ErrorMessage']['return'] = 0
        self._defaults['ErrorQuery'] = {}
        self._defaults['ErrorQuery']['return'] = 0
        self._defaults['ErrorQuery']['errorCode'] = None
        self._defaults['ErrorQuery']['errorMessage'] = None
        self._defaults['ExportSignal'] = {}
        self._defaults['ExportSignal']['return'] = 0
        self._defaults['ExtCalStoreBaselineForSelfCalibration'] = {}
        self._defaults['ExtCalStoreBaselineForSelfCalibration']['return'] = 0
        self._defaults['ExternalAlignmentAdjustPreselector'] = {}
        self._defaults['ExternalAlignmentAdjustPreselector']['return'] = 0
        self._defaults['FetchIqMultiRecordComplexF32'] = {}
        self._defaults['FetchIqMultiRecordComplexF32']['return'] = 0
        self._defaults['FetchIqMultiRecordComplexF32']['data'] = None
        self._defaults['FetchIqMultiRecordComplexF32']['wfmInfo'] = None
        self._defaults['FetchIqMultiRecordComplexF64'] = {}
        self._defaults['FetchIqMultiRecordComplexF64']['return'] = 0
        self._defaults['FetchIqMultiRecordComplexF64']['data'] = None
        self._defaults['FetchIqMultiRecordComplexF64']['wfmInfo'] = None
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['value'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['value'] = None
        self._defaults['GetAttributeViInt64'] = {}
        self._defaults['GetAttributeViInt64']['return'] = 0
        self._defaults['GetAttributeViInt64']['value'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['value'] = None
        self._defaults['GetAttributeViSession'] = {}
        self._defaults['GetAttributeViSession']['return'] = 0
        self._defaults['GetAttributeViSession']['value'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['value'] = None
        self._defaults['GetCalUserDefinedInfo'] = {}
        self._defaults['GetCalUserDefinedInfo']['return'] = 0
        self._defaults['GetCalUserDefinedInfo']['info'] = None
        self._defaults['GetCalUserDefinedInfoMaxSize'] = {}
        self._defaults['GetCalUserDefinedInfoMaxSize']['return'] = 0
        self._defaults['GetCalUserDefinedInfoMaxSize']['infoSize'] = None
        self._defaults['GetDeembeddingSparameters'] = {}
        self._defaults['GetDeembeddingSparameters']['return'] = 0
        self._defaults['GetDeembeddingSparameters']['sparameters'] = None
        self._defaults['GetDeembeddingSparameters']['numberOfSparameters'] = None
        self._defaults['GetDeembeddingSparameters']['numberOfPorts'] = None
        self._defaults['GetDeviceResponse'] = {}
        self._defaults['GetDeviceResponse']['return'] = 0
        self._defaults['GetDeviceResponse']['frequencies'] = None
        self._defaults['GetDeviceResponse']['magnitudeResponse'] = None
        self._defaults['GetDeviceResponse']['phaseResponse'] = None
        self._defaults['GetDeviceResponse']['numberOfFrequencies'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['errorDescription'] = None
        self._defaults['GetExtCalLastDateAndTime'] = {}
        self._defaults['GetExtCalLastDateAndTime']['return'] = 0
        self._defaults['GetExtCalLastDateAndTime']['year'] = None
        self._defaults['GetExtCalLastDateAndTime']['month'] = None
        self._defaults['GetExtCalLastDateAndTime']['day'] = None
        self._defaults['GetExtCalLastDateAndTime']['hour'] = None
        self._defaults['GetExtCalLastDateAndTime']['minute'] = None
        self._defaults['GetExtCalLastTemp'] = {}
        self._defaults['GetExtCalLastTemp']['return'] = 0
        self._defaults['GetExtCalLastTemp']['temperature'] = None
        self._defaults['GetExtCalRecommendedInterval'] = {}
        self._defaults['GetExtCalRecommendedInterval']['return'] = 0
        self._defaults['GetExtCalRecommendedInterval']['months'] = None
        self._defaults['GetFetchBacklog'] = {}
        self._defaults['GetFetchBacklog']['return'] = 0
        self._defaults['GetFetchBacklog']['backlog'] = None
        self._defaults['GetFrequencyResponse'] = {}
        self._defaults['GetFrequencyResponse']['return'] = 0
        self._defaults['GetFrequencyResponse']['frequencies'] = None
        self._defaults['GetFrequencyResponse']['magnitudeResponse'] = None
        self._defaults['GetFrequencyResponse']['phaseResponse'] = None
        self._defaults['GetFrequencyResponse']['numberOfFrequencies'] = None
        self._defaults['GetGainReferenceCalBaseline'] = {}
        self._defaults['GetGainReferenceCalBaseline']['return'] = 0
        self._defaults['GetGainReferenceCalBaseline']['gainReferenceCalConstants'] = None
        self._defaults['GetGainReferenceCalBaseline']['numberOfGainReferenceCalConstants'] = None
        self._defaults['GetNormalizationCoefficients'] = {}
        self._defaults['GetNormalizationCoefficients']['return'] = 0
        self._defaults['GetNormalizationCoefficients']['coefficientInfo'] = None
        self._defaults['GetNormalizationCoefficients']['numberOfCoefficientSets'] = None
        self._defaults['GetNumberOfSpectralLines'] = {}
        self._defaults['GetNumberOfSpectralLines']['return'] = 0
        self._defaults['GetNumberOfSpectralLines']['numberOfSpectralLines'] = None
        self._defaults['GetRelayName'] = {}
        self._defaults['GetRelayName']['return'] = 0
        self._defaults['GetRelayName']['name'] = None
        self._defaults['GetRelayOperationsCount'] = {}
        self._defaults['GetRelayOperationsCount']['return'] = 0
        self._defaults['GetRelayOperationsCount']['operationsCount'] = None
        self._defaults['GetScalingCoefficients'] = {}
        self._defaults['GetScalingCoefficients']['return'] = 0
        self._defaults['GetScalingCoefficients']['coefficientInfo'] = None
        self._defaults['GetScalingCoefficients']['numberOfCoefficientSets'] = None
        self._defaults['GetSelfCalLastDateAndTime'] = {}
        self._defaults['GetSelfCalLastDateAndTime']['return'] = 0
        self._defaults['GetSelfCalLastDateAndTime']['year'] = None
        self._defaults['GetSelfCalLastDateAndTime']['month'] = None
        self._defaults['GetSelfCalLastDateAndTime']['day'] = None
        self._defaults['GetSelfCalLastDateAndTime']['hour'] = None
        self._defaults['GetSelfCalLastDateAndTime']['minute'] = None
        self._defaults['GetSelfCalLastTemp'] = {}
        self._defaults['GetSelfCalLastTemp']['return'] = 0
        self._defaults['GetSelfCalLastTemp']['temp'] = None
        self._defaults['GetSpectralInfoForSmt'] = {}
        self._defaults['GetSpectralInfoForSmt']['return'] = 0
        self._defaults['GetSpectralInfoForSmt']['spectrumInfo'] = None
        self._defaults['GetStreamEndpointHandle'] = {}
        self._defaults['GetStreamEndpointHandle']['return'] = 0
        self._defaults['GetStreamEndpointHandle']['writerHandle'] = None
        self._defaults['GetTerminalName'] = {}
        self._defaults['GetTerminalName']['return'] = 0
        self._defaults['GetTerminalName']['terminalName'] = None
        self._defaults['GetUserData'] = {}
        self._defaults['GetUserData']['return'] = 0
        self._defaults['GetUserData']['data'] = None
        self._defaults['GetUserData']['actualDataSize'] = None
        self._defaults['Init'] = {}
        self._defaults['Init']['return'] = 0
        self._defaults['Init']['vi'] = None
        self._defaults['InitExtCal'] = {}
        self._defaults['InitExtCal']['return'] = 0
        self._defaults['InitExtCal']['vi'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['InitializeCalibrationStep'] = {}
        self._defaults['InitializeCalibrationStep']['return'] = 0
        self._defaults['InitializeExternalAlignment'] = {}
        self._defaults['InitializeExternalAlignment']['return'] = 0
        self._defaults['InitializeExternalAlignment']['vi'] = None
        self._defaults['InitializeExternalAlignmentStep'] = {}
        self._defaults['InitializeExternalAlignmentStep']['return'] = 0
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['InvalidateAllAttributes'] = {}
        self._defaults['InvalidateAllAttributes']['return'] = 0
        self._defaults['IsSelfCalValid'] = {}
        self._defaults['IsSelfCalValid']['return'] = 0
        self._defaults['IsSelfCalValid']['selfCalValid'] = None
        self._defaults['IsSelfCalValid']['validSteps'] = None
        self._defaults['LoadConfigurationsFromFile'] = {}
        self._defaults['LoadConfigurationsFromFile']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['PerformThermalCorrection'] = {}
        self._defaults['PerformThermalCorrection']['return'] = 0
        self._defaults['ReadIqSingleRecordComplexF64'] = {}
        self._defaults['ReadIqSingleRecordComplexF64']['return'] = 0
        self._defaults['ReadIqSingleRecordComplexF64']['data'] = None
        self._defaults['ReadIqSingleRecordComplexF64']['wfmInfo'] = None
        self._defaults['ReadPowerSpectrumF32'] = {}
        self._defaults['ReadPowerSpectrumF32']['return'] = 0
        self._defaults['ReadPowerSpectrumF32']['powerSpectrumData'] = None
        self._defaults['ReadPowerSpectrumF32']['spectrumInfo'] = None
        self._defaults['ReadPowerSpectrumF64'] = {}
        self._defaults['ReadPowerSpectrumF64']['return'] = 0
        self._defaults['ReadPowerSpectrumF64']['powerSpectrumData'] = None
        self._defaults['ReadPowerSpectrumF64']['spectrumInfo'] = None
        self._defaults['Reset'] = {}
        self._defaults['Reset']['return'] = 0
        self._defaults['ResetAttribute'] = {}
        self._defaults['ResetAttribute']['return'] = 0
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['ResetWithOptions'] = {}
        self._defaults['ResetWithOptions']['return'] = 0
        self._defaults['RevisionQuery'] = {}
        self._defaults['RevisionQuery']['return'] = 0
        self._defaults['RevisionQuery']['driverRev'] = None
        self._defaults['RevisionQuery']['instrRev'] = None
        self._defaults['SaveConfigurationsToFile'] = {}
        self._defaults['SaveConfigurationsToFile']['return'] = 0
        self._defaults['SelfCal'] = {}
        self._defaults['SelfCal']['return'] = 0
        self._defaults['SelfCalibrate'] = {}
        self._defaults['SelfCalibrate']['return'] = 0
        self._defaults['SelfCalibrateRange'] = {}
        self._defaults['SelfCalibrateRange']['return'] = 0
        self._defaults['SelfTest'] = {}
        self._defaults['SelfTest']['return'] = 0
        self._defaults['SelfTest']['testResult'] = None
        self._defaults['SelfTest']['testMessage'] = None
        self._defaults['SendSoftwareEdgeTrigger'] = {}
        self._defaults['SendSoftwareEdgeTrigger']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViInt64'] = {}
        self._defaults['SetAttributeViInt64']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViSession'] = {}
        self._defaults['SetAttributeViSession']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetCalUserDefinedInfo'] = {}
        self._defaults['SetCalUserDefinedInfo']['return'] = 0
        self._defaults['SetUserData'] = {}
        self._defaults['SetUserData']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niRFSA_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niRFSA_CalAdjustCalTonePower(self, vi, channel_list, measurement):  # noqa: N802
        if self._defaults['CalAdjustCalTonePower']['return'] != 0:
            return self._defaults['CalAdjustCalTonePower']['return']
        return self._defaults['CalAdjustCalTonePower']['return']

    def niRFSA_CalAdjustDeviceGain(self, vi, channel_list, frequency, gain):  # noqa: N802
        if self._defaults['CalAdjustDeviceGain']['return'] != 0:
            return self._defaults['CalAdjustDeviceGain']['return']
        return self._defaults['CalAdjustDeviceGain']['return']

    def niRFSA_CalAdjustDownconverterGain(self, vi, channel_list, frequency, gain):  # noqa: N802
        if self._defaults['CalAdjustDownconverterGain']['return'] != 0:
            return self._defaults['CalAdjustDownconverterGain']['return']
        return self._defaults['CalAdjustDownconverterGain']['return']

    def niRFSA_CalAdjustIfAttenuationCalibration(self, vi, channel_list, if_filter, number_of_attenuators, attenuator_settings, measurement):  # noqa: N802
        if self._defaults['CalAdjustIfAttenuationCalibration']['return'] != 0:
            return self._defaults['CalAdjustIfAttenuationCalibration']['return']
        # attenuator_settings
        if self._defaults['CalAdjustIfAttenuationCalibration']['attenuatorSettings'] is None:
            raise MockFunctionCallError("niRFSA_CalAdjustIfAttenuationCalibration", param='attenuatorSettings')
        if attenuator_settings is not None:
            attenuator_settings.contents.value = self._defaults['CalAdjustIfAttenuationCalibration']['attenuatorSettings']
        return self._defaults['CalAdjustIfAttenuationCalibration']['return']

    def niRFSA_CalAdjustIfResponseCalibration(self, vi, channel_list, if_filter, rf_frequency, band_width, number_of_measurements, measurements):  # noqa: N802
        if self._defaults['CalAdjustIfResponseCalibration']['return'] != 0:
            return self._defaults['CalAdjustIfResponseCalibration']['return']
        # measurements
        if self._defaults['CalAdjustIfResponseCalibration']['measurements'] is None:
            raise MockFunctionCallError("niRFSA_CalAdjustIfResponseCalibration", param='measurements')
        if measurements is not None:
            measurements.contents.value = self._defaults['CalAdjustIfResponseCalibration']['measurements']
        return self._defaults['CalAdjustIfResponseCalibration']['return']

    def niRFSA_CalAdjustLoExportCalibration(self, vi, channel_list, lo_number, number_of_frequency_points, frequency_points, lo_attenuation):  # noqa: N802
        if self._defaults['CalAdjustLoExportCalibration']['return'] != 0:
            return self._defaults['CalAdjustLoExportCalibration']['return']
        # frequency_points
        if self._defaults['CalAdjustLoExportCalibration']['frequencyPoints'] is None:
            raise MockFunctionCallError("niRFSA_CalAdjustLoExportCalibration", param='frequencyPoints')
        if frequency_points is not None:
            frequency_points.contents.value = self._defaults['CalAdjustLoExportCalibration']['frequencyPoints']
        # lo_attenuation
        if self._defaults['CalAdjustLoExportCalibration']['loAttenuation'] is None:
            raise MockFunctionCallError("niRFSA_CalAdjustLoExportCalibration", param='loAttenuation')
        if lo_attenuation is not None:
            lo_attenuation.contents.value = self._defaults['CalAdjustLoExportCalibration']['loAttenuation']
        return self._defaults['CalAdjustLoExportCalibration']['return']

    def niRFSA_CalAdjustRefLevelCalibration(self, vi, channel_list, reference_level_data_type, rf_band, attenuator_table_number, frequency, measurement):  # noqa: N802
        if self._defaults['CalAdjustRefLevelCalibration']['return'] != 0:
            return self._defaults['CalAdjustRefLevelCalibration']['return']
        return self._defaults['CalAdjustRefLevelCalibration']['return']

    def niRFSA_CalSetTemperature(self, vi, channel_list, temperature):  # noqa: N802
        if self._defaults['CalSetTemperature']['return'] != 0:
            return self._defaults['CalSetTemperature']['return']
        return self._defaults['CalSetTemperature']['return']

    def niRFSA_ChangeExtCalPassword(self, vi, old_password, new_password):  # noqa: N802
        if self._defaults['ChangeExtCalPassword']['return'] != 0:
            return self._defaults['ChangeExtCalPassword']['return']
        return self._defaults['ChangeExtCalPassword']['return']

    def niRFSA_CheckAcquisitionStatus(self, vi, is_done):  # noqa: N802
        if self._defaults['CheckAcquisitionStatus']['return'] != 0:
            return self._defaults['CheckAcquisitionStatus']['return']
        # is_done
        if self._defaults['CheckAcquisitionStatus']['isDone'] is None:
            raise MockFunctionCallError("niRFSA_CheckAcquisitionStatus", param='isDone')
        if is_done is not None:
            is_done.contents.value = self._defaults['CheckAcquisitionStatus']['isDone']
        return self._defaults['CheckAcquisitionStatus']['return']

    def niRFSA_ClearError(self, vi):  # noqa: N802
        if self._defaults['ClearError']['return'] != 0:
            return self._defaults['ClearError']['return']
        return self._defaults['ClearError']['return']

    def niRFSA_ClearSelfCalibrateRange(self, vi):  # noqa: N802
        if self._defaults['ClearSelfCalibrateRange']['return'] != 0:
            return self._defaults['ClearSelfCalibrateRange']['return']
        return self._defaults['ClearSelfCalibrateRange']['return']

    def niRFSA_Close(self, vi):  # noqa: N802
        if self._defaults['Close']['return'] != 0:
            return self._defaults['Close']['return']
        return self._defaults['Close']['return']

    def niRFSA_CloseCalibrationStep(self, vi):  # noqa: N802
        if self._defaults['CloseCalibrationStep']['return'] != 0:
            return self._defaults['CloseCalibrationStep']['return']
        return self._defaults['CloseCalibrationStep']['return']

    def niRFSA_CloseExtCal(self, vi, action):  # noqa: N802
        if self._defaults['CloseExtCal']['return'] != 0:
            return self._defaults['CloseExtCal']['return']
        return self._defaults['CloseExtCal']['return']

    def niRFSA_CloseExternalAlignment(self, vi, action):  # noqa: N802
        if self._defaults['CloseExternalAlignment']['return'] != 0:
            return self._defaults['CloseExternalAlignment']['return']
        return self._defaults['CloseExternalAlignment']['return']

    def niRFSA_CloseExternalAlignmentStep(self, vi):  # noqa: N802
        if self._defaults['CloseExternalAlignmentStep']['return'] != 0:
            return self._defaults['CloseExternalAlignmentStep']['return']
        return self._defaults['CloseExternalAlignmentStep']['return']

    def niRFSA_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niRFSA_ConfigureAcquisitionType(self, vi, acquisition_type):  # noqa: N802
        if self._defaults['ConfigureAcquisitionType']['return'] != 0:
            return self._defaults['ConfigureAcquisitionType']['return']
        return self._defaults['ConfigureAcquisitionType']['return']

    def niRFSA_ConfigureDeembeddingTableInterpolationLinear(self, vi, port, table_name, format):  # noqa: N802
        if self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return'] != 0:
            return self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return']
        return self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return']

    def niRFSA_ConfigureDeembeddingTableInterpolationNearest(self, vi, port, table_name):  # noqa: N802
        if self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return'] != 0:
            return self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return']
        return self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return']

    def niRFSA_ConfigureDeembeddingTableInterpolationSpline(self, vi, port, table_name):  # noqa: N802
        if self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return'] != 0:
            return self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return']
        return self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return']

    def niRFSA_ConfigureDigitalEdgeAdvanceTrigger(self, vi, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeAdvanceTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeAdvanceTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeAdvanceTrigger']['return']

    def niRFSA_ConfigureDigitalEdgeRefTrigger(self, vi, source, edge, pretrigger_samples):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeRefTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeRefTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeRefTrigger']['return']

    def niRFSA_ConfigureDigitalEdgeStartTrigger(self, vi, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']

    def niRFSA_ConfigureIqCarrierFrequency(self, vi, channel_list, carrier_frequency):  # noqa: N802
        if self._defaults['ConfigureIqCarrierFrequency']['return'] != 0:
            return self._defaults['ConfigureIqCarrierFrequency']['return']
        return self._defaults['ConfigureIqCarrierFrequency']['return']

    def niRFSA_ConfigureIqPowerEdgeRefTrigger(self, vi, source, level, slope, pretrigger_samples):  # noqa: N802
        if self._defaults['ConfigureIqPowerEdgeRefTrigger']['return'] != 0:
            return self._defaults['ConfigureIqPowerEdgeRefTrigger']['return']
        return self._defaults['ConfigureIqPowerEdgeRefTrigger']['return']

    def niRFSA_ConfigureIqRate(self, vi, channel_list, iq_rate):  # noqa: N802
        if self._defaults['ConfigureIqRate']['return'] != 0:
            return self._defaults['ConfigureIqRate']['return']
        return self._defaults['ConfigureIqRate']['return']

    def niRFSA_ConfigureNumberOfRecords(self, vi, channel_list, number_of_records_is_finite, number_of_records):  # noqa: N802
        if self._defaults['ConfigureNumberOfRecords']['return'] != 0:
            return self._defaults['ConfigureNumberOfRecords']['return']
        return self._defaults['ConfigureNumberOfRecords']['return']

    def niRFSA_ConfigureNumberOfSamples(self, vi, channel_list, number_of_samples_is_finite, samples_per_record):  # noqa: N802
        if self._defaults['ConfigureNumberOfSamples']['return'] != 0:
            return self._defaults['ConfigureNumberOfSamples']['return']
        return self._defaults['ConfigureNumberOfSamples']['return']

    def niRFSA_ConfigurePxiChassisClk10(self, vi, pxi_clk10_source):  # noqa: N802
        if self._defaults['ConfigurePxiChassisClk10']['return'] != 0:
            return self._defaults['ConfigurePxiChassisClk10']['return']
        return self._defaults['ConfigurePxiChassisClk10']['return']

    def niRFSA_ConfigureRefClock(self, vi, clock_source, ref_clock_rate):  # noqa: N802
        if self._defaults['ConfigureRefClock']['return'] != 0:
            return self._defaults['ConfigureRefClock']['return']
        return self._defaults['ConfigureRefClock']['return']

    def niRFSA_ConfigureReferenceLevel(self, vi, channel_list, reference_level):  # noqa: N802
        if self._defaults['ConfigureReferenceLevel']['return'] != 0:
            return self._defaults['ConfigureReferenceLevel']['return']
        return self._defaults['ConfigureReferenceLevel']['return']

    def niRFSA_ConfigureResolutionBandwidth(self, vi, channel_list, resolution_bandwidth):  # noqa: N802
        if self._defaults['ConfigureResolutionBandwidth']['return'] != 0:
            return self._defaults['ConfigureResolutionBandwidth']['return']
        return self._defaults['ConfigureResolutionBandwidth']['return']

    def niRFSA_ConfigureSoftwareEdgeAdvanceTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeAdvanceTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeAdvanceTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeAdvanceTrigger']['return']

    def niRFSA_ConfigureSoftwareEdgeRefTrigger(self, vi, pretrigger_samples):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeRefTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeRefTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeRefTrigger']['return']

    def niRFSA_ConfigureSoftwareEdgeStartTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeStartTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeStartTrigger']['return']

    def niRFSA_ConfigureSpectrumFrequencyCenterSpan(self, vi, channel_list, center_frequency, span):  # noqa: N802
        if self._defaults['ConfigureSpectrumFrequencyCenterSpan']['return'] != 0:
            return self._defaults['ConfigureSpectrumFrequencyCenterSpan']['return']
        return self._defaults['ConfigureSpectrumFrequencyCenterSpan']['return']

    def niRFSA_ConfigureSpectrumFrequencyStartStop(self, vi, channel_list, start_frequency, stop_frequency):  # noqa: N802
        if self._defaults['ConfigureSpectrumFrequencyStartStop']['return'] != 0:
            return self._defaults['ConfigureSpectrumFrequencyStartStop']['return']
        return self._defaults['ConfigureSpectrumFrequencyStartStop']['return']

    def niRFSA_CreateConfigurationList(self, vi, list_name, number_of_list_attributes, list_attribute_i_ds, set_as_active_list):  # noqa: N802
        if self._defaults['CreateConfigurationList']['return'] != 0:
            return self._defaults['CreateConfigurationList']['return']
        # list_attribute_i_ds
        if self._defaults['CreateConfigurationList']['listAttributeIDs'] is None:
            raise MockFunctionCallError("niRFSA_CreateConfigurationList", param='listAttributeIDs')
        if list_attribute_i_ds is not None:
            list_attribute_i_ds.contents.value = self._defaults['CreateConfigurationList']['listAttributeIDs']
        return self._defaults['CreateConfigurationList']['return']

    def niRFSA_CreateConfigurationListStep(self, vi, set_as_active_step):  # noqa: N802
        if self._defaults['CreateConfigurationListStep']['return'] != 0:
            return self._defaults['CreateConfigurationListStep']['return']
        return self._defaults['CreateConfigurationListStep']['return']

    def niRFSA_CreateDeembeddingSparameterTableArray(self, vi, port, table_name, frequencies, frequencies_size, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation):  # noqa: N802
        if self._defaults['CreateDeembeddingSparameterTableArray']['return'] != 0:
            return self._defaults['CreateDeembeddingSparameterTableArray']['return']
        return self._defaults['CreateDeembeddingSparameterTableArray']['return']

    def niRFSA_CreateDeembeddingSparameterTableS2PFile(self, vi, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        if self._defaults['CreateDeembeddingSparameterTableS2PFile']['return'] != 0:
            return self._defaults['CreateDeembeddingSparameterTableS2PFile']['return']
        return self._defaults['CreateDeembeddingSparameterTableS2PFile']['return']

    def niRFSA_DeleteAllDeembeddingTables(self, vi):  # noqa: N802
        if self._defaults['DeleteAllDeembeddingTables']['return'] != 0:
            return self._defaults['DeleteAllDeembeddingTables']['return']
        return self._defaults['DeleteAllDeembeddingTables']['return']

    def niRFSA_DeleteConfigurationList(self, vi, list_name):  # noqa: N802
        if self._defaults['DeleteConfigurationList']['return'] != 0:
            return self._defaults['DeleteConfigurationList']['return']
        return self._defaults['DeleteConfigurationList']['return']

    def niRFSA_DeleteDeembeddingTable(self, vi, port, table_name):  # noqa: N802
        if self._defaults['DeleteDeembeddingTable']['return'] != 0:
            return self._defaults['DeleteDeembeddingTable']['return']
        return self._defaults['DeleteDeembeddingTable']['return']

    def niRFSA_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niRFSA_DisableAdvanceTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableAdvanceTrigger']['return'] != 0:
            return self._defaults['DisableAdvanceTrigger']['return']
        return self._defaults['DisableAdvanceTrigger']['return']

    def niRFSA_DisableRefTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableRefTrigger']['return'] != 0:
            return self._defaults['DisableRefTrigger']['return']
        return self._defaults['DisableRefTrigger']['return']

    def niRFSA_DisableStartTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableStartTrigger']['return'] != 0:
            return self._defaults['DisableStartTrigger']['return']
        return self._defaults['DisableStartTrigger']['return']

    def niRFSA_EnableSessionAccess(self, vi, enable):  # noqa: N802
        if self._defaults['EnableSessionAccess']['return'] != 0:
            return self._defaults['EnableSessionAccess']['return']
        return self._defaults['EnableSessionAccess']['return']

    def niRFSA_ErrorMessage(self, vi, status_code, error_message):  # noqa: N802
        if self._defaults['ErrorMessage']['return'] != 0:
            return self._defaults['ErrorMessage']['return']
        return self._defaults['ErrorMessage']['return']

    def niRFSA_ErrorQuery(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['ErrorQuery']['return'] != 0:
            return self._defaults['ErrorQuery']['return']
        # error_code
        if self._defaults['ErrorQuery']['errorCode'] is None:
            raise MockFunctionCallError("niRFSA_ErrorQuery", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['ErrorQuery']['errorCode']
        # error_message
        if self._defaults['ErrorQuery']['errorMessage'] is None:
            raise MockFunctionCallError("niRFSA_ErrorQuery", param='errorMessage')
        test_value = self._defaults['ErrorQuery']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['ErrorQuery']['return']

    def niRFSA_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        if self._defaults['ExportSignal']['return'] != 0:
            return self._defaults['ExportSignal']['return']
        return self._defaults['ExportSignal']['return']

    def niRFSA_ExtCalStoreBaselineForSelfCalibration(self, vi, password, self_calibration_step):  # noqa: N802
        if self._defaults['ExtCalStoreBaselineForSelfCalibration']['return'] != 0:
            return self._defaults['ExtCalStoreBaselineForSelfCalibration']['return']
        return self._defaults['ExtCalStoreBaselineForSelfCalibration']['return']

    def niRFSA_ExternalAlignmentAdjustPreselector(self, vi, number_of_coefficients, coefficients):  # noqa: N802
        if self._defaults['ExternalAlignmentAdjustPreselector']['return'] != 0:
            return self._defaults['ExternalAlignmentAdjustPreselector']['return']
        return self._defaults['ExternalAlignmentAdjustPreselector']['return']

    def niRFSA_FetchIqMultiRecordComplexF32(self, vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, data, wfm_info):  # noqa: N802
        if self._defaults['FetchIqMultiRecordComplexF32']['return'] != 0:
            return self._defaults['FetchIqMultiRecordComplexF32']['return']
        # data
        if self._defaults['FetchIqMultiRecordComplexF32']['data'] is None:
            raise MockFunctionCallError("niRFSA_FetchIqMultiRecordComplexF32", param='data')
        if data is not None:
            data.contents.value = self._defaults['FetchIqMultiRecordComplexF32']['data']
        # wfm_info
        if self._defaults['FetchIqMultiRecordComplexF32']['wfmInfo'] is None:
            raise MockFunctionCallError("niRFSA_FetchIqMultiRecordComplexF32", param='wfmInfo')
        for field in self._defaults['FetchIqMultiRecordComplexF32']['wfm_info']._fields_:
            field_name = field[0]
            setattr(wfm_info.contents, field_name, getattr(self._defaults['FetchIqMultiRecordComplexF32']['wfm_info'], field_name))
        return self._defaults['FetchIqMultiRecordComplexF32']['return']

    def niRFSA_FetchIqMultiRecordComplexF64(self, vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, data, wfm_info):  # noqa: N802
        if self._defaults['FetchIqMultiRecordComplexF64']['return'] != 0:
            return self._defaults['FetchIqMultiRecordComplexF64']['return']
        # data
        if self._defaults['FetchIqMultiRecordComplexF64']['data'] is None:
            raise MockFunctionCallError("niRFSA_FetchIqMultiRecordComplexF64", param='data')
        if data is not None:
            data.contents.value = self._defaults['FetchIqMultiRecordComplexF64']['data']
        # wfm_info
        if self._defaults['FetchIqMultiRecordComplexF64']['wfmInfo'] is None:
            raise MockFunctionCallError("niRFSA_FetchIqMultiRecordComplexF64", param='wfmInfo')
        for field in self._defaults['FetchIqMultiRecordComplexF64']['wfm_info']._fields_:
            field_name = field[0]
            setattr(wfm_info.contents, field_name, getattr(self._defaults['FetchIqMultiRecordComplexF64']['wfm_info'], field_name))
        return self._defaults['FetchIqMultiRecordComplexF64']['return']

    def niRFSA_GetAttributeViBoolean(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # value
        if self._defaults['GetAttributeViBoolean']['value'] is None:
            raise MockFunctionCallError("niRFSA_GetAttributeViBoolean", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViBoolean']['value']
        return self._defaults['GetAttributeViBoolean']['return']

    def niRFSA_GetAttributeViInt32(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # value
        if self._defaults['GetAttributeViInt32']['value'] is None:
            raise MockFunctionCallError("niRFSA_GetAttributeViInt32", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt32']['value']
        return self._defaults['GetAttributeViInt32']['return']

    def niRFSA_GetAttributeViInt64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        # value
        if self._defaults['GetAttributeViInt64']['value'] is None:
            raise MockFunctionCallError("niRFSA_GetAttributeViInt64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt64']['value']
        return self._defaults['GetAttributeViInt64']['return']

    def niRFSA_GetAttributeViReal64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # value
        if self._defaults['GetAttributeViReal64']['value'] is None:
            raise MockFunctionCallError("niRFSA_GetAttributeViReal64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViReal64']['value']
        return self._defaults['GetAttributeViReal64']['return']

    def niRFSA_GetAttributeViSession(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViSession']['return'] != 0:
            return self._defaults['GetAttributeViSession']['return']
        # value
        if self._defaults['GetAttributeViSession']['value'] is None:
            raise MockFunctionCallError("niRFSA_GetAttributeViSession", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViSession']['value']
        return self._defaults['GetAttributeViSession']['return']

    def niRFSA_GetAttributeViString(self, vi, channel_name, attribute_id, buf_size, value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        # value
        if self._defaults['GetAttributeViString']['value'] is None:
            raise MockFunctionCallError("niRFSA_GetAttributeViString", param='value')
        if buf_size.value == 0:
            return len(self._defaults['GetAttributeViString']['value'])
        value.value = self._defaults['GetAttributeViString']['value'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niRFSA_GetCalUserDefinedInfo(self, vi, info):  # noqa: N802
        if self._defaults['GetCalUserDefinedInfo']['return'] != 0:
            return self._defaults['GetCalUserDefinedInfo']['return']
        # info
        if self._defaults['GetCalUserDefinedInfo']['info'] is None:
            raise MockFunctionCallError("niRFSA_GetCalUserDefinedInfo", param='info')
        test_value = self._defaults['GetCalUserDefinedInfo']['info']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(info) >= len(test_value)
        for i in range(len(test_value)):
            info[i] = test_value[i]
        return self._defaults['GetCalUserDefinedInfo']['return']

    def niRFSA_GetCalUserDefinedInfoMaxSize(self, vi, info_size):  # noqa: N802
        if self._defaults['GetCalUserDefinedInfoMaxSize']['return'] != 0:
            return self._defaults['GetCalUserDefinedInfoMaxSize']['return']
        # info_size
        if self._defaults['GetCalUserDefinedInfoMaxSize']['infoSize'] is None:
            raise MockFunctionCallError("niRFSA_GetCalUserDefinedInfoMaxSize", param='infoSize')
        if info_size is not None:
            info_size.contents.value = self._defaults['GetCalUserDefinedInfoMaxSize']['infoSize']
        return self._defaults['GetCalUserDefinedInfoMaxSize']['return']

    def niRFSA_GetDeembeddingSparameters(self, vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports):  # noqa: N802
        if self._defaults['GetDeembeddingSparameters']['return'] != 0:
            return self._defaults['GetDeembeddingSparameters']['return']
        # sparameters
        if self._defaults['GetDeembeddingSparameters']['sparameters'] is None:
            raise MockFunctionCallError("niRFSA_GetDeembeddingSparameters", param='sparameters')
        test_value = self._defaults['GetDeembeddingSparameters']['sparameters']
        try:
            sparameters_ref = sparameters.contents
        except AttributeError:
            sparameters_ref = sparameters
        assert len(sparameters_ref) >= len(test_value)
        for i in range(len(test_value)):
            sparameters_ref[i] = test_value[i]
        # number_of_sparameters
        if self._defaults['GetDeembeddingSparameters']['numberOfSparameters'] is None:
            raise MockFunctionCallError("niRFSA_GetDeembeddingSparameters", param='numberOfSparameters')
        if number_of_sparameters is not None:
            number_of_sparameters.contents.value = self._defaults['GetDeembeddingSparameters']['numberOfSparameters']
        # number_of_ports
        if self._defaults['GetDeembeddingSparameters']['numberOfPorts'] is None:
            raise MockFunctionCallError("niRFSA_GetDeembeddingSparameters", param='numberOfPorts')
        if number_of_ports is not None:
            number_of_ports.contents.value = self._defaults['GetDeembeddingSparameters']['numberOfPorts']
        return self._defaults['GetDeembeddingSparameters']['return']

    def niRFSA_GetDeviceResponse(self, vi, channel_list, response_type, buffer_size, frequencies, magnitude_response, phase_response, number_of_frequencies):  # noqa: N802
        if self._defaults['GetDeviceResponse']['return'] != 0:
            return self._defaults['GetDeviceResponse']['return']
        # frequencies
        if self._defaults['GetDeviceResponse']['frequencies'] is None:
            raise MockFunctionCallError("niRFSA_GetDeviceResponse", param='frequencies')
        test_value = self._defaults['GetDeviceResponse']['frequencies']
        try:
            frequencies_ref = frequencies.contents
        except AttributeError:
            frequencies_ref = frequencies
        assert len(frequencies_ref) >= len(test_value)
        for i in range(len(test_value)):
            frequencies_ref[i] = test_value[i]
        # magnitude_response
        if self._defaults['GetDeviceResponse']['magnitudeResponse'] is None:
            raise MockFunctionCallError("niRFSA_GetDeviceResponse", param='magnitudeResponse')
        test_value = self._defaults['GetDeviceResponse']['magnitudeResponse']
        try:
            magnitude_response_ref = magnitude_response.contents
        except AttributeError:
            magnitude_response_ref = magnitude_response
        assert len(magnitude_response_ref) >= len(test_value)
        for i in range(len(test_value)):
            magnitude_response_ref[i] = test_value[i]
        # phase_response
        if self._defaults['GetDeviceResponse']['phaseResponse'] is None:
            raise MockFunctionCallError("niRFSA_GetDeviceResponse", param='phaseResponse')
        test_value = self._defaults['GetDeviceResponse']['phaseResponse']
        try:
            phase_response_ref = phase_response.contents
        except AttributeError:
            phase_response_ref = phase_response
        assert len(phase_response_ref) >= len(test_value)
        for i in range(len(test_value)):
            phase_response_ref[i] = test_value[i]
        # number_of_frequencies
        if self._defaults['GetDeviceResponse']['numberOfFrequencies'] is None:
            raise MockFunctionCallError("niRFSA_GetDeviceResponse", param='numberOfFrequencies')
        if number_of_frequencies is not None:
            number_of_frequencies.contents.value = self._defaults['GetDeviceResponse']['numberOfFrequencies']
        return self._defaults['GetDeviceResponse']['return']

    def niRFSA_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niRFSA_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        # error_description
        if self._defaults['GetError']['errorDescription'] is None:
            raise MockFunctionCallError("niRFSA_GetError", param='errorDescription')
        if error_description_buffer_size.value == 0:
            return len(self._defaults['GetError']['errorDescription'])
        error_description.value = self._defaults['GetError']['errorDescription'].encode('ascii')
        return self._defaults['GetError']['return']

    def niRFSA_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetExtCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetExtCalLastDateAndTime']['return']
        # year
        if self._defaults['GetExtCalLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetExtCalLastDateAndTime']['year']
        # month
        if self._defaults['GetExtCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetExtCalLastDateAndTime']['month']
        # day
        if self._defaults['GetExtCalLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetExtCalLastDateAndTime']['day']
        # hour
        if self._defaults['GetExtCalLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetExtCalLastDateAndTime']['hour']
        # minute
        if self._defaults['GetExtCalLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetExtCalLastDateAndTime']['minute']
        return self._defaults['GetExtCalLastDateAndTime']['return']

    def niRFSA_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetExtCalLastTemp']['return'] != 0:
            return self._defaults['GetExtCalLastTemp']['return']
        # temperature
        if self._defaults['GetExtCalLastTemp']['temperature'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastTemp", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetExtCalLastTemp']['temperature']
        return self._defaults['GetExtCalLastTemp']['return']

    def niRFSA_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        if self._defaults['GetExtCalRecommendedInterval']['return'] != 0:
            return self._defaults['GetExtCalRecommendedInterval']['return']
        # months
        if self._defaults['GetExtCalRecommendedInterval']['months'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalRecommendedInterval", param='months')
        if months is not None:
            months.contents.value = self._defaults['GetExtCalRecommendedInterval']['months']
        return self._defaults['GetExtCalRecommendedInterval']['return']

    def niRFSA_GetFetchBacklog(self, vi, channel_list, record_number, backlog):  # noqa: N802
        if self._defaults['GetFetchBacklog']['return'] != 0:
            return self._defaults['GetFetchBacklog']['return']
        # backlog
        if self._defaults['GetFetchBacklog']['backlog'] is None:
            raise MockFunctionCallError("niRFSA_GetFetchBacklog", param='backlog')
        if backlog is not None:
            backlog.contents.value = self._defaults['GetFetchBacklog']['backlog']
        return self._defaults['GetFetchBacklog']['return']

    def niRFSA_GetFrequencyResponse(self, vi, channel_list, buffer_size, frequencies, magnitude_response, phase_response, number_of_frequencies):  # noqa: N802
        if self._defaults['GetFrequencyResponse']['return'] != 0:
            return self._defaults['GetFrequencyResponse']['return']
        # frequencies
        if self._defaults['GetFrequencyResponse']['frequencies'] is None:
            raise MockFunctionCallError("niRFSA_GetFrequencyResponse", param='frequencies')
        test_value = self._defaults['GetFrequencyResponse']['frequencies']
        try:
            frequencies_ref = frequencies.contents
        except AttributeError:
            frequencies_ref = frequencies
        assert len(frequencies_ref) >= len(test_value)
        for i in range(len(test_value)):
            frequencies_ref[i] = test_value[i]
        # magnitude_response
        if self._defaults['GetFrequencyResponse']['magnitudeResponse'] is None:
            raise MockFunctionCallError("niRFSA_GetFrequencyResponse", param='magnitudeResponse')
        test_value = self._defaults['GetFrequencyResponse']['magnitudeResponse']
        try:
            magnitude_response_ref = magnitude_response.contents
        except AttributeError:
            magnitude_response_ref = magnitude_response
        assert len(magnitude_response_ref) >= len(test_value)
        for i in range(len(test_value)):
            magnitude_response_ref[i] = test_value[i]
        # phase_response
        if self._defaults['GetFrequencyResponse']['phaseResponse'] is None:
            raise MockFunctionCallError("niRFSA_GetFrequencyResponse", param='phaseResponse')
        test_value = self._defaults['GetFrequencyResponse']['phaseResponse']
        try:
            phase_response_ref = phase_response.contents
        except AttributeError:
            phase_response_ref = phase_response
        assert len(phase_response_ref) >= len(test_value)
        for i in range(len(test_value)):
            phase_response_ref[i] = test_value[i]
        # number_of_frequencies
        if self._defaults['GetFrequencyResponse']['numberOfFrequencies'] is None:
            raise MockFunctionCallError("niRFSA_GetFrequencyResponse", param='numberOfFrequencies')
        if number_of_frequencies is not None:
            number_of_frequencies.contents.value = self._defaults['GetFrequencyResponse']['numberOfFrequencies']
        return self._defaults['GetFrequencyResponse']['return']

    def niRFSA_GetGainReferenceCalBaseline(self, vi, buffer_size, gain_reference_cal_constants, number_of_gain_reference_cal_constants):  # noqa: N802
        if self._defaults['GetGainReferenceCalBaseline']['return'] != 0:
            return self._defaults['GetGainReferenceCalBaseline']['return']
        # gain_reference_cal_constants
        if self._defaults['GetGainReferenceCalBaseline']['gainReferenceCalConstants'] is None:
            raise MockFunctionCallError("niRFSA_GetGainReferenceCalBaseline", param='gainReferenceCalConstants')
        test_value = self._defaults['GetGainReferenceCalBaseline']['gainReferenceCalConstants']
        try:
            gain_reference_cal_constants_ref = gain_reference_cal_constants.contents
        except AttributeError:
            gain_reference_cal_constants_ref = gain_reference_cal_constants
        assert len(gain_reference_cal_constants_ref) >= len(test_value)
        for i in range(len(test_value)):
            gain_reference_cal_constants_ref[i] = test_value[i]
        # number_of_gain_reference_cal_constants
        if self._defaults['GetGainReferenceCalBaseline']['numberOfGainReferenceCalConstants'] is None:
            raise MockFunctionCallError("niRFSA_GetGainReferenceCalBaseline", param='numberOfGainReferenceCalConstants')
        if number_of_gain_reference_cal_constants is not None:
            number_of_gain_reference_cal_constants.contents.value = self._defaults['GetGainReferenceCalBaseline']['numberOfGainReferenceCalConstants']
        return self._defaults['GetGainReferenceCalBaseline']['return']

    def niRFSA_GetNormalizationCoefficients(self, vi, channel_list, array_size, coefficient_info, number_of_coefficient_sets):  # noqa: N802
        if self._defaults['GetNormalizationCoefficients']['return'] != 0:
            return self._defaults['GetNormalizationCoefficients']['return']
        # coefficient_info
        if self._defaults['GetNormalizationCoefficients']['coefficientInfo'] is None:
            raise MockFunctionCallError("niRFSA_GetNormalizationCoefficients", param='coefficientInfo')
        test_value = self._defaults['GetNormalizationCoefficients']['coefficientInfo']
        try:
            coefficient_info_ref = coefficient_info.contents
        except AttributeError:
            coefficient_info_ref = coefficient_info
        assert len(coefficient_info_ref) >= len(test_value)
        for i in range(len(test_value)):
            coefficient_info_ref[i] = test_value[i]
        # number_of_coefficient_sets
        if self._defaults['GetNormalizationCoefficients']['numberOfCoefficientSets'] is None:
            raise MockFunctionCallError("niRFSA_GetNormalizationCoefficients", param='numberOfCoefficientSets')
        if number_of_coefficient_sets is not None:
            number_of_coefficient_sets.contents.value = self._defaults['GetNormalizationCoefficients']['numberOfCoefficientSets']
        return self._defaults['GetNormalizationCoefficients']['return']

    def niRFSA_GetNumberOfSpectralLines(self, vi, channel_list, number_of_spectral_lines):  # noqa: N802
        if self._defaults['GetNumberOfSpectralLines']['return'] != 0:
            return self._defaults['GetNumberOfSpectralLines']['return']
        # number_of_spectral_lines
        if self._defaults['GetNumberOfSpectralLines']['numberOfSpectralLines'] is None:
            raise MockFunctionCallError("niRFSA_GetNumberOfSpectralLines", param='numberOfSpectralLines')
        if number_of_spectral_lines is not None:
            number_of_spectral_lines.contents.value = self._defaults['GetNumberOfSpectralLines']['numberOfSpectralLines']
        return self._defaults['GetNumberOfSpectralLines']['return']

    def niRFSA_GetRelayName(self, vi, channel_list, index, name, buffer_size):  # noqa: N802
        if self._defaults['GetRelayName']['return'] != 0:
            return self._defaults['GetRelayName']['return']
        # name
        if self._defaults['GetRelayName']['name'] is None:
            raise MockFunctionCallError("niRFSA_GetRelayName", param='name')
        if buffer_size.value == 0:
            return len(self._defaults['GetRelayName']['name'])
        name.value = self._defaults['GetRelayName']['name'].encode('ascii')
        return self._defaults['GetRelayName']['return']

    def niRFSA_GetRelayOperationsCount(self, vi, channel_list, operations_count, buffer_size):  # noqa: N802
        if self._defaults['GetRelayOperationsCount']['return'] != 0:
            return self._defaults['GetRelayOperationsCount']['return']
        # operations_count
        if self._defaults['GetRelayOperationsCount']['operationsCount'] is None:
            raise MockFunctionCallError("niRFSA_GetRelayOperationsCount", param='operationsCount')
        if buffer_size.value == 0:
            return len(self._defaults['GetRelayOperationsCount']['operationsCount'])
        try:
            operations_count_ref = operations_count.contents
        except AttributeError:
            operations_count_ref = operations_count
        for i in range(len(self._defaults['GetRelayOperationsCount']['operationsCount'])):
            operations_count_ref[i] = self._defaults['GetRelayOperationsCount']['operationsCount'][i]
        return self._defaults['GetRelayOperationsCount']['return']

    def niRFSA_GetScalingCoefficients(self, vi, channel_list, array_size, coefficient_info, number_of_coefficient_sets):  # noqa: N802
        if self._defaults['GetScalingCoefficients']['return'] != 0:
            return self._defaults['GetScalingCoefficients']['return']
        # coefficient_info
        if self._defaults['GetScalingCoefficients']['coefficientInfo'] is None:
            raise MockFunctionCallError("niRFSA_GetScalingCoefficients", param='coefficientInfo')
        test_value = self._defaults['GetScalingCoefficients']['coefficientInfo']
        try:
            coefficient_info_ref = coefficient_info.contents
        except AttributeError:
            coefficient_info_ref = coefficient_info
        assert len(coefficient_info_ref) >= len(test_value)
        for i in range(len(test_value)):
            coefficient_info_ref[i] = test_value[i]
        # number_of_coefficient_sets
        if self._defaults['GetScalingCoefficients']['numberOfCoefficientSets'] is None:
            raise MockFunctionCallError("niRFSA_GetScalingCoefficients", param='numberOfCoefficientSets')
        if number_of_coefficient_sets is not None:
            number_of_coefficient_sets.contents.value = self._defaults['GetScalingCoefficients']['numberOfCoefficientSets']
        return self._defaults['GetScalingCoefficients']['return']

    def niRFSA_GetSelfCalLastDateAndTime(self, vi, self_calibration_step, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalLastDateAndTime']['return']
        # year
        if self._defaults['GetSelfCalLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetSelfCalLastDateAndTime']['year']
        # month
        if self._defaults['GetSelfCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetSelfCalLastDateAndTime']['month']
        # day
        if self._defaults['GetSelfCalLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetSelfCalLastDateAndTime']['day']
        # hour
        if self._defaults['GetSelfCalLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetSelfCalLastDateAndTime']['hour']
        # minute
        if self._defaults['GetSelfCalLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetSelfCalLastDateAndTime']['minute']
        return self._defaults['GetSelfCalLastDateAndTime']['return']

    def niRFSA_GetSelfCalLastTemp(self, vi, self_calibration_step, temp):  # noqa: N802
        if self._defaults['GetSelfCalLastTemp']['return'] != 0:
            return self._defaults['GetSelfCalLastTemp']['return']
        # temp
        if self._defaults['GetSelfCalLastTemp']['temp'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastTemp", param='temp')
        if temp is not None:
            temp.contents.value = self._defaults['GetSelfCalLastTemp']['temp']
        return self._defaults['GetSelfCalLastTemp']['return']

    def niRFSA_GetSpectralInfoForSmt(self, vi, spectrum_info):  # noqa: N802
        if self._defaults['GetSpectralInfoForSmt']['return'] != 0:
            return self._defaults['GetSpectralInfoForSmt']['return']
        # spectrum_info
        if self._defaults['GetSpectralInfoForSmt']['spectrumInfo'] is None:
            raise MockFunctionCallError("niRFSA_GetSpectralInfoForSmt", param='spectrumInfo')
        for field in self._defaults['GetSpectralInfoForSmt']['spectrum_info']._fields_:
            field_name = field[0]
            setattr(spectrum_info.contents, field_name, getattr(self._defaults['GetSpectralInfoForSmt']['spectrum_info'], field_name))
        return self._defaults['GetSpectralInfoForSmt']['return']

    def niRFSA_GetStreamEndpointHandle(self, vi, stream_endpoint, writer_handle):  # noqa: N802
        if self._defaults['GetStreamEndpointHandle']['return'] != 0:
            return self._defaults['GetStreamEndpointHandle']['return']
        # writer_handle
        if self._defaults['GetStreamEndpointHandle']['writerHandle'] is None:
            raise MockFunctionCallError("niRFSA_GetStreamEndpointHandle", param='writerHandle')
        if writer_handle is not None:
            writer_handle.contents.value = self._defaults['GetStreamEndpointHandle']['writerHandle']
        return self._defaults['GetStreamEndpointHandle']['return']

    def niRFSA_GetTerminalName(self, vi, signal, signal_identifier, buffer_size, terminal_name):  # noqa: N802
        if self._defaults['GetTerminalName']['return'] != 0:
            return self._defaults['GetTerminalName']['return']
        # terminal_name
        if self._defaults['GetTerminalName']['terminalName'] is None:
            raise MockFunctionCallError("niRFSA_GetTerminalName", param='terminalName')
        if buffer_size.value == 0:
            return len(self._defaults['GetTerminalName']['terminalName'])
        terminal_name.value = self._defaults['GetTerminalName']['terminalName'].encode('ascii')
        return self._defaults['GetTerminalName']['return']

    def niRFSA_GetUserData(self, vi, identifier, buffer_size, data, actual_data_size):  # noqa: N802
        if self._defaults['GetUserData']['return'] != 0:
            return self._defaults['GetUserData']['return']
        # data
        if self._defaults['GetUserData']['data'] is None:
            raise MockFunctionCallError("niRFSA_GetUserData", param='data')
        test_value = self._defaults['GetUserData']['data']
        try:
            data_ref = data.contents
        except AttributeError:
            data_ref = data
        assert len(data_ref) >= len(test_value)
        for i in range(len(test_value)):
            data_ref[i] = test_value[i]
        # actual_data_size
        if self._defaults['GetUserData']['actualDataSize'] is None:
            raise MockFunctionCallError("niRFSA_GetUserData", param='actualDataSize')
        if actual_data_size is not None:
            actual_data_size.contents.value = self._defaults['GetUserData']['actualDataSize']
        return self._defaults['GetUserData']['return']

    def niRFSA_Init(self, resource_name, id_query, reset, vi):  # noqa: N802
        if self._defaults['Init']['return'] != 0:
            return self._defaults['Init']['return']
        # vi
        if self._defaults['Init']['vi'] is None:
            raise MockFunctionCallError("niRFSA_Init", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['Init']['vi']
        return self._defaults['Init']['return']

    def niRFSA_InitExtCal(self, resource_name, password, option_string, vi):  # noqa: N802
        if self._defaults['InitExtCal']['return'] != 0:
            return self._defaults['InitExtCal']['return']
        # vi
        if self._defaults['InitExtCal']['vi'] is None:
            raise MockFunctionCallError("niRFSA_InitExtCal", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitExtCal']['vi']
        return self._defaults['InitExtCal']['return']

    def niRFSA_InitWithOptions(self, resource_name, id_query, reset, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # vi
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niRFSA_InitWithOptions", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niRFSA_InitializeCalibrationStep(self, vi, calibration_step):  # noqa: N802
        if self._defaults['InitializeCalibrationStep']['return'] != 0:
            return self._defaults['InitializeCalibrationStep']['return']
        return self._defaults['InitializeCalibrationStep']['return']

    def niRFSA_InitializeExternalAlignment(self, resource_name, option_string, vi):  # noqa: N802
        if self._defaults['InitializeExternalAlignment']['return'] != 0:
            return self._defaults['InitializeExternalAlignment']['return']
        # vi
        if self._defaults['InitializeExternalAlignment']['vi'] is None:
            raise MockFunctionCallError("niRFSA_InitializeExternalAlignment", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitializeExternalAlignment']['vi']
        return self._defaults['InitializeExternalAlignment']['return']

    def niRFSA_InitializeExternalAlignmentStep(self, vi, external_alignment_step):  # noqa: N802
        if self._defaults['InitializeExternalAlignmentStep']['return'] != 0:
            return self._defaults['InitializeExternalAlignmentStep']['return']
        return self._defaults['InitializeExternalAlignmentStep']['return']

    def niRFSA_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niRFSA_InvalidateAllAttributes(self, vi):  # noqa: N802
        if self._defaults['InvalidateAllAttributes']['return'] != 0:
            return self._defaults['InvalidateAllAttributes']['return']
        return self._defaults['InvalidateAllAttributes']['return']

    def niRFSA_IsSelfCalValid(self, vi, self_cal_valid, valid_steps):  # noqa: N802
        if self._defaults['IsSelfCalValid']['return'] != 0:
            return self._defaults['IsSelfCalValid']['return']
        # self_cal_valid
        if self._defaults['IsSelfCalValid']['selfCalValid'] is None:
            raise MockFunctionCallError("niRFSA_IsSelfCalValid", param='selfCalValid')
        if self_cal_valid is not None:
            self_cal_valid.contents.value = self._defaults['IsSelfCalValid']['selfCalValid']
        # valid_steps
        if self._defaults['IsSelfCalValid']['validSteps'] is None:
            raise MockFunctionCallError("niRFSA_IsSelfCalValid", param='validSteps')
        if valid_steps is not None:
            valid_steps.contents.value = self._defaults['IsSelfCalValid']['validSteps']
        return self._defaults['IsSelfCalValid']['return']

    def niRFSA_LoadConfigurationsFromFile(self, vi, channel_name, file_path):  # noqa: N802
        if self._defaults['LoadConfigurationsFromFile']['return'] != 0:
            return self._defaults['LoadConfigurationsFromFile']['return']
        return self._defaults['LoadConfigurationsFromFile']['return']

    def niRFSA_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niRFSA_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niRFSA_PerformThermalCorrection(self, vi):  # noqa: N802
        if self._defaults['PerformThermalCorrection']['return'] != 0:
            return self._defaults['PerformThermalCorrection']['return']
        return self._defaults['PerformThermalCorrection']['return']

    def niRFSA_ReadIqSingleRecordComplexF64(self, vi, channel_list, timeout, data, data_array_size, wfm_info):  # noqa: N802
        if self._defaults['ReadIqSingleRecordComplexF64']['return'] != 0:
            return self._defaults['ReadIqSingleRecordComplexF64']['return']
        # data
        if self._defaults['ReadIqSingleRecordComplexF64']['data'] is None:
            raise MockFunctionCallError("niRFSA_ReadIqSingleRecordComplexF64", param='data')
        if data is not None:
            data.contents.value = self._defaults['ReadIqSingleRecordComplexF64']['data']
        # wfm_info
        if self._defaults['ReadIqSingleRecordComplexF64']['wfmInfo'] is None:
            raise MockFunctionCallError("niRFSA_ReadIqSingleRecordComplexF64", param='wfmInfo')
        for field in self._defaults['ReadIqSingleRecordComplexF64']['wfm_info']._fields_:
            field_name = field[0]
            setattr(wfm_info.contents, field_name, getattr(self._defaults['ReadIqSingleRecordComplexF64']['wfm_info'], field_name))
        return self._defaults['ReadIqSingleRecordComplexF64']['return']

    def niRFSA_ReadPowerSpectrumF32(self, vi, channel_list, timeout, power_spectrum_data, data_array_size, spectrum_info):  # noqa: N802
        if self._defaults['ReadPowerSpectrumF32']['return'] != 0:
            return self._defaults['ReadPowerSpectrumF32']['return']
        # power_spectrum_data
        if self._defaults['ReadPowerSpectrumF32']['powerSpectrumData'] is None:
            raise MockFunctionCallError("niRFSA_ReadPowerSpectrumF32", param='powerSpectrumData')
        test_value = self._defaults['ReadPowerSpectrumF32']['powerSpectrumData']
        try:
            power_spectrum_data_ref = power_spectrum_data.contents
        except AttributeError:
            power_spectrum_data_ref = power_spectrum_data
        assert len(power_spectrum_data_ref) >= len(test_value)
        for i in range(len(test_value)):
            power_spectrum_data_ref[i] = test_value[i]
        # spectrum_info
        if self._defaults['ReadPowerSpectrumF32']['spectrumInfo'] is None:
            raise MockFunctionCallError("niRFSA_ReadPowerSpectrumF32", param='spectrumInfo')
        for field in self._defaults['ReadPowerSpectrumF32']['spectrum_info']._fields_:
            field_name = field[0]
            setattr(spectrum_info.contents, field_name, getattr(self._defaults['ReadPowerSpectrumF32']['spectrum_info'], field_name))
        return self._defaults['ReadPowerSpectrumF32']['return']

    def niRFSA_ReadPowerSpectrumF64(self, vi, channel_list, timeout, power_spectrum_data, data_array_size, spectrum_info):  # noqa: N802
        if self._defaults['ReadPowerSpectrumF64']['return'] != 0:
            return self._defaults['ReadPowerSpectrumF64']['return']
        # power_spectrum_data
        if self._defaults['ReadPowerSpectrumF64']['powerSpectrumData'] is None:
            raise MockFunctionCallError("niRFSA_ReadPowerSpectrumF64", param='powerSpectrumData')
        test_value = self._defaults['ReadPowerSpectrumF64']['powerSpectrumData']
        try:
            power_spectrum_data_ref = power_spectrum_data.contents
        except AttributeError:
            power_spectrum_data_ref = power_spectrum_data
        assert len(power_spectrum_data_ref) >= len(test_value)
        for i in range(len(test_value)):
            power_spectrum_data_ref[i] = test_value[i]
        # spectrum_info
        if self._defaults['ReadPowerSpectrumF64']['spectrumInfo'] is None:
            raise MockFunctionCallError("niRFSA_ReadPowerSpectrumF64", param='spectrumInfo')
        for field in self._defaults['ReadPowerSpectrumF64']['spectrum_info']._fields_:
            field_name = field[0]
            setattr(spectrum_info.contents, field_name, getattr(self._defaults['ReadPowerSpectrumF64']['spectrum_info'], field_name))
        return self._defaults['ReadPowerSpectrumF64']['return']

    def niRFSA_Reset(self, vi):  # noqa: N802
        if self._defaults['Reset']['return'] != 0:
            return self._defaults['Reset']['return']
        return self._defaults['Reset']['return']

    def niRFSA_ResetAttribute(self, vi, channel_name, attribute_id):  # noqa: N802
        if self._defaults['ResetAttribute']['return'] != 0:
            return self._defaults['ResetAttribute']['return']
        return self._defaults['ResetAttribute']['return']

    def niRFSA_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niRFSA_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niRFSA_ResetWithOptions(self, vi, steps_to_omit):  # noqa: N802
        if self._defaults['ResetWithOptions']['return'] != 0:
            return self._defaults['ResetWithOptions']['return']
        return self._defaults['ResetWithOptions']['return']

    def niRFSA_RevisionQuery(self, vi, driver_rev, instr_rev):  # noqa: N802
        if self._defaults['RevisionQuery']['return'] != 0:
            return self._defaults['RevisionQuery']['return']
        # driver_rev
        if self._defaults['RevisionQuery']['driverRev'] is None:
            raise MockFunctionCallError("niRFSA_RevisionQuery", param='driverRev')
        test_value = self._defaults['RevisionQuery']['driverRev']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(driver_rev) >= len(test_value)
        for i in range(len(test_value)):
            driver_rev[i] = test_value[i]
        # instr_rev
        if self._defaults['RevisionQuery']['instrRev'] is None:
            raise MockFunctionCallError("niRFSA_RevisionQuery", param='instrRev')
        test_value = self._defaults['RevisionQuery']['instrRev']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(instr_rev) >= len(test_value)
        for i in range(len(test_value)):
            instr_rev[i] = test_value[i]
        return self._defaults['RevisionQuery']['return']

    def niRFSA_SaveConfigurationsToFile(self, vi, channel_name, file_path):  # noqa: N802
        if self._defaults['SaveConfigurationsToFile']['return'] != 0:
            return self._defaults['SaveConfigurationsToFile']['return']
        return self._defaults['SaveConfigurationsToFile']['return']

    def niRFSA_SelfCal(self, vi):  # noqa: N802
        if self._defaults['SelfCal']['return'] != 0:
            return self._defaults['SelfCal']['return']
        return self._defaults['SelfCal']['return']

    def niRFSA_SelfCalibrate(self, vi, steps_to_omit):  # noqa: N802
        if self._defaults['SelfCalibrate']['return'] != 0:
            return self._defaults['SelfCalibrate']['return']
        return self._defaults['SelfCalibrate']['return']

    def niRFSA_SelfCalibrateRange(self, vi, steps_to_omit, min_frequency, max_frequency, min_reference_level, max_reference_level):  # noqa: N802
        if self._defaults['SelfCalibrateRange']['return'] != 0:
            return self._defaults['SelfCalibrateRange']['return']
        return self._defaults['SelfCalibrateRange']['return']

    def niRFSA_SelfTest(self, vi, test_result, test_message):  # noqa: N802
        if self._defaults['SelfTest']['return'] != 0:
            return self._defaults['SelfTest']['return']
        # test_result
        if self._defaults['SelfTest']['testResult'] is None:
            raise MockFunctionCallError("niRFSA_SelfTest", param='testResult')
        if test_result is not None:
            test_result.contents.value = self._defaults['SelfTest']['testResult']
        # test_message
        if self._defaults['SelfTest']['testMessage'] is None:
            raise MockFunctionCallError("niRFSA_SelfTest", param='testMessage')
        test_value = self._defaults['SelfTest']['testMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(test_message) >= len(test_value)
        for i in range(len(test_value)):
            test_message[i] = test_value[i]
        return self._defaults['SelfTest']['return']

    def niRFSA_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTrigger']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTrigger']['return']
        return self._defaults['SendSoftwareEdgeTrigger']['return']

    def niRFSA_SetAttributeViBoolean(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niRFSA_SetAttributeViInt32(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niRFSA_SetAttributeViInt64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niRFSA_SetAttributeViReal64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niRFSA_SetAttributeViSession(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViSession']['return'] != 0:
            return self._defaults['SetAttributeViSession']['return']
        return self._defaults['SetAttributeViSession']['return']

    def niRFSA_SetAttributeViString(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niRFSA_SetCalUserDefinedInfo(self, vi, info):  # noqa: N802
        if self._defaults['SetCalUserDefinedInfo']['return'] != 0:
            return self._defaults['SetCalUserDefinedInfo']['return']
        return self._defaults['SetCalUserDefinedInfo']['return']

    def niRFSA_SetUserData(self, vi, identifier, buffer_size, data):  # noqa: N802
        if self._defaults['SetUserData']['return'] != 0:
            return self._defaults['SetUserData']['return']
        return self._defaults['SetUserData']['return']

    def niRFSA_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niRFSA_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niRFSA_Abort.side_effect = MockFunctionCallError("niRFSA_Abort")
        mock_library.niRFSA_Abort.return_value = 0
        mock_library.niRFSA_CalAdjustCalTonePower.side_effect = MockFunctionCallError("niRFSA_CalAdjustCalTonePower")
        mock_library.niRFSA_CalAdjustCalTonePower.return_value = 0
        mock_library.niRFSA_CalAdjustDeviceGain.side_effect = MockFunctionCallError("niRFSA_CalAdjustDeviceGain")
        mock_library.niRFSA_CalAdjustDeviceGain.return_value = 0
        mock_library.niRFSA_CalAdjustDownconverterGain.side_effect = MockFunctionCallError("niRFSA_CalAdjustDownconverterGain")
        mock_library.niRFSA_CalAdjustDownconverterGain.return_value = 0
        mock_library.niRFSA_CalAdjustIfAttenuationCalibration.side_effect = MockFunctionCallError("niRFSA_CalAdjustIfAttenuationCalibration")
        mock_library.niRFSA_CalAdjustIfAttenuationCalibration.return_value = 0
        mock_library.niRFSA_CalAdjustIfResponseCalibration.side_effect = MockFunctionCallError("niRFSA_CalAdjustIfResponseCalibration")
        mock_library.niRFSA_CalAdjustIfResponseCalibration.return_value = 0
        mock_library.niRFSA_CalAdjustLoExportCalibration.side_effect = MockFunctionCallError("niRFSA_CalAdjustLoExportCalibration")
        mock_library.niRFSA_CalAdjustLoExportCalibration.return_value = 0
        mock_library.niRFSA_CalAdjustRefLevelCalibration.side_effect = MockFunctionCallError("niRFSA_CalAdjustRefLevelCalibration")
        mock_library.niRFSA_CalAdjustRefLevelCalibration.return_value = 0
        mock_library.niRFSA_CalSetTemperature.side_effect = MockFunctionCallError("niRFSA_CalSetTemperature")
        mock_library.niRFSA_CalSetTemperature.return_value = 0
        mock_library.niRFSA_ChangeExtCalPassword.side_effect = MockFunctionCallError("niRFSA_ChangeExtCalPassword")
        mock_library.niRFSA_ChangeExtCalPassword.return_value = 0
        mock_library.niRFSA_CheckAcquisitionStatus.side_effect = MockFunctionCallError("niRFSA_CheckAcquisitionStatus")
        mock_library.niRFSA_CheckAcquisitionStatus.return_value = 0
        mock_library.niRFSA_ClearError.side_effect = MockFunctionCallError("niRFSA_ClearError")
        mock_library.niRFSA_ClearError.return_value = 0
        mock_library.niRFSA_ClearSelfCalibrateRange.side_effect = MockFunctionCallError("niRFSA_ClearSelfCalibrateRange")
        mock_library.niRFSA_ClearSelfCalibrateRange.return_value = 0
        mock_library.niRFSA_Close.side_effect = MockFunctionCallError("niRFSA_Close")
        mock_library.niRFSA_Close.return_value = 0
        mock_library.niRFSA_CloseCalibrationStep.side_effect = MockFunctionCallError("niRFSA_CloseCalibrationStep")
        mock_library.niRFSA_CloseCalibrationStep.return_value = 0
        mock_library.niRFSA_CloseExtCal.side_effect = MockFunctionCallError("niRFSA_CloseExtCal")
        mock_library.niRFSA_CloseExtCal.return_value = 0
        mock_library.niRFSA_CloseExternalAlignment.side_effect = MockFunctionCallError("niRFSA_CloseExternalAlignment")
        mock_library.niRFSA_CloseExternalAlignment.return_value = 0
        mock_library.niRFSA_CloseExternalAlignmentStep.side_effect = MockFunctionCallError("niRFSA_CloseExternalAlignmentStep")
        mock_library.niRFSA_CloseExternalAlignmentStep.return_value = 0
        mock_library.niRFSA_Commit.side_effect = MockFunctionCallError("niRFSA_Commit")
        mock_library.niRFSA_Commit.return_value = 0
        mock_library.niRFSA_ConfigureAcquisitionType.side_effect = MockFunctionCallError("niRFSA_ConfigureAcquisitionType")
        mock_library.niRFSA_ConfigureAcquisitionType.return_value = 0
        mock_library.niRFSA_ConfigureDeembeddingTableInterpolationLinear.side_effect = MockFunctionCallError("niRFSA_ConfigureDeembeddingTableInterpolationLinear")
        mock_library.niRFSA_ConfigureDeembeddingTableInterpolationLinear.return_value = 0
        mock_library.niRFSA_ConfigureDeembeddingTableInterpolationNearest.side_effect = MockFunctionCallError("niRFSA_ConfigureDeembeddingTableInterpolationNearest")
        mock_library.niRFSA_ConfigureDeembeddingTableInterpolationNearest.return_value = 0
        mock_library.niRFSA_ConfigureDeembeddingTableInterpolationSpline.side_effect = MockFunctionCallError("niRFSA_ConfigureDeembeddingTableInterpolationSpline")
        mock_library.niRFSA_ConfigureDeembeddingTableInterpolationSpline.return_value = 0
        mock_library.niRFSA_ConfigureDigitalEdgeAdvanceTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureDigitalEdgeAdvanceTrigger")
        mock_library.niRFSA_ConfigureDigitalEdgeAdvanceTrigger.return_value = 0
        mock_library.niRFSA_ConfigureDigitalEdgeRefTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureDigitalEdgeRefTrigger")
        mock_library.niRFSA_ConfigureDigitalEdgeRefTrigger.return_value = 0
        mock_library.niRFSA_ConfigureDigitalEdgeStartTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureDigitalEdgeStartTrigger")
        mock_library.niRFSA_ConfigureDigitalEdgeStartTrigger.return_value = 0
        mock_library.niRFSA_ConfigureIqCarrierFrequency.side_effect = MockFunctionCallError("niRFSA_ConfigureIqCarrierFrequency")
        mock_library.niRFSA_ConfigureIqCarrierFrequency.return_value = 0
        mock_library.niRFSA_ConfigureIqPowerEdgeRefTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureIqPowerEdgeRefTrigger")
        mock_library.niRFSA_ConfigureIqPowerEdgeRefTrigger.return_value = 0
        mock_library.niRFSA_ConfigureIqRate.side_effect = MockFunctionCallError("niRFSA_ConfigureIqRate")
        mock_library.niRFSA_ConfigureIqRate.return_value = 0
        mock_library.niRFSA_ConfigureNumberOfRecords.side_effect = MockFunctionCallError("niRFSA_ConfigureNumberOfRecords")
        mock_library.niRFSA_ConfigureNumberOfRecords.return_value = 0
        mock_library.niRFSA_ConfigureNumberOfSamples.side_effect = MockFunctionCallError("niRFSA_ConfigureNumberOfSamples")
        mock_library.niRFSA_ConfigureNumberOfSamples.return_value = 0
        mock_library.niRFSA_ConfigurePxiChassisClk10.side_effect = MockFunctionCallError("niRFSA_ConfigurePxiChassisClk10")
        mock_library.niRFSA_ConfigurePxiChassisClk10.return_value = 0
        mock_library.niRFSA_ConfigureRefClock.side_effect = MockFunctionCallError("niRFSA_ConfigureRefClock")
        mock_library.niRFSA_ConfigureRefClock.return_value = 0
        mock_library.niRFSA_ConfigureReferenceLevel.side_effect = MockFunctionCallError("niRFSA_ConfigureReferenceLevel")
        mock_library.niRFSA_ConfigureReferenceLevel.return_value = 0
        mock_library.niRFSA_ConfigureResolutionBandwidth.side_effect = MockFunctionCallError("niRFSA_ConfigureResolutionBandwidth")
        mock_library.niRFSA_ConfigureResolutionBandwidth.return_value = 0
        mock_library.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureSoftwareEdgeAdvanceTrigger")
        mock_library.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger.return_value = 0
        mock_library.niRFSA_ConfigureSoftwareEdgeRefTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureSoftwareEdgeRefTrigger")
        mock_library.niRFSA_ConfigureSoftwareEdgeRefTrigger.return_value = 0
        mock_library.niRFSA_ConfigureSoftwareEdgeStartTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureSoftwareEdgeStartTrigger")
        mock_library.niRFSA_ConfigureSoftwareEdgeStartTrigger.return_value = 0
        mock_library.niRFSA_ConfigureSpectrumFrequencyCenterSpan.side_effect = MockFunctionCallError("niRFSA_ConfigureSpectrumFrequencyCenterSpan")
        mock_library.niRFSA_ConfigureSpectrumFrequencyCenterSpan.return_value = 0
        mock_library.niRFSA_ConfigureSpectrumFrequencyStartStop.side_effect = MockFunctionCallError("niRFSA_ConfigureSpectrumFrequencyStartStop")
        mock_library.niRFSA_ConfigureSpectrumFrequencyStartStop.return_value = 0
        mock_library.niRFSA_CreateConfigurationList.side_effect = MockFunctionCallError("niRFSA_CreateConfigurationList")
        mock_library.niRFSA_CreateConfigurationList.return_value = 0
        mock_library.niRFSA_CreateConfigurationListStep.side_effect = MockFunctionCallError("niRFSA_CreateConfigurationListStep")
        mock_library.niRFSA_CreateConfigurationListStep.return_value = 0
        mock_library.niRFSA_CreateDeembeddingSparameterTableArray.side_effect = MockFunctionCallError("niRFSA_CreateDeembeddingSparameterTableArray")
        mock_library.niRFSA_CreateDeembeddingSparameterTableArray.return_value = 0
        mock_library.niRFSA_CreateDeembeddingSparameterTableS2PFile.side_effect = MockFunctionCallError("niRFSA_CreateDeembeddingSparameterTableS2PFile")
        mock_library.niRFSA_CreateDeembeddingSparameterTableS2PFile.return_value = 0
        mock_library.niRFSA_DeleteAllDeembeddingTables.side_effect = MockFunctionCallError("niRFSA_DeleteAllDeembeddingTables")
        mock_library.niRFSA_DeleteAllDeembeddingTables.return_value = 0
        mock_library.niRFSA_DeleteConfigurationList.side_effect = MockFunctionCallError("niRFSA_DeleteConfigurationList")
        mock_library.niRFSA_DeleteConfigurationList.return_value = 0
        mock_library.niRFSA_DeleteDeembeddingTable.side_effect = MockFunctionCallError("niRFSA_DeleteDeembeddingTable")
        mock_library.niRFSA_DeleteDeembeddingTable.return_value = 0
        mock_library.niRFSA_Disable.side_effect = MockFunctionCallError("niRFSA_Disable")
        mock_library.niRFSA_Disable.return_value = 0
        mock_library.niRFSA_DisableAdvanceTrigger.side_effect = MockFunctionCallError("niRFSA_DisableAdvanceTrigger")
        mock_library.niRFSA_DisableAdvanceTrigger.return_value = 0
        mock_library.niRFSA_DisableRefTrigger.side_effect = MockFunctionCallError("niRFSA_DisableRefTrigger")
        mock_library.niRFSA_DisableRefTrigger.return_value = 0
        mock_library.niRFSA_DisableStartTrigger.side_effect = MockFunctionCallError("niRFSA_DisableStartTrigger")
        mock_library.niRFSA_DisableStartTrigger.return_value = 0
        mock_library.niRFSA_EnableSessionAccess.side_effect = MockFunctionCallError("niRFSA_EnableSessionAccess")
        mock_library.niRFSA_EnableSessionAccess.return_value = 0
        mock_library.niRFSA_ErrorMessage.side_effect = MockFunctionCallError("niRFSA_ErrorMessage")
        mock_library.niRFSA_ErrorMessage.return_value = 0
        mock_library.niRFSA_ErrorQuery.side_effect = MockFunctionCallError("niRFSA_ErrorQuery")
        mock_library.niRFSA_ErrorQuery.return_value = 0
        mock_library.niRFSA_ExportSignal.side_effect = MockFunctionCallError("niRFSA_ExportSignal")
        mock_library.niRFSA_ExportSignal.return_value = 0
        mock_library.niRFSA_ExtCalStoreBaselineForSelfCalibration.side_effect = MockFunctionCallError("niRFSA_ExtCalStoreBaselineForSelfCalibration")
        mock_library.niRFSA_ExtCalStoreBaselineForSelfCalibration.return_value = 0
        mock_library.niRFSA_ExternalAlignmentAdjustPreselector.side_effect = MockFunctionCallError("niRFSA_ExternalAlignmentAdjustPreselector")
        mock_library.niRFSA_ExternalAlignmentAdjustPreselector.return_value = 0
        mock_library.niRFSA_FetchIqMultiRecordComplexF32.side_effect = MockFunctionCallError("niRFSA_FetchIqMultiRecordComplexF32")
        mock_library.niRFSA_FetchIqMultiRecordComplexF32.return_value = 0
        mock_library.niRFSA_FetchIqMultiRecordComplexF64.side_effect = MockFunctionCallError("niRFSA_FetchIqMultiRecordComplexF64")
        mock_library.niRFSA_FetchIqMultiRecordComplexF64.return_value = 0
        mock_library.niRFSA_GetAttributeViBoolean.side_effect = MockFunctionCallError("niRFSA_GetAttributeViBoolean")
        mock_library.niRFSA_GetAttributeViBoolean.return_value = 0
        mock_library.niRFSA_GetAttributeViInt32.side_effect = MockFunctionCallError("niRFSA_GetAttributeViInt32")
        mock_library.niRFSA_GetAttributeViInt32.return_value = 0
        mock_library.niRFSA_GetAttributeViInt64.side_effect = MockFunctionCallError("niRFSA_GetAttributeViInt64")
        mock_library.niRFSA_GetAttributeViInt64.return_value = 0
        mock_library.niRFSA_GetAttributeViReal64.side_effect = MockFunctionCallError("niRFSA_GetAttributeViReal64")
        mock_library.niRFSA_GetAttributeViReal64.return_value = 0
        mock_library.niRFSA_GetAttributeViSession.side_effect = MockFunctionCallError("niRFSA_GetAttributeViSession")
        mock_library.niRFSA_GetAttributeViSession.return_value = 0
        mock_library.niRFSA_GetAttributeViString.side_effect = MockFunctionCallError("niRFSA_GetAttributeViString")
        mock_library.niRFSA_GetAttributeViString.return_value = 0
        mock_library.niRFSA_GetCalUserDefinedInfo.side_effect = MockFunctionCallError("niRFSA_GetCalUserDefinedInfo")
        mock_library.niRFSA_GetCalUserDefinedInfo.return_value = 0
        mock_library.niRFSA_GetCalUserDefinedInfoMaxSize.side_effect = MockFunctionCallError("niRFSA_GetCalUserDefinedInfoMaxSize")
        mock_library.niRFSA_GetCalUserDefinedInfoMaxSize.return_value = 0
        mock_library.niRFSA_GetDeembeddingSparameters.side_effect = MockFunctionCallError("niRFSA_GetDeembeddingSparameters")
        mock_library.niRFSA_GetDeembeddingSparameters.return_value = 0
        mock_library.niRFSA_GetDeviceResponse.side_effect = MockFunctionCallError("niRFSA_GetDeviceResponse")
        mock_library.niRFSA_GetDeviceResponse.return_value = 0
        mock_library.niRFSA_GetError.side_effect = MockFunctionCallError("niRFSA_GetError")
        mock_library.niRFSA_GetError.return_value = 0
        mock_library.niRFSA_GetExtCalLastDateAndTime.side_effect = MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime")
        mock_library.niRFSA_GetExtCalLastDateAndTime.return_value = 0
        mock_library.niRFSA_GetExtCalLastTemp.side_effect = MockFunctionCallError("niRFSA_GetExtCalLastTemp")
        mock_library.niRFSA_GetExtCalLastTemp.return_value = 0
        mock_library.niRFSA_GetExtCalRecommendedInterval.side_effect = MockFunctionCallError("niRFSA_GetExtCalRecommendedInterval")
        mock_library.niRFSA_GetExtCalRecommendedInterval.return_value = 0
        mock_library.niRFSA_GetFetchBacklog.side_effect = MockFunctionCallError("niRFSA_GetFetchBacklog")
        mock_library.niRFSA_GetFetchBacklog.return_value = 0
        mock_library.niRFSA_GetFrequencyResponse.side_effect = MockFunctionCallError("niRFSA_GetFrequencyResponse")
        mock_library.niRFSA_GetFrequencyResponse.return_value = 0
        mock_library.niRFSA_GetGainReferenceCalBaseline.side_effect = MockFunctionCallError("niRFSA_GetGainReferenceCalBaseline")
        mock_library.niRFSA_GetGainReferenceCalBaseline.return_value = 0
        mock_library.niRFSA_GetNormalizationCoefficients.side_effect = MockFunctionCallError("niRFSA_GetNormalizationCoefficients")
        mock_library.niRFSA_GetNormalizationCoefficients.return_value = 0
        mock_library.niRFSA_GetNumberOfSpectralLines.side_effect = MockFunctionCallError("niRFSA_GetNumberOfSpectralLines")
        mock_library.niRFSA_GetNumberOfSpectralLines.return_value = 0
        mock_library.niRFSA_GetRelayName.side_effect = MockFunctionCallError("niRFSA_GetRelayName")
        mock_library.niRFSA_GetRelayName.return_value = 0
        mock_library.niRFSA_GetRelayOperationsCount.side_effect = MockFunctionCallError("niRFSA_GetRelayOperationsCount")
        mock_library.niRFSA_GetRelayOperationsCount.return_value = 0
        mock_library.niRFSA_GetScalingCoefficients.side_effect = MockFunctionCallError("niRFSA_GetScalingCoefficients")
        mock_library.niRFSA_GetScalingCoefficients.return_value = 0
        mock_library.niRFSA_GetSelfCalLastDateAndTime.side_effect = MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime")
        mock_library.niRFSA_GetSelfCalLastDateAndTime.return_value = 0
        mock_library.niRFSA_GetSelfCalLastTemp.side_effect = MockFunctionCallError("niRFSA_GetSelfCalLastTemp")
        mock_library.niRFSA_GetSelfCalLastTemp.return_value = 0
        mock_library.niRFSA_GetSpectralInfoForSmt.side_effect = MockFunctionCallError("niRFSA_GetSpectralInfoForSmt")
        mock_library.niRFSA_GetSpectralInfoForSmt.return_value = 0
        mock_library.niRFSA_GetStreamEndpointHandle.side_effect = MockFunctionCallError("niRFSA_GetStreamEndpointHandle")
        mock_library.niRFSA_GetStreamEndpointHandle.return_value = 0
        mock_library.niRFSA_GetTerminalName.side_effect = MockFunctionCallError("niRFSA_GetTerminalName")
        mock_library.niRFSA_GetTerminalName.return_value = 0
        mock_library.niRFSA_GetUserData.side_effect = MockFunctionCallError("niRFSA_GetUserData")
        mock_library.niRFSA_GetUserData.return_value = 0
        mock_library.niRFSA_Init.side_effect = MockFunctionCallError("niRFSA_Init")
        mock_library.niRFSA_Init.return_value = 0
        mock_library.niRFSA_InitExtCal.side_effect = MockFunctionCallError("niRFSA_InitExtCal")
        mock_library.niRFSA_InitExtCal.return_value = 0
        mock_library.niRFSA_InitWithOptions.side_effect = MockFunctionCallError("niRFSA_InitWithOptions")
        mock_library.niRFSA_InitWithOptions.return_value = 0
        mock_library.niRFSA_InitializeCalibrationStep.side_effect = MockFunctionCallError("niRFSA_InitializeCalibrationStep")
        mock_library.niRFSA_InitializeCalibrationStep.return_value = 0
        mock_library.niRFSA_InitializeExternalAlignment.side_effect = MockFunctionCallError("niRFSA_InitializeExternalAlignment")
        mock_library.niRFSA_InitializeExternalAlignment.return_value = 0
        mock_library.niRFSA_InitializeExternalAlignmentStep.side_effect = MockFunctionCallError("niRFSA_InitializeExternalAlignmentStep")
        mock_library.niRFSA_InitializeExternalAlignmentStep.return_value = 0
        mock_library.niRFSA_Initiate.side_effect = MockFunctionCallError("niRFSA_Initiate")
        mock_library.niRFSA_Initiate.return_value = 0
        mock_library.niRFSA_InvalidateAllAttributes.side_effect = MockFunctionCallError("niRFSA_InvalidateAllAttributes")
        mock_library.niRFSA_InvalidateAllAttributes.return_value = 0
        mock_library.niRFSA_IsSelfCalValid.side_effect = MockFunctionCallError("niRFSA_IsSelfCalValid")
        mock_library.niRFSA_IsSelfCalValid.return_value = 0
        mock_library.niRFSA_LoadConfigurationsFromFile.side_effect = MockFunctionCallError("niRFSA_LoadConfigurationsFromFile")
        mock_library.niRFSA_LoadConfigurationsFromFile.return_value = 0
        mock_library.niRFSA_LockSession.side_effect = MockFunctionCallError("niRFSA_LockSession")
        mock_library.niRFSA_LockSession.return_value = 0
        mock_library.niRFSA_PerformThermalCorrection.side_effect = MockFunctionCallError("niRFSA_PerformThermalCorrection")
        mock_library.niRFSA_PerformThermalCorrection.return_value = 0
        mock_library.niRFSA_ReadIqSingleRecordComplexF64.side_effect = MockFunctionCallError("niRFSA_ReadIqSingleRecordComplexF64")
        mock_library.niRFSA_ReadIqSingleRecordComplexF64.return_value = 0
        mock_library.niRFSA_ReadPowerSpectrumF32.side_effect = MockFunctionCallError("niRFSA_ReadPowerSpectrumF32")
        mock_library.niRFSA_ReadPowerSpectrumF32.return_value = 0
        mock_library.niRFSA_ReadPowerSpectrumF64.side_effect = MockFunctionCallError("niRFSA_ReadPowerSpectrumF64")
        mock_library.niRFSA_ReadPowerSpectrumF64.return_value = 0
        mock_library.niRFSA_Reset.side_effect = MockFunctionCallError("niRFSA_Reset")
        mock_library.niRFSA_Reset.return_value = 0
        mock_library.niRFSA_ResetAttribute.side_effect = MockFunctionCallError("niRFSA_ResetAttribute")
        mock_library.niRFSA_ResetAttribute.return_value = 0
        mock_library.niRFSA_ResetDevice.side_effect = MockFunctionCallError("niRFSA_ResetDevice")
        mock_library.niRFSA_ResetDevice.return_value = 0
        mock_library.niRFSA_ResetWithDefaults.side_effect = MockFunctionCallError("niRFSA_ResetWithDefaults")
        mock_library.niRFSA_ResetWithDefaults.return_value = 0
        mock_library.niRFSA_ResetWithOptions.side_effect = MockFunctionCallError("niRFSA_ResetWithOptions")
        mock_library.niRFSA_ResetWithOptions.return_value = 0
        mock_library.niRFSA_RevisionQuery.side_effect = MockFunctionCallError("niRFSA_RevisionQuery")
        mock_library.niRFSA_RevisionQuery.return_value = 0
        mock_library.niRFSA_SaveConfigurationsToFile.side_effect = MockFunctionCallError("niRFSA_SaveConfigurationsToFile")
        mock_library.niRFSA_SaveConfigurationsToFile.return_value = 0
        mock_library.niRFSA_SelfCal.side_effect = MockFunctionCallError("niRFSA_SelfCal")
        mock_library.niRFSA_SelfCal.return_value = 0
        mock_library.niRFSA_SelfCalibrate.side_effect = MockFunctionCallError("niRFSA_SelfCalibrate")
        mock_library.niRFSA_SelfCalibrate.return_value = 0
        mock_library.niRFSA_SelfCalibrateRange.side_effect = MockFunctionCallError("niRFSA_SelfCalibrateRange")
        mock_library.niRFSA_SelfCalibrateRange.return_value = 0
        mock_library.niRFSA_SelfTest.side_effect = MockFunctionCallError("niRFSA_SelfTest")
        mock_library.niRFSA_SelfTest.return_value = 0
        mock_library.niRFSA_SendSoftwareEdgeTrigger.side_effect = MockFunctionCallError("niRFSA_SendSoftwareEdgeTrigger")
        mock_library.niRFSA_SendSoftwareEdgeTrigger.return_value = 0
        mock_library.niRFSA_SetAttributeViBoolean.side_effect = MockFunctionCallError("niRFSA_SetAttributeViBoolean")
        mock_library.niRFSA_SetAttributeViBoolean.return_value = 0
        mock_library.niRFSA_SetAttributeViInt32.side_effect = MockFunctionCallError("niRFSA_SetAttributeViInt32")
        mock_library.niRFSA_SetAttributeViInt32.return_value = 0
        mock_library.niRFSA_SetAttributeViInt64.side_effect = MockFunctionCallError("niRFSA_SetAttributeViInt64")
        mock_library.niRFSA_SetAttributeViInt64.return_value = 0
        mock_library.niRFSA_SetAttributeViReal64.side_effect = MockFunctionCallError("niRFSA_SetAttributeViReal64")
        mock_library.niRFSA_SetAttributeViReal64.return_value = 0
        mock_library.niRFSA_SetAttributeViSession.side_effect = MockFunctionCallError("niRFSA_SetAttributeViSession")
        mock_library.niRFSA_SetAttributeViSession.return_value = 0
        mock_library.niRFSA_SetAttributeViString.side_effect = MockFunctionCallError("niRFSA_SetAttributeViString")
        mock_library.niRFSA_SetAttributeViString.return_value = 0
        mock_library.niRFSA_SetCalUserDefinedInfo.side_effect = MockFunctionCallError("niRFSA_SetCalUserDefinedInfo")
        mock_library.niRFSA_SetCalUserDefinedInfo.return_value = 0
        mock_library.niRFSA_SetUserData.side_effect = MockFunctionCallError("niRFSA_SetUserData")
        mock_library.niRFSA_SetUserData.return_value = 0
        mock_library.niRFSA_UnlockSession.side_effect = MockFunctionCallError("niRFSA_UnlockSession")
        mock_library.niRFSA_UnlockSession.return_value = 0
