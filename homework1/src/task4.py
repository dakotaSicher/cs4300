def calculate_discount(_price, _discount):
    try:
        price = float(_price)
        discount = float(_discount)
    except ValueError:
        raise
    return round(price * (1- discount/100),2)