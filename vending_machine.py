from common.vending_machine import VendingMachine
from external.coins import *
from external.item_stock import *
import sys


class colors:
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    ORANGE = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"


def check_coins(machine: VendingMachine):
    """
    Checks the coin return of a machine, and removes any coins found within.

    Parameters:
        machine: [VendingMachine] - the machine to check.

    Returns:
        None, but does print what coins where found and removed.
    """

    coins = machine.coin_return

    if len(coins) == 0:
        print("Nothing in the coin return!")

    else:
        print(
            f"{colors.GREEN}Got some coins back: {[coin.name for coin in coins]}{colors.ENDC}"
        )
        machine.coin_return = []
        print(f"The coin return is now empty.")


def leave():
    print("Bye bye!")
    sys.exit()


def main():
    """
    Runs a simulation of interacting with the Vending Machine.

    No, there is no error handling in this and its bare bones as all get out. Its just to utilize the classes and give a
    somewhat possible show of the objects created
    """

    Vendomatic = VendingMachine()

    print("Items available: ")

    for i in range(0, len(Vendomatic.items)):
        print(f"\t * {i+1}: {Vendomatic.items[i].name}")

    selection = input("What would you like to buy? ")

    item_desired = Vendomatic.items[int(selection) - 1]

    dispatch = {
        "1": (Vendomatic.insert_coin, QUARTER),
        "2": (Vendomatic.insert_coin, DIME),
        "3": (Vendomatic.insert_coin, NICKLE),
        "4": (Vendomatic.insert_coin, PENNY),
        "5": (None, Vendomatic.check_display),
        "6": (Vendomatic.purchase, item_desired.name),
        "7": (check_coins, Vendomatic),
        "8": (leave, None),
    }

    product = None
    while product is None:
        print("Options")
        print("\t* 1. Insert Quarter")
        print("\t* 2. Insert Dime")
        print("\t* 3. Insert Nickle")
        print("\t* 4. Insert Penny")
        print("\t* 5. Check Display")
        print("\t* 6. Hit the Vend Button")
        print("\t* 7. Check Coin Return")
        print("\t* 8. Leave")

        select_act = input("Choose an option:\n ")

        product = check_dispatch(dispatch, select_act)

        if product is not None:
            print(f"\n{colors.GREEN}You got {product.name}!{colors.ENDC}")

    in_menu = None
    while in_menu is None:
        print("Now what?")
        print("\t* 5. Check Display")
        print("\t* 7. Check Coin Return")
        print("\t* 8. Leave")

        select_act = input("Choose an option:\n ")

        check_dispatch(dispatch, select_act)


def check_dispatch(dispatch, select_act):
    action = dispatch.get(select_act)

    product = None
    if callable(action[1]):
        value = action[1]()
        print(f"\n{colors.GREEN}{value}{colors.ENDC}\n")
    elif action[1] is not None:
        product = action[0](action[1])
    else:
        action[0]()
    return product


if __name__ == "__main__":
    main()
