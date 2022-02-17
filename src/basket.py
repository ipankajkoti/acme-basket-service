import math
from collections import defaultdict
from typing import Dict

from src import PRODUCT_CATALOGUE
from src.consts import AMOUNT_DECIMAL_PRECISION
from src.delivery import calculate_delivery_cost
from src.offer import ProductOfferHandler

PRODUCT_OFFER_HANDLER = ProductOfferHandler()


class Basket:
    def __init__(self):
        self._products: Dict[str, int] = defaultdict(int)

    def add_product(self, product_code: str, quantity: int = 1):
        """Adds a product to the basket with the given quantity.
        :param product_code: Code of the product to be added to the basket.
        :param quantity: Quantity of the product to be added to the basket.
        """
        if product_code not in PRODUCT_CATALOGUE:
            raise ValueError(f"Invalid product code {product_code} supplied")
        self._products[product_code] += quantity

    def _calculate_offer_discount_amount(self) -> float:
        """Calculates total discount amount by considering offers on each of the products in the basket."""
        total_discount_amount = 0
        for product_code, product_quantity in self._products.items():
            total_discount_amount += PRODUCT_OFFER_HANDLER.calculate_discount(product_code, product_quantity)
        return total_discount_amount

    def get_basket_total_amount(self) -> float:
        """Calculates total billing amount by subtracting discount amount as per product offers and adding shipping
        cost as per delivery cost rules."""
        total_amount = 0
        for product_code, product_quantity in self._products.items():
            total_amount += PRODUCT_CATALOGUE[product_code]["price"] * product_quantity
        discount_amount = self._calculate_offer_discount_amount()
        total_amount -= discount_amount
        shipping_cost = calculate_delivery_cost(total_amount)
        total_amount += shipping_cost
        # Not using round as the example expected output for 98.275 is 98.27, but `round` gives 98.28.
        # return round(total_amount, AMOUNT_DECIMAL_PRECISION)
        return math.floor(total_amount * 10 ** AMOUNT_DECIMAL_PRECISION) / (10 ** AMOUNT_DECIMAL_PRECISION)


if __name__ == "__main__":
    basket = Basket()
    basket.add_product("B01", 2)
    basket.add_product("R01", 3)
    print(basket.get_basket_total_amount())
