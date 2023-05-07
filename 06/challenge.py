#!/usr/bin/env python3
"""http://www.pythonchallenge.com/pc/def/channel.html"""
from PIL import Image
import requests
import re
from zipfile import ZipFile

def get_image():
    r = requests.get("http://www.pythonchallenge.com/pc/def/channel.jpg")
    with open("channel.jpg", 'wb') as fd:
        fd.write(r.content)

def get_zip():
    r = requests.get("http://www.pythonchallenge.com/pc/def/channel.zip")
    with open("channel.zip", 'wb') as fd:
        fd.write(r.content)


def get_next(filename):
    with open(filename, 'r') as fd:
        content = fd.read()
        regex = "[0-9]+$"
        res = re.findall(regex, content)
        if len(res) > 0:
            return (res[0], content)

    return None


def main():
    #get_zip()
    first = 90052
    zip_fd = ZipFile("channel.zip", 'r')

    comments = ""
    res = get_next(f"{first}.txt")
    while res is not None:
        (nxt, line) = res
        comments += zip_fd.getinfo(f"{nxt}.txt").comment.decode()

        res = get_next(f"{nxt}.txt")
        if res is None:
            with open(f"{nxt}.txt", 'r') as fd:
                print(fd.read())
    print(comments)
    root_url = "http://www.pythonchallenge.com/pc/def"
    print(f"{root_url}/hockey.html")
    print(f"{root_url}/oxygen.html")







if __name__ == "__main__":
    main()
