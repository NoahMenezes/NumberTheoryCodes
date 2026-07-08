choice=0
while choice!=3:
    print("\n1.Arithmetic, 2. Theorems, 3.Exit")
    choice=int(input("Enter the choice: "))
    

    match choice: 
        case 1:
            a=int(input("Enter the first number: "))
            b=int(input("Enter the second number: "))

            while True:
                op=int(input("Enter the operation: "))
                if op==1:
                    print("a+b: "+(a+b))
                elif op==2:
                    print("a-b: "+(a-b))
                elif op==3:
                    print("a*b: "+(a*b))
                elif op==4:
                    print("a/b: "+(a/b))
                elif op==5:
                    print("a**b: "+(a**b))
                elif op==6:
                    print("a//b: "+(a//b))
                elif op==7:
                    print("a%b: "+(a%b))
                elif op==8:
                    break
                else:
                    print("Invalid choice")
        case 2:
            x=int(input("Enter x: "))
            y=int(input("Enter y: "))
            z=int(input("Enter z: "))
            while True:
                ch=int(input("Choice: "))
                if ch==1:
                    if x!=0 and y%x==0 and z%y==0:
                        print("Transitivity is True")
                    else:
                        print("Transitivity is false")
                elif ch==2:
                    if x!=0 and y%x==0 and z%x==0:
                        m=int(input("Enter m: "))
                        n=int(input("Enter n:")) 
                        value=m*x+n*y
                        if value % x==0:
                            print("Thorem is verified")
                        else:
                            print("Theorem is not verified")
                elif ch==3:
                    break
                else:
                    print("Invalid choice")
        case 3:
            print("Goodbye!")
        case _:
            print("Invalid choice")
            