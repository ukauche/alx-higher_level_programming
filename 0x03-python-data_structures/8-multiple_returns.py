#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        length = 0
        first = None
    else:
        length = len(sentence)
        first = sentence[0]
    return length, first
