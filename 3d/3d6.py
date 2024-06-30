'''
# Input
  `2 <= A <= 500`

# Output
  `1` if `A` is a prime number, and `0` otherwise.

# Example
  * `A = 5`
    `Answer = 1`
  * `A = 4`
    `Answer = 0`
'''

from sim import *

soln = '''
. . . . . . . . .
. . . . . . . . .
. > . . 0 . . . .
^ A % . = . . . .
. . . . S . . . .
^ . . A . 0 . . .
2 > . / . # . . .
v 1 . . . S . . .
. + . . . . . . .
. . > . > . . . .
. . . . 5 @ 4 . .
. . . . . 4 . . .
'''

def is_prime(A):
    for x in range(2, A):
        if A % x == 0:
            return False
    return True

for A in range(2, 50):
    ret, history = simulate(soln, A=A, max_iter=500)
    print(f'{ret=}')
    assert ret == int(is_prime(A)), f'{ret=} {A=}'
print('[Str(' + repr('solve 3d6\n'+soln) + ')]')
