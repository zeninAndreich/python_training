# Общая фикстура для тестов. Перенес ее в верхний уровень, потому что в подкаталоге может не находить.
import fixture_for_contact
from fixture_for_group.application import Application
import pytest
from fixture_for_contact.application_contact import Application_contact

# Для того,чтобы фикстура создавалась одна на всю сессию, а не для каждого теста отдельно.


fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:

        # Создание фикстуры
        fixture = Application_contact()

    else:
        if not fixture.is_valid():
            fixture = Application_contact()
    fixture.session_for_contact.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session_for_contact.logout()
        fixture.destroy_contact()

    # Разрушение фикстуры
    request.addfinalizer(fin)
    return fixture
