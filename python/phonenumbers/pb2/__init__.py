"""Translate python-phonenumbers PhoneNumber to/from protobuf PhoneNumber

Examples of use:

>>> import phonenumbers
>>> from phonenumbers.pb2 import phonenumber_pb2, PBToPy, PyToPB
>>> x_py = phonenumbers.PhoneNumber(country_code=44, national_number=7912345678)
>>> print x_py
Country Code: 44 National Number: 7912345678 Leading Zero: False
>>> y_pb = phonenumber_pb2.PhoneNumber()
>>> y_pb.country_code = 44
>>> y_pb.national_number = 7912345678
>>> print str(y_pb).strip()
country_code: 44
national_number: 7912345678
>>> # Although italian_leading_zero is not set and doesn't appear in string representation
>>> y_pb.italian_leading_zero
False
>>> y_py = PBToPy(y_pb)
>>> print y_py
Country Code: 44 National Number: 7912345678 Leading Zero: False
>>> x_pb = PyToPB(x_py)
>>> print str(x_pb).strip()
country_code: 44
national_number: 7912345678
italian_leading_zero: false
>>> x_py == y_py
True
>>> # Protobuf versions are *not* equal, because one has False and one has (unset) for italian_leading_zero
>>> x_pb == y_pb
False
>>> # Explicitly set the field
>>> y_pb.italian_leading_zero = y_pb.italian_leading_zero
>>> x_pb == y_pb
True
"""

from phonenumber_pb2 import PhoneNumber as PhoneNumberPB
from phonenumbers import PhoneNumber

def PBToPy(numpb):
    """Convert phonenumber_pb2.PhoneNumber to phonenumber.PhoneNumber"""
    return PhoneNumber(numpb.country_code if numpb.HasField("country_code") else None,
                       numpb.national_number if numpb.HasField("national_number") else None,
                       numpb.extension if numpb.HasField("extension") else None,
                       numpb.italian_leading_zero if numpb.HasField("italian_leading_zero") else False,
                       numpb.raw_input if numpb.HasField("raw_input") else None,
                       numpb.country_code_source if numpb.HasField("country_code_source") else None,
                       numpb.preferred_domestic_carrier_code if numpb.HasField("preferred_domestic_carrier_code") else None)

def PyToPB(numobj):
    """Convert phonenumber.PhoneNumber to phonenumber_pb2.PhoneNumber"""
    numpb = PhoneNumberPB()
    if numobj.country_code is not None:
        numpb.country_code = numobj.country_code
    if numobj.national_number is not None:
        numpb.national_number = numobj.national_number
    if numobj.extension is not None:
        numpb.extension = numobj.extension
    # For italian_leading_zero, the Python object has two states (True/False),
    # but the protobuf version has three states (True/False/NotSet), and the
    # NotSet state is effectively False.
    numpb.italian_leading_zero = numobj.italian_leading_zero
    if numobj.raw_input is not None:
        numpb.raw_input = numobj.raw_input
    if numobj.country_code_source is not None:
        numpb.country_code_source = numobj.country_code_source
    if numobj.preferred_domestic_carrier_code is not None:
        numpb.preferred_domestic_carrier_code = numobj.preferred_domestic_carrier_code
    return numpb

__all__ = ['PBToPy', 'PyToPB']

if __name__ == '__main__':  # pragma no cover
    import doctest
    doctest.testmod()
