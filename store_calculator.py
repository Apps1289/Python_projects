# Creating a store calculator which takes user input for item prices till the
#  users decides to stop and then calculates the total price.

total = 0
while True:
    userInp = int(input("Enter the price: "))
    if userInp == -1:
        break

    total += userInp
    
print("Total price of items: ", total)
    