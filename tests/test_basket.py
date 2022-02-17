import contextlib
from contextlib import nullcontext as does_not_raise
from typing import Tuple

import pytest

from src.basket import Basket

PRODUCT_INPUT_EXPECTED_AMOUNT_OUTPUT_MAP = {
    ("B01", "G01"): 37.85,
    ("R01", "R01"): 54.37,
    ("R01", "G01"): 60.85,
    ("B01", "B01", "R01", "R01", "R01"): 98.27
}


def test_get_basket_total_amount():
    for product_codes, expected_total_amount in PRODUCT_INPUT_EXPECTED_AMOUNT_OUTPUT_MAP.items():
        basket = Basket()
        for product_code in product_codes:
            basket.add_product(product_code)
        assert basket.get_basket_total_amount() == expected_total_amount


@pytest.mark.parametrize(
    "product_code, error_expectation",
    [
        ("R01", does_not_raise()),
        ("G01", does_not_raise()),
        ("B01", does_not_raise()),
        ("Z01", pytest.raises(ValueError)),
    ],
)
def test_add_valid_product(product_code: str, error_expectation: Tuple[contextlib.nullcontext, ValueError]):
    basket = Basket()
    with error_expectation:
        basket.add_product(product_code)
