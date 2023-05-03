#!/usr/bin/env python3
"""http://www.pythonchallenge.com/pc/def/peak.html"""
import requests
import pickle

def get_pickle_file():
    r = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
    with open("banner.p", 'wb') as fd:
        fd.write(r.content)

def read_pickle(filename):
    with open(filename, 'rb') as fd:
        return pickle.Unpickler(fd).load()

def print_stuff(stuff):
    for l in stuff:
        line = ""
        for chunk in l:
            line = f"{line}{chunk[0] * chunk[1]}"
        print(line)

def main():
    get_pickle_file()
    r = read_pickle("banner.p")
    print_stuff(r)
    root_url = "http://www.pythonchallenge.com/pc/def"
    print(f"{root_url}/channel.html")

if __name__ == "__main__":
    main()
