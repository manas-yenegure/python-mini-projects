def add (n1,n2):
    return n1 + n2

def subtract (n1,n2):
    return n1 - n2

def multiply (n1,n2):
    return n1 * n2

def divide (n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,

}

def calculator():
    should_accumlate = True
    num1 = float(input("what is the first Number"))

    while should_accumlate:
        for symbol in operations:
            print(symbol)
        operations_symbol = input("pick an operation")
        num2 = float(input("what is the next number?:"))

        answer = operations[operations_symbol] (num1,num2)
        print(f"{num1}{operations_symbol}{num2} = {answer}")

        choice = input(f"Type 'y' to continue calcualting with {answer}, or type 'n' to start a new calculation:")

        if choice == "y":
            num1 = answer
        else:
            should_accumlate = False
            print("\n" * 20)
            calculator()

calculator()
