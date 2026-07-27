import argparse
import nirfsa
import numpy as np
import sys


def example(resource_name, options, center_frequency, reference_level):
    with nirfsa.Session(resource_name=resource_name, id_query=False, reset_device=False, options=options) as rfsa_session:
        # Configurations
        rfsa_session.acquisition_type = nirfsa.AcquisitionType.IQ

        rfsa_session.center_frequency = center_frequency
        rfsa_session.reference_level = reference_level
        rfsa_session.iq_rate = 1e6

        iq_data_array = np.zeros(1024, dtype=np.complex128)

        with rfsa_session.initiate():
            wfm_info = rfsa_session.fetch_iq_single_record_into(iq_data_array)

        number_of_samples = int(wfm_info.actual_samples)
        accumulator = 0.0

        # Do something useful with the data.
        # We will present average power: 10log(((I^2 + Q ^2) / 2R) * 1000), where
        # R = 50 Ohms.
        if number_of_samples > 0:
            for i in range(number_of_samples):
                magnitude_squared = iq_data_array[i].real * iq_data_array[i].real + iq_data_array[i].imag * iq_data_array[i].imag

                # we need to handle this because log(0) return a range error.
                if magnitude_squared == 0.0:
                    magnitude_squared = 0.00000001

                accumulator += 10.0 * np.log10((magnitude_squared / (2.0 * 50.0)) * 1000.0)

            print('Average power = %0.1f dBm' % (accumulator / number_of_samples))


def _main(argsv):
    parser = argparse.ArgumentParser(description='Acquires a power spectrum using NI-RFSA.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of the NI RF signal analyzer.')
    parser.add_argument('-c', '--center-frequency', default=1e9, type=float, help='Center frequency in Hz.')
    parser.add_argument('-r', '--reference-level', default=-10.0, type=float, help='Reference level in dBm.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.center_frequency, args.reference_level)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5841', }, }
    example('simulated5841', options, 1e9, -10.0)


def test_main():
    cmd_line = ['--resource-name', 'simulated5841', '--center-frequency', '1e9', '--reference-level', '-10', '--option-string', 'Simulate=1, DriverSetup=Model:5841']
    _main(cmd_line)


if __name__ == '__main__':
    main()
