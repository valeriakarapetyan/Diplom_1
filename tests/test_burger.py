import pytest
from unittest.mock import Mock
from praktikum.ingredient import Ingredient


class TestBurger:
    @pytest.mark.parametrize("initial_price, ingredient_price, expected_price", [
        (50.0, 100.0, 300.0),
        (50.0, 0.0, 200.0),
        (50.0, 50.0, 250.0)
    ])
    def test_burger_price(self, burger, mock_bun, mock_ingredient, initial_price, ingredient_price, expected_price):
        mock_bun.get_price.return_value = initial_price
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        ingredient_clone = Mock(spec=Ingredient)
        ingredient_clone.get_price.return_value = ingredient_price
        burger.add_ingredient(ingredient_clone)
        assert burger.get_price() == expected_price

    def test_burger_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        mock_bun.get_price.return_value = 50.0
        mock_bun.get_name.return_value = "Тостовая"
        mock_ingredient.get_price.return_value = 100.0
        mock_ingredient.get_name.return_value = "Говядина"
        mock_ingredient.get_type.return_value = "начинка"

        expected_receipt = (
            '(==== Тостовая ====)\n'
            '= начинка Говядина =\n'
            '(==== Тостовая ====)\n'
            '\n'
            'Price: 200.0'
        )

        assert burger.get_receipt() == expected_receipt

    def test_remove_ingredient(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        second_ingredient = Mock(spec=Ingredient)
        second_ingredient.get_name.return_value = "Салат"
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].get_name() == "Салат"
