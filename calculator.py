def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x / y

while True:
    print("Options:")
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("Enter 'q' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "1":
            print("Result: ", add(num1, num2))
        elif user_input == "2":
            print("Result: ", subtract(num1, num2))
        elif user_input == "3":
            print("Result: ", multiply(num1, num2))
        elif user_input == "4":
            print("Result: ", divide(num1, num2))
    else:
        print("Invalid input")

