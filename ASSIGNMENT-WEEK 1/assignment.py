def format_number(num):
    """Remove .0 from whole numbers while keeping decimals for floating-point"""
    if isinstance(num, (int, float)):
        return int(num) if num == int(num) else round(num, 2)
    return num

def compute_operations(a, b):
    # Perform calculations
    operations = {
        "+": a + b,
        "-": a - b,
        "×": a * b,
        "÷": a / b if b != 0 else "Undefined"
    }
    
    # Format numbers for display
    display_a = format_number(a)
    display_b = format_number(b)
    
    # Display results in table with operation between numbers
    print("\n{:<10} {:<5} {:<10} {:<15}".format('Num1', 'Op', 'Num2', 'Result'))
    print("-" * 40)
    for op, result in operations.items():
        display_result = format_number(result) if result != "Undefined" else result
        print("{:<10} {:<5} {:<10} {:<15}".format(
            display_a, op, display_b, display_result))

# Get user input
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    compute_operations(num1, num2)
except ValueError:
    print("Error: Please enter valid numbers")