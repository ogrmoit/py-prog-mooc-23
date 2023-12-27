# Write your solution here

def shortest(strings: list) -> str:
    short_str = strings[0]
    for string in strings:
        if len(string) < len(short_str):
            short_str = string
    return short_str

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)
