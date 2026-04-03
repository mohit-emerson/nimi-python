# -*- coding: utf-8 -*-
# This file was generated
import ctypes
import nirfsa._visatype as _visatype


class NIComplexNumber(ctypes.Structure):
    _fields_ = [("real", _visatype.ViReal64), ("imag", _visatype.ViReal64)]


class NIComplexNumberF32(ctypes.Structure):
    _fields_ = [("real", _visatype.ViReal32), ("imag", _visatype.ViReal32)]


class NIComplexI16(ctypes.Structure):
    _fields_ = [("real", _visatype.ViInt16), ("imag", _visatype.ViInt16)]


class niRFSA_coefficientInfo(ctypes.Structure):
    _fields_ = [("offset", _visatype.ViReal64), ("gain", _visatype.ViReal64), ("reserved1", _visatype.ViReal64), ("reserved2", _visatype.ViReal64)]
