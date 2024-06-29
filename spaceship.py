import numpy as np

from ir import *    

DV_TO_KEY = {
    (-1,-1): '1',
    (0,-1): '2',
    (1,-1): '3',
    (-1,0): '4',
    (0,0): '5',
    (1,0): '6',
    (-1,1): '7',
    (0,1): '8',
    (1,1): '9',
}

def solve(coords, name):
    coords = np.loadtxt(coords.split('\n'), dtype=int)
    coords = np.insert(coords, 0, np.array([(0,0), (0,0)]), axis=0)
    dx = coords[1:] - coords[:-1]
    dv = dx[1:] - dx[:-1]
    for i,x in enumerate(dv):
        if tuple(x) not in DV_TO_KEY:
            print(f'invalid solution on step {i}')
            break
    keys = ''.join(DV_TO_KEY[tuple(x)] for x in dv)
    print(f'[Str("solve {name} {keys}")]')
    

puzzles = {
    'spaceship1': '1 -1\n1 -3\n2 -5\n2 -8\n3 -10\n',
    'spaceship2': '0 1\n0 1\n-1 2\n-1 4\n0 7\n1 10\n3 12\n5 13\n7 14\n8 14\n8 13\n9 13\n10 14\n11 15\n12 15\n14 16\n17 16\n20 15\n22 15\n23 14\n25 12\n27 10\n29 8\n32 6\n35 4\n37 2\n40 -1\n44 -4\n49 -8\n53 -11\n58 -14\n63 -18\n68 -22\n72 -26\n77 -29\n81 -33\n85 -37\n88 -42\n90 -48\n92 -55\n94 -61\n95 -68\n95 -76\n94 -84\n93 -93\n92 -102\n92 -112\n92 -122\n93 -131\n94 -140\n',
    # 'spaceship3': '-1 1\n1 8\n4 15\n3 14\n3 13\n-1 3\n-1 0\n2 11\n0 5\n5 16\n',
    # manually augmented
    'spaceship3': '-1 1\n-1 2\n0 4\n1 6\n1 8\n2 11\n2 13\n3 14\n4 15\n4 15\n3 15\n3 14\n3 13\n2 12\n0 10\n-1 7\n-1 3\n-1 0\n0 -2\n1 -3\n2 -3\n2 -2\n2 0\n2 3\n2 7\n2 11\n1 14\n0 16\n0 17\n0 17\n0 16\n0 14\n0 11\n0 8\n0 5\n1 3\n2 2\n3 2\n4 3\n5 5\n5 8\n5 12\n5 16\n',
}

for k in puzzles:
    solve(puzzles[k], k)
