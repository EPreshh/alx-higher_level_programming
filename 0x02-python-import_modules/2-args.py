#!/usr/bin/python3
import sys
count = len(sys.argv) - 1
if __name__ == "__main__":
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
        print("{}: {}".format(count, sys.argv[1]))
    elif count > 1:
        print("{} arguments:".format(count))
        for i in range(1, count + 1):
            print("{}: {}".format(i, sys.argv[i]))
