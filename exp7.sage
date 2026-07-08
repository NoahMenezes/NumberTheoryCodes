# SageMath Primality Testing Tool
import random
from prettytable import PrettyTable

def trial_division(n):
    if n < 2: return False
    # Using Sage's isqrt equivalent
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fermat_test(n, k=5):
    if n < 4: return n == 2 or n == 3
    for _ in range(k):
        a = random.randint(2, n - 2)
        if power_mod(a, n - 1, n) != 1:
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
        x = power_mod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = power_mod(x, 2, n)
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
        
        # SageMath built-in primality check
        table.add_row(["Sage built-in is_prime", "Prime" if is_prime(n) else "Composite"])
        
        print(table)

    except ValueError:
        print("Invalid input.")

main()
