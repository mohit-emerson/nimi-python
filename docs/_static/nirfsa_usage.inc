Usage
------

The following is a basic example of using the **nirfsa** module to open a session to an RF Signal Analyzer and perform a spectrum acquisition.

.. code-block:: python

    import nirfsa

    # Configure the session
    with nirfsa.Session(resource_name='5840', id_query=False, reset_device=False, options='Simulate=1, DriverSetup=Model:5840') as session:
        # Configure RF settings
        session.configure_rf(
            center_frequency=1e9,  # Frequency in Hz
            reference_level=-10.0  # Reference level in dBm
        )
        session.acquisition_type = nirfsa.AcquisitionType.SPECTRUM

        # Start acquisition
        session.initiate()
        # Perform measurements...

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nirfsa/examples>`_
