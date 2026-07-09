def inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

def crt(a, m):
    M = 1

    for mod in m:
        M *= mod

    answer = 0

    for i in range(len(m)):
        Mi = M // m[i]
        Yi = inverse(Mi, m[i])

        answer += a[i] * Mi * Yi

    return answer % M


n = int(input("Number of congruences: "))

a = []
m = []

for i in range(n):
    a.append(int(input("Remainder: ")))
    m.append(int(input("Modulus: ")))

print("Solution =", crt(a, m))