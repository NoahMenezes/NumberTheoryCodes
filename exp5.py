def modular_inverse(a, m):
    m0 = m
    y = 0
    x = 1
    
    if m == 1:
        return 0
        
    while a > 1:
        q = a // m
        t = m
        
        m = a % m
        a = t
        t = y
        
        y = x - q * y
        x = t
        
    if x < 0:
        x = x + m0
        
    return x

def solve_crt(remainders, moduli):
    M = 1
    for m in moduli:
        M *= m
        
    result = 0
    for i in range(len(moduli)):
        Mi = M // moduli[i]
        yi = modular_inverse(Mi, moduli[i])
        result += remainders[i] * Mi * yi
        
    return result % M

if __name__ == "__main__":
    n = int(input("Enter number of congruences: "))
    
    a = []
    m = []
    
    print("\nEnter values for each congruence (x ≡ a mod m):")
    for i in range(n):
        val_a = int(input(f"Enter remainder a{i+1}: "))
        val_m = int(input(f"Enter modulus m{i+1}: "))
        a.append(val_a)
        m.append(val_m)
        
    sol = solve_crt(a, m)
    print(f"\nThe solution is x = {sol}")
