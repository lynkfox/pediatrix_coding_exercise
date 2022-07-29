from dataclasses import dataclass


@dataclass(frozen=True)
class CoinBoundary:
    """
    Minimum and Maximum values for Coins weight and diameter
    """

    MIN_DIAMETER: float = 17.0
    MAX_DIAMETER: float = 25.0
    MAX_WEIGHT: float = 5.7
    MIN_WEIGHT: float = 2.2


@dataclass(frozen=True)
class CoinValue:
    """
    Values of various coins.
    """

    PENNY: float = 0.01
    NICKLE: float = 0.05
    DIME: float = 0.1
    QUARTER: float = 0.25
