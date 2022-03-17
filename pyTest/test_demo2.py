# Any PyTest file should start with "test_"
# PyTest method name should start with "test"
# Any code should be wrapped in method
# you can mark (tag) @pytest.mark.smoke tests and then run with -m
# you can skip any test with @pytest.mark.skip

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"
