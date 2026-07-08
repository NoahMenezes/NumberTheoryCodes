import math
from prettytable import PrettyTable

def lcg(seed, a, c, m, n):
    res, x = [], seed
    for i in range(1, n + 1):
        x = (a * x + c) % m
        res.append([i, x, round(x / m, 4)])
    return res

def bbs(p, q, seed, n):
    m = p * q
    res, x = [], seed
    for i in range(1, n + 1):
        x = pow(x, 2, m)
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

if __name__ == "__main__":
    main()
