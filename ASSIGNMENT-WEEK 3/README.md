
```markdown
# 💰 Discount Price Calculator

A simple Python program that calculates the final price of an item after applying a discount (if eligible).  

## 🚀 Features
- **🛒 User Input:** Accepts original price and discount percentage.
- **🎯 Smart Discounting:** Only applies discounts of **20% or higher**.
- **💰 Final Price Calculation:** Computes the discounted price or returns the original.
- **📊 Clean Output:** Displays results in a user-friendly format.

## ⚙️ How It Works
1. The user enters:
   - The original price (e.g., `100`).
   - The discount percentage (e.g., `25`).
2. The program checks:
   - If the discount is **≥20%**, it applies the discount.
   - Otherwise, it keeps the original price.
3. The result is printed with clarity (e.g., `Final price after 25% discount: $75.00`).

## 📋 Code Example
```python
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price

original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))
final_price = calculate_discount(original_price, discount)

print(f"Final price: ${final_price:.2f}")
```

## 🏃‍♂️ How to Run
1. Save the script as `discount_calculator.py`.
2. Run it in a terminal:
   ```bash
   python discount_calculator.py
   ```
3. Follow the prompts!

## 🛠️ Possible Extensions
- **🔒 Input Validation:** Ensure prices/discounts are positive numbers.
- **📈 Tiered Discounts:** Add rules like "30% off for $200+ purchases".
- **📦 Multi-Item Support:** Calculate discounts for a shopping cart.

