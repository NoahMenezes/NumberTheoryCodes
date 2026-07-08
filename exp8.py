import math

def is_perfect_square(n):
    if n < 0:
        return False, 0
    root = math.isqrt(n)
    return root * root == n, root

def fermats_factorization(n):
    i = 0
    while i <= 10000:
        m = n + i * i
        print(f"Step {i}: m = n + i^2 = {n} + {i}^2 = {m}")
        is_sq, x = is_perfect_square(m)
        if is_sq:
            y = i
            p = x - y
            q = x + y
            print(f"sqrt({m}) = {x} is a perfect square")
            print(f"x = {x}, y = {y}")
            print(f"p = x - y = {x} - {y} = {p}")
            print(f"q = x + y = {x} + {y} = {q}")
            print(f"Factors: {p} and {q}")
            return p, q
        i += 1
    print("Algorithm fails")
    return None, None

def pollard_p_minus_1(n):
    a_in = input("Enter value of a (default 2): ").strip()
    a = int(a_in) if a_in else 2
    B = int(input("Enter bound B: "))
    g = math.gcd(a, n)
    print(f"gcd(a, n) = gcd({a}, {n}) = {g}")
    if g > 1:
        print(f"Found factor: {g}")
        return g
    for j in range(2, B + 1):
        a = pow(a, j, n)
        d = math.gcd(a - 1, n)
        print(f"j = {j}: a = {a}, d = gcd(a - 1, n) = gcd({a} - 1, {n}) = {d}")
        if d != 1 and d != n:
            print(f"Found factor: {d}")
            return d
    print("Algorithm fails")
    return None

def pollard_rho(n):
    x = 2
    y = x
    d = 1
    def g(val):
        return (val * val + 1) % n
    print(f"Initial: x = {x}, y = {y}, d = {d}")
    step = 1
    while d == 1:
        x = g(x)
        y = g(g(y))
        d = math.gcd(abs(x - y), n)
        print(f"Step {step}: x = {x}, y = {y}, |x - y| = {abs(x - y)}, d = gcd(|x - y|, n) = {d}")
        step += 1
    if d == n:
        print("Algorithm fails")
        return None
    print(f"Found factor: {d}")
    return d

def quadratic_sieve(n):
    X = math.ceil(math.sqrt(n))
    print(f"Initial: X = ceil(sqrt(n)) = {X}")
    step = 1
    while step <= 10000:
        Y2 = (X * X) % n
        print(f"Step {step}: X = {X}, Y^2 = X^2 mod n = {Y2}")
        is_sq, Y = is_perfect_square(Y2)
        if is_sq:
            print(f"Y^2 is a perfect square: Y = sqrt({Y2}) = {Y}")
            p = math.gcd(X - Y, n)
            q = math.gcd(X + Y, n)
            print(f"p = gcd(X - Y, n) = gcd({X} - {Y}, {n}) = {p}")
            print(f"q = gcd(X + Y, n) = gcd({X} + {Y}, {n}) = {q}")
            if p != 1 and p != n and q != 1 and q != n:
                print(f"Found non-trivial factors: {p} and {q}")
                return p, q
            else:
                print("Factors are trivial")
        X += 1
        step += 1
    print("Algorithm fails")
    return None, None

if __name__ == "__main__":
    while True:
        print("\nInteger Factorization")
        print("1. Fermat's")
        print("2. Pollard p-1")
        print("3. Pollard Rho")
        print("4. Quadratic Sieve")
        print("5. Exit")
        choice = input("Method (1-5): ").strip()
        if choice == "5":
            break
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice")
            continue
        try:
            n = int(input("Number: "))
            if n < 2:
                print("Error: n >= 2")
                continue
        except ValueError:
            print("Invalid input")
            continue
        if choice == "1":
            fermats_factorization(n)
        elif choice == "2":
            pollard_p_minus_1(n)
        elif choice == "3":
            pollard_rho(n)
        elif choice == "4":
            quadratic_sieve(n)
