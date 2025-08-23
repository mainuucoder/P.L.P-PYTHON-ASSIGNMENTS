
# Arithmetic Operations Formatter

This Python script allows users to input two numbers and displays the results of basic arithmetic operations — addition, subtraction, multiplication, and division — in a clean and readable table format.

## ✨ Features

- Handles both integer and floating-point numbers.
- Removes unnecessary `.0` from whole numbers for cleaner output.
- Rounds decimal results to 2 decimal places.
- Handles division by zero safely.
- Prints results in a well-formatted table.

## 📋 Example Output

```

Enter first number: 10
Enter second number: 3.5
 Num1       Op    Num2       Result

10         +     3.5        13.5
10         -     3.5        6.5
10         ×     3.5        35.0
10         ÷     3.5        2.86

````

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Save the script as `assignment.py` (or any filename you like).
3. Open a terminal or command prompt.
4. Run the script using:

```bash
python assignment.py
````

5. Enter two numbers when prompted.

## 🧠 How It Works

* `format_number(num)`: Removes `.0` if the number is whole, else rounds to 2 decimals.
* `compute_operations(a, b)`: Performs `+`, `-`, `×`, and `÷` operations and prints the results in a table.
* Division by zero is gracefully handled by displaying `"Undefined"`.


## 💡 Optional Enhancements

You can easily modify the script to:

* Allow multiple operations in a loop
* Export results to a file (e.g., CSV or TXT)
* Use a graphical interface (GUI) for better interactivity
