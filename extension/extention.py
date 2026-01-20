#In a file called extensions.py, implement a program that prompts 
# the user for the name of a file and then outputs that file’s media
#  type if the file’s name ends, case-insensitively, in any of these suffixes:

#Extension program
extention = input("Enter a file name")
if extention.endswith("gif"):
    print("image/gif")
elif extention.endswith("jpg"):
    print("image/jpg")
elif extention.endswith("jpeg"):
    print("image/jpeg")
elif extention.endswith("png"):
    print("image/png")
else:
    print("application/octet-stream")
