#Natnael Telku
# Function to perform basic arithmetic operations
def perform_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check for division by zero
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"


# Main calculator function
def calculator():
    try:
        # Get user input for the first number, used to handle both integers and decimal numbers
        num1 = float(input("Enter the first number: "))
        
        # Get user input for the arithmetic operator
        operator = input("Enter an operator (+, -, *, /): ")
        
        # Get user input for the second number
        num2 = float(input("Enter the second number: "))
        
        # Perform the calculation
        result = perform_operation(num1, num2, operator)
        
        # Display the result
        print("Result:", result)

    except ValueError:
        # Handle the case where the user enters a non-numeric value
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        # Handle any other unexpected errors
        print("An error occurred:", str(e))


# Call the calculator function
calculator()
