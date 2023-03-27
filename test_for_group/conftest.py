# Общая фикстура для тестов. Перенес ее в верхний уровень, потому что в подкаталоге может не находить.
import pytest
from fixture_for_group.application import Application

# Для того,чтобы фикстура создавалась одна на всю сессию, а не для каждого теста отдельно.

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        # Создание фикстуры
        fixture = Application()
        fixture.session_for_group.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session_for_group.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session_for_group.ensure_logout()
        fixture.destroy()
    # Указание на то,как фикстура должна быть разрушена
    request.addfinalizer(fin)
    return fixture
