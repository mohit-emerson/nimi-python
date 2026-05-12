import nirfsa
import numpy as np

# Configure and acquire IQ data
with nirfsa.Session("5841", id_query=False, reset=False,
                    options="Simulate=1, DriverSetup=Model:5841") as session:

    # Configure IQ acquisition
    session.acquisition_type = nirfsa.AcquisitionType.IQ
    session.reference_level = 0.0
    session.iq_rate = 1e6          # 1 MS/s
    session.number_of_samples = 1000

    # Initiate, fetch, then abort
    session.initiate()
    data = np.zeros(1000 * 2, dtype=np.float64)  # interleaved I/Q
    wfm_info = session.fetch_iq_single_record_complex(
        record_number=0,
        number_of_samples=1000,
        data=data,
        data_type=np.complex128,
        timeout=10.0,
    )
    session.abort()

    print(f"Samples fetched: {len(data)}")
    print(f"Waveform info: {wfm_info}")
