# Acme Widget Co - Basket service
Service responsible to handle baskets for the Acme Widget Co's sales system.

## Objective
The core objective of the project is to be able to create a basket, add products from the catalogue to the basket and
calculate total order amount with applying product specific offer discounts and adding the shipping cost as per the
delivery cost rules based on order amount.

## Scope
1. The project does not contain the code for a service as a whole and hence does not expose any endpoint but contains
only the business logic for handling baskets; specifically adding catalogue products to the basket
and calculating total basket price by considering available offers and delivery cost rules. <br/>
Exposing this business logic as service endpoints is outside the current scope and is future enhancement.<br/>
2. The input data for product catalogue, offers, and delivery costs is supplied via json data files. This can be
enhanced to be read and recorded from a database.

## Assumptions
1. The current design for handling offers is implemented to only handle offers for a single product and not for offers
across products. <br/>
e.g. The system can handle together if a product 1 has an offer A and product 2 has an offer B, but an offer which says
if you buy Product 1, then get some discount on Product 2 is not supported.

## Tests
1. Make sure virtualenv is created with the following command:
   ```pipenv install --dev```
2. Activate the virtualenv:
   ```pipenv shell```
3. Run the tests with coverage report:
   ```coverage run -m pytest && coverage report```

#### Current pytest with coverage output is:
```buildoutcfg
====================================== test session starts =======================================
platform darwin -- Python 3.7.9, pytest-7.0.1, pluggy-1.0.0
rootdir: /Users/pankajkoti/basket-service
plugins: mock-3.7.0
collected 19 items

tests/test_basket.py .....                                                                 [ 26%]
tests/test_delivery.py .........                                                           [ 73%]
tests/test_offer.py .....                                                                  [100%]

======================================= 19 passed in 0.06s =======================================
Name                     Stmts   Miss  Cover
--------------------------------------------
src/__init__.py              2      0   100%
src/basket.py               34      4    88%
src/consts.py                5      0   100%
src/delivery.py              9      1    89%
src/offer.py                34      5    85%
src/utils.py                21      0   100%
tests/__init__.py            0      0   100%
tests/test_basket.py        17      0   100%
tests/test_delivery.py       8      0   100%
tests/test_offer.py         12      0   100%
--------------------------------------------
TOTAL                      142     10    93%
```

## Developer contribution advice
After cloning the repository, make sure you run the following commands once to install the required pre-commit git
hooks to keep the python code in the repository compliant with PEP8 as well as to keep the Pipfile.lock consistent with
the Pipfile: <br/>
1. `make dev-install`
2. `make pre-commit-hook`

The above steps need to be run just once. Afterward, each time before you want to make a commit, you can run the below
<i>Makefile</i> targets to avoid commit failures:
1. `make format` Formats python code as per PEP8 style guidelines.
2. `make lint`   Checks and reports linting errors in the code that need to be fixed.
3. `make sort-imports` Sort imports alphabetically.
4. `make pipenv-lock` Update Pipfile.lock.


### Include new libraries as dependencies
Add the dependency in the Pipfile and run the below command to update the Pipfile.lock file
```console
pipenv lock --pre
```
