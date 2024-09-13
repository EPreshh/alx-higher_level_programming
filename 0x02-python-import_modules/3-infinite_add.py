#!/usr/bin/python3
import sys
count = 0
num_args = len(sys.argv) - 1
if __name__ == "__main__":
    for i in range(1, num_args + 1):
        arg = int(sys.argv[i])
        count += arg
    print(count)
