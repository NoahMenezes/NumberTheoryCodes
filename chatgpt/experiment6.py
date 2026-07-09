from prettytable import PrettyTable

# Linear Congruential Generator
def lcg(seed, a, c, m, n):

    table = PrettyTable(["Step", "Xi", "Ui"])

    x = seed

    for i in range(1, n + 1):

        x = (a * x + c) % m
        u = x / m

        table.add_row([i, x, round(u, 4)])

    print(table)


# Blum Blum Shub Generator
def bbs(p, q, seed, n):

    m = p * q

    table = PrettyTable(["Step", "Xi", "Bit"])

    x = seed

    for i in range(1, n + 1):

        x = (x * x) % m
        bit = x % 2

        table.add_row([i, x, bit])

    print(table)


# Main Program
while True:

    print("\n1. LCG")
    print("2. BBS")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        seed = int(input("Seed: "))
        a = int(input("a: "))
        c = int(input("c: "))
        m = int(input("m: "))
        n = int(input("Number of values: "))

        lcg(seed, a, c, m, n)

    elif choice == "2":

        p = int(input("p: "))
        q = int(input("q: "))
        seed = int(input("Seed: "))
        n = int(input("Number of values: "))

        bbs(p, q, seed, n)

    elif choice == "3":
        break

    else:
        print("Invalid Choice")