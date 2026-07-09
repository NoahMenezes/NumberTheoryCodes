import random
from prettytable import PrettyTable

# Fast Modular Exponentiation
def power(a, b, m):

    ans = 1
    a = a % m

    while b > 0:

        if b % 2 == 1:
            ans = (ans * a) % m

        a = (a * a) % m
        b = b // 2

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

    if n == 2 or n == 3:
        return True

    if n < 2:
        return False

    for i in range(k):

        a = random.randint(2, n - 2)

        if power(a, n - 1, n) != 1:
            return False

    return True


# Miller Rabin
def miller(n, k):

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n < 2:
        return False

    d = n - 1
    r = 0

    while d % 2 == 0:
        d = d // 2
        r = r + 1

    for i in range(k):

        a = random.randint(2, n - 2)

        x = power(a, d, n)

        if x == 1 or x == n - 1:
            continue

        flag = False

        for j in range(r - 1):

            x = (x * x) % n

            if x == n - 1:
                flag = True
                break

        if not flag:
            return False

    return True


# Main Program

n = int(input("Enter Number: "))
k = int(input("Enter Trials: "))

table = PrettyTable(["Method", "Result"])

table.add_row(["Trial Division",
               "Prime" if trial(n) else "Composite"])

table.add_row(["Fermat Test",
               "Probably Prime" if fermat(n, k) else "Composite"])

table.add_row(["Miller Rabin",
               "Probably Prime" if miller(n, k) else "Composite"])

print(table)
