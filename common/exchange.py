from common.models import Coin
from common.constants import CoinBoundary, CoinValue
from typing import List
from external.coins import VALUE_MAPPING
from decimal import Decimal

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


def determine_value_by_weight(coin: Coin) -> int:
    """
    Converts a coin based on its weight to its value.

    Parameters:
        coin: [common.models.Coin]: A coin object.

    Returns:
        [int]: The value of the coin
    """

    if coin.weight >= CoinBoundary.MAX_WEIGHT or coin.weight <= CoinBoundary.MIN_WEIGHT:
        return 0.0

    return MAPPING_BY_WEIGHT.get(coin.weight, 0.0)


def determine_value_by_diameter(coin: Coin) -> int:
    """
    Converts a coin based on its diameter to its value.

    Parameters:
        coin: [common.models.Coin]: A coin object.

    Returns:
        [int]: The value of the coin
    """

    if (
        coin.diameter >= CoinBoundary.MAX_DIAMETER
        or coin.diameter <= CoinBoundary.MIN_DIAMETER
    ):
        return 0.0

    return MAPPING_BY_DIAMETER.get(coin.diameter, 0.0)


def determine_return_coins(change_value: int) -> List[Coin]:
    """
    Recursively builds a list of coins of largest to smallest until remaining change is 0.

    Parameters:
        change_value: [int] - The remaining value worth of coins left to be returned. (value = 100*cents)

    Returns:
        [List[Coin]]: Coins to be returned.
    """

    # Taking advantage of the fact that Python dicts are now inherently "Ordered" in their keys.
    change = []

    value: int
    coin: Coin
    for value, coin in VALUE_MAPPING.items():
        if value <= change_value:
            change.append(coin)
            change_value = change_value - (value)

            change.extend(determine_return_coins(change_value))
            break

    return change
