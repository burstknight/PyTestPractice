from typing import Dict
import time
import random

def callExternalApi() -> Dict:
    """
    Description:
    =======================================================
    Simulate to call external API.

    Returns:
    =======================================================
    - rtype: Dict, Return the response from the external API.
    """
    time.sleep(0.5)

    if random.random() < 0.5:
        return {}
    # End of if-condition

    return {"response_value": random.random()}
# End of callExternalApi
