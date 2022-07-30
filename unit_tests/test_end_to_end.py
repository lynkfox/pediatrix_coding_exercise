from external.coins import *
from common.vending_machine import VendingMachine
from external.item_stock import *
from common.constants import DisplayMessage


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

    def test_display_message_with_nothing_done_is_INSERT_COIN(self):
        assert self.Vendomatic.check_display() == DisplayMessage.INSERT_COIN

    def test_display_message_with_no_coins_added_and_attempting_to_purchase_is_price(
        self,
    ):
        product = self.Vendomatic.purchase("Candy")

        assert product is None
        assert (
            self.Vendomatic.check_display() == f"{DisplayMessage.PRICE}: {CANDY.cost}"
        )

    def test_enough_money_for_product_check_display_says_thank_you(self):
        self.Vendomatic.insert_coin(QUARTER)
        self.Vendomatic.insert_coin(QUARTER)
        self.Vendomatic.insert_coin(DIME)
        self.Vendomatic.insert_coin(NICKLE)

        product = self.Vendomatic.purchase("Candy")

        assert product == CANDY
        assert self.Vendomatic.check_display() == DisplayMessage.THANK_YOU

    def test_enough_money_for_product_checking_display_a_second_time_says_insert_coin(
        self,
    ):
        self.Vendomatic.insert_coin(QUARTER)
        self.Vendomatic.insert_coin(QUARTER)
        self.Vendomatic.insert_coin(DIME)
        self.Vendomatic.insert_coin(NICKLE)

        product = self.Vendomatic.purchase("Candy")
        self.Vendomatic.check_display()  # THANK YOU

        assert product == CANDY
        assert self.Vendomatic.check_display() == DisplayMessage.INSERT_COIN

    def test_check_display_returns_current_amount_after_coin_inserted(self):
        self.Vendomatic.insert_coin(QUARTER)

        assert self.Vendomatic.check_display() == "$ 0.25"

    def test_check_display_returns_total_current_amount_after_multiple_coins(self):

        self.Vendomatic.insert_coin(DIME)
        self.Vendomatic.insert_coin(NICKLE)

        assert self.Vendomatic.check_display() == "$ 0.15"
