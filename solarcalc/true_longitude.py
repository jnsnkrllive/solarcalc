from .equation_of_center import equation_of_center
from .mean_longitude import mean_longitude


def true_longitude(t: float) -> float:
    """
    Calculate the sun's true longitude in decimal degrees.

    Parameters:
        t (float): The time in Julian Centuries (36525 days) since J2000.0

    Returns:
        float: The sun's true longitude at the given time
    """
    # t must be in the range from year 1901 thru year 2099
    if (t < -0.99 or 1.00 < t):
        raise ValueError("t must be beteween -0.99 and 1.00: " + str(t))

    return equation_of_center(t) + mean_longitude(t)
