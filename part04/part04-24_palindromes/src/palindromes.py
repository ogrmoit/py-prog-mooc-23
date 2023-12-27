# Write your solution here

def palindromes(string: str) -> bool:
    if len(string) == 0 or len(string) == 1:
        return True
    for i in range(len(string)//2):
        if string[i] != string[len(string)-i-1]:
            return False
    return True

def main():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        print("that wasn't a palindrome")

main()

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
