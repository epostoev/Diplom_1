from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BunData:
    NAME_PRICE = [
        ("Pink bun", 800),
        ("Black bun", 500),
        ("White bun", 600),
    ]
    PRICE = [price for _, price in NAME_PRICE]


class IngredientData:
    TYPE_NAME_PRICE = [
        (INGREDIENT_TYPE_SAUCE, "ketchup", 60),
        (INGREDIENT_TYPE_SAUCE, "tar-tar", 60),
        (INGREDIENT_TYPE_FILLING, "carrot", 100),
        (INGREDIENT_TYPE_FILLING, "patty", 150),
    ]
    PRICE = [price for _, _, price in TYPE_NAME_PRICE]


class ResultTest:
    PRICE_TEST_CASE = [
        (BunData.PRICE[0],
         IngredientData.PRICE[0],
         IngredientData.PRICE[2],
         BunData.PRICE[0] *
         2 +
         IngredientData.PRICE[0] +
         IngredientData.PRICE[2]),
        (BunData.PRICE[1],
         IngredientData.PRICE[1],
         IngredientData.PRICE[3],
         BunData.PRICE[1] *
         2 +
         IngredientData.PRICE[1] +
         IngredientData.PRICE[3]),
        (BunData.PRICE[2],
         IngredientData.PRICE[2],
         IngredientData.PRICE[0],
         BunData.PRICE[2] *
         2 +
         IngredientData.PRICE[2] +
         IngredientData.PRICE[0]),
    ]
