# SageMath Pohlig-Hellman Algorithm

def pohlig_hellman(a, b, p):
    n = p - 1
    # Using Sage's built-in factor
    pf = factor(n)
    congruences = []
    
    print(f"\nFactors of φ({p}) = {n}:")
    print(f"Prime factorization: {pf}\n")
    
    # Sage's factor output can be iterated as (prime, exponent) pairs
    for prime, exponent in pf:
        prime_power = prime ** exponent
        
        print(f"Solving for x mod {prime}^{exponent} = {prime_power}:")
        
        gamma = Mod(power_mod(a, n // prime_power, p), p)
        delta = Mod(power_mod(b, n // prime_power, p), p)
        
        print(f"  a^({n}//{prime_power}) mod {p} = {gamma}")
        print(f"  b^({n}//{prime_power}) mod {p} = {delta}")
        
        # We can find the discrete log in the subgroup of order prime_power
        # using Sage's built-in discrete_log or discrete_log_subgroup
        try:
            # Sage's discrete_log(target, base, ord) solves base^x = target mod p
            x_mod_prime_power = discrete_log(delta, gamma, ord=prime_power)
            print(f"  Found: x ≡ {x_mod_prime_power} (mod {prime_power})")
            congruences.append((x_mod_prime_power, prime_power))
        except ValueError:
            print(f"  No solution for this subgroup")
            return None
        print()
    
    if len(congruences) != len(pf):
        return None
        
    # Using Sage's native crt function
    # crt takes list of remainders and list of moduli, or vice versa?
    # Sage's crt(remainders, moduli)
    remainders = [int(c[0]) for c in congruences]
    moduli = [int(c[1]) for c in congruences]
    x = crt(remainders, moduli)
    return x % n

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
        
        if not is_prime(p):
            print(f"Error: {p} is not prime.")
            continue
            
        print(f"\n{'='*50}")
        print(f"Solving: {a}^x ≡ {b} (mod {p})")
        print(f"{'='*50}")
        
        x = pohlig_hellman(a, b, p)
        
        if x is not None:
            print(f"{'='*50}")
            print(f"Solution: x = {x}")
            print(f"Verification: {a}^{x} mod {p} = {power_mod(a, x, p)}")
            if power_mod(a, x, p) == b:
                print("✓ CORRECT!")
            else:
                print("✗ Error in calculation")
            print(f"{'='*50}")
        else:
            print("No solution found")
    
    except (ValueError, KeyboardInterrupt) as e:
        print(f"Error: {e}")
        break
