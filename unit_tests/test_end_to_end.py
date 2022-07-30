from external.coins import *
from common.vending_machine import VendingMachine
from external.item_stock import *


class Test_E2E_scenarios:
    def setup(self):
        self.Vendomatic = VendingMachine()

    def teardown(self):
        del self.Vendomatic

    def test_exact_change_returns_product_and_no_change_in_return(self):
        self.Vendomatic.insert_coin(QUARTER)
        self.Vendomatic.insert_coin(QUARTER)
        self.Vendomatic.insert_coin(QUARTER)
        self.Vendomatic.insert_coin(QUARTER)

        product = self.Vendomatic.purchase("Cola")

        assert product == COLA
        assert len(self.Vendomatic.coin_return) == 0

    def test_more_than_enough_coins_returns_product_and_change_in_coin_return(self):
        self.Vendomatic.insert_coin(QUARTER)
        self.Vendomatic.insert_coin(QUARTER)
        self.Vendomatic.insert_coin(QUARTER)
        self.Vendomatic.insert_coin(QUARTER)

        product = self.Vendomatic.purchase("Candy")

        assert product == CANDY
        assert len(self.Vendomatic.coin_return) == 2
        assert self.Vendomatic.coin_return == [QUARTER, DIME]
