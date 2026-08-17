print("Welcome to the Profit Calculator!")

Original_price = float(input("\nPlease enter the amount you bought the item for: "))

Selling_price = float(input("\nPlease enter the amount you sold the item for: "))

if Selling_price > Original_price:
    Profit = Selling_price - Original_price
    print("\nYou made a profit of", Profit)
else:
    Loss = Original_price - Selling_price
    print("\nYou made a loss ")
    print("You made a loss of", Loss)

print("\nThank you for using the Profit Calculator!")