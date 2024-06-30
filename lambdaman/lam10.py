from evaluate import *
from ir import *

# problem 10
'''
B. 'L'
B$ y L1 L2
if (v2 == 2500) ''
B. (if (0 == v2 % 50) '\n' '')
B. (if (0 == v2 % 11) '#' '.')
v1(v2+1)
# applied to 1
'''

def draw_lam10():
    out = 'L'
    for i in range(1, 2500):
        if i % 50 == 0: out += '\n'
        out += '#' if i % 11 == 0 else '.'
    return out

def solve_lam10(grid, f):
    i, j = 0,0
    grid = list(map(lambda x: list(x.strip()), grid.strip().split('\n')))
    width, height = len(grid[0]), len(grid)
    def move(d):
        nonlocal i, j
        if d == 'R':
            if (j < width-1) and grid[i][j+1] != '#':
                grid[i][j] = ' '
                grid[i][j+1] = 'L'
                j += 1
        elif d == 'L':
            if (j > 0) and grid[i][j-1] != '#':
                grid[i][j] = ' '
                grid[i][j-1] = 'L'
                j -= 1
        elif d == 'U':
            if (i > 0) and grid[i-1][j] != '#':
                grid[i][j] = ' '
                grid[i-1][j] = 'L'
                i -= 1
        else:
            assert d == 'D'
            if (i < height-1) and grid[i+1][j] != '#':
                grid[i][j] = ' '
                grid[i+1][j] = 'L'
                i += 1
    soln = f()
    for c in soln:
        move(c)
    print('\n'.join([''.join(row) for row in grid]))
    return all(map(lambda row: all(map(lambda c: c != '.', row)), grid))


def g(k):
    l = 'R' if k % 2 == 0 else 'L'
    out = ''
    for j in range(6):
        for i in range(10):
            out += l
        if k % 12 == 5:
            out += 'U' + 2*l + 'D'
        else:
            out += 'D' + 2*l + 'U'
    return out
def f():
    out = ''
    for k in range(60):
        out += g(k)
        if k % 12 == 0:
            out += 'DL'
        if k % 12 == 11:
            out += 'DR'
        if k % 12 != 5:
            out += 'D'
    return out

def dir_str(x):
    if x % 4 == 0: return 'D'
    elif x % 4 == 1: return 'U'
    elif x % 4 == 2: return 'R'
    else: return 'L'
def make_f_rand_walk(seed, g, p, n_iter):
    def f_rand_walk():
        x = seed
        out = ''
        for i in range(n_iter):
            out += dir_str(x % 4)
            x *= g
            x %= p
        return out
    return f_rand_walk

if __name__ == '__main__':
    grid = draw_lam10()
    # print(grid)
    # solve_lam10(grid, f)

    for seed in range(1, 1000):
        if solve_lam10(grid, make_f_rand_walk(seed, 104729, 131071, 100000)):
            print(f'SUCCESS {seed}')
            break
    else:
        print(f'FAILED!')
