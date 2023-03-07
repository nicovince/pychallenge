#!/usr/bin/env python3
import string

input_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alphabet = string.ascii_lowercase
url = "map"

def translate_letters(data, offset):
    table = f"{alphabet[offset:]}{alphabet[0:offset]}"
    trans = data.translate(str.maketrans(alphabet, table))
    print(trans)
    return trans

translate_letters(input_str, 2)
next = translate_letters(url, 2)
print(f"http://www.pythonchallenge.com/pc/def/{next}.html")
