#!/usr/bin/python3
def magic_calculation(a, b):
    try:
        if a > b:
            return a - b
        elif a < b:
            return (a + b) * 2
        else:
            return a * b
    except:
        return None

