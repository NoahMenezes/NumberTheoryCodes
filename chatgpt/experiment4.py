
import math

# Extended Euclidean Algorithm
def egcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


# Euler Totient Function
def phi(n):
    ans = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            ans -= ans // p
        p += 1

    if n > 1:
        ans -= ans // n

    return ans


# Fast Modular Exponentiation
def power(a, b, m):
    result = 1
    a %= m

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m

        a = (a * a) % m
        b //= 2

    return result


a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter m: "))

# ---------------- Method 1 ----------------
print("\nMethod 1 : Extended Euclid")

gcd, x, y = egcd(a, m)

if b % gcd != 0:
    print("No Solution")

else:
    x0 = (x * (b // gcd)) % m

    print("Solutions:")

    for i in range(gcd):
        print((x0 + i * (m // gcd)) % m)

# ---------------- Method 2 ----------------
print("\nMethod 2 : Euler Totient")

if math.gcd(a, m) == 1:

    p = phi(m)
    inverse = power(a, p - 1, m)

    print("Solution =", (inverse * b) % m)

else:
    print("Method not applicable")

# ---------------- Method 3 ----------------
print("\nMethod 3 : Modular Inverse")

gcd, x, y = egcd(a, m)

if gcd == 1:
    inverse = x % m
    print("Solution =", (inverse * b) % m)

else:
    print("Inverse does not exist")
