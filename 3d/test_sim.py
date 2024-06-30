from sim import *

def test_simulate_simple():
    ret, history = simulate('3 > S')
    assert len(history) == 2
    assert ret == 3

def test_simulate_eq_neq():
    ret, _ = simulate('''
      . 1 .
      2 = S
      . . .
    ''')
    assert ret is None
    ret, history = simulate('''
      . 1 .
      1 = S
      . . .
    ''')
    assert ret is 1 and len(history) == 2
    ret, history = simulate('''
      . 1 .
      1 = .
      . S .
    ''')
    assert ret is 1 and len(history) == 2
    ret, history = simulate('''
      . 1 .
      2 # S
      . . .
    ''')
    assert ret is 1 and len(history) == 2
    ret, history = simulate('''
      . 1 .
      2 # .
      . S .
    ''')
    assert ret is 2 and len(history) == 2

def test_move_value():
    ret, history = simulate('4 > .', max_iter=1)
    assert ret is None and history[-1] == parse('. > 4')
    ret, history = simulate('. < 4', max_iter=1)
    assert ret is None and history[-1] == parse('4 < .')
    ret, history = simulate('4\nv\n.', max_iter=1)
    assert ret is None and history[-1] == parse('.\nv\n4')
    ret, history = simulate('.\n^\n4', max_iter=1)
    assert ret is None and history[-1] == parse('4\n^\n.')

def test_copy_value():
    ret, history = simulate('''
      4 > .
      v . .
      . . .
    ''', max_iter=1)
    assert ret is None
    assert history[-1] == parse('''
      . > 4
      v . .
      4 . .
    ''')

def test_preserve_value():
    ret, history = simulate('''
      . . . 0 .
      4 > . = .
      . . . S .
    ''', max_iter=2)
    assert ret is None
    assert history[0] == parse('''
      . . . 0 .
      4 > . = .
      . . . S .
    ''')
    assert history[1] == parse('''
      . . . 0 .
      . > 4 = .
      . . . S .
    ''')
    assert history[2] == parse('''
      . . . 0 .
      . > 4 = .
      . . . S .
    ''')

def test_simulate_example():
    ret, history = simulate('''
       . . . . 0 . . . .
       . B > . = . . . .
       . v 1 . . > . . .
       . . - . . . + S .
       . . . . . ^ . . .
       . . v . . 0 > . .
       . . . . . . A + .
       . 1 @ 6 . . < . .
       . . 3 . 0 @ 3 . .
       . . . . . 3 . . .
    ''', A=3, B=4, max_iter=20)
    assert ret == 12
