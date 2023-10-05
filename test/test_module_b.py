import pytest
from src.module_b import updateValueByKey, checkKeyExists
from test.fixture import test_dict # import test_dict

def test_updateValueByKey(test_dict):
    dctNew = updateValueByKey(test_dict, "b", 999 )

    assert dctNew["b"] == 999
# End of test_updateValueByKey

def test_updateValueByKey_error(test_dict):
    with pytest.raises(KeyError):
        dctNew = updateValueByKey(dctRaw=test_dict, key="error_key", value=999)
    # End of with-block
# End of test_updateValueByKey_error

def test_checkKeyExits(test_dict):
    assert checkKeyExists(dctData=test_dict, key="a")
    assert not checkKeyExists(dctData=test_dict, key="not existed")

