#!/usr/bin/env python3
import os
import requests

def get_file(dest_dir):
    r = requests.get("http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx")
    img = f"{dest_dir}/evil2.gfx"
    with open(img, 'wb') as fd:
        fd.write(r.content)
    return img

def main():
    root_url = "http://www.pythonchallenge.com/pc/return/"
    answer_url = "http://www.pythonchallenge.com/pcc/return/"
    git_dir = os.popen('git rev-parse --show-toplevel').read().rstrip("\n")
    challenge = "12"
    challenge_dir = f"{git_dir}/{challenge:02}"

    gfx = get_file(challenge_dir)
    with open(gfx, 'rb') as fd:
        data = fd.read()
    for i in range(5):
        with open(f"{i}.jpg", 'wb') as fd:
            fd.write(data[i::5])

    res = "disproportional"
    print(f"{root_url}/{res}.html")
    print(f"{answer_url}/{res}.html")



if __name__ == "__main__":
    main()
