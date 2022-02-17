import pytest

from src.delivery import calculate_delivery_cost


@pytest.mark.parametrize(
    "order_amount, expected_delivery_cost",
    [
        (117.17, 0),
        (90, 0),
        (89.999, 2.95),
        (68, 2.95),
        (50, 2.95),
        (49.99, 4.95),
        (10, 4.95),
        (0, 4.95),  # It could happen that order amount equals to 0 after applying discounts. However, we still want
        # to charge for the shipping cost.
    ],
)
def test_calculate_delivery_cost(order_amount: float, expected_delivery_cost: float):
    assert calculate_delivery_cost(order_amount) == expected_delivery_cost


def test_invalid_order_amount_calculate_delivery_cost():
    with pytest.raises(ValueError):
        calculate_delivery_cost(-20.01)
