
def add(n1, n2):
    return n1 + n2

# todo: write out the other 3 functions - subtract multiply divide

def subtract(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# todo: add these 4 functions into a dictionary as the values. keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#todo use the dictionary operations to perform the calculations. multiply 4 * 8 using the dictionary

# print(operations["*"](4,8))

def calculator():
  
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)

            for symbol in operations:
                print(symbol)
                calculator()
calculator()