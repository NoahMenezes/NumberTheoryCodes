import math

def factor_number(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def discrete_log_subgroup(base, target, p, order):
    for x in range(order):
        if pow(base, x, p) == target:
            return x
    return None

def pohlig_hellman(a, b, p):
    n = p - 1
    pf = factor_number(n)
    congruences = []
    
    print(f"\nFactors of φ({p}) = {n}:")
    print(f"Prime factorization: {pf}\n")
    
    for prime, exponent in pf.items():
        prime_power = prime ** exponent
        
        print(f"Solving for x mod {prime}^{exponent} = {prime_power}:")
        
        gamma = pow(a, n // prime_power, p)
        delta = pow(b, n // prime_power, p)
        
        print(f"  a^({n}//{prime_power}) mod {p} = {gamma}")
        print(f"  b^({n}//{prime_power}) mod {p} = {delta}")
        
        x_mod_prime_power = discrete_log_subgroup(gamma, delta, p, prime_power)
        
        if x_mod_prime_power is not None:
            print(f"  Found: x ≡ {x_mod_prime_power} (mod {prime_power})")
            congruences.append((x_mod_prime_power, prime_power))
        else:
            print(f"  No solution for this subgroup")
            return None
        print()
    
    if len(congruences) != len(pf):
        return None
    x = crt(congruences)
    return x % n

def crt(congruences):
    """Chinese Remainder Theorem"""
    M = 1
    for _, m in congruences:
        M *= m
    
    result = 0
    for r, m in congruences:
        Mi = M // m
        yi = pow(Mi, -1, m)
        result += r * Mi * yi
    
    return result % M

if __name__ == "__main__":
    while True:
        print("\nPohlig-Hellman Algorithm")
        print("Solve: a^x ≡ b (mod p)")
        print("1. Solve")
        print("2. Exit\n")
        
        try:
            choice = input("Option (1-2): ").strip()
            
            if choice == "2":
                break
            
            if choice != "1":
                print("Invalid choice")
                continue
            
            a = int(input("a: "))
            b = int(input("b: "))
            p = int(input("p (prime): "))
            
            print(f"\n{'='*50}")
            print(f"Solving: {a}^x ≡ {b} (mod {p})")
            print(f"{'='*50}")
            
            x = pohlig_hellman(a, b, p)
            
            if x is not None:
                print(f"{'='*50}")
                print(f"Solution: x = {x}")
                print(f"Verification: {a}^{x} mod {p} = {pow(a, x, p)}")
                if pow(a, x, p) == b:
                    print("✓ CORRECT!")
                else:
                    print("✗ Error in calculation")
                print(f"{'='*50}")
            else:
                print("No solution found")
        
        except (ValueError, KeyboardInterrupt):
            print("Error")
            break
