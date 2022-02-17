import pytest
from pytest_mock import MockerFixture

import src.utils
from src.offer import ProductOfferHandler

MOCKED_PRODUCT_OFFERS = {
    "M01": {
        "offerType": "SECOND_UNIT_PERCENT_DISCOUNT",
        "value": 0.5
    },
    "Y01": {
        "offerType": "FLAT_DISCOUNT",
        "value": 10
    },
    "C01": {
        "offerType": "PERCENT_DISCOUNT",
        "value": 0.05
    }
}

MOCKED_PRODUCT_CATALOGUE = {
    "M01": {
        "name": "Maroon Widget",
        "price": 32.95
    },
    "Y01": {
        "name": "Yellow Widget",
        "price": 64.50
    },
    "C01": {
        "name": "Cyan Widget",
        "price": 18
    }
}


PRODUCT_OFFER_HANDLER = ProductOfferHandler()


@pytest.mark.parametrize(
    "product_code, product_quantity, expected_discount",
    [
        ("M01", 2, 16.475),
        ("M01", 3, 16.475),
        ("M01", 4, 32.95),
        ("Y01", 3, 30),
        ("C01", 1, 0.9),
    ],
)
def test_calculate_discount(mocker: MockerFixture, product_code: str, product_quantity: int, expected_discount: float):
    mocker.patch.object(src.offer, "PRODUCT_OFFERS", MOCKED_PRODUCT_OFFERS)
    mocker.patch.object(src.offer, "PRODUCT_CATALOGUE", MOCKED_PRODUCT_CATALOGUE)
    assert PRODUCT_OFFER_HANDLER.calculate_discount(product_code, product_quantity) == expected_discount
