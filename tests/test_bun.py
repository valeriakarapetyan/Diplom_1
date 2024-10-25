import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("Пшеничная", 100.0),
        ("С сыром", 150.50),
        ("Диетическая", 175.0),
    ])
    def test_bun_creation_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        ("Пшеничная", 100.0),
        ("С сыром", 150.50),
        ("Диетическая", 175.0),
    ])
    def test_bun_creation_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

    def test_bun_correct_name_type(self):
        bun = Bun("С кунжутом", 55.99)
        assert type(bun.get_name()) == str

    def test_bun_correct_price_type(self):
        bun = Bun("С кунжутом", 55.99)
        assert type(bun.get_price()) == float
