def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount (if applicable).

    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to be applied.

    Returns:
    - float: The final price after applying the discount (if discount is 20% or higher),
             otherwise returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: ksh{final_price:.2f}")
else:
    print(f"No discount applied. Original price: ksh{original_price:.2f}")