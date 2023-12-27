# Write your solution here

def longest_series_of_neighbours(numbers: list) -> int:
    neighbours = 0
    max_neighbours = 0
    for i in range(len(numbers)-1):
        if abs(numbers[i]-numbers[i+1]) == 1:
            neighbours += 1
            if neighbours > max_neighbours:
                max_neighbours = neighbours
        else:
            neighbours = 0
    return max_neighbours + 1

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
