#Create a Python program that calculates the final price of a product after applying a discount.
while True:
    try:
        original_price = float(input("The price of your product is: $"))
        if original_price <= 0:
            raise ValueError("Price must be positive.")
        discount_percentage = float(input("Your discount was: %"))
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount must be between 0 and 100.")
        break  # Exit the loop if input is valid
    except ValueError as ve:
        print(f"Invalid input: {ve}")

after_discount = original_price - (discount_percentage/100 * original_price)
print(f"The original price was ${original_price:.2f}. After a discount of {discount_percentage:.0f}%, your price is ${after_discount:.2f}.")
