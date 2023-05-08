#!/usr/bin/env python3
import os
import requests

def main():
    root_url = "http://www.pythonchallenge.com/pc/def"
    answer_url = "http://www.pythonchallenge.com/pcc/return/"
    git_dir = os.popen('git rev-parse --show-toplevel').read().rstrip("\n")
    challenge = "10"
    challenge_dir = f"{git_dir}/{challenge:02}"

    res = "bull"
    print(f"{root_url}/{res}.html")
    print(f"{answer_url}/{res}.html")



if __name__ == "__main__":
    main()
