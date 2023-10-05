from src.module_mock import getCurrentMoth, sleepTime
from unittest.mock import patch
from datetime import datetime
from pytest import raises, mark
import time

def test_getCurrentMonth():
    with patch("src.module_mock.datetime") as oMockDatetime:
        oMockDatetime.now.return_value = datetime(2023, 3, 1, 0, 0, 0)
        iMonth = getCurrentMoth()

        assert iMonth ==3
    # End of with-block
# End of test_getCurrentMonth

def test_getCurrentMonth_fail():
    with patch("src.module_mock.datetime") as oMockDatetime:
        with raises(Exception):
            oMockDatetime.now.return_value = datetime(2023, -1, 5, 0, 0, 0)
            iMonth = getCurrentMoth()
        # End of with-block
    # End of with-block
# ENd of test_getCurrentMonth_fail


@mark.long_time_test
def test_sleepTime():
    # Use the wrong wat to perform a long time test.

    iResponse = sleepTime(20)

    assert iResponse == 20
# End of test_sleepTime

def test_sleepTime_mock():
    # Use the first way to use `patch` to replace `time.sleepTime()` with `None` object.

    with patch("src.module_mock.time.sleep"):
        iResponse = sleepTime(20)

        assert iResponse == 20
    # End of with-block
# End of test_sleepTime_mock

def test_sleepTime_replace():
    # Use `patch` to replace `time.sleep()` with the function `time.sleep(2)`

    with patch("src.module_mock.time.sleep", new_callable=time.sleep(2)):
        iResponse = sleepTime(20)

        assert iResponse == 20
    # End of with-block
# End of test_sleepTime_replace
