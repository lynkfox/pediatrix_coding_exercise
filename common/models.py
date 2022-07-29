from dataclasses import dataclass, field


@dataclass
class Product:
    """
    A Product for delivery from the Vending Machine.
    """

    name: str
    cost: float
