import math
from .mean_anomaly import mean_anomaly


def equation_of_center(t: float) -> float:
    """
    Calculate the equation of center for the sun in decimal degrees.

    Parameters:
        t (float): The time in Julian Centuries (36525 days) since J2000.0

    Returns:
        float: The sun's equation of center at the given time
    """
    # t must be in the range from year 1901 thru year 2099
    if (t < -0.99 or 1.00 < t):
        raise ValueError("t must be beteween -0.99 and 1.00: " + str(t))

    m = mean_anomaly(t)
    sinm = math.sin(math.radians(m))
    sin2m = math.sin(2 * math.radians(m))
    sin3m = math.sin(3 * math.radians(m))
    return sinm * (-0.000014 * pow(t, 2) - 0.004817 * t + 1.914602)\
        + sin2m * (-0.000101 * t + 0.019993)\
        + sin3m * 0.000289
