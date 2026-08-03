Usage
------

The following is a basic example of using the **nirfsa** module to open a session to an RF Signal Analyzer and perform a spectrum acquisition.

.. code-block:: python

    import nirfsa

    # Configure the session
    with nirfsa.Session(resource_name=resource_name, id_query=False, reset_device=False, options=options) as rfsa_session:
        rfsa_session.acquisition_type = nirfsa.AcquisitionType.SPECTRUM
        rfsa_session.configure_ref_clock(nirfsa.ReferenceClockSource.ONBOARD_CLOCK, 10e6)
        rfsa_session.reference_level = 0
        rfsa_session.resolution_bandwidth = 10e3

        rfsa_session.configure_spectrum_frequency(center_frequency=center_frequency, span=span)
        rfsa_session.number_of_spectral_lines = 1024

        spectrum_buf = np.zeros(rfsa_session.number_of_spectral_lines, dtype=np.float64)

        spectrum_info = rfsa_session.read_power_spectrum_into(spectrum_buf, timeout=10.0)

        # Perform measurements...

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nirfsa/examples>`_
