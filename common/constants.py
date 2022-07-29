from dataclasses import dataclass


@dataclass(frozen=True)
class CoinBoundary:
    MIN_DIAMETER: float = 17.0
    MAX_DIAMETER: float = 25.0
    MAX_WEIGHT: float = 5.7
    MIN_WEIGHT: float = 2.2
