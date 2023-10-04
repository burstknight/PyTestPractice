from typing import Dict, Union

def updateValueByKey(dctRaw: Dict, key: str, value: Union[str, int ,float]) -> Dict:
    """
    Description:
    =======================================================
    Update the value with the given key.

    Args:
    =======================================================
    - dctRaw: Given a dictionary to update value.
    - key: Give a key to update value
    - value: Give a new value to update the dictionary.

    Exception:
    =======================================================
    - KeyError: This method will issue `KeyError` if the given key dosen't exit.

    Returns:
    =======================================================
    - rtype: Dict, Return the updated dictionary.
    """
    if key not in dctRaw:
        raise KeyError
    # End of if-condition

    dctNew = dctRaw
    dctNew[key] = value

    return dctNew
# End of updateValueByKey

def checkKeyExists(dctData: Dict, key: str) -> bool:
    """
    Description:
    =======================================================
    Check if the given key exits in the given dictionary.

    Args:
    =======================================================
    - dctData: Give a dictionary to check.
    - key: Give a key to check if it exits in the dictionary.

    Returns:
    =======================================================
    - rtype: bool, Return `True` if the given key exits, otherwsie return `False`.
    """
    if key in dctData:
        return True
    else:
        return False
    # End of if-condition
# End of checkKeyExists
