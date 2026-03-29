a = int(input("Enter first numbers:"))
b = int(input("Enter second numbers:"))
c = int(input("Enter third numbers:"))

if a > b:
    if a > c:
        print(a, "is the largest number")
    else:
        print(c,"is the largest number")
else:
    if b > c:
        print(b,"is the largest number")
    else:
        print(c,"is the largesr number")
