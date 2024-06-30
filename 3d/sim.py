import copy
import operator as op

OPS = [
    # unary
    '<', '>', '^', 'v',
    # binary
    '+', '-', '*', '/', '%', '=', '#',
    # quad
    '@',
    # in/out
    'S', 'A', 'B'
]

def idiv(x, y):
    if x < 0:
        return -idiv(-x, y)
    else:
        return x // y
def imod(x, y):
    return x - idiv(x,y)*y
def prop(x, y):
    return x, y

BIN_OPS = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': idiv,
    '%': imod,
    '=': prop,
    '#': prop
}


def parse(grid):
    grid = [row.split() for row in grid.strip().split('\n')]
    for row in grid:
        for j,c in enumerate(row):
            try:
                row[j] = int(c)
            except ValueError:
                continue
    return grid

def step(history):
    """Evaluate one step, possible rewriting history, possibly returning a value"""
    grid = history[-1]
    grid2 = copy.deepcopy(history[-1])
    outputs = [[[] for _ in grid[-1]] for _ in grid]
    ret_value = None
    time_warps = []
    def consume(i, j):
        grid2[i][j] = '.'
        return grid[i][j]
    def write(i, j, val):
        if val != '.':
            outputs[i][j].append(val)
    for i,row in enumerate(grid):
        for j,c in enumerate(row):
            if isinstance(c, int):
                continue
            elif c == '.':
                continue
            elif c == '<':
                write(i, j-1, consume(i, j+1))
            elif c == '>':
                write(i, j+1, consume(i, j-1))
            elif c == '^':
                write(i-1, j, consume(i+1, j))
            elif c == 'v':
                write(i+1, j, consume(i-1, j))
            elif c in BIN_OPS:
                x, y = grid[i][j-1], grid[i-1][j]
                if not (isinstance(x, int) and isinstance(y, int)):
                    continue
                if c == '=' and x != y or c == '#' and x == y:
                    continue
                consume(i, j-1), consume(i-1, j)
                out = BIN_OPS[c](x, y)
                if isinstance(out, tuple):
                    xp, yp = out
                else:
                    xp, yp = out, out
                write(i+1, j, xp)
                write(i, j+1, yp)
            elif c == '@':
                dx, dy = grid[i][j-1], grid[i][j+1]
                v, dt = grid[i-1][j], grid[i+1][j]
                if not (isinstance(dx, int) and isinstance(dy, int) and isinstance(dt, int)):
                    continue
                if v == '.':
                    continue
                consume(i, j-1), consume(i, j+1), consume(i-1, j), consume(i+1, j)
                assert dt <= len(history), f'cannot rewind {dt} with history {len(history)}'
                time_warps.append((dt, v, i-dy, j-dx))

    for i,row in enumerate(grid):
        for j,c in enumerate(row):
            vals = outputs[i][j]
            if len(vals) == 0: continue
            if len(vals) > 1:
                raise RuntimeError(f'write conflict {i} {j} {vals}')
            v = vals[0]
            if grid2[i][j] == '.':
                grid2[i][j] = v
            elif grid2[i][j] == 'S':
                if ret_value is not None and v != ret_value:
                    raise RuntimeError(f'return conflict {v} {ret_value}')
                ret_value = v
            else:
                grid2[i][j] = v
    if ret_value is not None:
        history.append(grid2)
        return ret_value

    if len(time_warps) > 0:
        print('TIME WARP!!!')
        warp_dt = None
        writes = {}
        for dt, v, x, y in time_warps:
            if warp_dt is None:
                warp_dt = dt
            if dt != warp_dt:
                raise RuntimeError(f'conflict in warp dt {dt} vs {warp_dt}')
            if (x,y) in writes and writes[(x,y)] != v:
                raise RuntimeError(f'conflict in warp write at {(x,y)}: {v} vs {writes[(x,y)]}')
            writes[(x,y)] = v
        del history[-warp_dt:]
        print('Rewound to:')
        draw(history[-1])
        print('Applying writes:', writes)
        grid2 = copy.deepcopy(history[-1])
        for x,y in writes:
            v = writes[(x,y)]
            if grid2[x][y] == 'S':
                if ret_value is not None and ret_value != v:
                    raise RuntimeError(f'return conflict on warp write {v} vs {ret_value}')
                ret_value = v
            else:
                grid2[x][y] = v
                
    history.append(grid2)
    return ret_value

def draw(grid):
    for row in grid:
        print(' '.join(map(lambda x: str(x).rjust(3), row)))
        print()
    print()

def simulate(grid, A=0, B=0, *, max_iter=100):
    grid = parse(grid)
    for row in grid:
        for j,c in enumerate(row):
            assert isinstance(c, int) or c == '.' or c in OPS
            if c == 'A':
                row[j] = A
            elif c == 'B':
                row[j] = B
    V = len(grid) * len(grid[0]) # assumes initial volume = max volume
    history = [grid]

    max_t = 1
    for i in range(max_iter):
        print(f'Step {i+1}')
        ret = step(history)
        draw(history[-1])
        print(f'History {len(history)}')
        max_t = max(len(history), max_t)
        print(f'Cost = {max_t * V}')
        if ret is not None:
            return ret, history
    return None, history
