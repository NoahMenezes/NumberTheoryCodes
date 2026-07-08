choice = 0
while choice != 3:
    print("\n--- MATH TOOLBOX ---")
    print("1. Run Arithmetic")
    print("2. Check Theorems")
    print("3. Quit")
    
    try:
        choice = int(input("\nWhat would you like to do? "))
    except ValueError:
        print("That's not a number. Try again.")
        continue
    
    match choice:
        
        case 1:
            num1 = int(input("\nEnter your first number: "))
            num2 = int(input("Enter your second number: "))
             
            choice2 = 0 
            while choice2 != 9:
                print("\n-- Arithmetic Options --")
                print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power")
                print("6. Floor Division\n7. Modulus\n8. Divisibility Check\n9. Back")
                
                try:
                    choice2 = int(input("\nPick an operation: ")) 
                except ValueError:
                    print("Invalid input.")
                    continue

                if choice2 == 1:
                    result = num1 + num2
                    print(f"\nTotal: {num1} + {num2} = {result}")
    
                elif choice2 == 2:
                    result = num1 - num2
                    print(f"\nResult: {num1} - {num2} = {result}")

                elif choice2 == 3:
                    result = num1 * num2
                    print(f"\nProduct: {num1} * {num2} = {result}")

                elif choice2 == 4:
                    if num2 != 0:
                        result = num1 / num2 
                        print(f"\nDivision: {num1} / {num2} = {result}")
                    else:
                        print("\nError: You can't divide by zero!")

                elif choice2 == 5:
                    result = num1 ** num2
                    print(f"\nResult: {num1} to the power of {num2} is {result}")
     
                elif choice2 == 6:
                    if num2 != 0:
                        result = num1 // num2
                        print(f"\nFloor Result: {num1} // {num2} = {result}")
                    else:
                        print("\nError: Can't divide by zero!")

                elif choice2 == 7:
                    if num2 != 0:
                        result = num1 % num2
                        print(f"\nRemainder: {num1} % {num2} = {result}")
                    else:
                        print("\nError: Can't divide by zero!")

                elif choice2 == 8:
                    if num2 != 0:
                        q = num1 // num2
                        r = num1 % num2
                        print(f"\nDivision Lemma: {num1} = ({q} * {num2}) + {r}")
                    else:
                        print("\nError: Can't divide by zero!")

                elif choice2 == 9:
                    print("Going back...")

        case 2:
            print("\n--- Theorem Testing ---")
            a = int(input("Enter a (divisor): "))
            b = int(input("Enter b (first dividend): "))
            c = int(input("Enter c (second dividend): "))
            
            choice3 = 0
            while choice3 != 3:
                print("\nAvailable Theorems:")
                print("1. Transitivity (a|b and b|c means a|c)")
                print("2. Linear Combination (a|b and a|c means a|mb+nc)")
                print("3. Back")
                
                try:
                    choice3 = int(input("\nSelect a theorem: "))
                except ValueError:
                    print("Please enter 1, 2, or 3.")
                    continue

                if choice3 == 1:
                    print(f"\nChecking Transitivity for {a}, {b}, and {c}:")
                    if a != 0 and b != 0:
                        if (b % a == 0) and (c % b == 0):
                            if c % a == 0:
                                print(f"Confirmed: {a} divides {b} and {b} divides {c}, so {a} divides {c}.\n")
                            else:
                                print("Something is wrong with the math logic here.\n")   
                        else:
                            print(f"Condition not met: Check if {a}|{b} and {b}|{c} are both true.\n")
                    else:
                        print("Error: Divisors cannot be zero.\n")

                elif choice3 == 2:
                    print("\nTesting Linear Combination:")
                    if a != 0:
                        if (b % a == 0) and (c % a == 0):
                            m = int(input("Enter integer m: "))
                            n = int(input("Enter integer n: "))
                            
                            val = (m * b) + (n * c)
                            print(f"\nTesting: Does {a} divide ({m}*{b} + {n}*{c})?")
                            print(f"Calculation: {val}")
        
                            if val % a == 0:
                                print(f"Yes! {a} divides {val} perfectly.")
                            else:
                                print(f"No, {a} does not divide {val}.")
                        else:
                            print(f"\nFailed: {a} must divide both {b} and {c} for this to work.")
                    else:
                        print("Error: Divisor 'a' can't be zero.")
                
                elif choice3 == 3:
                    print("Going back...")

        case 3:
            print("\nCatch you later!")
            
        case _:
            print("\nThat's not a valid option.")