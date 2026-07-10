# menu={
#     "Pizza":99,
#     "Pasta":60,
#     "Burger":70,
#     "Salad":80,
#     "Coffe":60,
#     "Tea":50,
#     "Veg Manchow Soup": 140,
#     "Paneer Tikka": 220,
#     "Chicken Lollipops": 250,
#     "Crispy Veg": 180,
#     "Veg Manchow Soup": 140,
#     "Paneer Tikka": 220,
#     "Chicken Lollipops": 250,
#     "Crispy Veg": 180,
# }

# print("Welcome to Python Restaurant...")
# print("""
# Pizza: Rs 99
# Pasta: Rs 60
# Burger: Rs 70
# Salad: Rs 80
# Coffee: Rs 60
# Tea: Rs 50
# Veg Manchow Soup: Rs 140
# Paneer Tikka: Rs 220
# Chicken Lollipops: Rs 250
# Crispy Veg: Rs 180
# """)

# order_total=0

# item_1=input("Enter the name of item you want to order : ")

# if item_1  in menu:
#     order_total+= menu[item_1]
#     print(f"Your item {item_1} has been added to your order")
# else:
#     print(f"Ordered item {item_1} is not available yet!")
# another_order = input("Do you want to add another item? (Yes/No) :")    
# if another_order=="yes":
#     item_2 = input ("Enter the name of second item = ")
#     if item_2 in menu:
#         order_total += menu[item_2]
#         print(f"Item {item_2} has been added to order")  
#     else:
#         print(f"Ordered item {item_2} is  not available!")

# print(f"The total amount of items to pay is {order_total}") 
# print("\n------------------------------------------")
# print("     Thank You for Visiting Our Restaurant!")
# print("        We Hope to Serve You Again 😊")
# print("           Have a Great Day!")
# print("------------------------------------------")                    

menu={
    "Pizza":99,
    "Pasta":60,
    "Burger":70,
    "Salad":80,
    "Coffe":60,
    "Tea":50,
    "Veg Manchow Soup": 140,
    "Paneer Tikka": 220,
    "Chicken Lollipops": 250,
    "Crispy Veg": 180,
    "Veg Manchow Soup": 140,
    "Paneer Tikka": 220,
    "Chicken Lollipops": 250,
    "Crispy Veg": 180,
}

print("Welcome to Python Restaurant...")
print("""
Pizza: Rs 99
Pasta: Rs 60
Burger: Rs 70
Salad: Rs 80
Coffee: Rs 60
Tea: Rs 50
Veg Manchow Soup: Rs 140
Paneer Tikka: Rs 220
Chicken Lollipops: Rs 250
Crispy Veg: Rs 180
""")

order_total=0
item_1=input("Enter the name of item you want to order : ")
if item_1  in menu:
    order_total+= menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")
another_order = input("Do you want to add another item? (Yes/No) :")    
if another_order=="yes":
    item_2 = input ("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")  
    else:
        print(f"Ordered item {item_2} is  not available!")
print(f"The total amount of items to pay is {order_total}") 
print("\n------------------------------------------")
print("     Thank You for Visiting Our Restaurant!")
print("        We Hope to Serve You Again 😊")
print("           Have a Great Day!")
print("------------------------------------------")      



