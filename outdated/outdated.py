#In a file called outdated.py, implement a program that prompts the
#  user for a date, anno Domini, in month-day-year order, formatted 
# like 9/8/1636 or September 8, 1636, wherein the month in the latter 
# might be any of the values in the list below:

# grocery.py

groceries = {}

while True:
    try:
        item = input().strip().lower()

        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1

    except EOFError:
        break

for item in sorted(groceries):
    print(groceries[item], item.upper())
