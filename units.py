"""Unit conversions"""

MM_PER_IN = 25.4
IN_PER_FT = 12


def ft(feet=0, inches=0):
    """Millimetres from feet and inches."""
    return (feet * IN_PER_FT + inches) * MM_PER_IN
