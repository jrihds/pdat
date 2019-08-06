#!/usr/bin/env python3
"""Generator objects."""

colours = ['blue', 'red', 'green', 'yellow']

def e_count(_list):
    """Count how many e's in a string."""
    for element in _list:
        yield element.count('e')

for value in e_count(colours):
    print(value)
