#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first_char = None
        return (0, None)
    else:
        first_char = sentence[0]
        length = len(sentence)
    return (length, first_char)
