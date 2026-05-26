print("===============BASIC CALCULATOR===============")

while True:  
    print("""What operation you wanna do?
    [1] Addition;
    [2] Subtraction;
    [3] Multiplication;
    [4] Division;
    [5] Exit calculator.
    """)
 
    operation = int(input())


    if operation == 1:
        num1 = float(input("Type a number: "))
        num2 = float(input("Type another number: "))
        result = num1 + num2
        print(f"The result is: {result}")
    elif operation == 2:
        num1 = float(input("Type a number: "))
        num2 = float(input("Type another number: "))
        result = num1 - num2
        print(f"The result is: {result}")
    elif operation == 3:
        num1 = float(input("Type a number: "))
        num2 = float(input("Type another number: "))
        result = num1 * num2
        print(f"The result is: {result}")
    elif operation == 4:
        num1 = float(input("Type a number: "))
        num2 = float(input("Type another number: "))
        result = num1 / num2
        print(f"The result is: {result}")
    elif operation == 5:
        print("Thank you to use my calculator!")
        break
    else:
        print("Invalid option!")
