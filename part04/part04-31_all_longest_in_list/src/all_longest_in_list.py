# Write your solution here

def all_the_longest(strings: list) -> list:
    long_str_lst = []
    long_len = len(strings[0])
    long_str = strings[0]
    for string in strings:
        if len(string) > long_len:
            long_len = len(string)
    for string in strings:
        if len(string) == long_len:
            long_str_lst.append(string)
    return long_str_lst

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
