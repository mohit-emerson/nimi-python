import numpy as np

import nirfsa


NUMBER_OF_SAMPLES = 1000


def run_read_iq_case(session, label, buffer_length, reallocation_policy):
    iq_data_array = np.zeros(buffer_length, dtype=np.complex128)
    print(f"\n{label}")
    print(f"  before read: len={len(iq_data_array)}, policy={reallocation_policy}")

    try:
        wfm_info = session.read_iq_single_record(
            channel_list="",
            iq_data_array=iq_data_array,
            timeout=10.0,
            reallocation_policy=reallocation_policy,
        )
        print(f"  after read:  len={len(iq_data_array)}")
        print(f"  actual samples read: {wfm_info.actual_samples}")
    except ValueError as error:
        print(f"  read_iq_single_record raised ValueError: {error}")


with nirfsa.Session(
    "5841",
    id_query=False,
    reset_device=False,
    options="Simulate=1, DriverSetup=Model:5841",
) as session:
    session.acquisition_type = nirfsa.AcquisitionType.IQ
    session.reference_level = 0.0
    session.iq_rate = 1e6
    session.number_of_samples = NUMBER_OF_SAMPLES

    run_read_iq_case(
        session,
        label="Scenario 1: smaller buffer with TO_GROW",
        buffer_length=250,
        reallocation_policy=nirfsa.ReallocationPolicy.TO_GROW,
    )
    run_read_iq_case(
        session,
        label="Scenario 2: smaller buffer with DO_NOT_REALLOCATE",
        buffer_length=250,
        reallocation_policy=nirfsa.ReallocationPolicy.DO_NOT_REALLOCATE,
    )
    run_read_iq_case(
        session,
        label="Scenario 3: larger buffer than number_of_samples",
        buffer_length=1500,
        reallocation_policy=nirfsa.ReallocationPolicy.TO_GROW,
    )
