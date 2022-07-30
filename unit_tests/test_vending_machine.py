from common.vending_machine import VendingMachine
from common.constants import DisplayMessage
from common.models import Product
from external.item_stock import COLA, CHIPS
from external.coins import DIME, PENNY
import pytest


class Test_VendingMachine:
    def setup(self):
        self.test_object = VendingMachine()

    def teardown(self):
        del self.test_object

    def test_has_items_available_that_is_a_list(self):
        assert isinstance(self.test_object.items, list)

    def test_has_display_that_is_a_string(self):
        assert isinstance(self.test_object.display, str)

    def test_display_defaults_to_INSERT_COIN(self):
        assert self.test_object.display == DisplayMessage.INSERT_COIN

    def test_has_current_inserted_value_that_is_a_float(self):
        assert isinstance(self.test_object.current_inserted_value, float)

    def test_current_inserted_value_defaults_to_0_0(self):
        self.test_object.current_inserted_value == 0.0

    def test_has_coin_return_that_is_a_list(self):
        assert isinstance(self.test_object.coin_return, list)

    def test_initial_coin_return_is_empty(self):
        assert len(self.test_object.coin_return) == 0


class Test_VendingMachine_get_price:
    def setup(self):
        self.test_object = VendingMachine()

    def teardown(self):
        del self.test_object

    def test_returns_price_as_a_float(self):
        assert isinstance(self.test_object.get_price("Cola"), float)

    def test_given_cola_returns_its_cost(self):
        assert self.test_object.get_price("Cola") == COLA.cost

    def test_given_chips_returns_its_cost(self):
        assert self.test_object.get_price("Chips") == CHIPS.cost

    def test_raises_ValueError_if_cannot_find_item_name(self):
        with pytest.raises(ValueError, match="NoItemByName"):
            self.test_object.get_price("GobblyGook")


class Test_VendingMachine_insert_coin:
    def setup(self):
        self.test_object = VendingMachine()

    def teardown(self):
        del self.test_object

    def test_given_a_valid_coin_updates_current_inserted_value(self):
        assert self.test_object.current_inserted_value == 0.0

        self.test_object.insert_coin(DIME)

        assert self.test_object.current_inserted_value == 0.1

    def test_given_an_invalid_coin_current_inserted_value_does_not_change(self):
        original_value = self.test_object.current_inserted_value

        self.test_object.insert_coin(PENNY)

        assert self.test_object.current_inserted_value == original_value

    def test_if_invalid_coin_given_coin_is_put_in_coin_return(self):
        self.test_object.insert_coin(PENNY)

        assert PENNY in self.test_object.coin_return

    def test_adding_multiple_invalid_coins_adds_them_all_to_the_coin_return(self):
        self.test_object.insert_coin(PENNY)
        self.test_object.insert_coin(PENNY)
        self.test_object.insert_coin(PENNY)
        self.test_object.insert_coin(PENNY)

        assert len(self.test_object.coin_return) == 4


class Test_VendingMachine_enough_value_for_product:
    def setup(self):
        self.test_object = VendingMachine()

    def teardown(self):
        del self.test_object

    def test_returns_boolean(self):
        assert isinstance(self.test_object.enough_value_for_product("Cola"), bool)

    def test_returns_True_if_current_inserted_value_greater_than_product_price(self):
        self.test_object.current_inserted_value = 2.0

        assert self.test_object.enough_value_for_product("Cola") is True

    def test_returns_true_if_exactly_enough_for_product(self):
        self.test_object.current_inserted_value = COLA.cost

        assert self.test_object.enough_value_for_product("Cola") is True

    def test_returns_false_if_not_enough_for_product(self):
        assert self.test_object.enough_value_for_product("Cola") is False


class Test_VendingMachine_vend_product:
    def setup(self):
        self.test_object = VendingMachine()

    def teardown(self):
        del self.test_object

    def test_returns_product_if_enough_value_in_machine(self):
        self.test_object.current_inserted_value = COLA.cost

        assert isinstance(self.test_object.vend_product("Cola"), Product)

    def test_properly_returns_cola_product_if_provided_Cola(self):
        self.test_object.current_inserted_value = COLA.cost

        assert self.test_object.vend_product("Cola") == COLA

    def test_returns_none_if_not_enough_value(self):
        assert self.test_object.vend_product("Cola") is None

    def test_raises_KeyError_if_product_name_not_found(self):
        with pytest.raises(KeyError):
            self.test_object.vend_product("Randomness")


class Test_VendingMachine_check_display:
    def setup(self):
        self.test_object = VendingMachine()

    def teardown(self):
        del self.test_object

    def test_returns_a_string(self):
        assert isinstance(self.test_object.check_display(), str)

    def test_if_nothing_else_done_returns_InsertCoin(self):
        assert self.test_object.check_display() == DisplayMessage.INSERT_COIN

    def test_after_product_successfully_vended_returns_ThankYou(self):
        self.test_object.current_inserted_value = COLA.cost
        self.test_object.vend_product("Cola")

        assert self.test_object.check_display() == DisplayMessage.THANK_YOU

    def test_a_second_time_after_vended_product_returns_InsertCoin(self):
        self.test_object.current_inserted_value = COLA.cost
        self.test_object.vend_product("Cola")
        self.test_object.check_display()

        assert self.test_object.check_display() == DisplayMessage.INSERT_COIN

    def test_when_zero_inserted_value_returns_price_of_vend_item(self):
        self.test_object.vend_product("Cola")
        self.test_object.check_display()

        assert (
            self.test_object.check_display() == f"{DisplayMessage.PRICE}: {COLA.cost}"
        )

    def test_when_not_enough_value_for_vend_item_returns_price_of_vend_item(self):
        self.test_object.current_inserted_value = 0.1
        self.test_object.vend_product("Cola")
        self.test_object.check_display()

        assert (
            self.test_object.check_display() == f"{DisplayMessage.PRICE}: {COLA.cost}"
        )
