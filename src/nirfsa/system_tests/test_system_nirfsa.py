import nirfsa
import pathlib
import pytest
import sys


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
# import system_test_utilities  # noqa: E402

use_simulated_session = True
real_hw_resource_name = '5841'

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'generated/nirfsa'))


class SystemTests:
    @pytest.fixture(scope='function')
    def rfsa_device_session(self, session_creation_kwargs):
        if use_simulated_session:
            with nirfsa.Session("5841sim", options="Simulate=1, DriverSetup=Model:5841", **session_creation_kwargs) as sim_5841_session:
                yield sim_5841_session
        else:
            with nirfsa.Session(real_hw_resource_name, **session_creation_kwargs) as real_rfsa_device_session:
                yield real_rfsa_device_session

# Attribute set and get related tests
    def test_get_float_attribute(self, rfsa_device_session):
        value = rfsa_device_session.reference_level
        assert isinstance(value, float)

    def test_set_float_attribute(self, rfsa_device_session):
        rfsa_device_session.reference_level = -1.0
        assert rfsa_device_session.reference_level == -1.0


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}
