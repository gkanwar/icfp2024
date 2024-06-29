import numpy as np

from evaluate import *
from ir import *

DV_TO_KEY = {
    (-1,-1): '1',
    (0,-1): '2',
    (1,-1): '3',
    (-1,0): '4',
    (0,0): '5',
    (1,0): '6',
    (-1,1): '7',
    (0,1): '8',
    (1,1): '9',
}
LABEL_TO_KEY = {
    'u': '8',
    'd': '2',
    'l': '4',
    'r': '6',
}

def solve(coords, name):
    coords = np.loadtxt(coords.split('\n'), dtype=int)
    coords = np.insert(coords, 0, np.array([(0,0), (0,0)]), axis=0)
    dx = coords[1:] - coords[:-1]
    dv = dx[1:] - dx[:-1]
    for i,x in enumerate(dv):
        if tuple(x) not in DV_TO_KEY:
            print(f'invalid solution on step {i}')
            break
    keys = ''.join(DV_TO_KEY[tuple(x)] for x in dv)
    print(f'[Str("solve {name} {keys}")]')


puzzles = {
    'spaceship1': '1 -1\n1 -3\n2 -5\n2 -8\n3 -10\n',
    'spaceship2': '0 1\n0 1\n-1 2\n-1 4\n0 7\n1 10\n3 12\n5 13\n7 14\n8 14\n8 13\n9 13\n10 14\n11 15\n12 15\n14 16\n17 16\n20 15\n22 15\n23 14\n25 12\n27 10\n29 8\n32 6\n35 4\n37 2\n40 -1\n44 -4\n49 -8\n53 -11\n58 -14\n63 -18\n68 -22\n72 -26\n77 -29\n81 -33\n85 -37\n88 -42\n90 -48\n92 -55\n94 -61\n95 -68\n95 -76\n94 -84\n93 -93\n92 -102\n92 -112\n92 -122\n93 -131\n94 -140\n',
    # 'spaceship3': '-1 1\n1 8\n4 15\n3 14\n3 13\n-1 3\n-1 0\n2 11\n0 5\n5 16\n',
    # manually augmented
    'spaceship3': '-1 1\n-1 2\n0 4\n1 6\n1 8\n2 11\n2 13\n3 14\n4 15\n4 15\n3 15\n3 14\n3 13\n2 12\n0 10\n-1 7\n-1 3\n-1 0\n0 -2\n1 -3\n2 -3\n2 -2\n2 0\n2 3\n2 7\n2 11\n1 14\n0 16\n0 17\n0 17\n0 16\n0 14\n0 11\n0 8\n0 5\n1 3\n2 2\n3 2\n4 3\n5 5\n5 8\n5 12\n5 16\n',
}

for k in puzzles:
    solve(puzzles[k], k)


y = [
    Lambda(0),
    BApply(),
    Lambda(1), BApply(), Var(0), BApply(), Var(1), Var(1),
    Lambda(1), BApply(), Var(0), BApply(), Var(1), Var(1),
]

def solve_spiral(name, *, n_iter):
    step_rec = [
        Lambda(4),
        Lambda(0), Lambda(1), Lambda(2),
        If(), BEq(), Var(0), Int([0]),
        Str(''),
        BCat(), Var(1), BCat(), Var(2),
        BApply(), BApply(), BApply(),
        Var(4),
        BMinus(), Var(0), Int([1]),
        Var(1), Var(2),
    ]
    step_test = [
        BApply(), BApply(), BApply(), BApply(),
    ] + y + step_rec + [
        Int([6]), Str(LABEL_TO_KEY['u']), Str(LABEL_TO_KEY['d'])
    ]
    step_prog = parse_all(step_test)
    assert eval_lazy(step_prog, Bindings())() == '82'*6

    solve_rec = [
        Lambda(4),
        Lambda(0), # i
        If(), BEq(), Var(0), Var(9), # i == n
        Str(''),
        BApply(),
        Lambda(8), # j = 2*i+1
        BCat(),
        BApply(), BApply(), BApply(), BApply(),
    ] + y + step_rec + [
        Var(8), Str(LABEL_TO_KEY['u']), Str(LABEL_TO_KEY['d']),
        BCat(),
        BApply(), BApply(), BApply(), BApply(),
    ] + y + step_rec + [
        Var(8), Str(LABEL_TO_KEY['r']), Str(LABEL_TO_KEY['l']),
        BCat(),
        BApply(), BApply(), BApply(), BApply(),
    ] + y + step_rec + [
        BPlus(), Int([1]), Var(8), Str(LABEL_TO_KEY['d']), Str(LABEL_TO_KEY['u']),
        BCat(),
        BApply(), BApply(), BApply(), BApply(),
    ] + y + step_rec + [
        BPlus(), Int([1]), Var(8), Str(LABEL_TO_KEY['l']), Str(LABEL_TO_KEY['r']),
        # recurse
        BApply(),
        Var(4), BPlus(), Var(0), Int([1]),
        # j = 2*i+1
        BPlus(), Int([1]), BMul(), Var(0), Int([2]),
    ]
    solve_full = [
        BCat(), Str(f'solve {name} '),
        BApply(), Lambda(9), # n
        BApply(), BApply(),
    ] + y + solve_rec + [
        Int([0]),
        Int(Int.to_digits(n_iter)),
    ]
    solve_prog = parse_all(solve_full)
    # print(eval_lazy(solve_prog, Bindings())())
    print(enc(solve_full))


# works for spaceship 4, with a very bad score!
solve_spiral(f'spaceship{4}', n_iter=200)
