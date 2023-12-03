"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for item in items:
        if not isinstance(item, str):
            string = str(item)
        else:
            string = item

        if string in frequencies:
            frequencies[string] += 1
        else:
            frequencies[string] = 1

    return frequencies
