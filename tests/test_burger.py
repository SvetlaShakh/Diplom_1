from praktikum.burger import Burger
from tests.data_stellar_burgers import DataStellarBurgers
from tests.helpers import Helpers


class TestBurger:

    def test_set_bun_burger(self):
        burger = Burger()
        bun = Helpers.create_mock_bun()
        burger.set_buns(bun)
        assert burger.bun.name == DataStellarBurgers.bun_name and burger.bun.price == DataStellarBurgers.bun_price

    def test_add_ingredient_one_ingredient_burger_one_in_list(self):
        burger = Burger()
        sauce = Helpers.create_mock_sauce()
        burger.add_ingredient(sauce)
        assert len(burger.ingredients) == 1

    def test_add_ingredient_two_different_ingredient_burger_two_in_list(self):
        burger = Burger()
        sauce = Helpers.create_mock_sauce()
        filling = Helpers.create_mock_filling()
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert len(burger.ingredients) == 2

    def test_add_ingredient_two_same_ingredient_burger_two_in_list(self):
        burger = Burger()
        sauce = Helpers.create_mock_sauce()
        burger.add_ingredient(sauce)
        burger.add_ingredient(sauce)
        assert len(burger.ingredients) == 2

    def test_remove_ingredient_one_in_list_ingredient_burger_zero_in_list(self):
        burger = Burger()
        sauce = Helpers.create_mock_sauce()
        burger.add_ingredient(sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_two_in_list_ingredient_burger_one_in_list(self):
        burger = Burger()
        sauce = Helpers.create_mock_sauce()
        burger.add_ingredient(sauce)
        burger.add_ingredient(sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_move_ingredient_burger(self):
        burger = Burger()
        sauce = Helpers.create_mock_sauce()
        filling = Helpers.create_mock_filling()
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        first_ingredient = burger.ingredients[0]
        second_ingredient = burger.ingredients[1]
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == second_ingredient and burger.ingredients[1] == first_ingredient

    def test_get_price_burger(self, create_mock_ingredients):
        burger = Burger()
        bun = create_mock_ingredients[0]
        sauce = create_mock_ingredients[1]
        filling = create_mock_ingredients[2]
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert burger.get_price() == DataStellarBurgers.price_test_burger

    def test_get_receipt_burger(self, create_mock_ingredients):
        burger = Burger()
        bun = create_mock_ingredients[0]
        sauce = create_mock_ingredients[1]
        filling = create_mock_ingredients[2]
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert burger.get_receipt() == DataStellarBurgers.receipt_test_burger
