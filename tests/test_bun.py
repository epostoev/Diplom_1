import pytest

from praktikum.bun import Bun
from data import BunData


class TestBun:
    "Тесты модели булочки"
    @pytest.mark.parametrize("name, price", BunData.NAME_PRICE)
    def test_get_name_success(self, name, price):
        bun = Bun(name, price)
        result = bun.get_name()
        assert result == name

    @pytest.mark.parametrize("name, price", BunData.NAME_PRICE)
    def test_get_price_success(self, name, price):
        bun = Bun(name, price)
        result = bun.get_price()
        assert result == price
