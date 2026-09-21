# Get price and quantity from the user
price_input = input("Enter the price of one item: ")
quantity_input = input("Enter the quantity you want to buy: ")

# Convert input strings to numbers
price = float(price_input)
quantity = int(quantity_input)

# Calculate the total cost
total = price * quantity

# Display the friendly summary
print(f"{quantity} items at {price:.2f} each = {total:.2f}")