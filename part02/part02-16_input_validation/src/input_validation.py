# Write your solution here

from math import sqrt

while True:
    num = int(input("Please type in a number: "))
    if num < 0:
        print("Invalid number")
    elif num == 0:
        break
    else:
        print(sqrt(num))
print("Exiting...")
