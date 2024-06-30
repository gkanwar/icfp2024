'''
# Input
  `1 <= A <= 9999999999`

# Output
  `1` if `A` is a palindrome (a number that is the same when reversed), and `0` otherwise.

# Example
  * `A = 1233321`
    `Answer = 1`
  * `A = 3123`
    `Answer = 0`
'''

from sim import *

soln = '''
.  .  10 <  10 .  x  .  .  .  .  .
.  .  v  .  ^  .  +  .  .  .  .  .
.  .  10 >  10 ^  .  .  .  .  .  .
.  .  .  .  %  .  .  .  .  .  .  .
.  .  .  ^  .  .  10 .  10 .  .  .
.  .  .  A  .  .  v  .  ^  .  .  .
0  <  0  #  .  .  10 >  10 <  .  .
v  .  ^  .  #  .  >  .  /  .  .  .
0  >  0  .  .  v  .  .  .  .  .  .
.  .  .  .  .  .  .  5  @  4  .  .
.  .  .  .  .  v  .  .  3  .  .  .
.  .  .  .  .  .  .  .  .  .  .  .
.  .  .  .  2  @  5  .  .  .  .  .
.  .  .  .  .  3  .  .  .  .  .  .
'''

ret, history = simulate(soln, A=12345678, max_iter=40)
