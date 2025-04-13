import math

def volume_of_sphere(radius: float) -> float:
    """finds volume of sphere with radius"""
    volume = (4/3*radius**3)*math.pi
    return volume
assert volume_of_sphere(4) == 4/3*(4**3)*math.pi
assert volume_of_sphere(3) ==4/3*(3**3)*math.pi





