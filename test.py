from ir import *
from evaluate import *

# print(eval_lazy(parse_all(dec('''SS/52}3/,54)/.}&/2},!-"$!-!.Y}7!3}72/.'l''')), Bindings())())
def show(x):
    print(eval_lazy(parse_all(dec(x)), Bindings())())

show('''
S=/22%#4j}9/5}3/,6%$},!-"$!-!.[}7)4(}!}3#/2%}/&}VW]_~
''')
# print(eval_lazy(parse_all(dec('''B. S3/,6%},!-"$!-!.Y} B$ B$ B$ L! B$ L" B$ v! B$ v" v" L" B$ v! B$ v" v" L% L! L" ? B= v! I! S B. v" B$ B$ v% B- v! I" v" I#, SL''')), Bindings())())
