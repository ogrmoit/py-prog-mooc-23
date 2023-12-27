# Write your solution here

def line(times, text):
    if text == "":
        text = "*"
    print(text[0] * times)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")
