from unittest.mock import Mock
from tests.data_stellar_burgers import DataStellarBurgers

class Helpers:

    @staticmethod
    def create_mock_bun():
        mock_bun = Mock()
        mock_bun.configure_mock(name=DataStellarBurgers.bun_name)
        mock_bun.configure_mock(price=DataStellarBurgers.bun_price)
        return mock_bun

    @staticmethod
    def create_mock_sauce():
        mock_sauce = Mock()
        mock_sauce.configure_mock(type=DataStellarBurgers.type_sauce)
        mock_sauce.configure_mock(name=DataStellarBurgers.sauce_name)
        mock_sauce.configure_mock(price=DataStellarBurgers.sause_price)
        return mock_sauce

    @staticmethod
    def create_mock_filling():
        mock_filling = Mock()
        mock_filling.configure_mock(type=DataStellarBurgers.type_filling)
        mock_filling.configure_mock(name=DataStellarBurgers.filling_name)
        mock_filling.configure_mock(price=DataStellarBurgers.filling_price)
        return mock_filling
