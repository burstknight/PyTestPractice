def square(num: int) -> int:
    """
    Description:
    =======================================================
    Calculate square for the given number.

    Args:
    =======================================================
    - num: Give an integer.

    Returns:
    =======================================================
    - rtype: int, Return a squared number.
    """
    return num**2
# End of square

def concat(s1: str, s2: str) -> str:
    """
    Description:
    =======================================================
    Concat two strings as a string.

    Args:
    =======================================================
    - s1: Give the first string.
    - s2: Give the second string.

    Returns:
    =======================================================
    - rtype: str, Return the concated string.
    """
    if not (isinstance(s1, str) and isinstance(s2, str)):
        raise TypeError("Paramenter type error!")
    else:
        return s1 + s2
    # End of if-condition
# End of concat
