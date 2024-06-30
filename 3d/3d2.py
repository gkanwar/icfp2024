from sim import *

# Problem 2: Absolute value without comparison operators.
# we can use properties of C modulo (A mod -A) = 1

'''
# Input
  `-100 <= A <= 100`

# Output
  The absolute value of `A`.

# Example
  * `A = 3`
    `Answer = 3`
  * `A = -6`
    `Answer = 6`
'''

print('[Str('+repr('''solve 3d2
. . . 1 . . . .
. . A + . . 0 .
. . . . . A = S
A > . # . % . .
v 1 . . . . . 1
. - . % . * . +
. . . . . . . S
''')+')]')

# print('[Str('+repr('''solve 3d2
soln = '''
. A . -1 .
. = A * .
^ S . . .
0 > . = S
v 1 . . .
. + . . .
. . . . .
1 @ 4 . .
. 2 . . .
'''

for A in range(-10, 10):
    ret, history = simulate(soln, A=A, max_iter=50)
    print(f'{ret=}')
    assert ret == abs(A)
print('[Str(' + repr('solve 3d2\n'+soln) + ')]')
