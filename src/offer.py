import logging
from typing import Callable, Dict

from src import PRODUCT_CATALOGUE
from src.consts import FLAT_DISCOUNT, PERCENT_DISCOUNT, SECOND_UNIT_PERCENT_DISCOUNT
from src.utils import get_product_offers

PRODUCT_OFFERS = get_product_offers()


class ProductOfferHandler:
    def __init__(self):
        self._offer_type_handler_map: Dict[str, Callable] = {
            FLAT_DISCOUNT: self._flat_discount_handler,
            PERCENT_DISCOUNT: self._percent_discount_handler,
            SECOND_UNIT_PERCENT_DISCOUNT: self._second_unit_percent_discount_handler
        }

    @staticmethod
    def _second_unit_percent_discount_handler(product_code: str, product_quantity: int, discount_value: float) -> float:
        """Calculates the discount amount by applying given percent discount to every alternate unit for the given
        quantities of the product."""
        if discount_value < 0 or discount_value > 1:
            raise ValueError(f"Invalid percent discount value {discount_value} supplied for product {product_code}")
        discount_applicable_quantities = product_quantity // 2
        return PRODUCT_CATALOGUE[product_code]["price"] * discount_value * discount_applicable_quantities

    @staticmethod
    def _flat_discount_handler(product_code: str, product_quantity: int, discount_value: float) -> float:
        """Calculates the discount amount by applying given flat discount value for each quantity of the given
        product."""
        if discount_value < 0:
            raise ValueError(f"Invalid flat discount value {discount_value} supplied for product {product_code}")
        return discount_value * product_quantity

    @staticmethod
    def _percent_discount_handler(product_code: str, product_quantity: int, discount_value: float) -> float:
        """Calculates the discount amount by applying given percent discount value for each quantity of the given
        product."""
        if discount_value < 0 or discount_value > 1:
            raise ValueError(f"Invalid percent discount value {discount_value} supplied for product {product_code}")
        return PRODUCT_CATALOGUE[product_code]["price"] * discount_value * product_quantity

    def calculate_discount(self, product_code: str, product_quantity: int) -> float:
        """Calculates discount amount for the given product code by applying product specific offer on the given
        product quantity.
        :param product_code: Product code.
        :param product_quantity: Product quantity.
        :return: Calculated discount amount for the product."""
        if product_code not in PRODUCT_OFFERS:
            return 0
        offer = PRODUCT_OFFERS[product_code]
        offer_type = offer["offerType"]
        if offer_type not in self._offer_type_handler_map:
            logging.error(f"Handler not implemented for offer type {offer_type} ")
            return 0
        return self._offer_type_handler_map[offer_type](product_code, product_quantity, offer["value"])
