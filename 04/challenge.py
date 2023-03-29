#!/usr/bin/env python3
import re
import requests

def get_next_nothing(base_url, nothing):
    url = f"{base_url}?nothing={nothing}"
    r = requests.get(url)
    print(r.text)
    regex = "[0-9]+$"
    res = re.findall(regex, r.text)
    if len(res) > 0:
        return res[0]
    return None

def main():
    root_url = "http://www.pythonchallenge.com/pc/def"
    base_url = f"{root_url}/linkedlist.php"
    #first_nothing = 12345
    current_nothing = 3875
    while current_nothing is not None:
        prev_nothing = current_nothing
        current_nothing = get_next_nothing(base_url, current_nothing)

    print(f"{base_url}?nothing={int(int(prev_nothing)/2)}")

    current_nothing = int(int(prev_nothing) / 2)
    while current_nothing is not None:
        prev_nothing = current_nothing
        current_nothing = get_next_nothing(base_url, current_nothing)

    r = requests.get(f"{base_url}?nothing={prev_nothing}")
    print(f"{root_url}/{r.text}")

if __name__ == "__main__":
    main()
