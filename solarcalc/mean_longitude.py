def mean_longitude(t: float) -> float:
    """
    Calculate the sun's mean longitude in decimal degrees.

    Parameters:
        t (float): The time in Julian Centuries (36525 days) since J2000.0

    Returns:
        float: The sun's mean longitude at the given time
    """
    # t must be in the range from year 1901 thru year 2099
    if (t < -0.99 or 1.00 < t):
        raise ValueError("t must be beteween -0.99 and 1.00: " + str(t))

    l = (0.0003032 * pow(t, 2) + 36000.76983 * t + 280.46646) % 360
    return l + 360 if l < 0 else l
