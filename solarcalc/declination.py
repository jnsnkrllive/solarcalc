from math import asin, degrees, radians, sin
from .apparent_longitude import apparent_longitude
from .obliquity_of_ecliptic import obliquity_of_ecliptic


def declination(t: float) -> float:
    """
    Calculate the declination of the sun as seen from earth in decimal degrees.

    Parameters:
        t (float): The time in Julian Centuries (36525 days) since J2000.0

    Returns:
        float: The sun's declination at the given time
    """
    # t must be in the range from year 1901 thru year 2099
    if (t < -0.99 or 1.00 < t):
        raise ValueError("t must be beteween -0.99 and 1.00: " + str(t))

    sin_epsilon = sin(radians(obliquity_of_ecliptic(t)))
    sin_lambda = sin(radians(apparent_longitude(t)))
    return degrees(asin(sin_epsilon * sin_lambda))
