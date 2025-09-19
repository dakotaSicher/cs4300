def calculate_discount(price, discount):
    #verify privided inputs are of numerical type
    #also would 
    ret_val = None
    try:
        ret_val = round(price * (1- discount/100), 2)
    except TypeError:
        raise
    return ret_val

if __name__ == "__main__":
    price = input("enter a price: ")
    discount = input("enter a discount percent: ")
    print(f"discount price: ${calculate_discount(float(price),float(discount))}")