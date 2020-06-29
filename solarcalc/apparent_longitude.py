from math import radians, sin
from .true_longitude import true_longitude


def apparent_longitude(t: float) -> float:
    """
    Calculate the sun's apparent longitude in decimal degrees.

    Parameters:
        t (float): The time in Julian Centuries (36525 days) since J2000.0

    Returns:
        float: The sun's apparent longitude at the given time
    """
    # t must be in the range from year 1901 thru year 2099
    if (t < -0.99 or 1.00 < t):
        raise ValueError("t must be beteween -0.99 and 1.00: " + str(t))

    correction = 0.00569 + 0.00478 * sin(radians(-1934.136 * t + 125.04))
    return true_longitude(t) - correction
