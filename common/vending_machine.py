from external.item_stock import COLA, CANDY, CHIPS
from common.constants import DisplayMessage, CoinValue
from common.models import Coin, Product
from typing import List
from common.exchange import determine_value_by_diameter, determine_value_by_weight


class VendingMachine:
    def __init__(self) -> None:
        """
        A Vending Machine. Comes pre stocked with items.

        Properties:
            items: [List[Product]] - Products available in the machine.
            display: [str] - The current message to display
            current_inserted_value: [float] - the value of inserted coins up to this point.
        """

        self.items: List[Product] = [COLA, CANDY, CHIPS]
        self.display: str = DisplayMessage.INSERT_COIN
        self.current_inserted_value: float = 0.0

        self._item_mapping = {item.name: item.cost for item in self.items}

    def get_price(self, product_name: str) -> float:
        """
        Returns the cost of a product based on its name.

        Parameters:
            product_name: [str] - The name of a product

        Returns:
            [float]: The cost of the product

        Raises:
            ValueError(NoItemByName) if item name not found.
        """
        try:
            return self._item_mapping[product_name]
        except KeyError:
            raise ValueError("NoItemByName")

    def insert_coin(self, coin: Coin) -> None:
        """
        Adds a coin's value to the self.current_inserted_value. Rejects pre-determined coin types.
        """

        NOT_ACCEPTED_VALUES = [CoinValue.PENNY]

        value = determine_value_by_weight(coin)

        self.current_inserted_value += 0 if value in NOT_ACCEPTED_VALUES else value
