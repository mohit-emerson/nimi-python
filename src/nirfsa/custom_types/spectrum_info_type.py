import ctypes

import nirfsa._visatype


# This class is an internal implementation detail
# ctypes definition
# Name must match exactly what the name of the structure type is named in the C API.
class struct_niRFSA_spectrumInfo(ctypes.Structure):  # noqa N801
    _pack_ = 8
    _fields_ = [
        ('initial_frequency', nirfsa._visatype.ViReal64),
        ('frequency_increment', nirfsa._visatype.ViReal64),
        ('number_of_spectral_lines', nirfsa._visatype.ViInt32),
        ('reserved', nirfsa._visatype.ViReal64),
    ]

    def __init__(self, data=None, initial_frequency=0.0, frequency_increment=0.0,
                 number_of_spectral_lines=0, reserved=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.initial_frequency = data.initial_frequency
            self.frequency_increment = data.frequency_increment
            self.number_of_spectral_lines = data.number_of_spectral_lines
            self.reserved = data.reserved
        else:
            self.initial_frequency = initial_frequency
            self.frequency_increment = frequency_increment
            self.number_of_spectral_lines = number_of_spectral_lines
            self.reserved = reserved


class SpectrumInfoT:
    '''Python-friendly wrapper for niRFSA spectrum info'''

    def __init__(self, data=None, initial_frequency=0.0, frequency_increment=0.0,
                 number_of_spectral_lines=0, reserved=0.0):
        if data is not None:
            self.initial_frequency = data.initial_frequency
            self.frequency_increment = data.frequency_increment
            self.number_of_spectral_lines = data.number_of_spectral_lines
            self.reserved = data.reserved
        else:
            self.initial_frequency = initial_frequency
            self.frequency_increment = frequency_increment
            self.number_of_spectral_lines = number_of_spectral_lines
            self.reserved = reserved

    def _create_copy(self, target_class):
        return target_class(
            initial_frequency=self.initial_frequency,
            frequency_increment=self.frequency_increment,
            number_of_spectral_lines=self.number_of_spectral_lines,
            reserved=self.reserved
        )

    def __repr__(self):
        return (
            f'{self.__class__.__name__}(data=None, '
            f'initial_frequency={self.initial_frequency}, '
            f'frequency_increment={self.frequency_increment}, '
            f'number_of_spectral_lines={self.number_of_spectral_lines}, '
            f'reserved={self.reserved})'
        )

    def __str__(self):
        return self.__repr__()
