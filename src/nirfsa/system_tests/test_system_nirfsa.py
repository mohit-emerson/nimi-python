import nirfsa
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
            with nirfsa.Session(resource_name="invalid_model", id_query=False, reset=False, options="Simulate=1, DriverSetup=Model:invalid_model", **session_creation_kwargs):
                assert False
        except nirfsa.Error as e:
            assert e.code != 0

    def test_save_load_configuration(self, rfsa_device_session):
        rfsa_device_session.center_frequency = 2.4e9
        rfsa_device_session.reference_level = -5.0
        rfsa_device_session.save_configurations_to_file(get_test_file_path('tempConfiguration.json'))
        assert os.path.exists(get_test_file_path('tempConfiguration.json'))
        rfsa_device_session.center_frequency = 1e9
        rfsa_device_session.reference_level = -10.0
        assert rfsa_device_session.center_frequency == 1e9
        assert rfsa_device_session.reference_level == -10.0
        rfsa_device_session.load_configurations_from_file(get_test_file_path('tempConfiguration.json'))
        assert rfsa_device_session.center_frequency == 2.4e9
        assert rfsa_device_session.reference_level == -5.0
        os.remove(get_test_file_path('tempConfiguration.json'))


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}
