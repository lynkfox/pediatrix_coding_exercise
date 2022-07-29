from common.exchange import determine_cost_by_weight
from common.models import Coin


class Test_determine_cost_by_weight:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_returns_a_float(self):
        assert isinstance(determine_cost_by_weight(coin=Coin("Test", 1, 1)), float)
