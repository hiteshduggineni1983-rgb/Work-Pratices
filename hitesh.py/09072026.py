def get_item_price(item: str) -> str:
    # Convert input to lowercase for case-insensitivity
    match item.lower().strip():
        case "pizza":
            return "Price: 30 bucks"
        case "burger":
            return "Price: 15 bucks"
        case "pasta":
            return "Price: 20 bucks"
        case "salad":
            return "Price: 10 bucks"
        case _:
            return "Item not available"

# Example usage:
print(get_item_price("BURGER"))  # Output: Price: 15 bucks
print(get_item_price("pizza"))   # Output: Price: 30 bucks
print(get_item_price("taco"))    # Output: Item not available