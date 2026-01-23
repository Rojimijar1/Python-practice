#In a file called coke.py, implement a program that prompts the user 
# to insert a coin, one at a time, each time informing the user of the 
# amount due. Once the user has inputted at least 50 cents, output how 
# many cents in change the user is owed. Assume that the user will only
#  input integers, and ignore any integer that isn’t an accepted denomination.


total = 0
while total<50:
    coin = int(input("Insert coin:"))
    coin_accepted = [10,5,25]
    if coin in coin_accepted:
        total+=coin
        print("Amount due:",50-total)
    else:
         print("coin not accepted")
print("change owed:",total-50)
