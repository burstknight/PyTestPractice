from src.module_a import square, concat
import pytest

@pytest.mark.math
def test_square():
    assert square(8) == 64
# End of test_square

@pytest.mark.string
def test_concat():
    sA = "Hello! "
    sB = "Joe!"

    assert concat(sA, sB) == "Hello! Joe!"
# End of test_concat

@pytest.mark.string
def test_concat_failed():
    sA = 555
    sB = 777

    """
    Use `with` and `pytest.raises()` to expect the function `concat()` will issue `TypeError`.
    """
    with pytest.raises(TypeError):
        concat(sA, sB)
    # End of with-block
# End of test_concat_failed
