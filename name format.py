import re

"""
if __name__ == '__main__':
    name = input("What's your name? ").strip()
    if matches := re.search(r"^(.+), *(.+)$", name):  # here parenthesis is used to capture the data
        name = matches.group(1) + " " + matches.group(2)
    print(f"Hello {name}")
"""
if __name__ == '__main__':
    url = input("URL: ").strip()
    # if matches:=re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    #    print(f"Username: {matches.group(2)}")  # group(2) is needed coz in the "www." is stored in group(1)
    if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
        print(f"Username: {matches.group(1)}")  # (?: ) makes sure the content in it is not captured
