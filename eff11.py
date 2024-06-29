NODES = [n for n in range(11, 100) if n % 10 != 0]
def solve():
    values = [
        5, 6, 4, 8, 9, 3, 7, 1, 2,
        7, 8, 9, 5, 2, 1, 4, 3, 6,
        3, 2, 1, 6, 4, 7, 8, 5, 9,
        2, 3, 7, 1, 8, 4, 6, 9, 5,
        6, 9, 5, 7, 3, 2, 1, 8, 4,
        4, 1, 8, 9, 5, 6, 2, 7, 3,
        9, 7, 3, 2, 6, 8, 5, 4, 1,
        8, 4, 6, 3, 1, 5, 9, 2, 7,
        1, 5, 2, 4, 7, 9, 3, 6, 8,
    ]
    out = 0
    for n,v in zip(NODES, values):
        out *= 9
        out += v-1
    print(out)
    
if __name__ == '__main__':
    solve()
