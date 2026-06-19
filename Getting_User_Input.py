# # # Getting the user input
# # name = input("What is your name? ")
# # print("your name is ", name)
# # print(type(name))

# Price = input("Enter price")
# Quantity = input("Enter quantity")
# Total_value = Price * Quantity
# Print(total_value)
# # The above code will give an error because the input function returns a string and we cannot multiply two strings. We need to convert the input to a number before performing the multiplication.

Price = input("Enter price: ")
Quantity = input("Enter quantity: ")
Total_value = float(Price) * int(Quantity)
print(Total_value)
# In the above code, we have converted the price to a float and the quantity to an integer before performing the multiplication. This will give us the correct total value.




