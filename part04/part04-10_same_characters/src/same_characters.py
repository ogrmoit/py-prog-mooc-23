# Write your solution here

def same_chars(text, index1, index2):
    if index1 < 0 or index2 < 0:
        return False
    elif index1 >= len(text) or index2 >= len(text):
        return False
    return text[index1] == text[index2]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    # same characters m and m
    print(same_chars("programmer", 6, 7)) # True

    # different characters p and r
    print(same_chars("programmer", 0, 4)) # False

    # the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False
