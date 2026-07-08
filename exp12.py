def main():
    q = int(input("Enter prime q: "))
    alpha = int(input("Enter primitive root alpha: "))
    Xa = int(input("Enter private key Xa: "))
    Xb = int(input("Enter private key Xb: "))

    Ya = pow(alpha, Xa, q)
    Yb = pow(alpha, Xb, q)

    print(f"Public Key Ya: {alpha}^{Xa} mod {q} = {Ya}")
    print(f"Public Key Yb: {alpha}^{Xb} mod {q} = {Yb}")

    ka = pow(Yb, Xa, q)
    kb = pow(Ya, Xb, q)

    print("\n--- Key Agreement Verification ---")
    print(f"Key computed by A (ka): {Yb}^{Xa} mod {q} = {ka}")
    print(f"Key computed by B (kb): {Ya}^{Xb} mod {q} = {kb}")

    if ka == kb:
        print(f"\nProof Success: ka = kb = {ka}")
    else:
        print("\nProof Failed: Keys do not match")

if __name__ == "__main__":
    main()
