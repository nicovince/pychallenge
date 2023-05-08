#!/usr/bin/env python3
"""http://www.pythonchallenge.com/pc/def/integrity.html"""
import bz2
import os

def main():
    root_url = "http://www.pythonchallenge.com/pc/def"
    git_dir = os.popen('git rev-parse --show-toplevel').read().rstrip("\n")
    challenge = "08"
    challenge_dir = f"{git_dir}/{challenge}"

    un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

    print(bz2.decompress(un))
    print(bz2.decompress(pw))

if __name__ == "__main__":
    main()
