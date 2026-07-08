# SageMath Diffie-Hellman Key Exchange

def main():
    q = int(input("Enter prime q: "))
    
    # Verify q is prime using Sage's is_prime
    if not is_prime(q):
        print("Warning: q is not prime. Diffie-Hellman might not be secure.")
        
    alpha = int(input("Enter primitive root alpha: "))
    
    # Check if alpha is primitive root modulo q
    if is_prime(q) and not Mod(alpha, q).is_primitive_root():
        print(f"Warning: {alpha} is not a primitive root modulo {q}.")

    Xa = int(input("Enter private key Xa: "))
    Xb = int(input("Enter private key Xb: "))

    # Use Sage's power_mod for modular exponentiation
    Ya = power_mod(alpha, Xa, q)
    Yb = power_mod(alpha, Xb, q)

    print(f"Public Key Ya: {alpha}^{Xa} mod {q} = {Ya}")
    print(f"Public Key Yb: {alpha}^{Xb} mod {q} = {Yb}")

    ka = power_mod(Yb, Xa, q)
    kb = power_mod(Ya, Xb, q)

    print("\n--- Key Agreement Verification ---")
    print(f"Key computed by A (ka): {Yb}^{Xa} mod {q} = {ka}")
    print(f"Key computed by B (kb): {Ya}^{Xb} mod {q} = {kb}")

    if ka == kb:
        print(f"\nProof Success: ka = kb = {ka}")
    else:
        print("\nProof Failed: Keys do not match")

main()
