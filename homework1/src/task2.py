from typeguard import typechecked

"""
Addition, Subtraction and Multiplication work the same with any mix of floats and ints
If both operands are ints the results will be an int, else a float
Float precision can result in unexpected results ie 1.1 + 2.2 != 3.3 (its 3.3000000000000003)
"""
@typechecked
def addNum(op1:int|float, op2:int|float)->int|float:
    """
    Adds two numbers.

    Args:
        op1 (int or float): Augend 
        op2 (int or float): Addend 

    Returns:
        int or float: The sum of a and b.
    """
    return op1 + op2

@typechecked
def subNum(op1:int|float, op2:int|float)->int|float:
    """
    Subtracts two numbers

    Args:
        op1 (int or float): Minuend
        op2 (int or float): Subtrahend 

    Returns:
        int or float: The difference of a and b.
    """
    return op1 - op2

@typechecked
def multNum(op1:int|float, op2:int|float)->int|float:
    """
    Multiplies two numbers

    Args:
        op1 (int or float): Multiplicand
        op2 (int or float): Multiplier

    Returns:
        int or float: The product of a and b.
    """
    return op1 * op2


@typechecked
def div(op1:int|float, op2:int|float)->float:
    """
    Divides two numbers

    Args:
        op1 (int or float): Dividend
        op2 (int or float): Divisor

    Returns:
        float: The quotient of a and b.
    """
    return op1 / op2


@typechecked
def floorDiv(op1:int|float, op2:int|float)->int|float:
    """
    Divides two numbers and takes the floor

    Args:
        op1 (int or float): Dividend
        op2 (int or float): Divisor

    Returns:
        int or float: The floor of the quotient of a and b.
    """
    return op1 // op2


@typechecked
def modNum(op1:int|float, op2:int|float)->int|float:
    """
    Divides two numbers and returns the remainder

    Args:
        op1 (int or float): Dividend
        op2 (int or float): Divisor

    Returns:
        int or float: The remainder of division of a by b.
        The result will always have the save sign as the divisor
    """
    return op1 % op2


@typechecked
def catStr(op1:str, op2:str)->str:
    """
    Concatenates two strings in operand order

    Args:
        op1 (str): 'front' string
        op2 (str): 'back' string

    Returns:
        str: the combined string op1op2
    """
    return op1 + op2


@typechecked
def repStr(op1:str, op2:int)->str:
    """
    Repeats the string

    Args:
        op1 (str): The string
        op2 (int): Number of times to repeat
 
    Returns:
        str: The repeated string
    """
    return op1 * op2


def sliceStr(op1: str, op2:int|None = None, op3: int|None = None, op4: int|None = None)->str:
    """
    Finds the slice of a string

    Args:
        op1 (str): The string
        op2 (int or None): The index or start
        op3 (int or None): The end (exclusive)
        op4 (int or None): The interval

    Returns:
        str: A slice of the string
    """
    if op2 is not None and op3 is None and op4 is None:
        return op1[op2]
    else:
        return op1[op2:op3:op4]
    




if __name__=="__main__":
    h = "hello world"
    print(h[::])
    print(sliceStr(h,1))
    print(sliceStr(h,0,6))
    print(sliceStr(h,2,op4=2))
    print(sliceStr(h,op4=-1))
    print(sliceStr(h,op3=2, op4=-2))
