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

* `python3 vending_machine.py`


# A note on linting:

I used Black to lint, but I am not the greatest fan of how it handles line length at times. There are times I feel its decisions are more difficult to read than helpful (yes I know line length can be adjusted as one of the only things Black allows to be adjusted) - however Black is a well accepted standard in Python for linting, so I went with it not knowing what environments anyone who reviews this code is likely to see.


# A Note on common vs external

The external directory is representing items that have a common "accepted schema" (in this case a class object) but are not controlled by the VendingMachine.

i.e. Coins are known to have a Name, Weight, Diameter, and Value. The VendingMachine cannot control any of these factors - it can only accept what it is given, and the only thing it is allowed to know is the weight and diameter. Same thing with Products - the VendingMachine does not know or care what a product is, only that it knows its value.

So these things are defined "externally" to the VendingMachine as they would be provided by the vendors (i.e. the Snack vender and the Government/Treasury)

This allows the VendingMachine to properly be told its offerings, yet those offerings (as long as their schema remains the same) could change any day. It also allows it to take any coin the Treasury wants to produce, but uses the values on its own terms to determine what the values are (hence why the value mapping is within common, not external for example, but the reverse mapping from value to Coin is in External)

It was not required that the change be determined by weight - I went with the assumption that once the coins are sorted into the machine it knows what each coin is internally and its 'value' and can drop them into the coin return without needing to check their weight/size

# A note on `vending_machine.py`

This is bare bones. I threw this together in 20 mins to use the class and provide a way to interact with it in a more direct manner than the tests alone.  It is single item use, and only very vaguely tested.

# A Note on float vs int

Ugh. I knew I should have done int from the beginning for cost/value amounts, but alas I figured floating point rounding errors wouldn't rear their ugly heads with just a few coins. And one or two coins its fine, but of course (and I knew this from the start I just got ahead of myself) it doesn't really just stay a few coins.

So, that is why there is in the middle of the commit history a sudden change from floats to int. I knew it was coming and I kinda was hoping not too, then I just bit the bullet and did it anyways. Shoulda just dealt with it at the start

# A note on error handling, repeatability, some tests:

The exercise did not require any extensive error handling through the three user stories provided. (I would have expected a GivenWhenThen for specific error handling if this had been a requirement) It also did not require that the vending machine be able to be used for more than one item, so once used it cannot be reset in the same 'session' without restarting the script. That would be a very fine feature to add to it in a future development cycle :)
