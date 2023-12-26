# Write your solution here

def print_many_times(text, times):
    while times > 0:
        print(text)
        times -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("hi", 5)

    print()

    text = "All Pythons, except one, grow up"
    times = 3
    print_many_times(text, times)
