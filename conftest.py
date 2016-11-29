import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app2(request):
    global fixture
    # параметры, которые при запуске из командной строки позволяют указывать браузер и/или стартовую страницу
    browser = request.config.getoption("--browser")
    baseurl = request.config.getoption("--baseurl")
    if fixture is None:
        # строка ниже инициализирует фикстуру, происходит создание сессии
        fixture = Application(browser=browser, baseurl=baseurl)
    else:
        # метод, проверяющий, валидна ли фикстура
        if not fixture.is_valid():
            # строка ниже инициализирует фикстуру, происходит создание сессии
            fixture = Application(browser=browser, baseurl=baseurl)
    fixture.session.ensure_login(username="admin", password="secret")
    # возвращаем фикстуру (что с ней, работает или нет)
    return fixture


@pytest.fixture(scope="session", autouse=True) #autouse=True - атрибут, который принудительно заставляет фикстуру разрушиться в конце всех тестов
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseurl", action="store", default="http://localhost/addressbook/")