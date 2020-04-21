def mean_anomaly(t: float) -> float:
    """
    Calculate the sun's mean anomaly in decimal degrees.

    Parameters:
        t (float): The time in Julian Centuries (36525 days) since J2000.0

    Returns:
        float: The sun's mean anomaly at the given time
    """
    # t must be in the range from year 1901 thru year 2099
    if (t < -0.99 or 1.00 < t):
        raise ValueError("t must be beteween -0.99 and 1.00: " + str(t))

    return -0.0001537 * pow(t, 2) + 35999.05029 * t + 357.52911
