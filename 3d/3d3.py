from sim import *

'''
# Input
  `-100 <= A <= 100`

# Output
  The sign of `A`, which is `-1` for negative numbers, `0` for `0`, and `1` for positive numbers.

# Example
  * `A = 3`
    `Answer = 1`
  * `A = -6`
    `Answer = -1`
'''

soln = '''
. 1 . 0 . . .
. = A = S . .
^ S . 99 . -1 .
A > . + . = .
v 1 . . . S .
. - . . . . .
. . . . . . .
1 @ 4 . . . .
. 2 . . . . .
'''

def sign(x):
    if x == 0: return x
    return x / abs(x)

for A in range(-10, 10):
    ret, history = simulate(soln, A=A, max_iter=300)
    print(f'{ret=}')
    assert ret == sign(A)
print('[Str(' + repr('solve 3d3\n'+soln) + ')]')
