from dataclasses import dataclass


@dataclass(frozen=True)
class CoinBoundary:
    """
    Minimum and Maximum values for Coins weight and diameter.
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

    PENNY: int = 1
    NICKLE: int = 5
    DIME: int = 10
    QUARTER: int = 25


@dataclass(frozen=True)
class DisplayMessage:
    """
    Messages the Vending Machine can display.
    """

    INSERT_COIN: str = "INSERT COIN"
    THANK_YOU: str = "THANK YOU"
    PRICE: str = "PRICE"
