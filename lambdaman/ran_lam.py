### Simple random walker
from evaluate import *
from ir import *

y = [
    Lambda(0),
    BApply(),
    Lambda(1), BApply(), Var(0), BApply(), Var(1), Var(1),
    Lambda(1), BApply(), Var(0), BApply(), Var(1), Var(1),
]

dir_str = [
    Lambda(0),
    If(), BEq(), Var(0), Int([0]), Str('D'),
    If(), BEq(), Var(0), Int([1]), Str('U'),
    If(), BEq(), Var(0), Int([2]), Str('R'),
    Str('L'),
]

def make_f_rec(g, p):
    return [
        Lambda(4), Lambda(0), Lambda(1),
        If(), BEq(), Var(0), Int([0]), Str(''),
        BCat(), BApply(),
    ] + dir_str + [
        BIMod(), Var(1), Int([4]),
        BApply(), BApply(), Var(4),
        BMinus(), Var(0), Int([1]),
        BIMod(), BMul(), Var(1), g, p,
    ]

def make_prog(seed, g, p, n):
    g = Int(Int.to_digits(g))
    p = Int(Int.to_digits(p))
    seed = Int(Int.to_digits(seed))
    return [
        BApply(), BApply(), BApply(),
    ] + y + make_f_rec(g, p) + [
        Int(Int.to_digits(n)), seed,
    ]
# g = 104729
# p = 131071
# f_test = make_prog(1, g, p, 10000)
# f_test_prog = parse_all(f_test)
# print(eval_lazy(f_test_prog, Bindings())())

# works except lam8, lam10
# for n in range(4, 11):
#     print(enc([BCat(), Str(f'solve lambdaman{n} ')] + f_test))
# good seed=8 for lam10
# print(enc([BCat(), Str('solve lambdaman10 ')] + make_prog(8, g, p, 100000)))

# for n in range(11, 21+1):
#     print(enc([BCat(), Str(f'solve lambdaman{n} ')] + make_prog(1000000)))


# NOTE: needed to be careful about finding a primitive root for max randness
p = 1000000009
g = 13
n = 1000000
# print(enc([BCat(), Str('solve lambdaman17 ')] + make_prog(1, g, p, n)))
print(enc([BCat(), Str('solve lambdaman21 ')] + make_prog(3, g, p, n)))
