choice = 0

while choice != 3:
    print("\n--- MATH TOOLBOX ---")
    print("1. Arithmetic")
    print("2. Theorems")
    print("3. Exit")

    try:
        choice = int(input("Enter choice: "))
    except:
        print("Invalid input")
        continue

    match choice:

        case 1:
            a = int(input("First Number: "))
            b = int(input("Second Number: "))

            while True:
                print("\n1.Add 2.Subtract 3.Multiply")
                print("4.Divide 5.Power")
                print("6.Floor Div 7.Modulus")
                print("8.Divisibility 9.Back")

                op = int(input("Choice: "))

                if op == 1:
                    print("Answer =", a + b)

                elif op == 2:
                    print("Answer =", a - b)

                elif op == 3:
                    print("Answer =", a * b)

                elif op == 4:
                    if b != 0:
                        print("Answer =", a / b)
                    else:
                        print("Division by zero!")

                elif op == 5:
                    print("Answer =", a ** b)

                elif op == 6:
                    if b != 0:
                        print("Answer =", a // b)
                    else:
                        print("Division by zero!")

                elif op == 7:
                    if b != 0:
                        print("Answer =", a % b)
                    else:
                        print("Division by zero!")

                elif op == 8:
                    if b != 0:
                        print(f"{a} = ({a//b} x {b}) + {a%b}")
                    else:
                        print("Division by zero!")

                elif op == 9:
                    break

                else:
                    print("Invalid Choice")

        case 2:
            x = int(input("Enter divisor (a): "))
            y = int(input("Enter b: "))
            z = int(input("Enter c: "))

            while True:
                print("\n1.Transitivity")
                print("2.Linear Combination")
                print("3.Back")

                ch = int(input("Choice: "))

                if ch == 1:
                    if x != 0 and y != 0:
                        if y % x == 0 and z % y == 0:
                            print("Transitivity is True")
                        else:
                            print("Conditions not satisfied")
                    else:
                        print("Divisor cannot be zero")

                elif ch == 2:
                    if x != 0 and y % x == 0 and z % x == 0:
                        m = int(input("Enter m: "))
                        n = int(input("Enter n: "))
                        value = m * y + n * z

                        if value % x == 0:
                            print("Theorem Verified")
                        else:
                            print("Not Verified")
                    else:
                        print("Conditions not satisfied")

                elif ch == 3:
                    break

                else:
                    print("Invalid Choice")

        case 3:
            print("Goodbye!")

        case _:
            print("Invalid Menu Choice")