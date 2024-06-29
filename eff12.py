# appears to be a(n) = phi(n)+1
# A039649
memo = {}
def f(x):
    if x <= 2:
        return x
    if x in memo:
        return memo[x]
    print(f'f({x})')
    z = x
    for y in range(2, x):
        fy = f(y)
        if fy <= y-1 or x % y != 0:
            continue
        # for all divisors of x
        z = (z // fy) * (fy-1)
    out = min(x,1+z)
    memo[x] = out
    return out
print([f(n) for n in range(2, 25)])
