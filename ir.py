ASCII_BASE = 33
ASCII_CHARS = [chr(i) for i in range(ASCII_BASE, ASCII_BASE+94)]

class IRNode:
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
    return [dec_token(tok) for tok in s.strip().split(' ')]
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

class Int(IRNode):
    """Integer represented by base-94 digits"""
    BASE = 94
    IND = 'I'

    def __init__(self, digits):
        self.digits = digits
        value = 0
        for d in self.digits:
            value *= Int.BASE
            value += d
        self.value = value

    def enc(self):
        assert len(ASCII_CHARS) >= self.BASE
        return self.IND + ''.join(ASCII_CHARS[x] for x in self.digits)

    @classmethod
    def dec(cls, s):
        assert s[0] == cls.IND
        digits = [ord(c) - ASCII_BASE for c in s[1:]]
        return cls(digits)
ALL_OPS.append(Int)

class Str(IRNode):
    """Custom ascii string"""
    ALPHABET = (
        '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'''
        '''!"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n'''
    )
    IND = 'S'

    def __init__(self, s):
        self.s = s

    def enc(self):
        return self.IND + ''.join(ASCII_CHARS[self.ALPHABET.index(c)] for c in self.s)

    @classmethod
    def dec(cls, s):
        assert s[0] == cls.IND
        return cls(''.join(cls.ALPHABET[ASCII_CHARS.index(c)] for c in s[1:]))
ALL_OPS.append(Str)


### UNARY
UN_OPS = [] # hack for convenience
class Unary(IRNode):
    kind: str
    IND = 'U'
    BODY = '?'
    def enc(self):
        assert len(self.kind) == 1
        return self.IND + self.kind
    @staticmethod
    def dec(s):
        assert s[0] == Unary.IND
        assert len(s) == 2
        for op in UN_OPS:
            if s[1] == op.BODY:
                return op()
        raise ValueError(f'invalid unary op {s[1]}')
ALL_OPS.append(Unary)

class UNeg(Unary):
    BODY = '-'
class UNot(Unary):
    BODY = '!'
class US2I(Unary):
    BODY = '#'
class UI2S(Unary):
    BODY = '$'
UN_OPS.extend([UNeg, UNot, US2I, UI2S])


### BINARY
BIN_OPS = [] # hack for convenience
class Binary(IRNode):
    IND = 'B'
    BODY = '?'
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

class BPlus(Binary):
    BODY = '+'
class BMinus(Binary):
    BODY = '-'
class BMul(Binary):
    BODY = '*'
class BIDiv(Binary):
    BODY = '/'
class BIMod(Binary):
    BODY = '%'
class BILess(Binary):
    BODY = '<'
class BIGtr(Binary):
    BODY = '>'
class BEq(Binary):
    BODY = '='
class BOr(Binary):
    BODY = '|'
class BAnd(Binary):
    BODY = '&'
class BCat(Binary):
    BODY = '.'
class BTake(Binary):
    BODY = 'T'
class BDrop(Binary):
    BODY = 'D'
class BApply(Binary):
    BODY = '$'
BIN_OPS.extend([
    BPlus, BMinus, BMul, BIDiv, BIMod, BILess, BIGtr, BEq, BOr, BAnd, BCat,
    BTake, BDrop, BApply
])


### CONTROL
class If(IRNode):
    IND = '?'
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
    def __init__(self, bind):
        # bound variable name in encoded form (no need to decode to int)
        self.bind = bind
    def enc(self):
        return self.IND + self.bind
    @classmethod
    def dec(cls, s):
        assert s[0] == cls.IND
        assert len(s) == 2
        return cls(s[1])
ALL_OPS.append(Lambda)

class Var(IRNode):
    IND = 'v'
    def __init__(self, name):
        # variable name in encoded form (no need to decode to int)
        self.name = name
    def enc(self):
        return self.IND + self.name
    @classmethod
    def dec(cls, s):
        assert s[0] == cls.IND
        assert len(s) == 2
        return cls(s[1])
ALL_OPS.append(Var)
