# Any PyTest file should start with "test_"
# PyTest method name should start with "test"
# Any code should be wrapped in method
# -k stands for method names execution, -s logs in output, -v stands for more information
# you can run specific file with py.test <filename>
# @pytest.mark.xfail - it does not show failed test
# fixture is used as setup methods that will be executed Before and After every test
# fixture can be used for all tests by creating a file conftest.py
# params can be done with return statements in tuple format
# when you define fixture scope to class only, it will return once before class initialized and once after

import pytest

'''@pytest.fixture()
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")
'''

@pytest.mark.smoke
def test_firstProgram(setup):
    print("HELLO")


@pytest.mark.xfail
def test_GreetCreditCard(setup):
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
