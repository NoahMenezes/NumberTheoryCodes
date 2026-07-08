# SageMath Random Number Generators (LCG and BBS)
from prettytable import PrettyTable

def lcg(seed, a, c, m, n):
    res, x = [], seed
    for i in range(1, n + 1):
        x = (a * x + c) % m
        res.append([i, x, round(float(x / m), 4)])
    return res

def bbs(p, q, seed, n):
    # Check BBS mathematical conditions
    if not (is_prime(p) and is_prime(q)):
        print("Warning: p and q should be prime for BBS.")
    if p % 4 != 3 or q % 4 != 3:
        print("Warning: p and q should be congruent to 3 mod 4 for BBS.")
    
    m = p * q
    if gcd(seed, m) != 1:
        print("Warning: Seed should be coprime to p*q.")

    res, x = [], seed
    for i in range(1, n + 1):
        x = power_mod(x, 2, m)
        bit = x % 2
        res.append([i, x, bit])
    return res

def main():
    while True:
        print("\n1. Linear Congruential (LCG)\n2. Blum Blum Shub (BBS)\n3. Exit")
        cmd = input("> ")
        if cmd == '3': break

        try:
            if cmd == '1':
                x0, a, c, m, n = [int(input(f"{k}: ")) for k in ('x0', 'a', 'c', 'm', 'n')]
                data = lcg(x0, a, c, m, n)
                t = PrettyTable(["Step", "X_i", "U_i"])
                for r in data: t.add_row(r)
                print(t)
            elif cmd == '2':
                p, q, s, n = [int(input(f"{k}: ")) for k in ('p', 'q', 'seed', 'n')]
                data = bbs(p, q, s, n)
                t = PrettyTable(["Step", "X_i", "Bit"])
                for r in data: t.add_row(r)
                print(t)
        except Exception as e:
            print(f"Error: {e}")

main()
