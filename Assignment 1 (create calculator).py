def get_number_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

n1 = get_number_input("Enter your first number: ")
n2 = get_number_input("Enter your second number: ")

while True:
    print("What would you like to do?")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'power' for power")
    
    user_input = input("Enter your choice: ")
    
    if user_input == "add":
        print("Result:", n1 + n2)
    elif user_input == "subtract":
        print("Result:", n1 - n2)
    elif user_input == "multiply":
        print("Result:", n1 * n2)
    elif user_input == "divide":
        if n2 == 0:
            print("Cannot be divided by 0")
        else:
            print("Result:", n1 / n2)
    elif user_input =="power":
        print("Result:", n1**n2)
    else:
        print("Invalid input. Please try again.")