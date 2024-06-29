from ir import *

def fmt(prog):
    """Format a sequence of IR tokens to be printable"""
    out = []
    for tok in prog:
        if isinstance(tok, Str):
            out.append(repr(tok.value))
        elif isinstance(tok, Int):
            out.append(tok.enc() + f'({tok.value})')
        elif isinstance(tok, Lambda):
            out.append(f'L{tok.bind}')
        elif isinstance(tok, Var):
            out.append(f'v{tok.bind}')
        else:
            out.append(tok.enc())
    return ' '.join(out)
