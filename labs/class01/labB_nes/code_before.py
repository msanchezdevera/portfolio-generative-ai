# Utilities for 2D points (int coordinates)

from math import sqrt

def distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    # Typo on purpose to trigger NES (this is invalid Python):
    # 'cont' will likely be suggested to change into a proper assignment.
    cont dx = a[0] - b[0]
    cont dy = a[1] - b[1]
    return sqrt(dx * dx + dy * dy)
