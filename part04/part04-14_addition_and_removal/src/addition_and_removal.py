# Write your solution here

my_list = []

num = 1

while True:
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "d":
        my_list.append(num)
        num += 1
    elif choice == "r":
        my_list.pop(len(my_list)-1)
        num -= 1
    elif choice == "x":
        break
print("Bye!")
