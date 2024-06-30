'''
# Input
  `1 <= A <= 500` and `1 <= B <= 500`

# Output
  The least common multiple (LCM) of `A` and `B`, e.g. the smallest positive number that is divisible by both `A` and `B`.

# Example
  * `A = 3`
    `B = 7`
    `Answer = 21`
  * `A = 2`
    `B = 6`
    `Answer = 6`
'''

import math
from sim import *

soln = '''
. . . . . . . . .
. . . . . B . 0 .
A > . > . % . = .
v . . A . . . . .
. > . % . = . + .
v . . . . . . . .
. > . > . > . + .
v A . . . . . S .
. + . . . . . . .
. . > . > . . . .
. . 3 @ 8 . . . .
. . . 5 . . . . .
'''

for A, B in [(1, 1), (2, 6), (2, 3), (12, 15), (491, 499)]:
    ret, history = simulate(soln, A=A, B=B, max_iter=1000000)
    print(f'{ret=}')
    assert ret == math.lcm(A, B)
print('[Str(' + repr('solve 3d5\n'+soln) + ')]')
