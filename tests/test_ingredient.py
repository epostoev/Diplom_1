import pytest

from praktikum.ingredient import Ingredient
from data import IngredientData


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", IngredientData.TYPE_NAME_PRICE)
    def test_get_price_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        result = ingredient.get_price()
        assert result == price

    @pytest.mark.parametrize("ingredient_type, name, price", IngredientData.TYPE_NAME_PRICE)
    def test_get_name_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        result = ingredient.get_name()
        assert result == name

    @pytest.mark.parametrize("ingredient_type, name, price", IngredientData.TYPE_NAME_PRICE)
    def test_get_type_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        result = ingredient.get_type()
        assert result == ingredient_type