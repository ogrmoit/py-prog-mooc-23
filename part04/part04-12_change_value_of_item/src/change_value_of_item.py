# Write your solution here

my_list = [1, 2, 3, 4, 5]

while True:
    i = int(input("Index: "))
    if i == -1:
        break
    val = int(input("New value: "))
    my_list[i] = val
    print(my_list)
