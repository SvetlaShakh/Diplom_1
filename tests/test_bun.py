from praktikum.bun import Bun
from tests.data_stellar_burgers import DataStellarBurgers


class TestBun:

    def test_get_name_bun(self):
        bun = Bun(DataStellarBurgers.bun_name, DataStellarBurgers.bun_price)
        assert bun.get_name() == DataStellarBurgers.bun_name

    def test_get_price_bun(self):
        bun = Bun(DataStellarBurgers.bun_name, DataStellarBurgers.bun_price)
        assert bun.get_price() == DataStellarBurgers.bun_price
