import pytest
from src.module_b import updateValueByKey, checkKeyExists

def test_updateValueByKey():
    dctTest = {"a": 1, "b": 2}

    dctNew = updateValueByKey(dctTest, "b", 999 )

    assert dctNew["b"] == 999
# End of test_updateValueByKey

def test_updateValueByKey_error():
    dctTest = {"a": 1, "b": 2}

    with pytest.raises(KeyError):
        dctNew = updateValueByKey(dctRaw=dctTest, key="error_key", value=999)
    # End of with-block
# End of test_updateValueByKey_error

def test_checkKeyExits():
    dctTest = {"a": 1, "b": 2}

    assert checkKeyExists(dctData=dctTest, key="a")
    assert not checkKeyExists(dctData=dctTest, key="not existed")

