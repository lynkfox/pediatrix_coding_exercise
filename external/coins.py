from common.models import Coin


PENNY = Coin(name="Penny", weight=2.5, diameter=19.05)

NICKLE = Coin(
    name="Nickle",
    weight=5.0,
    diameter=21.21,
)

DIME = Coin(name="Dime", weight=2.268, diameter=17.91)

QUARTER = Coin(name="Quarter", weight=5.67, diameter=24.26)


VALUE_MAPPING = {0.25: QUARTER, 0.1: DIME, 0.05: NICKLE, 0.01: PENNY}
