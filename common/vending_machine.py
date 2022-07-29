from external.item_stock import COLA, CANDY, CHIPS
from common.constants import DisplayMessage


class VendingMachine:
    def __init__(self) -> None:
        """
        A Vending Machine. Comes pre stocked with items.
        """

        self.items = [COLA, CANDY, CHIPS]
        self.display = DisplayMessage.INSERT_COIN
