def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def ext_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = ext_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def mod_inverse(e, phi):
    g, x, y = ext_gcd(e, phi)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

def main():
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))
    e = int(input("Enter e: "))
    m = input("Enter message string: ")

    n = p * q
    phi = (p - 1) * (q - 1)

    if gcd(e, phi) != 1:
        print("Error: e is not coprime to phi(n)")
        return

    d = mod_inverse(e, phi)
    print(f"n = {n}")
    print(f"phi(n) = {phi}")
    print(f"d = {d}")

    m = ''.join(c for c in m.lower() if c.isalpha())

    print("\n--- Proof of Encryption and Decryption ---")
    encrypted_vals = []
    decrypted_chars = []

    for char in m:
        val = ord(char) - ord('a')
        if val >= n:
            print(f"Warning: Value of '{char}' ({val}) >= n ({n}). RSA may fail for this character.")

        c = pow(val, e, n)
        dec_val = pow(c, d, n)
        dec_char = chr(dec_val + ord('a'))

        encrypted_vals.append(c)
        decrypted_chars.append(dec_char)

        print(f"Char: '{char}' (Value: {val})")
        print(f"  Encryption: c = {val}^{e} mod {n} = {c}")
        print(f"  Decryption: m = {c}^{d} mod {n} = {dec_val} ('{dec_char}')")

    print("\nResults:")
    print(f"Original: {m}")
    print(f"Ciphertext: {encrypted_vals}")
    print(f"Decrypted: {''.join(decrypted_chars)}")

if __name__ == "__main__":
    main()
