#!/usr/bin/python3
def multiple_returns(sentence):
    for char in sentence:
        if len(sentence) == 0:
            first = None
        else:
            length = len(sentence)
            first = sentence[0]
    return length, first
