from common.exchange import determine_value_by_weight, determine_value_by_diameter
from common.models import Coin


class Test_determine_cost_by_weight:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_returns_a_float(self):
        assert isinstance(determine_value_by_weight(coin=Coin("Test", 3, 20)), float)

    def test_coin_weight_of_0_returns_0_cost(self):
        assert determine_value_by_weight(coin=Coin("Test", weight=0, diameter=20)) == 0

    def test_coin_of_weight_of_MAX_or_greater_returns_0(self):
        # heaviest accepted coin is a Quarter at 5.670 grams
        assert (
            determine_value_by_weight(coin=Coin("Test", weight=5.7, diameter=20)) == 0
        )
        assert determine_value_by_weight(coin=Coin("Test", weight=6, diameter=20)) == 0

    def test_coin_of_weight_of_MIN_or_less_returns_0(self):
        # lightest accepted coin is a Dime at 2.268 grams
        assert (
            determine_value_by_weight(coin=Coin("Test", weight=2.2, diameter=20)) == 0
        )
        assert determine_value_by_weight(coin=Coin("Test", weight=1, diameter=20)) == 0

    def test_passed_values_for_quarter_returns_25_cents(self):
        assert (
            determine_value_by_weight(
                coin=Coin("TestQuarter", weight=5.670, diameter=24.26)
            )
            == 0.25
        )

    def test_passed_values_for_dime_returns_10_cents(self):
        assert (
            determine_value_by_weight(
                coin=Coin("TestQuarter", weight=2.268, diameter=17.91)
            )
            == 0.1
        )

    def test_passed_values_for_nickle_returns_5_cents(self):
        assert (
            determine_value_by_weight(
                coin=Coin("TestQuarter", weight=5.0, diameter=21.21)
            )
            == 0.05
        )

    def test_passed_values_for_penny_returns_1_cent(self):
        assert (
            determine_value_by_weight(
                coin=Coin("TestQuarter", weight=2.5, diameter=19.05)
            )
            == 0.01
        )


class Test_determine_value_by_diameter:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_returns_a_float(self):
        assert isinstance(determine_value_by_diameter(coin=Coin("Test", 3, 20)), float)

    def test_coin_diameter_of_0_returns_0_cost(self):
        assert determine_value_by_diameter(coin=Coin("Test", weight=3, diameter=0)) == 0

    def test_coin_of_diameter_MAX_or_greater_returns_0(self):
        # largest coin accepted is a Quarter, with a diameter of 24.26mm
        assert (
            determine_value_by_diameter(coin=Coin("Test", weight=3, diameter=25)) == 0
        )
        assert (
            determine_value_by_diameter(coin=Coin("Test", weight=3, diameter=30)) == 0
        )

    def test_coin_of_diameter_of_MIN_or_smaller_returns_0(self):
        # smallest coin is a dime, with a diameter of 17.91mm
        assert (
            determine_value_by_diameter(coin=Coin("Test", weight=3, diameter=17)) == 0
        )
        assert (
            determine_value_by_diameter(coin=Coin("Test", weight=3, diameter=10)) == 0
        )

    def test_passed_values_for_quarter_returns_25_cents(self):
        assert (
            determine_value_by_diameter(
                coin=Coin("TestQuarter", weight=5.670, diameter=24.26)
            )
            == 0.25
        )

    def test_passed_values_for_dime_returns_10_cents(self):
        assert (
            determine_value_by_diameter(
                coin=Coin("TestQuarter", weight=2.268, diameter=17.91)
            )
            == 0.1
        )

    def test_passed_values_for_nickle_returns_5_cents(self):
        assert (
            determine_value_by_diameter(
                coin=Coin("TestQuarter", weight=5.0, diameter=21.21)
            )
            == 0.05
        )

    def test_passed_values_for_penny_returns_1_cent(self):
        assert (
            determine_value_by_diameter(
                coin=Coin("TestQuarter", weight=2.5, diameter=19.05)
            )
            == 0.01
        )
