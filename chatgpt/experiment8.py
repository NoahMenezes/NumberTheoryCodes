import math

# Fermat Factorization
def fermat(n):

    a = math.ceil(math.sqrt(n))

    while True:

        b2 = a * a - n
        b = math.isqrt(b2)

        if b * b == b2:
            print("Factors:", a - b, a + b)
            break

        a = a + 1


# Pollard p-1
def pollard_p1(n):
    a = 2
    B = int(input("Enter B: "))

    for j in range(2, B + 1):

        a = pow(a, j, n)

        d = math.gcd(a - 1, n)

        if d > 1 and d < n:
            print("Factor:", d)
            return

    print("Factor Not Found")


# Pollard Rho
def pollard_rho(n):

    x = 2
    y = 2
    d = 1

    while d == 1:

        x = (x * x + 1) % n
        y = (y * y + 1) % n
        y = (y * y + 1) % n

        d = math.gcd(abs(x - y), n)

    if d == n:
        print("Failed")
    else:
        print("Factor:", d)


# Quadratic Sieve (Simple Version)
def quadratic(n):

    x = math.ceil(math.sqrt(n))

    while True:

        y2 = (x * x) % n
        y = math.isqrt(y2)

        if y * y == y2:

            p = math.gcd(x - y, n)
            q = math.gcd(x + y, n)

            if p != 1 and q != 1:
                print("Factors:", p, q)
                return

        x = x + 1


# Main Program

while True:

    print("\n1. Fermat")
    print("2. Pollard p-1")
    print("3. Pollard Rho")
    print("4. Quadratic Sieve")
    print("5. Exit")

    ch = input("Choice: ")

    if ch == "5":
        break

    n = int(input("Enter Number: "))

    if ch == "1":
        fermat(n)

    elif ch == "2":
        pollard_p1(n)

    elif ch == "3":
        pollard_rho(n)

    elif ch == "4":
        quadratic(n)