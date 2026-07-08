# SageMath RSA implementation using built-in number theory functions

# Prompt user for inputs
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
e = int(input("Enter e: "))
m = input("Enter message string: ")

# Check if inputs are prime (using Sage's built-in is_prime)
if not (is_prime(p) and is_prime(q)):
    print("Error: Both p and q must be prime numbers.")
    exit()

n = p * q
phi = (p - 1) * (q - 1)

# Check if e is coprime to phi (using Sage's built-in gcd)
if gcd(e, phi) != 1:
    print("Error: e is not coprime to phi(n)")
    exit()

# Compute the modular inverse (using Sage's built-in inverse_mod)
d = inverse_mod(e, phi)

print(f"n = {n}")
print(f"phi(n) = {phi}")
print(f"d = {d}")

# Filter message to lowercase letters only
m = ''.join(c for c in m.lower() if c.isalpha())

print("\n--- Proof of Encryption and Decryption ---")
encrypted_vals = []
decrypted_chars = []

for char in m:
    val = ord(char) - ord('a')
    if val >= n:
        print(f"Warning: Value of '{char}' ({val}) >= n ({n}). RSA may fail for this character.")

    # Encrypt: c = val^e mod n (using Sage's built-in power_mod)
    c = power_mod(val, e, n)
    
    # Decrypt: dec_val = c^d mod n
    dec_val = power_mod(c, d, n)
    
    # Convert integer back to character
    dec_char = chr(int(dec_val) + ord('a'))

    encrypted_vals.append(c)
    decrypted_chars.append(dec_char)

    print(f"Char: '{char}' (Value: {val})")
    print(f"  Encryption: c = {val}^{e} mod {n} = {c}")
    print(f"  Decryption: m = {c}^{d} mod {n} = {dec_val} ('{dec_char}')")

print("\nResults:")
print(f"Original: {m}")
print(f"Ciphertext: {encrypted_vals}")
print(f"Decrypted: {''.join(decrypted_chars)}")
