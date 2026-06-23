from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDatabase:
    def test_available_buns_return_list(self):
        # Arrange
        self.database = Database()
        # Act
        result = self.database.available_buns()
        # Assert
        assert isinstance(result, list)
    def test_available_buns_not_empty(self):
        # Arrange
        self.database = Database()
        # Act
        result = self.database.available_buns()
        # Assert
        assert len(result) > 0
    def test_available_buns_contains_bun_instances(self):
        # Arrange
        self.database = Database()
        # Act
        result = self.database.available_buns()
        # Assert
        assert all(isinstance(bun, Bun) for bun in result)

    def test_available_ingredients_returns_list(self):
        # Arrange
        self.database = Database()
        # Act
        result = self.database.available_ingredients()
        # Assert
        assert isinstance(result, list)
    def test_available_ingredients_not_empty(self):
        # Arrange
        self.database = Database()
        # Act
        result = self.database.available_ingredients()
        # Assert
        assert len(result) > 0
    def test_available_ingredients_contains_ingredient_instances(self):
        # Arrange
        self.database = Database()
        # Act
        result = self.database.available_ingredients()
        # Assert
        assert all(isinstance(ing, Ingredient) for ing in result)
