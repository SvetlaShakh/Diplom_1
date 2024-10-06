import pytest
from praktikum.database import Database
from tests.data_stellar_burgers import DataStellarBurgers


class TestDatabase:

    def test_available_buns(self):
        database = Database()
        list_buns = database.available_buns()
        assert len(list_buns) == DataStellarBurgers.numbers_buns and type(list_buns) == list

    @pytest.mark.parametrize('index', DataStellarBurgers.index_bun)
    def test_name_and_price_buns(self, index):
        database = Database()
        bun = database.buns[index]
        name_price_bun = []
        name_price_bun.append(bun.get_name())
        name_price_bun.append(bun.get_price())
        assert name_price_bun in DataStellarBurgers.expected_list_buns

    def test_available_ingredients(self):
        database = Database()
        list_ingredients = database.available_ingredients()
        assert len(list_ingredients) == DataStellarBurgers.numbers_ingredients and type(list_ingredients) == list

    @pytest.mark.parametrize('index', DataStellarBurgers.index_ingredients)
    def test_list_name_sauce(self, index):
        database = Database()
        ingredient = database.ingredients[index]
        data_ingredient = []
        data_ingredient.append(ingredient.get_type())
        data_ingredient.append(ingredient.get_name())
        data_ingredient.append(ingredient.get_price())
        assert data_ingredient in DataStellarBurgers.expected_list_ingredients