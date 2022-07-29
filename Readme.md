# Pediatrix Coding Challenge

This is a submission for the Pediatrix Vending Machine coding challenge.

# First time set up:

* Install Python 3.9.5
* Create a virtual environment
 * `python3 -m venv .venv`
 * Enter:
   * `source .venv/bin/activate` (non Windows)
   * `& .venv/Scripts/Activate.ps1` (powershell)
 * Upgrade pip
   * `pip install -u pip`
* Install dev dependencies:
  * `pip install -r requirements-dev.txt`

## If developing:
* Install Pre-Commit
  * `pre-commit install`

# Run Tests:

* `pytest`


# Run script:

* `python vending-machine.py`


# A Note on common vs external

The external directory is representing items that have a common "accepted schema" (ie in this case a class object) but are not controlled by the VendingMachine.

i.e. Coins are known to have a Name, Weight, Diameter, and Value. The VendingMachine cannot control any of these factors - it can only accept what it is given, and the only thing it is allowed to know is the weight and diameter. Same thing with Products - the VendingMachine does not know or care what a product is, only that it knows its value.

So these things are defined "externally" to the VendingMachine as they would be provided by the vendors (i.e. the Snack vender and the Government/Treasury)

This allows the VendingMachine to properly be told its offerings, yet those offerings (as long as their schema remains the same) could change any day. It also allows it to take any coin the Treasury wants to produce, but uses the values on its own terms to determine what the values are (hence why the value mapping is within common, not external for example)
