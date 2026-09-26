import math
while True:
    print("---calculator---\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. SquareRoot (sqrt)")
    print("6. Power (x^y)")
    print("7. Percentage (%)")
    print("8. Exit")
    print("Enter your choice:")
    choice = int(input())
    if choice == 8:
        print("     --exit--     ")
        break
    elif choice in [1, 2, 3, 4, 6]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == 1:
            result = a + b
        elif choice == 2:
            result = a - b
        elif choice == 3:
            result = a * b
        elif choice == 4:
            if b == 0:
                print("Cannot divide by zero")
                continue
            result = a / b
        elif choice == 6:
            result = a ** b
        print("Result:", result)
    elif choice == 5:
        a = float(input("Enter number: "))
        if a < 0:
            print("sqrt of a negative number is undefined")
            continue
        result = math.sqrt(a)
        print("Result:", result)
    elif choice == 7:
        a = float(input("Enter number: "))
        result = a / 100
        print("Result:", result)
    else:
        print("Invalid choice")

    


