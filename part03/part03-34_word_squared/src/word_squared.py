# Write your solution here

def squared(text, times):
    i = 0
    text = text * (times * times)
    while i < times * times:
        print(text[i:i+times])
        i += times

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
