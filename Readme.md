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
