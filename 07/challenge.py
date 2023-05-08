#!/usr/bin/env python3
"""http://www.pythonchallenge.com/pc/def/oxygen.html
http://www.pythonchallenge.com/pc/def/oxygen.png
"""
import requests
import os
import re
from PIL import Image

def get_png(dest_dir):
    r = requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png")
    img = f"{dest_dir}/oxygen.png"
    with open(img, 'wb') as fd:
        fd.write(r.content)
    return img

def main():
    root_url = "http://www.pythonchallenge.com/pc/def"
    git_dir = os.popen('git rev-parse --show-toplevel').read().rstrip("\n")
    challenge = "07"
    challenge_dir = f"{git_dir}/{challenge}"
    img = get_png(challenge_dir)
    with Image.open(img) as im:
        #print(im.size)
        row = [im.getpixel((x, im.size[1] / 2)) for x in range(im.size[0])]
        #print(row)
        grey_pix = [p for p in row if p[0] == p[1] == p[2]]
        chars = [chr(p[0]) for p in grey_pix]
        prev = None
        grey_str = "".join(chars[::7])
        nums = re.findall("\d+", grey_str)
        print(f"{nums=}")
        s = "".join([chr(int(x)) for x in nums])
    print(f"{root_url}/{s}.html")



if __name__ == "__main__":
    main()
