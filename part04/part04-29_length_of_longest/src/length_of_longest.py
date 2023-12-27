# Write your solution here

def length_of_longest(strings: list) -> int:
    long_len = len(strings[0])
    for string in strings:
        if len(string) > long_len:
            long_len = len(string)
    return long_len

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)
