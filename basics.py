def calculate_discount(price, is_member):
    """
    Returns the discounted price.
    Members receive a 10% discount.
    """

    if price < 0:
        raise ValueError
    
    if is_member:
        return price - (price * 0.1)
    return price
