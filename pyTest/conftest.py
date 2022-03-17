import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul", "Shetty", "academy.com"]


@pytest.fixture(params= [("chrome","Rahul"),("Firefox", "asdsf"), ("IE", "SS")])
def crossBrowser(request):
    return request.param
