# Stubs for numbers (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Number:
    __hash__ = ... # type: Any

class Complex(Number):
    def __complex__(self): ...
    def __bool__(self): ...
    @property
    def real(self): ...
    @property
    def imag(self): ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __neg__(self): ...
    def __pos__(self): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def __pow__(self, exponent): ...
    def __rpow__(self, base): ...
    def __abs__(self): ...
    def conjugate(self): ...
    def __eq__(self, other): ...

class Real(Complex):
    def __float__(self): ...
    def __trunc__(self): ...
    def __floor__(self): ...
    def __ceil__(self): ...
    def __round__(self, ndigits=None): ...
    def __divmod__(self, other): ...
    def __rdivmod__(self, other): ...
    def __floordiv__(self, other): ...
    def __rfloordiv__(self, other): ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __complex__(self): ...
    @property
    def real(self): ...
    @property
    def imag(self): ...
    def conjugate(self): ...

class Rational(Real):
    @property
    def numerator(self): ...
    @property
    def denominator(self): ...
    def __float__(self): ...

class Integral(Rational):
    def __int__(self): ...
    def __index__(self): ...
    def __pow__(self, exponent, modulus=None): ...
    def __lshift__(self, other): ...
    def __rlshift__(self, other): ...
    def __rshift__(self, other): ...
    def __rrshift__(self, other): ...
    def __and__(self, other): ...
    def __rand__(self, other): ...
    def __xor__(self, other): ...
    def __rxor__(self, other): ...
    def __or__(self, other): ...
    def __ror__(self, other): ...
    def __invert__(self): ...
    def __float__(self): ...
    @property
    def numerator(self): ...
    @property
    def denominator(self): ...
