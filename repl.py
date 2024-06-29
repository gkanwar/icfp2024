import json
import requests

from ir import *
from fmt import *

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
    print(fmt(dec(resp)))
    while True:
        try:
            x = input('> ')
        except EOFError:
            print()
            break
        if len(x) == 0:
            break
        resp = send(enc(eval(x)))
        print(repr(resp))
        print(fmt(dec(resp)))

if __name__ == '__main__':
    run_repl()
