import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app2():
    global fixture
    if fixture is None:
        # строка ниже инициализирует фикстуру, происходит создание сессии
        fixture = Application()
        #fixture.session.ensure_login(username="admin", password="secret")
    else:
        # метод, проверяющий, валидна ли фикстура
        if not fixture.is_valid():
            # строка ниже инициализирует фикстуру, происходит создание сессии
            fixture = Application()
            #fixture.session.ensure_login(username="admin", password="secret")
    #  если убирать эту строку выше в if-than-else, то падают тесты, которые разлогиниваются в процессе прохождения
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
