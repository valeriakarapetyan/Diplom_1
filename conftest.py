from unittest.mock import Mock

import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Тостовая"
    bun.get_price.return_value = 50.0
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Говядина"
    ingredient.get_price.return_value = 100.0
    ingredient.get_type.return_value = "начинка"
    return ingredient


@pytest.fixture
def database():
    return Database()
