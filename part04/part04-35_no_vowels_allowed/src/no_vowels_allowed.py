# Write your solution here

def no_vowels(string: str) -> str:
    des_str = ""
    for char in string:
        if char in ["a", "e", "i", "o", "u"]:
            des_str += ""
        else:
            des_str += char
    return des_str

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
