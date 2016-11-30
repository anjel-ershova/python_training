import os.path
import json
import pytest
from fixture.application import Application

fixture = None
target = None

@pytest.fixture
def app2(request):
    global fixture
    global target
    # параметры, которые при запуске из командной строки позволяют указывать браузер и/или стартовую страницу
    browser = request.config.getoption("--browser")
    if target is None:
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        # config_file_path - лок. перем., содержащая путь к конфигу,
        # config_file_obj - переменная, которая содержит объект, указывающий на открытый файл
        with open(config_file_path) as config_file_obj:
            target = json.load(config_file_obj)
    if fixture is None or not fixture.is_valid():
        # строка ниже инициализирует фикстуру eckb ее нет или она невалидна, происходит создание сессии
        fixture = Application(browser=browser, baseurl=target["baseurl"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
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
    parser.addoption("--target", action="store", default="target.json")