from typeguard import typechecked

@typechecked
def calculate_discount(price:int|float, discount: int|float)->float:
    """
    Calculates the discounted price 

    Args: 
        price(int or float):    The price to be discounted
        discount(int or float): The discount in percent

    Returns:
        float: The discounted price

    """
    return round(price * (1 - discount/100), 2)


if __name__ == "__main__":
    price = input("enter a price: ")
    discount = input("enter a discount percent: ")
    print(f"discount price: ${calculate_discount(price,discount)}")