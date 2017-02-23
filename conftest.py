import os.path
import jsonpickle
import json
import pytest
from fixture.application import Application
import importlib
from fixture.db import DbFixture

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        # config_file_path - лок. перем., содержащая путь к конфигу,
        # config_file_obj - переменная, которая содержит объект, указывающий на открытый файл
        with open(config_file_path) as config_file_obj:
            target = json.load(config_file_obj)
    return target

@pytest.fixture
def app2(request):
    global fixture
    # параметры, которые при запуске из командной строки позволяют указывать браузер
# browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():
        # строка ниже инициализирует фикстуру eckb ее нет или она невалидна, происходит создание сессии
        fixture = Application(browser=request.config.getoption("--browser"), baseurl=web_config["baseurl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    # возвращаем фикстуру (что с ней, работает или нет)
    return fixture

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=db_config["host"], database=db_config["database"],
                          user=db_config["user"], password=db_config["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True) #autouse=True - атрибут, который принудительно заставляет фикстуру разрушиться в конце всех тестов
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            # для .parametrize используются такие параметры:
            # 1 - название параметра, куда передаются тест. данные,
            # 2 - откуда тест. данные брать,
            # 3 - список с текстовым предлставлением тест. данных
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\\%s.json" % file)) as f:
        return jsonpickle.decode(f.read())

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")