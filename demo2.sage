# SageMath Extended GCD & Diophantine Solver (demo2.sage)
from prettytable import PrettyTable

def extended_gcd_pretty(a, b):
    rows = []
    headers = ["q", "r1", "r2", "r", "s1", "s2", "s", "t1", "t2", "t"]

    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    original_a, original_b = a, b

    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        s = s1 - q * s2
        t = t1 - q * t2

        rows.append([q, r1, r2, r, s1, s2, s, t1, t2, t])

        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t

    rows.append(["-", r1, 0, "-", s1, s2, "-", t1, t2, "-"])

    summary = (
        f"GCD({original_a}, {original_b}) = {r1}\n"
        f"{original_a}({s1}) + {original_b}({t1}) = {r1}"
    )

    return rows, headers, summary, r1, s1, t1


def solve(a, b, c):
    if a == 0 and b == 0:
        if c == 0:
            print("Every integer pair (x, y) works.")
        else:
            print("No solution.")
        return

    # Using SageMath's gcd/xgcd for confirmation and table builder
    rows, headers, summary, d, s, t = extended_gcd_pretty(abs(a), abs(b))

    table = PrettyTable()
    table.field_names = headers
    for row in rows:
        table.add_row(row)

    print("\nExtended GCD steps:")
    print(table)
    print(summary)

    if c % d != 0:
        print("No solution since gcd does not divide c.")
        return

    x0 = s * (c // d)
    y0 = t * (c // d)

    if a < 0:
        x0 = -x0
    if b < 0:
        y0 = -y0

    print("\nParticular solution:")
    print("x0 =", x0, ", y0 =", y0)

    b_d = b // d
    a_d = a // d

    print("\nGeneral solution:")
    print("x =", x0, "+ k*", b_d)
    print("y =", y0, "- k*", a_d)

    example_table = PrettyTable()
    example_table.field_names = ["k", "x", "y"]

    for k in range(-3, 4):
        x = x0 + k * b_d
        y = y0 - k * a_d
        example_table.add_row([k, x, y])

    print("\nSome values:")
    print(example_table)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print("\nSolving:", a, "x +", b, "y =", c)
solve(a, b, c)
