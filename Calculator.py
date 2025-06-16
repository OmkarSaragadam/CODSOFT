def calculator():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Enter operator (+ - * /): ")

            valid = True
            result = 0

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                if b == 0:
                    print("Cannot divide by zero.")
                    valid = False
                else:
                    result = a / b
            else:
                print("Invalid operator.")
                valid = False

            if valid:
                print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter numbers only.")

        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

calculator()
