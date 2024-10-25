import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("Начинка", "Куриная котлета", 120.0),
        ("Соус", "1000 Островов", 45.5),
        ("Начинка", "Хэшбраун", 90.20),
        ("Соус", "Майонез", 35.0),
    ])
    def test_ingredient_creation_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("Начинка", "Куриная котлета", 120.0),
        ("Соус", "1000 Островов", 45.5),
        ("Начинка", "Хэшбраун", 90.20),
        ("Соус", "Майонез", 35.0),
    ])
    def test_ingredient_creation_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("Начинка", "Куриная котлета", 120.0),
        ("Соус", "1000 Островов", 45.5),
        ("Начинка", "Хэшбраун", 90.20),
        ("Соус", "Майонез", 35.0),
    ])
    def test_ingredient_creation_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    def test_ingredient_correct_name_type(self):
        ingredient = Ingredient("Начинка", "Котлетка", 55.55)
        assert isinstance(ingredient.get_name(), str)

    def test_ingredient_correct_price_type(self):
        ingredient = Ingredient("Начинка", "Котлетка", 55.55)
        assert isinstance(ingredient.get_price(), float)

    def test_ingredient_correct_type_type(self):
        ingredient = Ingredient("Начинка", "Котлетка", 55.55)
        assert isinstance(ingredient.get_type(), str)
