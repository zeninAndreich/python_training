# Общая фикстура для тестов. Перенес ее в верхний уровень, потому что в подкаталоге может не находить.

from fixture_for_group.application import Application
import pytest


# Для того,чтобы фикстура создавалась одна на всю сессию, а не для каждого теста отдельно.


@pytest.fixture(scope="session")
def app(request):
    # Создание фикстуры
    fixture = Application()
    # Указание на то,как фикстура должна быть разрушена
    request.addfinalizer(fixture.destroy)
    return fixture
