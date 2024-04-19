i = 0
j = 0
k = 0
price1 = 0
price2 = 0
price3 = 0
count_i = 0
count_j = 0
count_k = 0
user_name = input("Welcome to GC Fruit Market! \nWhat is your name? \n")
choice = int(input(f"Welcome {user_name}! Which fruit would you like to buy? "
                   f"\n1. Apple at $2 \n2. Grape at $1 \n3. Orange at $3  \n"))
if choice == 1:
    i += 1
    print("You bought an apple at $2")
    price1 += 2
    count_i = i
elif choice == 2:
    j += 1
    print("You bought grape at $1")
    price2 += 1
    count_j = j
else:
    k += 1
    print("You bought an orange at $3")
    price3 += 3
    count_k = k
choice1 = input("Would you like to buy another piece of fruit? y/n  \n")
while choice1 != 'n':
    choice = int(input(f"Welcome {user_name}! Which fruit would you like to buy? "
                       f"\n1. Apple at $2 \n2. Grape at $1 \n3. Orange at $3  \n"))
    if choice == 1:
        i += 1
        print("You bought an apple at $2")
        price1 += 2
        count_i = i
    elif choice == 2:
        j += 1
        print("You bought grape at $1")
        price2 += 1
        count_j = j
    else:
        k += 1
        print("You bought an orange at $3")
        price3 += 3
        count_k = k
    choice1 = input("Would you like to buy another piece of fruit? y/n  \n")

print(f"Order for {user_name}")
print(f"{count_i} apple(s) at $2 apiece")
print(f"{count_j} grape(s) at $1 apiece")
print(f"{count_k} oranges(s) at $3 apiece")
Subtotal = price1 + price2 + price3
print(f"Subtotal: {Subtotal}")
Tax = Subtotal * 0.05
print(f"Tax 5%: {Tax}")
Total = Subtotal + Tax
print(f"Total: {Total}")
