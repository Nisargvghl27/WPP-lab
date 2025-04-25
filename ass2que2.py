# Write a program that repeatedly asks the user to enter product names and prices. Store all of these in a dictionary whose keys are the product names and whose values are the prices. When the user is done entering products and prices, allow them to repeatedly enter a product name and print the corresponding price or a message if the product is not in the dictionary.

dic = {}
while True:
    product = input("Enter product name (0 to exit the loop): ").strip()
    if product == "0":
        break
    else:
        try:
            price = float(input(f"Enter price of product {product} : "))
            print()
            dic[product] = price
        except ValueError:
            print("Entered price is invalid.")

print()
while True:
    check = input("Enter product name to check (0 to exit the loop): ")
    if check == "0":
        break
    else:
        if check in dic:
            product = check
            price = dic[product]
            print(f"Product '{product}' is available and its price is {price} Rs. .")
        else:
            print("Item is unavailable.")
    print()
