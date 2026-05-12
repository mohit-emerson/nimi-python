import hightime
import nirfsa
import numpy as np
import pathlib
import pytest
import sys


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402

use_simulated_session = True
real_hw_resource_name = '5841'

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'generated/nirfsa'))


class SystemTests:
    @pytest.fixture(scope='function')
    def rfsa_device_session(self, session_creation_kwargs):
        if use_simulated_session:
            with nirfsa.Session("5841sim", id_query=False, reset=False, options="Simulate=1, DriverSetup=Model:5841", **session_creation_kwargs) as sim_5841_session:
                yield sim_5841_session
        else:
            with nirfsa.Session(real_hw_resource_name, id_query=False, reset=False, **session_creation_kwargs) as real_rfsa_device_session:
                yield real_rfsa_device_session

# Attribute set and get related tests
    def test_get_float_attribute(self, rfsa_device_session):
        value = rfsa_device_session.reference_level
        assert isinstance(value, float)

    def test_set_float_attribute(self, rfsa_device_session):
        rfsa_device_session.reference_level = -1.0
        assert rfsa_device_session.reference_level == -1.0

    def test_get_string_attribute(self, rfsa_device_session):
        model = rfsa_device_session.instrument_model
        assert model == "NI PXIe-5841"

    def test_get_list_of_strings_attribute(self, rfsa_device_session):
        models = rfsa_device_session.supported_instrument_models
        assert isinstance(models, list) and all(isinstance(model, str) for model in models)
        assert "NI PXIe-5841" in models

    def test_get_int64_attribute(self, rfsa_device_session):
        value = rfsa_device_session.number_of_samples
        assert isinstance(value, int)

    def test_set_int64_attribute(self, rfsa_device_session):
        rfsa_device_session.number_of_samples = 2000
        assert rfsa_device_session.number_of_samples == 2000

    def test_get_boolean_attribute(self, rfsa_device_session):
        value = rfsa_device_session.number_of_samples_is_finite
        assert isinstance(value, bool)

    def test_set_boolean_attribute(self, rfsa_device_session):
        rfsa_device_session.number_of_records_is_finite = True
        assert rfsa_device_session.number_of_records_is_finite is True

    def test_set_enum_attribute(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        assert rfsa_device_session.acquisition_type == nirfsa.AcquisitionType.IQ

    def test_set_float_iq_rate_attribute(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.iq_rate = 1e6
        assert rfsa_device_session.iq_rate == 1e6

    def test_get_timedelta_attribute(self, rfsa_device_session):
        value = rfsa_device_session.external_calibration_recommended_interval
        assert isinstance(value, hightime.timedelta)

    def test_set_invalid_attribute_raises(self, rfsa_device_session):
        with pytest.raises(AttributeError):
            rfsa_device_session.non_existent_attribute = 123

# Multi-threading related tests
    def test_multi_threading_lock_unlock(self, rfsa_device_session):
        system_test_utilities.impl_test_multi_threading_lock_unlock(rfsa_device_session)

    def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, rfsa_device_session):
        system_test_utilities.impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(rfsa_device_session.abort)

# Error handling related tests
    def test_error_message(self, session_creation_kwargs):
        try:
            with nirfsa.Session(resource_name="invalid_model", id_query=False, reset=False, options="Simulate=1, DriverSetup=Model:invalid_model", **session_creation_kwargs):
                assert False
        except nirfsa.Error as e:
            assert e.code != 0
            assert e.description != ''

    def test_get_error(self, rfsa_device_session):
        try:
            rfsa_device_session.instrument_model = ''
            assert False
        except nirfsa.Error as e:
            assert e.code != 0
            assert "read-only" in e.description.lower() or "Attribute is read-only" in e.description

# Utility method tests
    def test_reset(self, rfsa_device_session):
        default_ref_level = rfsa_device_session.reference_level
        rfsa_device_session.reference_level = default_ref_level + 1.0
        assert rfsa_device_session.reference_level == default_ref_level + 1.0
        rfsa_device_session.reset()
        assert rfsa_device_session.reference_level == default_ref_level

    def test_self_test(self, rfsa_device_session):
        rfsa_device_session.self_test()

    @pytest.mark.skipif(use_simulated_session is False, reason="Takes long time in real device")
    def test_self_cal(self, rfsa_device_session):
        rfsa_device_session.self_calibrate(nirfsa.StepsToOmit.NONE)

    def test_clear_self_calibrate_range(self, rfsa_device_session):
        rfsa_device_session.clear_self_calibrate_range()

    def test_commit(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.reference_level = 0.0
        rfsa_device_session.iq_rate = 1e6
        rfsa_device_session.number_of_samples = 1000
        rfsa_device_session.commit()

    def test_check_acquisition_status(self, rfsa_device_session):
        status = rfsa_device_session.check_acquisition_status()
        assert isinstance(status, bool)

# Configuration method tests
    def test_configure_ref_clock(self, rfsa_device_session):
        rfsa_device_session.configure_ref_clock(nirfsa.RefClockSource.ONBOARD_CLOCK, 10e6)

    def test_configure_digital_edge_start_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_digital_edge_start_trigger('PXI_Trig0', nirfsa.StartTriggerDigitalEdgeEdge.RISING)
        rfsa_device_session.disable_start_trigger()

    def test_configure_digital_edge_ref_trigger(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.configure_digital_edge_ref_trigger('PXI_Trig0', nirfsa.RefTriggerDigitalEdgeEdge.RISING, 100)
        rfsa_device_session.disable_ref_trigger()

# IQ acquisition tests
    def test_fetch_iq_single_record_complex_f64(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.reference_level = 0.0
        rfsa_device_session.iq_rate = 1e6
        num_samples = 1000
        rfsa_device_session.number_of_samples = num_samples
        data = np.zeros(num_samples * 2, dtype=np.float64)
        rfsa_device_session.initiate()
        wfm_info = rfsa_device_session.fetch_iq_single_record_complex(0, num_samples, data, np.complex128)
        assert wfm_info is not None

    def test_fetch_iq_single_record_complex_f32(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.reference_level = 0.0
        rfsa_device_session.iq_rate = 1e6
        num_samples = 1000
        rfsa_device_session.number_of_samples = num_samples
        data = np.zeros(num_samples * 2, dtype=np.float32)
        rfsa_device_session.initiate()
        wfm_info = rfsa_device_session.fetch_iq_single_record_complex(0, num_samples, data, np.complex64)
        assert wfm_info is not None

    def test_fetch_iq_single_record_complex_i16(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.reference_level = 0.0
        rfsa_device_session.iq_rate = 1e6
        num_samples = 1000
        rfsa_device_session.number_of_samples = num_samples
        data = np.zeros(num_samples * 2, dtype=np.int16)
        rfsa_device_session.initiate()
        wfm_info = rfsa_device_session.fetch_iq_single_record_complex(0, num_samples, data, np.int16)
        assert wfm_info is not None

    def test_fetch_iq_multi_record_complex_f64(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.reference_level = 0.0
        rfsa_device_session.iq_rate = 1e6
        num_samples = 1000
        num_records = 2
        rfsa_device_session.number_of_samples = num_samples
        rfsa_device_session.number_of_records = num_records
        data = np.zeros(num_samples * num_records * 2, dtype=np.float64)
        rfsa_device_session.initiate()
        wfm_info = rfsa_device_session.fetch_iq_multi_record_complex(0, num_records, num_samples, data, np.complex128)
        assert wfm_info is not None

    def test_fetch_iq_with_wrong_datatype(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.reference_level = 0.0
        rfsa_device_session.iq_rate = 1e6
        num_samples = 1000
        rfsa_device_session.number_of_samples = num_samples
        data = np.zeros(num_samples * 2, dtype=np.int32)
        with pytest.raises(TypeError):
            rfsa_device_session.fetch_iq_single_record_complex(0, num_samples, data, np.int32)

    def test_read_iq_single_record_complex_f64(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.reference_level = 0.0
        rfsa_device_session.iq_rate = 1e6
        num_samples = 1000
        rfsa_device_session.number_of_samples = num_samples
        data = np.zeros(num_samples * 2, dtype=np.float64)
        wfm_info = rfsa_device_session.read_iq_single_record_complex_f64(data)
        assert wfm_info is not None

    def test_get_terminal_name(self, rfsa_device_session):
        terminal_name = rfsa_device_session.get_terminal_name(nirfsa.Signal.REF_TRIGGER, '')
        assert isinstance(terminal_name, str)
        assert len(terminal_name) > 0

    def test_get_fetch_backlog(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        backlog = rfsa_device_session.get_fetch_backlog(0)
        assert isinstance(backlog, int)


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}
