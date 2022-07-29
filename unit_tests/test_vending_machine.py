from common.vending_machine import VendingMachine
from common.constants import DisplayMessage


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
