import ctypes
import nirfsa._visatype


# This class is an internal ctypes implementation detail that corresponds to
# niRFSA_coefficientInfo in the C API
class struct_niRFSA_coefficientInfo(ctypes.Structure):  # noqa N801
    _pack_ = 8
    _fields_ = [
        ('offset', nirfsa._visatype.ViReal64),
        ('gain', nirfsa._visatype.ViReal64),
        ('reserved1', nirfsa._visatype.ViReal64),
        ('reserved2', nirfsa._visatype.ViReal64),
    ]

    def __init__(self, data=None, offset=0.0, gain=0.0,
                 reserved1=0.0, reserved2=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.offset = data.offset
            self.gain = data.gain
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
        else:
            self.offset = offset
            self.gain = gain
            self.reserved1 = reserved1
            self.reserved2 = reserved2


class CoefficientInfo:
    """Python-friendly wrapper for niRFSA coefficient info."""

    def __init__(self, data=None, offset=0.0, gain=0.0,
                 reserved1=0.0, reserved2=0.0):
        if data is not None:
            self.offset = data.offset
            self.gain = data.gain
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
        else:
            self.offset = offset
            self.gain = gain
            self.reserved1 = reserved1
            self.reserved2 = reserved2

    def _create_copy(self, target_class):
        try:
            return target_class(
                offset=self.offset,
                gain=self.gain,
                reserved1=self.reserved1,
                reserved2=self.reserved2,
            )
        except TypeError:
            return target_class(data=self)

    def __repr__(self):
        return "{}.{}(offset={}, gain={}, reserved1={}, reserved2={})".format(
            self.__class__.__module__,
            self.__class__.__qualname__,
            self.offset,
            self.gain,
            self.reserved1,
            self.reserved2,
        )

    def __str__(self):
        return self.__repr__()
