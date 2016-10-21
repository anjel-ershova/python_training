import pytest
from fixture.application import Application


@pytest.fixture(scope = "session")
def app2(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
