from common.models import Coin

_COIN_NAME = "Quarter"
_COIN_WEIGHT = 5.670  # grams
_COIN_DIAMETER = 30.61  # millimeters


class Test_Coin:
    def setup(self):
        self._coin = Coin(name=_COIN_NAME, weight=_COIN_WEIGHT, diameter=_COIN_DIAMETER)

    def teardown(self):
        del self._coin

    def test_has_name(self):
        assert self._coin.name == _COIN_NAME

    def test_name_is_string(self):
        assert isinstance(self._coin.name, str)

    def test_has_weight(self):
        assert self._coin.weight == _COIN_WEIGHT

    def test_weight_is_float(self):
        assert isinstance(self._coin.weight, float)

    def test_has_diameter(self):
        assert self._coin.diameter == _COIN_DIAMETER

    def test_diameter_is_float(self):
        assert isinstance(self._coin.diameter, float)
