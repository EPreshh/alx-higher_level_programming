#!/usr/bin/python3
def uppercase(str):
    result = []
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            result.append(chr(ord(i) - 32))
        else:
            result.append(i)
    print("{}".format("".join(result)))
