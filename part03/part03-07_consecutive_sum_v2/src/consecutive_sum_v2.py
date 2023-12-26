# Write your solution here

limit = int(input("Limit: "))

total = 0
numbers = ""

i = 1
while total < limit:
    total += i
    if total >= limit:
        numbers += f"{i}"
    else:
        numbers += f"{i} + "
    i += 1

print(f"The consecutive sum: {numbers} = {total}")
