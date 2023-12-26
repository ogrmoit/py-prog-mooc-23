# Write your solution here

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

i = string.find(substring)

twice = False

if i != -1 and i+len(substring) <= len(string):
    i2 = string.find(substring, i+len(substring))
    if i2 != -1:
        twice = True

if twice:
    print(f"The second occurrence of the substring is at index {i2}.")
else:
    print(f"The substring does not occur twice in the string.")
