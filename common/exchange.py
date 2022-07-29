from common.models import Coin
from common.constants import CoinBoundary, CoinValue

MAPPING_BY_WEIGHT = {
    5.67: CoinValue.QUARTER,
    2.268: CoinValue.DIME,
    5: CoinValue.NICKLE,
    2.5: CoinValue.PENNY,
}

MAPPING_BY_DIAMETER = {
    24.26: CoinValue.QUARTER,
    17.91: CoinValue.DIME,
    21.21: CoinValue.NICKLE,
    19.05: CoinValue.PENNY,
}


def determine_value_by_weight(coin: Coin) -> float:
    """
    Converts a coin based on its weight to its value.

    Parameters:
        coin: [common.models.Coin]: A coin object.

    Returns:
        [float]: The value of the coin
    """

    if coin.weight >= CoinBoundary.MAX_WEIGHT or coin.weight <= CoinBoundary.MIN_WEIGHT:
        return 0.0

    return MAPPING_BY_WEIGHT.get(coin.weight, 0.0)


def determine_value_by_diameter(coin: Coin):
    """
    Converts a coin based on its diameter to its value.

    Parameters:
        coin: [common.models.Coin]: A coin object.

    Returns:
        [float]: The value of the coin
    """

    if (
        coin.diameter >= CoinBoundary.MAX_DIAMETER
        or coin.diameter <= CoinBoundary.MIN_DIAMETER
    ):
        return 0.0

    return MAPPING_BY_DIAMETER.get(coin.diameter, 0.0)
