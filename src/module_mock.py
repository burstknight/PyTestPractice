from datetime import datetime

def getCurrentMoth() -> int:
    """
    Description:
    =======================================================
    Get the current month.

    Returns:
    =======================================================
    - rtype: int, Return the current month.
    """
    oToday = datetime.now()

    iMonth = oToday.month
    if iMonth < 0:
        raise Exception("Wrong month")
    # End of if-condition

    return iMonth
# End of getCurrentMoth
