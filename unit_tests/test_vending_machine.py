from common.vending_machine import VendingMachine
from common.constants import DisplayMessage
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
