from external.item_stock import COLA, CANDY, CHIPS
from common.constants import DisplayMessage, CoinValue
from common.models import Coin, Product
from typing import List, Optional
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
        self.coin_return: List[Coin] = []

        self._item_mapping = {item.name: item for item in self.items}
        self._item_vended_flag = False

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
            return self._item_mapping[product_name].cost
        except KeyError:
            raise ValueError("NoItemByName")

    def insert_coin(self, coin: Coin) -> None:
        """
        Adds a coin's value to the self.current_inserted_value. Rejects pre-determined coin types.

        Parameters:
            coin: [Coin]
        """

        NOT_ACCEPTED_VALUES = [CoinValue.PENNY]

        value = determine_value_by_weight(coin)

        if value in NOT_ACCEPTED_VALUES:
            self.coin_return.append(coin)

        else:
            self.current_inserted_value += value

    def enough_value_for_product(self, product_name: str) -> bool:
        """
        Accepts a product, and determines if enough value has been inserted into the VendingMachine.

        Parameters:
            product: [str] - The name of a product.

        Returns:
            [bool]: True if current_inserted_value is more than cost of product
        """

        return self.current_inserted_value >= self.get_price(product_name)

    def vend_product(self, product_name: str) -> Optional[Product]:
        """
        Outputs the requested product if enough value is in the VendingMachine

        Parameters:
            product_name: [str] - the name of a product to vend.

        Returns:
            [Optional[Product]]: A Product requested or None if not enough value.

        Raises:
            [ValueError] - If product name not found.
        """

        product = self._item_mapping[product_name]

        if self.enough_value_for_product(product_name):
            self.display = DisplayMessage.THANK_YOU
            self._item_vended_flag = True
            return product

        else:
            self.display = f"{DisplayMessage.PRICE}: {product.cost}"
            return None

    def check_display(self):
        """
        Checks the current display message. Contains some logic to reset the display message after a successful vend.

        Returns:
            [str]: The display message.
        """
        if self.display == DisplayMessage.THANK_YOU and self._item_vended_flag is False:
            self.display = DisplayMessage.INSERT_COIN

        self._item_vended_flag = False
        return self.display

    def make_change(self):
        """
        Determines the change necessary and adds coins to the coin return.

        Parameters:
            None

        Returns:
            None
        """

        pass
