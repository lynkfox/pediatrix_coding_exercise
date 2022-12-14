from common.models import Product

_PRODUCT_NAME = "TestProduct"
_PRODUCT_COST = 150


class Test_Product:
    def setup(self):
        self._product = Product(name=_PRODUCT_NAME, cost=_PRODUCT_COST)

    def teardown(self):
        del self._product

    def test_has_a_name(self):
        assert self._product.name == _PRODUCT_NAME

    def test_name_is_a_string(self):
        assert isinstance(self._product.name, str)

    def test_has_a_cost(self):
        assert self._product.cost == _PRODUCT_COST

    def test_cost_is_a_int(self):
        assert isinstance(self._product.cost, int)
