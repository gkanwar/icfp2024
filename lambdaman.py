### Lambdaman puzzles

from evaluate import *
from ir import *

soln_lambda1 = [Str("solve lambdaman1 UDLLLDURRRRRURR")]
soln_lambda2 = [Str("solve lambdaman2 RDURRDDRRUUDDLLLDLLDDRRRUR")]
soln_lambda3 = [Str("solve lambdaman3 DRDRLLLUDLLUURURLLURLUURRRRRDLLLRDRRDLRD")]

y = [
    Lambda(0),
    BApply(),
    Lambda(1), BApply(), Var(0), BApply(), Var(1), Var(1),
    Lambda(1), BApply(), Var(0), BApply(), Var(1), Var(1),
]
    
move_rec = [
    Lambda(4),
    Lambda(0), Lambda(1),
    If(), BEq(), Var(0), Int([0]),
    Str(''),
    BCat(), Var(1),
    BApply(),
    BApply(), Var(4),
    BMinus(), Var(0), Int([1]),
    Var(1),
]

# recursion with y-combinator!
move_test = [
    BApply(), BApply(), BApply(),
] + y + move_rec + [Int([2,11]), Str('R')]
move_test_prog = parse_all(move_test)
# print(move_test_prog)
assert eval_lazy(move_test_prog, Bindings())() == 'R'*199
print(enc([BCat(), Str("solve lambdaman6 ")] + move_test))

compute_rec = [
    Lambda(4),
    # compute(s, l)
    Lambda(0), Lambda(2),
    # if l == 0
    If(), BEq(), Var(2), Int([0]),
    Str(''),
    # else let n,d = s2i(take(1, s)), take(1, drop(1, s))
    BApply(), BApply(),
    Lambda(8), Lambda(9),
    # move(n, d) .
    BCat(),
    BApply(), BApply(), BApply(),
] + y + move_rec + [
    Var(8), Var(9),
    # compute(drop(2, s), l-2)
    BApply(), BApply(), Var(4),
    # drop (2, s)
    BDrop(), Int([2]), Var(0),
    # l-2
    BMinus(), Var(2), Int([2]),
    # feed n,d
    US2I(), BTake(), Int([1]), Var(0),
    BTake(), Int([1]), BDrop(), Int([1]), Var(0),
]

compute_test = [
    BApply(), BApply(), BApply(),
] + y + compute_rec + [Str(
    chr(ord(Str.ALPHABET[0])+6) + 'D' +
    chr(ord(Str.ALPHABET[0])+4) + 'U'
), Int([4])]
compute_test_prog = parse_all(compute_test)
print(eval_lazy(compute_test_prog, Bindings())())
print(len(enc(compute_test)))


#####################
#...#.#.........#...#
#.###.#.#####.###.###
#...#.#.....#.......#
###.#.#.###.#########
#.#....L..#.#.......#
#.#####.###.#.###.###
#.#.#...#.......#...#
#.#.#######.#######.#
#.#...#.#...#.#.....#
#.#.###.#.###.###.#.#
#.....#...#.......#.#
#.###.###.###.#####.#
#.#.#...#...#...#...#
###.#.#.#.#####.###.#
#...#.#...#.....#...#
#.###.#.#.#####.#####
#.....#.#.....#.#...#
#.###.#.#.#.#.#.#.###
#.#...#.#.#.#.#.....#
#####################


### Lambdaman 8
