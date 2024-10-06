import pytest

from praktikum.ingredient import Ingredient
from tests.data_stellar_burgers import DataStellarBurgers


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type, name, price', DataStellarBurgers.list_test_ingredient)
    def test_get_type_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_type, name, price', DataStellarBurgers.list_test_ingredient)
    def test_get_name_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', DataStellarBurgers.list_test_ingredient)
    def test_get_price_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
