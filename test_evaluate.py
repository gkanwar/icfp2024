from evaluate import *
from ir import *

def test_bindings():
    b = Bindings()
    b.push(0, lambda: 'hello')
    b.push(1, lambda: 'world')
    assert b.get(0)() == 'hello' and b.get(1)() == 'world'
    b.push(0, lambda: 'goodbye')
    assert b.get(0)() == 'goodbye' and b.get(1)() == 'world'
    b.pop(0)
    assert b.get(0)() == 'hello' and b.get(1)() == 'world'
    b.pop(0)
    b.push(0, lambda: 'hey')
    assert b.get(0)() == 'hey'

def test_eval_if():
    tokens = dec('? B> I# I$ S9%3 S./')
    prog = parse_all(tokens)
    assert eval_lazy(prog, Bindings())() == 'no'

def test_eval_lambda():
    tokens = dec('L# v#')
    prog = parse_all(tokens)
    # prog returns an identity lambda, which we can thunk-ily evaluate
    assert eval_lazy(prog, Bindings())()(lambda: 'asdf')() == 'asdf'
    
    tokens = dec('B$ B$ L# L$ v# B. SB%,,/ S}Q/2,$_ IK')
    prog = parse_all(tokens)
    assert eval_lazy(prog, Bindings())() == 'Hello World!'

def test_eval_bind_shadowing():
    tokens = dec('B$ L# B$ L# U- v# v# I%')
    prog = parse_all(tokens)
    assert eval_lazy(prog, Bindings())() == -4

def test_lazy_infinite_loop():
    # first lambda should ignore infinite loop argument if properly evaluated
    tokens = dec('B$ LX I% B$ LY B$ vY vY LY B$ vY vY')
    prog = parse_all(tokens)
    # eval_lazy(prog, Bindings())
    assert eval_lazy(prog, Bindings())() == 4

def test_eval_language_test():
    prog = parse_all(dec(
        '''? B= B$ B$ B$ B$ L$ L$ L$ L# v$ I" I# I$ I% I$ ? B= B$ L$ v$ I+ I+ ? B= BD I$ S4%34 S4 ? B= BT I$ S4%34 S4%3 ? B= B. S4% S34 S4%34 ? U! B& T F ? B& T T ? U! B| F F ? B| F T ? B< U- I$ U- I# ? B> I$ I# ? B= U- I" B% U- I$ I# ? B= I" B% I( I$ ? B= U- I" B/ U- I$ I# ? B= I# B/ I( I$ ? B= I' B* I# I$ ? B= I$ B+ I" I# ? B= U$ I4%34 S4%34 ? B= U# S4%34 I4%34 ? U! F ? B= U- I$ B- I# I& ? B= I$ B- I& I# ? B= S4%34 S4%34 ? B= F F ? B= I$ I$ ? T B. B. SM%,&k#(%#+}IEj}3%.$}z3/,6%},!.'5!'%y4%34} U$ B+ I# B* I$> I1~s:U@ Sz}4/}#,!)-}0/).43}&/2})4 S)&})3}./4}#/22%#4 S").!29}q})3}./4}#/22%#4 S").!29}q})3}./4}#/22%#4 S").!29}q})3}./4}#/22%#4 S").!29}k})3}./4}#/22%#4 S5.!29}k})3}./4}#/22%#4 S5.!29}_})3}./4}#/22%#4 S5.!29}a})3}./4}#/22%#4 S5.!29}b})3}./4}#/22%#4 S").!29}i})3}./4}#/22%#4 S").!29}h})3}./4}#/22%#4 S").!29}m})3}./4}#/22%#4 S").!29}m})3}./4}#/22%#4 S").!29}c})3}./4}#/22%#4 S").!29}c})3}./4}#/22%#4 S").!29}r})3}./4}#/22%#4 S").!29}p})3}./4}#/22%#4 S").!29}{})3}./4}#/22%#4 S").!29}{})3}./4}#/22%#4 S").!29}d})3}./4}#/22%#4 S").!29}d})3}./4}#/22%#4 S").!29}l})3}./4}#/22%#4 S").!29}N})3}./4}#/22%#4 S").!29}>})3}./4}#/22%#4 S!00,)#!4)/.})3}./4}#/22%#4 S!00,)#!4)/.})3}./4}#/22%#4'''
    ))
    assert eval_lazy(prog, Bindings())() == (
        'Self-check OK, send `solve language_test 4w3s0m3` to claim points for it'
    )
