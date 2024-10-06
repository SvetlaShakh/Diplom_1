import praktikum.ingredient_types
class DataStellarBurgers:

    bun_name = 'black bun'
    bun_price = 100
    type_sauce = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
    sauce_name = 'hot sauce'
    sause_price = 100
    type_filling = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
    filling_name = 'dinosaur'
    filling_price = 200
    list_test_ingredient = [[type_sauce, sauce_name, sause_price], [type_filling, filling_name, filling_price]]
    price_test_burger = bun_price*2+sause_price+filling_price
    receipt_test_burger = (f'(==== {bun_name} ====)\n= sauce hot sauce =\n= filling dinosaur =\n(==== {bun_name} ====)\n'
                           f'\nPrice: {price_test_burger}')
    numbers_buns = 3
    index_bun = list(range(0, numbers_buns))
    expected_list_buns = [['black bun', 100], ['white bun', 200], ['red bun', 300]]
    numbers_ingredients = 6
    index_ingredients = list(range(0, numbers_ingredients))
    expected_list_ingredients = [['SAUCE', 'hot sauce', 100], ['SAUCE', 'sour cream', 200],
                                 ['SAUCE', 'chili sauce', 300], ['FILLING', 'cutlet', 100],
                                 ['FILLING', 'dinosaur', 200], ['FILLING', 'sausage', 300]]

