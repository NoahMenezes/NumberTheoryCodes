# SageMath CRT Solver using built-in crt()

n = int(input("Enter number of congruences: "))

a = []
m = []

print("\nEnter values for each congruence (x ≡ a mod m):")
for i in range(n):
    val_a = int(input(f"Enter remainder a{i+1}: "))
    val_m = int(input(f"Enter modulus m{i+1}: "))
    a.append(val_a)
    m.append(val_m)
    
try:
    # Using Sage's native crt function
    sol = crt(a, m)
    print(f"\nThe solution is x = {sol}")
except ValueError as e:
    print(f"\nError solving CRT: {e}. Check if moduli are pairwise coprime.")
