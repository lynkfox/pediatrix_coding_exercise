from common.models import Coin
from common.constants import CoinBoundary


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

    return 1.00


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

    return 1.00
