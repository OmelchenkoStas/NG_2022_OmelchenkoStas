firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter second number: "))
Operation = input("Enter operation +, -, *, /, **, sqrt: ")
if Operation == "+":
    print(firstNumber+secondNumber)
if Operation == "-":
    print(firstNumber-secondNumber)
if Operation == "*":
    print(firstNumber*secondNumber)
if Operation == "/":
    print(firstNumber/secondNumber)
if Operation == "**":
    print(pow(firstNumber, secondNumber))
if Operation == "sqrt":
    print(firstNumber**(1/secondNumber))