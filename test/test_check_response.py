from unittest import mock
from pytest_mock import MockFixture
from src.check_response import checkResponse
import pytest

def test_checkResponse_than_05():
    # Use `unittest.mock` to replace `callExternalApi()`

    with mock.patch("src.check_response.callExternalApi") as oMockApi:
        oMockApi.return_value = {"response_value": 0.95}

        assert checkResponse()
    # End of with-block
# End of test_checkResponse_than_05

def test_checkResponse_less_05(mocker: MockFixture):
    # Use `pytest_mock` to replace `callExternalApi()`.

    oMockApi = mocker.patch("src.check_response.callExternalApi", return_value= {"response_value": 0.25})

    assert False == checkResponse()
# End of test_checkResponse_less_05

def test_checkResponse_error(mocker: MockFixture):
    oMockApi = mocker.patch("src.check_response.callExternalApi", return_value= {})

    with pytest.raises(KeyError):
        checkResponse()
    # End of with-block
# End fo test_checkResponse_error
