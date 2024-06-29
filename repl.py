import json
import requests

from evaluate import *
from fmt import *
from ir import *

TARGET = 'https://boundvariable.space/communicate'
HEADERS = {
    'User-Agent': 'Team-IDKJava',
}
with open('.auth.json', 'r') as f:
    HEADERS.update(json.load(f))

s = requests.Session()
def send(x):
    return s.post(TARGET, data=x.encode(), headers=HEADERS).content.decode()

def run_repl():
    resp = send(enc([Str("get index")]))
    print(eval_lazy(parse_all(dec(resp)), Bindings())())
    while True:
        try:
            x = input('> ')
        except EOFError:
            print()
            break
        if len(x) == 0:
            break
        resp = send(enc(eval(x)))
        print('== RAW ==')
        print(repr(resp))
        tokens = dec(resp)
        print('== TOKENS ==')
        print(fmt(tokens))
        prog = parse_all(tokens)
        print('== RESULT ==')
        try:
            print(eval_lazy(prog, Bindings())())
        except RecursionError:
            print('<recursion limit>')

if __name__ == '__main__':
    run_repl()
