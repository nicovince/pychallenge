#!/usr/bin/env python3
"""http://www.pythonchallenge.com/pc/return/bull.html"""
import os
import requests


def get_next(v):
    v_str = f"{v}"
    cnt = 1
    last_cnt = cnt
    prev = v_str[0]
    res = ""

    for c in v_str[1:]:
        if c != prev:
            #print(f"{c=}; {prev=}; {cnt=}")
            res += f"{cnt}{prev}"
            cnt = 1
            last_cnt = cnt
        else:
            cnt += 1
            last_cnt = cnt
        prev = c
    res += f"{last_cnt}{prev}"
    return int(res)

def main():
    root_url = "http://www.pythonchallenge.com/pc/return"
    answer_url = "http://www.pythonchallenge.com/pcc/return"
    git_dir = os.popen('git rev-parse --show-toplevel').read().rstrip("\n")
    challenge = "10"
    challenge_dir = f"{git_dir}/{challenge:02}"

    prev = 1
    l = [prev]
    for i in range(30):
        current = get_next(prev)
        #print(f"{i}: {prev} -> {current}")
        cur_str = f"{current}"
        print(f"{i}: {len(cur_str)}")
        prev = current
        l.append(current)
    print(l[0: 8])

    res = len(f"{l[30]}")


    print(f"{root_url}/{res}.html")
    print(f"{answer_url}/{res}.html")



if __name__ == "__main__":
    main()
