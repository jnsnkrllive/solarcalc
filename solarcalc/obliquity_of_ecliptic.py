import math


def obliquity_of_ecliptic(t: float) -> float:
    """
    Calculate the obliquity of earth's ecliptic around the sun in decimal degrees.

    Parameters:
        t (float): The time in Julian Centuries (36525 days) since J2000.0

    Returns:
        float: The obliquity of earth's ecliptic at the given time
    """
    # t must be in the range from year 1901 thru year 2099
    if (t < -0.99 or 1.00 < t):
        raise ValueError("t must be beteween -0.99 and 1.00: " + str(t))

    e0 = (0.001813 * pow(t, 3) - 0.00059 * pow(t, 2) - 46.815 * t + 1581.448) / 3600 + 23
    omega = -1934.136 * t + 125.04 
    return e0 + 0.00256 * math.cos(math.radians(omega))
