# Question : Write a program that takes user age as input and gets discount if they are on wednesday. 

age = int(input("Enter your age: \n"))
price = 12 if age >= 18 else 8

is_wednesday = True
price -= 2 if is_wednesday else 0
print("++Discounted++") if is_wednesday else print("++Not discounted++")
print("Original price: $12") if age >= 18 else print("Original price: $8")
print(f"Ticket price: ${price}")