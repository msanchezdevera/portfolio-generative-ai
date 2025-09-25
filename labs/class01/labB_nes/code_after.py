from math import sqrt

def distance_3d(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    """Euclidean distance between two 3D integer points."""
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dz = a[2] - b[2]
    return sqrt(dx * dx + dy * dy + dz * dz)
