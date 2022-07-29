from dataclasses import dataclass, field


@dataclass
class Product:
    """
    A Product for delivery from the Vending Machine.

    Parameters:
        name: [str] - The name of the product.
        cost: [float] - The cost of the product in Dollars and Cents (50 cents => .5)
    """

    name: str
    cost: float


@dataclass
class Coin:
    """
    A Coin object.

    Parameters:
        name: [str] - The name of the coin.
        weight: [float] - The weight of the coin, in grams.
        diameter: [float] - The diameter of the coin, in millimeters
    """

    name: str
    weight: float
    diameter: float
