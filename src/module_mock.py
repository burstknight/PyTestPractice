from datetime import datetime
import time

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

def sleepTime(iSecond: int) -> int:
    """
    Description:
    =======================================================
    Simulate to perform a long time function.

    Args:
    =======================================================
    - iSecond: Give a number to sleep.

    Returns:
    =======================================================
    - rtype: int, Return the sleeping time.
    """
    print("Ready for sleeping!")
    time.sleep(iSecond)

    return iSecond
# End of sleepTime
