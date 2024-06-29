from ir import *

# problem 1
eff1 = [Str("solve efficiency1 17592186044416")]

# problem 2
# y = (L1 B$ L2 B$ v1 B$ v2 v2 L2 B$ v1 B$ v2 v2)
eff2 = [Str("solve efficiency2 2134")]
'''
(B+ 2134 B* B$ B$ y L3 L4 if (v4 == 0) 1 else (1 + (B$ v3 v4-1)) I":c1+0(9345873499) I!(0)
(2134 + (0 * (B$ B$ y L3 L4 if (v4 == 0) 1 else (1 + (B$ v3 (v4 - 1))) 9345873499)))
human interpretation
2134 + 0 * f(9345873499)
where f(x) = x+1
'''

# problem 3
# same as problem 3 but * 1 instead of * 0
'''
B+ I7c(2134) B* B$ B$ L1 B$ L2 B$ v1 B$ v2 v2 L2 B$ v1 B$ v2 v2 L3 L4 ? B= v4 I!(0) I"(1) B+ I"(1) B$ v3 B- v4 I"(1) I":c1+0(9345873499) I"(1)
'''
# 2134 + (9345873499+1) = 
eff3 = [Str("solve efficiency3 9345875634")]

# problem 4
'''
B$ B$ y L3 L4 if (v4 < 2) 1 else (+ (v3 (v4 - 1)) (v3 (v4 - 2))) 40
human interpretation
fib(40)
def fib(x):
    if x < 2: return 1
    return fib(x - 1) + fib(x - 2)
= F(41) as defined in A000045
'''
eff4 = [Str("solve efficiency4 165580141")]

# problem 5
'''
B$ L6 B$ L7 B$ B$ y L3 L4 ? B& B> v4 I"41=(1000000) B& B$ v6 v4 B$ v7 B+ v4 I"(1) v4 B$ v3 B+ v4 I"(1) I#(2) B$ y L3 L4 ? B= v4 I"(1) T ? B= B% v4 I#(2) I"(1) F B$ v3 B/ v4 I#(2) L5 B$ B$ y L3 L4 ? B= v4 v5 T ? B= B% v5 v4 I!(0) F B$ v3 B+ v4 I"(1) I#(2)

(L6 (L7 (B$ B$ y L3 L4
if (v4 > 1000000 and v6(v4) and v7(v4+1)) v4
else
v3(v4+1)
2)
# v7 - "is power of two"
B$ y L3 L4
if (v4 == 1) T
else if (v4 % 2 == 1) F
else
v3(v4/2)
# v6 - "is prime"
L5 B$ B$ y L3 L4
if (v4 == v5) T
else if ((v5%v4) == 0) F
else
v3(v4+1)
# called on 2

human interpretation
first Mersenne prime x > 1000000
'''
eff5 = [Str("solve efficiency5 2147483647")]
