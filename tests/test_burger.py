import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data import ResultTest


class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert (mock_ingredient in burger.ingredients) and (
            len(burger.ingredients) == 1)

    def test_remove_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [
            mock_filling] and len(burger.ingredients) == 1

    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_filling, mock_sauce]

    @pytest.mark.parametrize(
        "bun_price, ing_1_price, ing_2_price, expected_price",
        ResultTest.PRICE_TEST_CASE)
    def test_get_price(
            self,
            bun_price,
            ing_1_price,
            ing_2_price,
            expected_price):
        # Arrange
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ing_1 = Mock()
        mock_ing_1.get_price.return_value = ing_1_price
        mock_ing_2 = Mock()
        mock_ing_2.get_price.return_value = ing_2_price
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        # Act
        result = burger.get_price()
        # Assert
        assert result == expected_price

    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        # Arrange
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_receipt = (
            f"(==== {
                mock_bun.get_name()} ====)\n" f"= {
                mock_sauce.get_type().lower()} {
                mock_sauce.get_name()} =\n" f"= {
                    mock_filling.get_type().lower()} {
                        mock_filling.get_name()} =\n" f"(==== {
                            mock_bun.get_name()} ====)" f"\n\nPrice: {
                                burger.get_price()}")
        # Act
        result = burger.get_receipt()
        # Assert
        assert result == expected_receipt
