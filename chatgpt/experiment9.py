def factor(n):

    f = {}
    d = 2

    while d * d <= n:

        while n % d == 0:

            f[d] = f.get(d, 0) + 1
            n = n // d

        d = d + 1

    if n > 1:
        f[n] = 1

    return f


# Brute Force Discrete Log
def dlog(a, b, p, limit):

    for x in range(limit):

        if pow(a, x, p) == b:
            return x

    return None


# Chinese Remainder Theorem
def crt(data):

    M = 1

    for r, m in data:
        M = M * m

    ans = 0

    for r, m in data:

        Mi = M // m
        inv = pow(Mi, -1, m)

        ans = ans + r * Mi * inv

    return ans % M


# Pohlig Hellman
def pohlig(a, b, p):

    n = p - 1

    factors = factor(n)

    eq = []

    for prime, power in factors.items():

        m = prime ** power

        g = pow(a, n // m, p)

        h = pow(b, n // m, p)

        x = dlog(g, h, p, m)

        if x == None:
            return None

        eq.append((x, m))

    return crt(eq)


# Main Program

while True:

    print("\n1. Solve")
    print("2. Exit")

    ch = input("Choice: ")

    if ch == "2":
        break

    a = int(input("a: "))
    b = int(input("b: "))
    p = int(input("Prime p: "))

    x = pohlig(a, b, p)

    if x != None:
        print("Answer =", x)
        print("Check =", pow(a, x, p))
    else:
        print("No Solution")