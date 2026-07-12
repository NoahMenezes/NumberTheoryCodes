q=int(input("q: "))
a=int(input("alpha: "))
xa=int(input("Xa: "))
xb=int(input("Xb: "))

ya=pow(a,xa,q)
yb=pow(a,xb,q)

ka=pow(yb,xa,q)
kb=pow(ya,xb,q)

print("Ya =",ya)
print("Yb =",yb)
print("Shared Key =",ka)

if ka==kb:
    print("Keys Match")
    