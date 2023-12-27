# Write your solution here

def distinct_numbers(integers: list) -> list:
    nums = []
    for num in sorted(integers):
        if num not in nums:
            nums.append(num)
    return nums

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
