import pytest
from unittest.mock import Mock
from data import BunData, IngredientData
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING



@pytest.fixture(params=BunData.NAME_PRICE)
def mock_bun(request):
    name, price = request.param
    mock = Mock()
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    return mock

@pytest.fixture(params=IngredientData.TYPE_NAME_PRICE)
def mock_ingredient(request):
    ingredient_type, name, price = request.param
    mock = Mock()
    mock.get_type.return_value = ingredient_type
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    return mock

@pytest.fixture
def mock_sauce():
    mock = Mock()
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock.get_name.return_value = "ketchup"
    mock.get_price.return_value = 60
    return mock

@pytest.fixture
def mock_filling():
    mock = Mock()
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock.get_name.return_value = "carrot"
    mock.get_price.return_value = 100
    return mock
