from external.item_stock import COLA, CANDY, CHIPS
from common.constants import DisplayMessage


class VendingMachine:
    def __init__(self) -> None:
        """
        A Vending Machine. Comes pre stocked with items.

        Properties:
            items: [List[Product]] - Products available in the machine.
            display: [str] - The current message to display
            current_inserted_value: [float] - the value of inserted coins up to this point.
        """

        self.items = [COLA, CANDY, CHIPS]
        self.display = DisplayMessage.INSERT_COIN
        self.current_inserted_value = 0.0
