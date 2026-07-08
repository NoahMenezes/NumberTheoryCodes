# SageMath Linear Congruence Solver

def euclid_method(a, b, m):
    # Using Sage's xgcd
    gcd_val, s, t = xgcd(a, m)
    if b % gcd_val != 0:
        return None, gcd_val
    x0 = (s * (b // gcd_val)) % m
    solutions = [(x0 + i * (m // gcd_val)) % m for i in range(gcd_val)]
    solutions.sort()
    return solutions, gcd_val

def totient_method(a, b, m):
    # Using Sage's gcd and euler_phi
    gcd_val = gcd(a, m)
    if gcd_val != 1:
        return None, gcd_val
    p = euler_phi(m)
    # Using Sage's power_mod
    inv = power_mod(a, p - 1, m)
    return [(inv * b) % m], gcd_val

def inv_method(a, b, m):
    # Using Sage's gcd and inverse_mod
    gcd_val = gcd(a, m)
    if gcd_val != 1:
        return None, gcd_val
    inv = inverse_mod(a, m)
    return [(inv * b) % m], gcd_val

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

solve()
