print("== Simple Calculator ==")
print("Operators: + - * /")
print("Type 'exit' to quit.")



while True:
    num1 = input("Enter First Number ")
    if num1.lower() == "exit":
        print("Calculator Closed!")
        break

    num2 = input("Enter Second Number: ")
    if num2.lower() == "exit":
        print("Calculator Closed!")
        break


    operator = input("Enter Operator: + - * /")
    if operator.lower() == "exit":
        print("Calculator Closed")
        break



    num1 = float(num1)
    num2 = float(num2)


    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        result = "Invalid Operator."

    print(f"Result", {result})
    break








    