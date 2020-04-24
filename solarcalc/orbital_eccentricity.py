def orbital_eccentricity(t: float) -> float:
    """
    Calculate the eccentricity of earth's orbit around the sun.

    Parameters:
        t (float): The time in Julian Centuries (36525 days) since J2000.0

    Returns:
        float: The earth's orbital eccentricity at the given time
    """
    # t must be in the range from year 1901 thru year 2099
    if (t < -0.99 or 1.00 < t):
        raise ValueError("t must be beteween -0.99 and 1.00: " + str(t))

    return -0.0000001267 * pow(t, 2) - 0.000042037 * t + 0.016708634
