#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    select_names = [name for name in names if not name.startswith("__")]
    select_names.sort()
    for name in select_names:
        print(name)
