import string
import math
from math import gcd

def caesar(text, shift, encrypt=True):
    s = shift if encrypt else -shift
    res = []
    for c in text:
        if c.lower() in string.ascii_lowercase:
            base = ord('A') if c.isupper() else ord('a')
            res.append(chr((ord(c) - base + s) % 26 + base))
        else:
            res.append(c)
    return "".join(res)

def affine(text, a, b, encrypt=True):
    if gcd(a, 26) != 1 and encrypt:
        raise ValueError("a must be coprime with 26")
    res = []
    for c in text:
        if c.lower() in string.ascii_lowercase:
            base = ord('A') if c.isupper() else ord('a')
            if encrypt:
                x = (a * (ord(c) - base) + b) % 26
            else:
                a_inv = pow(a, -1, 26)
                x = (a_inv * (ord(c) - base - b)) % 26
            res.append(chr(x + base))
        else:
            res.append(c)
    return "".join(res)

def vigenere(text, key, encrypt=True):
    key = key.lower()
    res = []
    ki = 0
    for c in text:
        if c.lower() in string.ascii_lowercase:
            base = ord('A') if c.isupper() else ord('a')
            s = ord(key[ki % len(key)]) - ord('a')
            s = s if encrypt else -s
            res.append(chr((ord(c) - base + s) % 26 + base))
            ki += 1
        else:
            res.append(c)
    return "".join(res)

def playfair_prepare(text):
    text = text.upper().replace('J', 'I')
    clean = ''.join(c for c in text if c.isalpha())
    pairs = []
    i = 0
    while i < len(clean):
        if i + 1 < len(clean) and clean[i] != clean[i + 1]:
            pairs.append(clean[i:i+2])
            i += 2
        elif i + 1 < len(clean):
            pairs.append(clean[i] + 'X')
            i += 1
        else:
            pairs.append(clean[i] + 'X')
            i += 1
    return pairs

def playfair_build_matrix(keyword):
    kw = keyword.upper().replace('J', 'I')
    seen = set()
    ms = ''
    for c in kw:
        if c.isalpha() and c not in seen:
            ms += c
            seen.add(c)
    for c in string.ascii_uppercase:
        if c != 'J' and c not in seen:
            ms += c
    return [list(ms[i:i+5]) for i in range(0, 25, 5)]

def playfair_find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def playfair(text, keyword, encrypt=True):
    m = playfair_build_matrix(keyword)
    pairs = playfair_prepare(text)
    res = ''
    d = 1 if encrypt else -1
    for p in pairs:
        r1, c1 = playfair_find_position(m, p[0])
        r2, c2 = playfair_find_position(m, p[1])
        if r1 == r2:
            c1 = (c1 + d) % 5
            c2 = (c2 + d) % 5
        elif c1 == c2:
            r1 = (r1 + d) % 5
            r2 = (r2 + d) % 5
        else:
            c1, c2 = c2, c1
        res += m[r1][c1] + m[r2][c2]
    return res

def adfgx_build_square(keyword):
    kw = keyword.upper().replace('J', 'I')
    seen = set()
    ss = ''
    for c in kw:
        if c.isalpha() and c not in seen:
            ss += c
            seen.add(c)
    for c in string.ascii_uppercase:
        if c != 'J' and c not in seen:
            ss += c
            seen.add(c)
    sq = {}
    labels = 'ADFGX'
    for i in range(5):
        for j in range(5):
            sq[ss[i*5 + j]] = labels[i] + labels[j]
    return sq

def adfgx_reverse_square(keyword):
    kw = keyword.upper().replace('J', 'I')
    seen = set()
    ss = ''
    for c in kw:
        if c.isalpha() and c not in seen:
            ss += c
            seen.add(c)
    for c in string.ascii_uppercase:
        if c != 'J' and c not in seen:
            ss += c
            seen.add(c)
    rev = {}
    labels = 'ADFGX'
    for i in range(5):
        for j in range(5):
            rev[labels[i] + labels[j]] = ss[i*5 + j]
    return rev

def columnar_transposition(text, keyword, encrypt=True):
    cols = len(keyword)
    ko = sorted(range(cols), key=lambda x: keyword[x])
    if encrypt:
        columns = ['' for _ in range(cols)]
        for i, char in enumerate(text):
            columns[i % cols] += char
        res = ''
        for idx in ko:
            res += columns[idx]
        return res
    else:
        total_len = len(text)
        rows = math.ceil(total_len / cols)
        num_long_cols = total_len % cols
        col_lengths = {}
        for idx in range(cols):
            if num_long_cols == 0:
                col_lengths[idx] = rows
            else:
                col_lengths[idx] = rows if idx < num_long_cols else rows - 1
        col_content = {}
        ti = 0
        for idx in ko:
            length = col_lengths[idx]
            col_content[idx] = text[ti:ti+length]
            ti += length
        res = []
        for r in range(rows):
            for c in range(cols):
                if r < len(col_content[c]):
                    res.append(col_content[c][r])
        return ''.join(res)

def adfgx(text, keyword1, keyword2, encrypt=True):
    if encrypt:
        sq = adfgx_build_square(keyword1)
        pt = text.upper().replace('J', 'I')
        pt = ''.join(c for c in pt if c.isalpha())
        sub = ''.join(sq.get(c, '') for c in pt)
        return columnar_transposition(sub, keyword2, encrypt=True)
    else:
        rev = adfgx_reverse_square(keyword1)
        trans = columnar_transposition(text, keyword2, encrypt=False)
        res = ''
        for i in range(0, len(trans), 2):
            if i + 1 < len(trans):
                pair = trans[i:i+2]
                if pair in rev:
                    res += rev[pair]
        return res

if __name__ == "__main__":
    while True:
        print("\n1. Caesar\n2. Affine\n3. Vigenere\n4. Playfair\n5. ADFGX\n6. Exit")
        ch = input("> ").strip()
        if ch == '6':
            break
        if ch not in ['1', '2', '3', '4', '5']:
            print("Invalid")
            continue
        txt = input("Text: ").strip()
        enc = input("Encrypt? (y/n): ").lower() == 'y'
        try:
            if ch == '1':
                s = int(input("Shift: "))
                print(f"Out: {caesar(txt, s, enc)}")
            elif ch == '2':
                a = int(input("a: "))
                b = int(input("b: "))
                if gcd(a, 26) != 1:
                    print("a must be coprime with 26")
                    continue
                print(f"Out: {affine(txt, a, b, enc)}")
            elif ch == '3':
                k = input("Key: ").strip()
                print(f"Out: {vigenere(txt, k, enc)}")
            elif ch == '4':
                kw = input("Keyword: ").strip()
                print(f"Out: {playfair(txt, kw, enc)}")
            elif ch == '5':
                k1 = input("Key1: ").strip()
                k2 = input("Key2: ").strip()
                print(f"Out: {adfgx(txt, k1, k2, enc)}")
        except Exception as e:
            print(f"Error: {e}")
