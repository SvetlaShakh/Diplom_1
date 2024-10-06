import pytest
from tests.data_stellar_burgers import DataStellarBurgers
from tests.helpers import Helpers


@pytest.fixture()
def create_mock_ingredients():
    mock_bun = Helpers.create_mock_bun()
    mock_bun.get_price.return_value = DataStellarBurgers.bun_price
    mock_bun.get_name.return_value = DataStellarBurgers.bun_name
    mock_sauce = Helpers.create_mock_sauce()
    mock_sauce.get_price.return_value = DataStellarBurgers.sause_price
    mock_sauce.get_type.return_value = DataStellarBurgers.type_sauce
    mock_sauce.get_name.return_value = DataStellarBurgers.sauce_name
    mock_filling = Helpers.create_mock_filling()
    mock_filling.get_price.return_value = DataStellarBurgers.filling_price
    mock_filling.get_type.return_value = DataStellarBurgers.type_filling
    mock_filling.get_name.return_value = DataStellarBurgers.filling_name
    return mock_bun, mock_sauce, mock_filling
