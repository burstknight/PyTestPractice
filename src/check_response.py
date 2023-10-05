from src.external import callExternalApi

def checkResponse() -> bool:
    """
    Description:
    =======================================================
    Check if the response of the function `callExternalApi()`
    is greater than `0.5`.

    Returns:
    =======================================================
    - rtype: bool, Return `True` if the response is greater than `0.5`, otherwise return `False`.
    """
    dctResult = callExternalApi()
    fResponseValue = dctResult.get("response_value", None)

    if fResponseValue is None:
        raise KeyError("response_value not exists!")
    elif fResponseValue > 0.5:
        return True
    else:
        return False
    # End of if-condition
# End of checkResponse
