from sim import *

'''
# Input
  `1 <= A <= 100`

# Output
  The factorial of `A`.
  `A! = 1 * 2 * .. * (A - 1) * A`

# Example
  * `A = 5`
    `Answer = 120`
'''

# this gadget works to produce 1!, 2!, and 3! on tick 3
test = '''test 3d 1 0
. . . < A > . . .
. 1 = . v 3 = . .
. . . . . . . . .
. . v 2 = 2 * . .
. . . . . > . . .
'''

soln = '''
. . . . . . . 2 . . .
. . . < . < A = . . .
. . v . v 1 = . > . .
. . . . . - . . 1 * .
. . v . < . v 1 . S .
. . . * . . . - . . .
. . . . . . . . v . .
. . 1 * . . . < . . .
. . < . . 0 @ 7 . . .
-1 @ 2 v . . 7 . . . .
. 7 . . . . . . . . .
. . -5 @ 8 . . . . . .
. . . 7 . . . . . . .
'''

def fact(x):
    if x <= 2: return x
    return x*fact(x-1)
for A in range(1, 100):
    ret, history = simulate(soln, A=A, max_iter=1000)
    assert ret == fact(A), f'{A=} {ret} vs {fact(A)}'
    print(f'{ret=}')
print('[Str(' + repr('solve 3d1\n'+soln) + ')]')
