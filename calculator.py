def calculator():
    print("Simple Python Calculator")
    print("Operations: +  -  *  /")

    num1 = float(input("Enter First number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter Second number: "))

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operator")

calculator()
