#In a file called einstein.py, implement a program in Python that 
# prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

#E=mc^2
def square(c):
    c=pow(300000000,2)
    return c
def einstein():
    m= int(input("m:"))
    e=m*square(m)
    print("e:",e)
einstein()

