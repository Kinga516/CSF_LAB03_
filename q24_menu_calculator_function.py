while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    a, b = map(int, input("Enter two numbers: ").split())

    if choice == 1:
        print("Sum =", a + b)
    elif choice == 2:
        print("Difference =", a - b)
    elif choice == 3:
        print("Product =", a * b)
    elif choice == 4:
        print("Quotient =", a / b)
    else:
        print("Invalid choice")