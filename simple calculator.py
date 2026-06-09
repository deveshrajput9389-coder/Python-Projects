'''Description: 
               Develop a basic calculator that can perform four primary arithmetic operations: addition, subtraction, multiplication, and division
     OBJECTIVE:
               1. Create functions for each operation.
               2. Take two inputs from the user and allow them to select the desired operation.
               3. Handle division by zero with appropriate error messages '''

def oper():
    # operation functions
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return None
        return x / y

    while True:
        # taking input of two numbers
        try:
            a = float(input("Enter First Number : "))
            b = float(input("Enter Second Number : "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        # Let the user choose the operation
        print("Choose Operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice [1/2/3/4/5]: ")

        if choice == "1":
            print(f"Sum of {a} and {b} is {add(a, b)}")

        elif choice == "2":
            print(f"Subtraction of {a} and {b} is {subtract(a, b)}")

        elif choice == "3":
            print(f"Multiplication of {a} and {b} is {multiply(a, b)}")

        elif choice == "4":
            res = divide(a, b)
            if res is None:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Division of {a} by {b} is {res}")

        elif choice == "5":
            print("Calculator exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")
    return 0

oper()