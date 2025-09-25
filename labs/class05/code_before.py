# Goal: Return the index of value in the list, or -1 if not found.
# Known issues (let the reviewer catch them):
# - It keeps iterating after found.
# - Missing type hints and docstring.
# - Performance and readability can be improved.

def find_index(lst, value):
    pos = -1
    for i in range(len(lst)):
        if lst[i] == value:
            pos = i   # keeps iterating after finding
    return pos
