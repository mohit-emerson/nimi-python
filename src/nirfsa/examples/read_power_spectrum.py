import numpy as np

import nirfsa


NUMBER_OF_SPECTRAL_LINES = 1024


def run_read_power_spectrum_case(session, label, buffer_length, reallocation_policy):
    power_spectrum_data_array = np.zeros(buffer_length, dtype=np.float64)
    print(f"\n{label}")
    print(f"  before read: len={len(power_spectrum_data_array)}, policy={reallocation_policy}")

    try:
        spectrum_info = session.read_power_spectrum(
            channel_list="",
            power_spectrum_data_array=power_spectrum_data_array,
            timeout=10.0,
            reallocation_policy=reallocation_policy,
        )
        print(f"  after read:  len={len(power_spectrum_data_array)}")
        print(f"  number of spectral lines: {spectrum_info.number_of_spectral_lines}")
    except ValueError as error:
        print(f"  read_power_spectrum raised ValueError: {error}")


with nirfsa.Session(
    "5841",
    id_query=False,
    reset_device=False,
    options="Simulate=1, DriverSetup=Model:5841",
) as session:
    session.acquisition_type = nirfsa.AcquisitionType.SPECTRUM
    session.reference_level = 0.0
    session.number_of_spectral_lines = NUMBER_OF_SPECTRAL_LINES

    run_read_power_spectrum_case(
        session,
        label="Scenario 1: smaller buffer with TO_GROW",
        buffer_length=256,
        reallocation_policy=nirfsa.ReallocationPolicy.TO_GROW,
    )
    run_read_power_spectrum_case(
        session,
        label="Scenario 2: smaller buffer with DO_NOT_REALLOCATE",
        buffer_length=256,
        reallocation_policy=nirfsa.ReallocationPolicy.DO_NOT_REALLOCATE,
    )
    run_read_power_spectrum_case(
        session,
        label="Scenario 3: larger buffer than number_of_spectral_lines",
        buffer_length=2048,
        reallocation_policy=nirfsa.ReallocationPolicy.TO_GROW,
    )
