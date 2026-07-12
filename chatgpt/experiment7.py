import random

# Fast Modular Exponentiation
def power(a, b, m):
    ans = 1
    a %= m
    while b > 0:
        if b % 2:
            ans = (ans * a) % m
        a = (a * a) % m
        b //= 2
    return ans

# Trial Division
def trial(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Fermat Test
def fermat(n, k):
    if n in (2, 3):
        return True
    if n < 2:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if power(a, n - 1, n) != 1:
            return False
    return True

# Miller Rabin Test
def miller(n, k):
    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for i in range(k):
        a = random.randint(2, n - 2)
        x = power(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for i in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False

    return True

# Main Program
n = int(input("Enter Number: "))
k = int(input("Enter Trials: "))

print("\nResults:")
print("Trial Division :", "Prime" if trial(n) else "Composite")
print("Fermat Test    :", "Probably Prime" if fermat(n, k) else "Composite")
print("Miller Rabin   :", "Probably Prime" if miller(n, k) else "Composite")