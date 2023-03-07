# Общая фикстура для тестов. Перенес ее в верхний уровень, потому что в подкаталоге может не находить.

from fixture_for_group.application import Application
import pytest
from fixture_for_contact.application_contact import Application_contact


# Для того,чтобы фикстура создавалась одна на всю сессию, а не для каждого теста отдельно.


@pytest.fixture
def app(request):
    # Создание фикстуры
    fixture = Application_contact()
    # Разрушение фикстуры
    request.addfinalizer(fixture.destroy_contact)
    return fixture