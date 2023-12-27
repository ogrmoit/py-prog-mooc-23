# Write your solution here

def list_of_stars(integers: list) -> None:
    for num in integers:
        print("*" * num)

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])
