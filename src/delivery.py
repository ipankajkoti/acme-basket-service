from src.utils import get_delivery_costs

SORTED_DELIVERY_COSTS = get_delivery_costs()


def calculate_delivery_cost(order_amount: float) -> float:
    """Calculates delivery cost based on the delivery rules for the given order amount."""
    if order_amount < 0:
        raise ValueError(f"Invalid order amount {order_amount} supplied")
    for cost in SORTED_DELIVERY_COSTS:
        if order_amount >= cost["orderAmountGreaterThan"]:
            return cost["cost"]
    raise Exception("Something went wrong while calculating delivery cost")
