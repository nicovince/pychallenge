#!/usr/bin/env python3
import os
import requests
from PIL import Image

def get_img(dest_dir):
    r = requests.get("http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg")
    img = f"{dest_dir}/cave.jpg"
    with open(img, 'wb') as fd:
        fd.write(r.content)
    return img

def main():
    root_url = "http://www.pythonchallenge.com/pc/def"
    answer_url = "http://www.pythonchallenge.com/pcc/return/"
    git_dir = os.popen('git rev-parse --show-toplevel').read().rstrip("\n")
    challenge = "11"
    challenge_dir = f"{git_dir}/{challenge:02}"

    img = get_img(challenge_dir)
    odd_img = f"{challenge_dir}/odd.jpg"
    even_img = f"{challenge_dir}/even.jpg"
    all_odd_img = f"{challenge_dir}/all_odd.jpg"
    all_even_img = f"{challenge_dir}/all_even.jpg"
    with Image.open(img) as im:
        (x_len, y_len) = im.size
        print(f"{x_len=}, {y_len=}")
        print(f"{im.mode=}")
        with Image.new(im.mode, (int(x_len / 2), y_len)) as odd_im:
            for y in range(y_len):
                for x in range(1, x_len, 2):
                    odd_im.putpixel((int(x / 2), y), im.getpixel((x, y)))
            odd_im.save(odd_img, "JPEG")
        with Image.new(im.mode, (int(x_len / 2), y_len)) as even_im:
            for y in range(y_len):
                for x in range(0, x_len, 2):
                    even_im.putpixel((int(x / 2), y), im.getpixel((x, y)))
            even_im.save(even_img, "JPEG")
        with Image.new(im.mode, (int(x_len / 2), int(y_len / 2))) as all_even_im:
            for y in range(0, y_len, 2):
                for x in range(0, x_len, 2):
                    all_even_im.putpixel((int(x / 2), int(y / 2)), im.getpixel((x, y)))
            all_even_im.save(all_even_img, "JPEG")
        with Image.new(im.mode, (int(x_len / 2), int(y_len / 2))) as all_odd_im:
            for y in range(1, y_len, 2):
                for x in range(1, x_len, 2):
                    all_odd_im.putpixel((int(x / 2), int(y / 2)), im.getpixel((x, y)))
            all_odd_im.save(all_odd_img, "JPEG")

    res = "evil"
    print(f"{root_url}/{res}.html")
    print(f"{answer_url}/{res}.html")



if __name__ == "__main__":
    main()
