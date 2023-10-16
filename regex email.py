import re

if __name__ == '__main__':
    email = input("Enter email? ").strip()
    if re.search(r"^(?:\w|\.)+@(?:\w|\.)*\w+\.(?:com|in|edu)$", email, re.IGNORECASE):
        # parenthesis() is used to group the items
        print("Valid")
    else:
        print("Invalid")

# "\d" decimal digit
# "\D" not a decimal digit
# "\s" whitespace characters
# "\S" not whitespace characters
# "\w" word character(including numbers and underscore)
# "\W" not a word character
