from src.module_mock import getCurrentMoth
from unittest.mock import patch
from datetime import datetime
from pytest import raises

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

