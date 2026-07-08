# SageMath Euclidean & Extended Euclidean Algorithm Visualizer
from prettytable import PrettyTable

def euclidean_algorithm(a, b):
    rows = []
    headers = ["q", "a", "b", "r", "x", "y"]
    x1, x2 = 1, 0
    y1, y2 = 0, 1
    
    while b != 0:
        q = a // b
        r = a % b
        x = x1 - q * x2
        y = y1 - q * y2
        rows.append([q, a, b, r, x, y])
        
        a, b = b, r
        x1, x2 = x2, x
        y1, y2 = y2, y
        
    return a, rows, headers

def extended_gcd_pretty(a, b):
    rows = []
    headers = ["q", "r1", "r2", "r", "s1", "s2", "s", "t1", "t2", "t"]
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    
    initial_a, initial_b = a, b
    
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        s = s1 - q * s2
        t = t1 - q * t2
        rows.append([q, r1, r2, r, s1, s2, s, t1, t2, t])
        
        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t
    
    rows.append(["X", r1, 0, "X", s1, s2, "X", t1, t2, "X"])
    
    summary = (
        f"GCD({initial_a}, {initial_b}) = {r1}\n"
        f"Coefficients: s = {s1}, t = {t1}\n"
        f"Linear Combination: {initial_a}({s1}) + {initial_b}({t1}) = {r1}"
    )
    
    return rows, headers, summary

try:
    print("--- Euclidean Algorithm Visualizer ---")
    a_val = int(input("Enter first number (a): "))
    b_val = int(input("Enter second number (b): "))
except ValueError:
    print("Error: Please input valid integers.")
    exit()

gcd_val, euc_rows, euc_headers = euclidean_algorithm(a_val, b_val)
ext_rows, ext_headers, ext_summary = extended_gcd_pretty(a_val, b_val)

print(f"\n1. Standard Euclidean Steps (GCD({a_val}, {b_val}) = {gcd_val})")
euc_table = PrettyTable()
euc_table.field_names = euc_headers
for row in euc_rows:
    euc_table.add_row(row)
print(euc_table)

print("\n2. Extended Euclidean Steps (Finding Coefficients)")
ext_table = PrettyTable()
ext_table.field_names = ext_headers
for row in ext_rows:
    ext_table.add_row(row)
print(ext_table)

print("\n" + "="*40)
print(ext_summary)
print("="*40)
