def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

p = int(input("Enter p: "))
q = int(input("Enter q: "))
e = int(input("Enter e: "))
msg = input("Enter message: ").lower()

n = p * q
phi = (p - 1) * (q - 1)

if gcd(e, phi) != 1:
    print("Invalid e")
else:
    for d in range(1, phi):
        if (e * d) % phi == 1:
            break

    print("n =", n)
    print("phi =", phi)
    print("d =", d)

    cipher = []
    plain = ""

    for ch in msg:
        if ch.isalpha():
            m = ord(ch) - 97
            c = pow(m, e, n)
            cipher.append(c)
            plain += chr(pow(c, d, n) + 97)

    print("Original :", msg)
    print("Cipher   :", cipher)
    print("Decrypted:", plain)