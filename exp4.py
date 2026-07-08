import math

def extended_gcd(a, m):
    if m == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(m, a % m)
        x = y1
        y = x1 - (a // m) * y1
        return gcd, x, y

def euclid_method(a, b, m):
    gcd, s, t = extended_gcd(a, m)
    if b % gcd != 0:
        return None, gcd
    x0 = (s * (b // gcd)) % m
    solutions = [(x0 + i * (m // gcd)) % m for i in range(gcd)]
    solutions.sort()
    return solutions, gcd

def phi(n):
    res = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            res -= res // p
        p += 1
    if n > 1:
        res -= res // n
    return res

def mod_exp(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return res

def totient_method(a, b, m):
    gcd = math.gcd(a, m)
    if gcd != 1:
        return None, gcd
    p = phi(m)
    inv = mod_exp(a, p - 1, m)
    return [(inv * b) % m], gcd

def inv_method(a, b, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None, gcd
    inv = (x % m + m) % m
    return [(inv * b) % m], gcd

def solve():
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        m = int(input("m: "))
        
        print("\nMethod 1 (Euclid):")
        sol1, g1 = euclid_method(a, b, m)
        if sol1:
            print(f"gcd({a}, {m}) = {g1}")
            print(f"Solutions: {sol1}")
        else:
            print("No solution exists.")

        print("\nMethod 2 (Totient):")
        sol2, g2 = totient_method(a, b, m)
        if sol2:
            print(f"Solution: {sol2[0]}")
        else:
            print(f"gcd({a}, {m}) = {g2}, method not applicable.")

        print("\nMethod 3 (Inverse):")
        sol3, g3 = inv_method(a, b, m)
        if sol3:
            print(f"Solution: {sol3[0]}")
        else:
            print("Inverse does not exist.")

    except ValueError:
        print("Enter valid numbers.")

if __name__ == "__main__":
    solve()