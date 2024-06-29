import copy
from ir import *
from typing import TypeAlias

ZERO_ARG_OPS = [
    BoolT, BoolF, Int, Str, Var,
]
def parse(tokens: list[IRNode], i) -> int:
    """
    Parse list of tokens into an expression tree. Uses in-place pointer
    assignment on the existing tokens for simplicity.
    """
    assert len(tokens) > i
    op = tokens[i]
    j = i+1
    if any(isinstance(op, x) for x in ZERO_ARG_OPS):
        return j
    elif isinstance(op, Lambda):
        op.arg1 = tokens[j]
        return parse(tokens, j)
    elif isinstance(op, Unary):
        op.arg1 = tokens[j]
        return parse(tokens, j)
    elif isinstance(op, Binary):
        op.arg1 = tokens[j]
        j = parse(tokens, j)
        op.arg2 = tokens[j]
        return parse(tokens, j)
    elif isinstance(op, If):
        op.arg1 = tokens[j]
        j = parse(tokens, j)
        op.arg2 = tokens[j]
        j = parse(tokens, j)
        op.arg3 = tokens[j]
        return parse(tokens, j)
    else:
        raise ValueError(f'Unknown token {op}')

def parse_all(tokens: list[IRNode]):
    l = parse(tokens, 0)
    assert l == len(tokens), 'leftover program tokens'
    return tokens[0]

# def token_has_args(tok: IRNode):
#     """Validate token args have been assigned"""
#     if any(isinstance(tok, x) for x in ZERO_ARG_OPS):
#         return True
#     elif isinstance(tok, Lambda) or isinstance(tok, Unary):
#         return tok.arg1 is not None
#     elif isinstance(tok, Binary):
#         return tok.arg1 is not None and tok.arg2 is not None
#     elif isinstance(tok, If):
#         return tok.arg1 is not None and tok.arg2 is not None and tok.arg3 is not None
#     else:
#         raise ValueError(f'Unknown token {tok}')
    
class CachedLazy:
    def __init__(self, x):
        self.x = x
    def __call__(self):
        while callable(self.x):
            try:
                self.x = self.x()
            except TypeError:
                break
        return self.x

Thunk: TypeAlias = Callable[[],Any]

class Bindings:
    bindings: dict[int, list[Thunk]]
    def __init__(self):
        self.bindings = {}
    def get(self, bind: int):
        return self.bindings[bind][-1]
    def push(self, bind: int, value: Thunk):
        if bind not in self.bindings:
            self.bindings[bind] = []
        self.bindings[bind].append(value)
    def pop(self, bind: int):
        assert bind in self.bindings
        assert len(self.bindings[bind]) >= 1
        self.bindings[bind].pop()
        if len(self.bindings[bind]) == 0:
            del self.bindings[bind]

def eval_lazy(prog: IRNode, bindings: Bindings) -> Thunk:
    """Evaluate a parsed program."""
    if isinstance(prog, BoolT):
        return lambda: True
    elif isinstance(prog, BoolF):
        return lambda: False
    elif isinstance(prog, Int):
        return lambda: prog.value
    elif isinstance(prog, Str):
        return lambda: prog.value
    elif isinstance(prog, Lambda):
        assert prog.arg1 is not None
        body_prog = prog.arg1
        # TODO: more efficient alternative?
        local_bindings = copy.deepcopy(bindings)
        def call(x):
            local_bindings.push(prog.bind, x)
            body = eval_lazy(body_prog, local_bindings)
            local_bindings.pop(prog.bind)
            return body
        return lambda: call
    elif isinstance(prog, Var):
        return bindings.get(prog.bind)
    elif isinstance(prog, Unary):
        assert prog.arg1 is not None
        arg1 = eval_lazy(prog.arg1, bindings)
        f = prog.F
        return CachedLazy(lambda: f(arg1))
    elif isinstance(prog, Binary):
        assert prog.arg1 is not None
        assert prog.arg2 is not None
        arg1 = eval_lazy(prog.arg1, bindings)
        arg2 = eval_lazy(prog.arg2, bindings)
        f = prog.F
        return CachedLazy(lambda: f(arg1, arg2))
    elif isinstance(prog, If):
        assert prog.arg1 is not None
        assert prog.arg2 is not None
        assert prog.arg3 is not None
        arg1 = eval_lazy(prog.arg1, bindings)
        arg2 = eval_lazy(prog.arg2, bindings)
        arg3 = eval_lazy(prog.arg3, bindings)
        return CachedLazy(lambda: arg2 if arg1() else arg3)
    else:
        raise ValueError(f'unknown node type {prog}')
