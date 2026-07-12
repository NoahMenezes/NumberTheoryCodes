from math import gcd

# Caesar Cipher
def caesar(text, s):
    out = ""
    for ch in text.lower():
        if ch.isalpha():
            out += chr((ord(ch) - 97 + s) % 26 + 97)
        else:
            out += ch
    return out

# Affine Cipher
def affine(text, a, b, enc):
    out = ""
    inv = pow(a, -1, 26)
    for ch in text.lower():
        if ch.isalpha():
            x = ord(ch) - 97
            if enc:
                x = (a * x + b) % 26
            else:
                x = (inv * (x - b)) % 26
            out += chr(x + 97)
    return out

# Vigenere Cipher
def vigenere(text, key, enc):
    out = ""
    j = 0
    key = key.lower()

    for ch in text.lower():
        if ch.isalpha():
            s = ord(key[j % len(key)]) - 97
            if not enc:
                s = -s
            out += chr((ord(ch) - 97 + s) % 26 + 97)
            j += 1
    return out

# Playfair Cipher
def matrix(key):
    key = (key + "ABCDEFGHIKLMNOPQRSTUVWXYZ").upper()
    seen = ""
    for c in key:
        if c not in seen and c != "J":
            seen += c
    return [list(seen[i:i+5]) for i in range(0, 25, 5)]

def pos(m, ch):
    if ch == "J":
        ch = "I"
    for i in range(5):
        for j in range(5):
            if m[i][j] == ch:
                return i, j

def playfair(text, key):
    m = matrix(key)
    text = "".join(c for c in text.upper().replace("J", "I") if c.isalpha())

    if len(text) % 2:
        text += "X"

    out = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = pos(m, a)
        r2, c2 = pos(m, b)

        if r1 == r2:
            out += m[r1][(c1 + 1) % 5]
            out += m[r2][(c2 + 1) % 5]
        elif c1 == c2:
            out += m[(r1 + 1) % 5][c1]
            out += m[(r2 + 1) % 5][c2]
        else:
            out += m[r1][c2]
            out += m[r2][c1]

    return out

# ADFGX Cipher
def adfgx(text, key):
    labels = "ADFGX"
    key = (key + "ABCDEFGHIKLMNOPQRSTUVWXYZ").upper()
    seen = ""

    for c in key:
        if c not in seen and c != "J":
            seen += c

    d = {}
    k = 0
    for i in labels:
        for j in labels:
            d[seen[k]] = i + j
            k += 1

    out = ""
    for c in text.upper():
        if c == "J":
            c = "I"
        if c in d:
            out += d[c]
    return out

# Menu
while True:
    print("\n1. Caesar")
    print("2. Affine")
    print("3. Vigenere")
    print("4. Playfair")
    print("5. ADFGX")
    print("6. Exit")

    ch = input("Choice: ")

    if ch == "6":
        break

    text = input("Enter text: ")

    if ch == "1":
        s = int(input("Shift: "))
        print("Encrypted:", caesar(text, s))
        print("Decrypted:", caesar(caesar(text, s), -s))

    elif ch == "2":
        a = int(input("a: "))
        b = int(input("b: "))
        if gcd(a, 26) != 1:
            print("a must be coprime with 26")
        else:
            c = affine(text, a, b, True)
            print("Encrypted:", c)
            print("Decrypted:", affine(c, a, b, False))

    elif ch == "3":
        key = input("Key: ")
        c = vigenere(text, key, True)
        print("Encrypted:", c)
        print("Decrypted:", vigenere(c, key, False))

    elif ch == "4":
        key = input("Key: ")
        print("Encrypted:", playfair(text, key))

    elif ch == "5":
        key = input("Key: ")
        print("Encrypted:", adfgx(text, key))

    else:
        print("Invalid Choice")