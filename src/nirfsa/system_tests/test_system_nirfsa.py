import hightime
import nirfsa
import numpy as np
import os
import pathlib
import pytest
import sys


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402, F401

test_files_base_dir = os.path.join(os.path.dirname(__file__))
use_simulated_session = True
real_hw_resource_name = '5841'


def get_test_file_path(file_name):
    return os.path.join(test_files_base_dir, file_name)


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'generated/nirfsa'))


class SystemTests:
    @pytest.fixture(scope='function')
    def rfsa_device_session(self, session_creation_kwargs):
        if use_simulated_session:
            with nirfsa.Session("5841sim", id_query=False, reset_device=False, options="Simulate=1, DriverSetup=Model:5841", **session_creation_kwargs) as sim_5841_session:
                yield sim_5841_session
        else:
            with nirfsa.Session(real_hw_resource_name, id_query=False, reset_device=False, **session_creation_kwargs) as real_rfsa_device_session:
                yield real_rfsa_device_session

# Attribute set and get related tests
    def test_get_float_attribute(self, rfsa_device_session):
        value = rfsa_device_session.reference_level
        assert isinstance(value, float)

    def test_set_float_attribute(self, rfsa_device_session):
        rfsa_device_session.reference_level = -1.0
        assert rfsa_device_session.reference_level == -1.0

    def test_get_int64_attribute(self, rfsa_device_session):
        value = rfsa_device_session.fetch_offset
        assert isinstance(value, int)

    def test_set_int64_attribute(self, rfsa_device_session):
        rfsa_device_session.fetch_offset = 5
        assert rfsa_device_session.fetch_offset == 5

    def test_get_bool_attribute(self, rfsa_device_session):
        value = rfsa_device_session.allow_more_records_than_memory
        assert isinstance(value, bool)

    def test_set_bool_attribute(self, rfsa_device_session):
        rfsa_device_session.allow_more_records_than_memory = True
        assert rfsa_device_session.allow_more_records_than_memory is True

    def test_get_string_attribute(self, rfsa_device_session):
        value = rfsa_device_session.serial_number
        assert isinstance(value, str)

    def test_get_set_center_frequency(self, rfsa_device_session):
        rfsa_device_session.center_frequency = 2.4e9
        assert rfsa_device_session.center_frequency == 2.4e9

    def test_get_instrument_model(self, rfsa_device_session):
        model = rfsa_device_session.instrument_model
        assert model == "NI PXIe-5841"

    def test_set_invalid_attribute_raises(self, rfsa_device_session):
        with pytest.raises(AttributeError):
            rfsa_device_session.non_existent_attribute = 123

    def test_get_error(self, rfsa_device_session):
        try:
            rfsa_device_session.instrument_model = ''
            assert False
        except nirfsa.Error as e:
            assert e.code == -1074135027
            assert "Attribute is read-only" in e.description

# Multi-threading related tests
    def test_multi_threading_lock_unlock(self, rfsa_device_session):
        system_test_utilities.impl_test_multi_threading_lock_unlock(rfsa_device_session)

    def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, rfsa_device_session):
        system_test_utilities.impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(rfsa_device_session.abort)

# Error handling related tests
    def test_error_message(self, session_creation_kwargs):
        try:
            with nirfsa.Session(resource_name="invalid_model", id_query=False, reset_device=False, options="Simulate=1, DriverSetup=Model:invalid_model", **session_creation_kwargs):
                assert False
        except nirfsa.Error as e:
            assert e.code != 0

    def test_save_load_configuration(self, rfsa_device_session):
        rfsa_device_session.center_frequency = 2.4e9
        rfsa_device_session.reference_level = -5.0
        rfsa_device_session.save_configurations_to_file('', get_test_file_path('tempConfiguration.json'))
        assert os.path.exists(get_test_file_path('tempConfiguration.json'))
        rfsa_device_session.center_frequency = 1e9
        rfsa_device_session.reference_level = -10.0
        assert rfsa_device_session.center_frequency == 1e9
        assert rfsa_device_session.reference_level == -10.0
        rfsa_device_session.load_configurations_from_file('', get_test_file_path('tempConfiguration.json'))
        assert rfsa_device_session.center_frequency == 2.4e9
        assert rfsa_device_session.reference_level == -5.0
        os.remove(get_test_file_path('tempConfiguration.json'))

# Utility method tests
    def test_reset(self, rfsa_device_session):
        default_reference_level = rfsa_device_session.reference_level
        rfsa_device_session.reference_level = default_reference_level + 1.0
        assert rfsa_device_session.reference_level == default_reference_level + 1.0
        rfsa_device_session.reset()
        assert rfsa_device_session.reference_level == default_reference_level

    def test_self_test(self, rfsa_device_session):
        # We should not get an assert if self_test passes
        rfsa_device_session.self_test()

    @pytest.mark.skipif(use_simulated_session is False, reason="Takes long time on real device")
    def test_self_calibrate_range(self, rfsa_device_session):
        steps_to_omit = nirfsa.SelfCalibrateRangeStepsToOmit.DIGITIZER_SELF_CAL | nirfsa.SelfCalibrateRangeStepsToOmit.LO_SELF_CAL
        rfsa_device_session.self_calibrate_range(steps_to_omit, 1e9, 2e9, -20, 0)

    def test_clear_self_calibrate_range(self, rfsa_device_session):
        rfsa_device_session.clear_self_calibrate_range()

    @pytest.mark.skipif(use_simulated_session is True, reason="Bad date returned by driver for simulated device")
    def test_get_ext_cal_last_date_and_time(self, rfsa_device_session):
        dt = rfsa_device_session.get_ext_cal_last_date_and_time()
        assert isinstance(dt, hightime.datetime)

    def test_get_terminal_name(self, rfsa_device_session):
        terminal_name = rfsa_device_session.get_terminal_name(nirfsa.Signal.REF_TRIGGER, '')
        print(terminal_name)
        assert isinstance(terminal_name, str)

    def test_abort(self, rfsa_device_session):
        rfsa_device_session.center_frequency = 2.4e9
        rfsa_device_session.initiate()
        rfsa_device_session.check_acquisition_status()
        rfsa_device_session.abort()

# Trigger configuration tests
    def test_configure_digital_edge_start_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_digital_edge_start_trigger('PXI_Trig1', nirfsa.StartTriggerDigitalEdgeEdge.RISING)
        assert rfsa_device_session.start_trigger_type == nirfsa.StartTriggerType.DIGITAL_EDGE

    def test_disable_start_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_digital_edge_start_trigger('PXI_Trig1', nirfsa.StartTriggerDigitalEdgeEdge.RISING)
        assert rfsa_device_session.start_trigger_type == nirfsa.StartTriggerType.DIGITAL_EDGE
        rfsa_device_session.disable_start_trigger()
        assert rfsa_device_session.start_trigger_type == nirfsa.StartTriggerType.NONE

    @pytest.mark.skipif(use_simulated_session is True, reason="Simulated device does not support software trigger behavior")
    def test_send_software_edge_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_software_edge_start_trigger()
        assert rfsa_device_session.start_trigger_type == nirfsa.StartTriggerType.SOFTWARE_EDGE
        rfsa_device_session.initiate()
        assert rfsa_device_session.check_acquisition_status() is False
        rfsa_device_session.send_software_edge_trigger(nirfsa.SoftwareTriggerType.START, '')
        assert rfsa_device_session.check_acquisition_status() is True
        rfsa_device_session.abort()

# Deembedding tests
    def test_set_get_deembedding_sparameters(self, rfsa_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        sparameter_tables = np.array([[[1 + 1j, 2 + 2j], [3 + 3j, 4 + 4j]], [[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], [[9 + 9j, 10 + 10j], [11 + 11j, 12 + 12j]]], dtype=np.complex128)
        expected_sparameter_table = np.array([[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], dtype=np.complex128)
        rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, sparameter_tables, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsa_device_session.center_frequency = 2e9
        returned_sparameter_table = rfsa_device_session.get_deembedding_sparameters()
        assert returned_sparameter_table.all() == expected_sparameter_table.all()

    def test_configure_deembedding_table_interpolation(self, rfsa_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        sparameter_tables = np.array([[[1 + 1j, 2 + 2j], [3 + 3j, 4 + 4j]], [[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], [[9 + 9j, 10 + 10j], [11 + 11j, 12 + 12j]]], dtype=np.complex128)
        rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, sparameter_tables, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsa_device_session.configure_deembedding_table_interpolation_linear('', 'myTable1', nirfsa.LinearInterpolationFormat.MAGNITUDE_AND_PHASE)
        rfsa_device_session.delete_deembedding_table('', 'myTable1')

    @pytest.mark.skipif(sys.platform == "linux", reason="Function not supported on Linux OS")
    def test_create_deembedding_sparameter_table_s2p_file(self, rfsa_device_session):
        rfsa_device_session.create_deembedding_sparameter_table_s2p_file('', 'myTable1', get_test_file_path('samples2pfile.s2p'), nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsa_device_session.create_deembedding_sparameter_table_s2p_file('', 'myTable2', get_test_file_path('samples2pfile.s2p'), nirfsa.SparameterOrientation.PORT1_TOWARDS_DUT)
        rfsa_device_session.configure_deembedding_table_interpolation_linear('', 'myTable1', nirfsa.LinearInterpolationFormat.MAGNITUDE_AND_PHASE)
        rfsa_device_session.ports[''].deembedding_selected_table = 'myTable1'
        with rfsa_device_session.initiate():
            rfsa_device_session.check_acquisition_status()
        rfsa_device_session.delete_deembedding_table('', 'myTable1')
        rfsa_device_session.ports[''].deembedding_selected_table = 'myTable2'
        with rfsa_device_session.initiate():
            rfsa_device_session.check_acquisition_status()
        rfsa_device_session.delete_all_deembedding_tables()
        try:
            rfsa_device_session.commit()
            assert False
        except nirfsa.Error as e:
            assert e.code == -1074097772
            assert 'de-embedding table cannot be found' in e.description
        rfsa_device_session.ports[''].deembedding_selected_table = ''
        with rfsa_device_session.initiate():
            rfsa_device_session.check_acquisition_status()

    def test_create_deembedding_sparameter_table_array_error_cases(self, rfsa_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        wrong_number_of_tables = np.full((2, 2, 2), 2.0 + 0.0j, dtype=np.complex128)
        wrong_table_size = np.full((3, 2, 3), 2.0 + 0.0j, dtype=np.complex128)
        wrong_array_dimensions = np.full((3, 2), 2.0 + 0.0j, dtype=np.complex128)
        try:
            rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, wrong_number_of_tables, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
            assert False
        except ValueError as e:
            assert str(e) == 'Frequencies count does not match the sparameter table count. Frequencies count is 3 and sparameter table count is 2.'
        try:
            rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, wrong_table_size, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
            assert False
        except ValueError as e:
            assert str(e) == 'Row and column count of sparameter table should be equal. Table row count is 2 and column count is 3.'
        try:
            rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, wrong_array_dimensions, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
            assert False
        except ValueError as e:
            assert str(e) == 'Unsupported array dimension. Is 2, expected 3'

    def test_delete_all_deembedding_tables(self, rfsa_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        sparameter_tables = np.array([[[1 + 1j, 2 + 2j], [3 + 3j, 4 + 4j]], [[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], [[9 + 9j, 10 + 10j], [11 + 11j, 12 + 12j]]], dtype=np.complex128)
        rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, sparameter_tables, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable2', frequencies, sparameter_tables, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsa_device_session.delete_all_deembedding_tables()


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}
