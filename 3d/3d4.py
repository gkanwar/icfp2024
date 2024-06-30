from sim import *

'''
# Input
  `-100 <= A <= 100` and `-100 <= B <= 100`

# Output
  The maximum of `A` and `B`.

# Example
  * `A = 3`
    `B = 7`
    `Answer = 7`
  * `A = -2`
    `B = -6`
    `Answer = -2`
'''
soln = '''
. 1 . B . . . .
A + . = . . . .
. . . S 1 . A .
1 @ 2 B + B = .
. 1 . . . . S .
. . . 1 @ 2 . .
. . . . 1 . . .
'''

for A, B in [(-3,6), (6,-3), (6,6), (3,3), (3,-9)]:
    print(f'== {A} {B} ==')
    ret, history = simulate(soln, A=A, B=B, max_iter=100)
    print(f'{ret=}')
    assert ret == max(A, B), f'{ret=} {A=} {B=}'
print('[Str(' + repr('solve 3d4\n'+soln) + ')]')
