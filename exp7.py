import random
from prettytable import PrettyTable

def power(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res

def trial_division(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fermat_test(n, k=5):
    if n < 4: return n == 2 or n == 3
    for _ in range(k):
        a = random.randint(2, n - 2)
        if power(a, n - 1, n) != 1:
            return False
    return True

def miller_rabin(n, k=5):
    if n < 4: return n == 2 or n == 3
    if n % 2 == 0: return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = power(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = power(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def main():
    print(" Primality Testing Tool ")
    print("Suggested test values: 104729 (Prime), 561 (Carmichael), 2147483647 (Large Prime)\n")
    
    try:
        n = int(input("Enter number to test (n): "))
        k = int(input("Enter number of trials (k): "))
        
        if n < 2:
            print("Numbers less than 2 are not prime.")
            return

        print(f"\nResults for n = {n}:")
        
        table = PrettyTable()
        table.field_names = ["Method", "Result"]
        
        table.add_row(["Trial Division", "Prime" if trial_division(n) else "Composite"])
        table.add_row(["Fermat Test", "Probably Prime" if fermat_test(n, k) else "Composite"])
        table.add_row(["Miller-Rabin", "Probably Prime" if miller_rabin(n, k) else "Composite"])
        
        print(table)

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
