# SageMath Linear Diophantine Equation Solver
import matplotlib.pyplot as plt

def extended_gcd_table(a, b):
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = abs(a), abs(b)
    extended_rows = []
    while r != 0:
        quotient = old_r // r
        new_r = old_r - quotient * r
        new_s = old_s - quotient * s
        new_t = old_t - quotient * t
        extended_rows.append([quotient, old_r, r, new_r, old_s, s, new_s, old_t, t, new_t])
        old_r, r = r, new_r
        old_s, s = s, new_s
        old_t, t = t, new_t
    if a < 0: old_s = -old_s
    if b < 0: old_t = -old_t
    return old_r, old_s, old_t, extended_rows

def plot_extended_gcd_table(orig_a, orig_b, gcd_val, extended_rows):
    print("\n[!] Generating table window... (Close the window to continue to the tester)")
    fig_height = max(4, len(extended_rows) * 0.5 + 1)
    fig, ax = plt.subplots(figsize=(12, fig_height))
    ax.axis('off')
    extended_columns = ["q", "r1", "r2", "r", "s1", "s2", "s", "t1", "t2", "t"]
    table = ax.table(
        cellText=extended_rows,
        colLabels=extended_columns,
        cellLoc='center',
        loc='center',
        bbox=[0, 0, 1, 1]
    )
    table.auto_set_font_size(False)
    table.set_fontsize(12)

    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor("#2C7BC9")
            cell.set_text_props(color="white", weight="bold")
        else:
            cell.set_facecolor("#A7D0F3")
    
    ax.set_title(f"Extended Euclid Algorithm Table | GCD({orig_a}, {orig_b}) = {gcd_val}", pad=20,
                 fontweight="bold", fontsize=14)
    plt.tight_layout()
    plt.show()

def lde(a, b, c):
    print(f"\nEquation: {a}x + {b}y = {c}\n")
    # Verify/calculate with Sage's built-in xgcd
    d, s_sage, t_sage = xgcd(a, b)
    
    # We still use the table helper to get rows for display
    _, s_orig, t_orig, table_rows = extended_gcd_table(a, b)
    
    print(f"d = gcd({a}, {b}) = {d}")
    plot_extended_gcd_table(a, b, d, table_rows)
    
    if c % d != 0:
        print(f"Since {d} does not divide {c}, no integer solution exists.")
        return None
        
    a1 = a // d
    b1 = b // d
    c1 = c // d
    print(f"\nStep 1: Reduced equation is {a1}x + {b1}y = {c1}")
    # Using Sage's xgcd for reduced coefficients
    _, s, t = xgcd(a1, b1)
    print(f"Step 2: Solving {a1}s + {b1}t = 1 yields s = {s}, t = {t}")
    x0 = c1 * s
    y0 = c1 * t
    print(f"Step 3: Particular solution is x0 = {x0}, y0 = {y0}")
    print("\nGeneral Solution: ")
    print(f"x = {x0} + k({b1})")
    print(f"y = {y0} - k({a1})")
    print("Where 'k' is any integer.")
    return x0, y0, a1, b1

def main():
    print("Linear Diophantine Equation Solver: ")
    try:
        user_a = int(input("Enter value for a: "))
        user_b = int(input("Enter value for b: "))
        user_c = int(input("Enter value for c: "))
        print("-" * 40)
        result = lde(user_a, user_b, user_c)
        
        if result is not None:
            x0, y0, a1, b1 = result
            print("-" * 40)
            while True:
                k_input = input("\nEnter an integer value for k to test (or type 'q' to quit): ")
                if k_input.lower() == 'q':
                    print("Exiting tester")
                    break
                try:
                    user_k = int(k_input)
                    x_k = x0 + user_k * b1
                    y_k = y0 - user_k * a1
                    print(f"\nCalculations for k = {user_k}:")
                    print(f"x = {x0} + {user_k}({b1}) = {x_k}")
                    print(f"y = {y0} - {user_k}({a1}) = {y_k}")
                    print("\nVerification: ")
                    calculated_c = (user_a * x_k) + (user_b * y_k)
                    print(f"Plugging x and y back into the original equation:")
                    print(f"{user_a}({x_k}) + {user_b}({y_k}) = {calculated_c}")
                    if calculated_c == user_c:
                        print("Status: SUCCESS! The equation is satisfied.")
                    else:
                        print("Status: FAILED. The math did not check out.")
                except ValueError:
                    print("Invalid input. Please enter an integer or 'q' to quit.")
    except ValueError:
        print("Invalid input. Please make sure to enter integers only for a, b, and c.")

main()
