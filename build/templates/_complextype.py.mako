${template_parameters['encoding_tag']}
# This file was generated
<%
    import build.helper as helper
    config = template_parameters['metadata'].config
    module_name = config['module_name']
%>\
import ctypes
import ${module_name}._visatype as _visatype


class NIComplexNumber(ctypes.Structure):
    _fields_ = [("real", _visatype.ViReal64), ("imag", _visatype.ViReal64)]


class NIComplexNumberF32(ctypes.Structure):
    _fields_ = [("real", _visatype.ViReal32), ("imag", _visatype.ViReal32)]


class NIComplexI16(ctypes.Structure):
    _fields_ = [("real", _visatype.ViInt16), ("imag", _visatype.ViInt16)]

% if module_name == 'nirfsa':

class niRFSA_coefficientInfo(ctypes.Structure):
    _fields_ = [("offset", _visatype.ViReal64), ("gain", _visatype.ViReal64), ("reserved1", _visatype.ViReal64), ("reserved2", _visatype.ViReal64)]
% endif
