import json
import pathlib
from typing import Any, Dict, List

CURRENT_FILE_PATH = pathlib.Path(__file__)
CURRENT_DIRECTORY = CURRENT_FILE_PATH.parent
DATA_DIRECTORY = CURRENT_DIRECTORY.parent / "data"


def read_json_content(file_path: pathlib.Path) -> Dict[Any, Any]:
    """Reads json content from the json file at the given file_path."""
    with open(file_path, "r") as json_file:
        json_content = json.load(json_file)
    return json_content


def get_product_catalogue() -> Dict[str, Any]:
    """Reads product catalogue from the corresponding json file."""
    product_catalog_file_path = DATA_DIRECTORY / "product_catalogue.json"
    return read_json_content(product_catalog_file_path)


def get_product_offers() -> Dict[str, Any]:
    """Reads product specific offers from the corresponding json file."""
    product_offers_file_path = DATA_DIRECTORY / "product_offers.json"
    return read_json_content(product_offers_file_path)


def get_delivery_costs() -> List[Dict[str, Any]]:
    """Reads a list of delivery cost rules and sorts them by order amount in a descending fashion."""
    delivery_costs_file_path = DATA_DIRECTORY / "delivery_cost.json"
    delivery_costs = read_json_content(delivery_costs_file_path)["deliveryCosts"]
    sorted_delivery_costs = sorted(delivery_costs, key=lambda cost: cost["orderAmountGreaterThan"], reverse=True)
    return sorted_delivery_costs
