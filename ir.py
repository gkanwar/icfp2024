from typing import Any, Callable, Optional

ASCII_BASE = 33
ASCII_CHARS = [chr(i) for i in range(ASCII_BASE, ASCII_BASE+94)]

class IRNode:
    IND: str
    def enc(self) -> str:
        raise NotImplementedError()

ALL_OPS = [] # hack for convenience
def dec_token(s):
    assert len(s) > 0
    ind = s[0]
    for op in ALL_OPS:
        if ind == op.IND:
            return op.dec(s)
    raise RuntimeError(f'could not decode token {s}')

def dec(s):
    """Decode (lex) input string into sequence of IR tokens"""
    return [dec_token(tok) for tok in s.strip().split()]
def enc(tokens):
    """Encode sequence of IR tokens into output string"""
    return ' '.join(tok.enc() for tok in tokens)


### CORE
class BoolT(IRNode):
    IND = 'T'
    def enc(self):
        return self.IND
    @classmethod
    def dec(cls, s):
        assert s[0] == cls.IND
        assert len(s) == 1
        return cls()
class BoolF(IRNode):
    IND = 'F'
    def enc(self):
        return self.IND
    @classmethod
    def dec(cls, s):
        assert s[0] == cls.IND
        assert len(s) == 1
        return cls()
ALL_OPS.extend([BoolT, BoolF])

def dec_digits(s):
    return [ord(c) - ASCII_BASE for c in s]
def enc_digits(digits):
    return ''.join(ASCII_CHARS[x] for x in digits)

class Int(IRNode):
    """Integer represented by base-94 digits"""
    BASE = 94
    IND = 'I'

    def __init__(self, digits):
        self.digits = digits
        self.value = self.from_digits(digits)

    @staticmethod
    def from_digits(digits):
        value = 0
        for d in digits:
            value *= Int.BASE
            value += d
        return value

    @staticmethod
    def to_digits(value):
        if value == 0:
            return [0]
        digits = []
        while value > 0:
            digits.insert(0, value % Int.BASE)
            value //= Int.BASE
        return digits

    def enc(self):
        assert len(ASCII_CHARS) >= self.BASE
        return self.IND + enc_digits(self.digits)

    @classmethod
    def dec(cls, s):
        assert s[0] == cls.IND
        return cls(dec_digits(s[1:]))
ALL_OPS.append(Int)

class Str(IRNode):
    """Custom ascii string"""
    ALPHABET = (
        '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'''
        '''!"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n'''
    )
    IND = 'S'

    def __init__(self, s):
        self.value = s

    def enc(self):
        return self.IND + ''.join(ASCII_CHARS[self.ALPHABET.index(c)] for c in self.value)

    @classmethod
    def dec(cls, s):
        assert s[0] == cls.IND
        return cls(''.join(cls.ALPHABET[ASCII_CHARS.index(c)] for c in s[1:]))
ALL_OPS.append(Str)


### UNARY
UN_OPS = [] # hack for convenience
class Unary(IRNode):
    IND = 'U'
    BODY: str
    F: Callable[[Any], Any]
    arg1: Optional[IRNode] = None
    def enc(self):
        assert len(self.BODY) == 1
        return self.IND + self.BODY
    @staticmethod
    def dec(s):
        assert s[0] == Unary.IND
        assert len(s) == 2
        for op in UN_OPS:
            if s[1] == op.BODY:
                return op()
        raise ValueError(f'invalid unary op {s[1]}')
ALL_OPS.append(Unary)

def s2i(s):
    tok = Str(s).enc()
    value = Int.dec('I' + tok[1:]).value
    # print(f's2i {value}')
    return value
def i2s(x):
    tok = Int(Int.to_digits(x)).enc()
    return Str.dec('S' + tok[1:]).value

class UNeg(Unary):
    BODY = '-'
    F = staticmethod(lambda x: -x())
class UNot(Unary):
    BODY = '!'
    F = staticmethod(lambda x: not x())
class US2I(Unary):
    BODY = '#'
    F = staticmethod(lambda x: s2i(x()))
class UI2S(Unary):
    BODY = '$'
    F = staticmethod(lambda x: i2s(x()))
class UPrint(Unary):
    BODY = 'P'
    def __init__(self, prefix):
        self.prefix = prefix
    def F(self, x):
        print(self.prefix, x())
        return x()
    def enc(self):
        return ''
UN_OPS.extend([UNeg, UNot, US2I, UI2S, UPrint])


### BINARY
BIN_OPS = [] # hack for convenience
class Binary(IRNode):
    IND = 'B'
    BODY: str
    F: Callable[[Any,Any], Any]
    arg1: Optional[IRNode] = None
    arg2: Optional[IRNode] = None
    def enc(self):
        assert len(self.BODY) == 1
        return self.IND + self.BODY
    @staticmethod
    def dec(s):
        assert s[0] == Binary.IND
        assert len(s) == 2
        for op in BIN_OPS:
            if s[1] == op.BODY:
                return op()
        raise ValueError(f'invalid binary op {s[1]}')
ALL_OPS.append(Binary)

def idiv(x, y):
    assert isinstance(x, int) and isinstance(y, int)
    if x < 0:
        return -idiv(-x, y)
    else:
        return x // y
def imod(x, y):
    assert isinstance(x, int) and isinstance(y, int)
    return x - idiv(x,y)*y
def strcat(x, y):
    assert isinstance(x, str) and isinstance(y, str), f'{x=} {y=}'
    return x+y
def strtake(x, y):
    assert isinstance(x, int) and isinstance(y, str), f'{x=} {y=}'
    # print(f'strtake {y[:x]}')
    return y[:x]
def strdrop(x, y):
    assert isinstance(x, int) and isinstance(y, str), f'{x=} {y=}'
    # print(f'strdrop {y[x:]}')
    return y[x:]

class BPlus(Binary):
    BODY = '+'
    F = staticmethod(lambda x,y: x() + y())
class BMinus(Binary):
    BODY = '-'
    F = staticmethod(lambda x,y: x() - y())
class BMul(Binary):
    BODY = '*'
    F = staticmethod(lambda x,y: x() * y())
class BIDiv(Binary):
    BODY = '/'
    F = staticmethod(lambda x,y: idiv(x(), y()))
class BIMod(Binary):
    BODY = '%'
    F = staticmethod(lambda x,y: imod(x(), y()))
class BILess(Binary):
    BODY = '<'
    F = staticmethod(lambda x,y: x() < y())
class BIGtr(Binary):
    BODY = '>'
    F = staticmethod(lambda x,y: x() > y())
class BEq(Binary):
    BODY = '='
    F = staticmethod(lambda x,y: x() == y())
class BOr(Binary):
    BODY = '|'
    F = staticmethod(lambda x,y: x() or y())
class BAnd(Binary):
    BODY = '&'
    F = staticmethod(lambda x,y: x() and y())
class BCat(Binary):
    BODY = '.'
    F = staticmethod(lambda x,y: strcat(x(), y()))
class BTake(Binary):
    BODY = 'T'
    F = staticmethod(lambda x,y: strtake(x(), y()))
class BDrop(Binary):
    BODY = 'D'
    F = staticmethod(lambda x,y: strdrop(x(), y()))
class BApply(Binary):
    BODY = '$'
    F = staticmethod(lambda x,y: x()(y))
BIN_OPS.extend([
    BPlus, BMinus, BMul, BIDiv, BIMod, BILess, BIGtr, BEq, BOr, BAnd, BCat,
    BTake, BDrop, BApply
])


### CONTROL
class If(IRNode):
    IND = '?'
    arg1: Optional[IRNode] = None
    arg2: Optional[IRNode] = None
    arg3: Optional[IRNode] = None
    def enc(self):
        return self.IND
    @classmethod
    def dec(cls, s):
        assert s[0] == cls.IND
        assert len(s) == 1
        return cls()
ALL_OPS.append(If)

class Lambda(IRNode):
    IND = 'L'
    arg1: Optional[IRNode] = None
    def __init__(self, bind: int):
        self.bind = bind
    def enc(self):
        return self.IND + enc_digits(Int.to_digits(self.bind))
    @classmethod
    def dec(cls, s):
        assert s[0] == cls.IND
        assert len(s) >= 2
        return cls(Int.from_digits(dec_digits(s[1:])))
    def __repr__(self):
        return f'L{self.bind}'
ALL_OPS.append(Lambda)

class Var(IRNode):
    IND = 'v'
    def __init__(self, bind: int):
        self.bind = bind
    def enc(self):
        return self.IND + enc_digits(Int.to_digits(self.bind))
    @classmethod
    def dec(cls, s):
        assert s[0] == cls.IND
        assert len(s) >= 2
        return cls(Int.from_digits(dec_digits(s[1:])))
    def __repr__(self):
        return f'v{self.bind}'
ALL_OPS.append(Var)
