import ctypes

import nirfsa._visatype


# This class is an internal implementation detail
# ctypes definition
# Name must match exactly what the name of the structure type is named in the C API.
class struct_niRFSA_wfmInfo(ctypes.Structure):  # noqa N801
    _pack_ = 8
    _fields_ = [
        ('absolute_initial_x', nirfsa._visatype.ViReal64),
        ('relative_initial_x', nirfsa._visatype.ViReal64),
        ('x_increment', nirfsa._visatype.ViReal64),
        ('actual_samples', nirfsa._visatype.ViInt64),
        ('offset', nirfsa._visatype.ViReal64),
        ('gain', nirfsa._visatype.ViReal64),
        ('reserved1', nirfsa._visatype.ViReal64),
        ('reserved2', nirfsa._visatype.ViReal64),
    ]

    def __init__(self, data=None, absolute_initial_x=0.0, relative_initial_x=0.0,
                 x_increment=0.0, actual_samples=0, offset=0.0, gain=0.0,
                 reserved1=0.0, reserved2=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.absolute_initial_x = data.absolute_initial_x
            self.relative_initial_x = data.relative_initial_x
            self.x_increment = data.x_increment
            self.actual_samples = data.actual_samples
            self.offset = data.offset
            self.gain = data.gain
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
        else:
            self.absolute_initial_x = absolute_initial_x
            self.relative_initial_x = relative_initial_x
            self.x_increment = x_increment
            self.actual_samples = actual_samples
            self.offset = offset
            self.gain = gain
            self.reserved1 = reserved1
            self.reserved2 = reserved2


class WaveformInfo:
    '''Python-friendly wrapper for niRFSA waveform info'''

    def __init__(self, data=None, absolute_initial_x=0.0, relative_initial_x=0.0,
                 x_increment=0.0, actual_samples=0, offset=0.0, gain=0.0,
                 reserved1=0.0, reserved2=0.0):
        if data is not None:
            self.absolute_initial_x = data.absolute_initial_x
            self.relative_initial_x = data.relative_initial_x
            self.x_increment = data.x_increment
            self.actual_samples = data.actual_samples
            self.offset = data.offset
            self.gain = data.gain
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
        else:
            self.absolute_initial_x = absolute_initial_x
            self.relative_initial_x = relative_initial_x
            self.x_increment = x_increment
            self.actual_samples = actual_samples
            self.offset = offset
            self.gain = gain
            self.reserved1 = reserved1
            self.reserved2 = reserved2

    def _create_copy(self, target_class):
        return target_class(
            absolute_initial_x=self.absolute_initial_x,
            relative_initial_x=self.relative_initial_x,
            x_increment=self.x_increment,
            actual_samples=self.actual_samples,
            offset=self.offset,
            gain=self.gain,
            reserved1=self.reserved1,
            reserved2=self.reserved2
        )

    def __repr__(self):
        return (
            f'{self.__class__.__name__}(data=None, '
            f'absolute_initial_x={self.absolute_initial_x}, '
            f'relative_initial_x={self.relative_initial_x}, '
            f'x_increment={self.x_increment}, '
            f'actual_samples={self.actual_samples}, '
            f'offset={self.offset}, '
            f'gain={self.gain}, '
            f'reserved1={self.reserved1}, '
            f'reserved2={self.reserved2})'
        )

    def __str__(self):
        return self.__repr__()
