from common.models import Coin
from common.constants import CoinBoundary


def determine_cost_by_weight(coin: Coin) -> float:
    """
    Converts a coin based on its weight to its cost.

    Parameters:
        coin: [common.models.Coin]: A coin object.

    Returns:
        [float]: The cost of the coin
    """

    if (
        coin.diameter >= CoinBoundary.MAX_DIAMETER
        or coin.diameter <= CoinBoundary.MIN_DIAMETER
    ):
        return 0.0

    if coin.weight >= CoinBoundary.MAX_WEIGHT or coin.weight <= CoinBoundary.MIN_WEIGHT:
        return 0.0

    return 1.00
