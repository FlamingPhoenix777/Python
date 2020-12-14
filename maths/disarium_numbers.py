def is_disarium(num: int) -> bool:
    """
    Checks if a number is a "Disarium number".
    A Disarium number is a number defined by the following process:
    Sum of its digits powered with their respective position is equal
    to the original number. The number must be a whole number greater than 0.

    For more info on disarium numbers:
    https://www.geeksforgeeks.org/disarium-number/

    >>> is_disarium(89)
    True
    >>> is_disarium(175)
    True
    >>> is_disarium(518)
    True
    >>> is_disarium(42)
    False
    >>> is_disarium(12)
    False
    >>> is_disarium(20)
    False
    >>> is_disarium(0)
    False
    >>> is_disarium(-3)
    False
    """
    if (num >= 0):
        return sum([int(digit) ** (pos + 1) for pos, digit in enumerate(str(num))]) == num
    else:
        return False
