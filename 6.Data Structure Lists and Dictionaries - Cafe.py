# Create a list called menu containing at least four items sold in the cafe
menu = ["octapus", "asparagus", "lasagne", "lemonade", "ice cream"]

# Create a dictionary called stock to contain the stock value for each item on the menu
stock = {"octapus": 17, "asparagus": 8, "lasagne": 14, "lemonade": 5, "ice cream": 10}

# Create a dictionary called price to contain the price for each item on the menu
price = {"octapus": 9, "asparagus": 23, "lasagne": 11, "lemonade": 7, "ice cream": 4}

# Calculate the total stock worth in the cafe and print the result
total_stock_value = sum (stock[items] * price[items] for items in menu)
print(f"The total stock value for items on the menu is {total_stock_value}")