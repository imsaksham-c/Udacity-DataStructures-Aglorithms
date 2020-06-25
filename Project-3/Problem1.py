def sqrt(number: int):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number < 0:
        return None

    if (number == 0) or (number == 1):
        return number

    i_start = 0
    i_end = number // 2

    while i_start <= i_end:
        i_middle = (i_end + i_start) // 2
        i_middle_pow = i_middle * i_middle

        if i_middle_pow == number:
            return i_middle
        elif i_middle_pow < number:
            i_start = i_middle + 1
            result = i_middle
        else:
            i_end = i_middle - 1

    return result

# Normal cases
print('Normal Cases:')
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (2 == sqrt(4)) else "Fail")
print("Pass" if (3 == sqrt(16)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")

# Edge cases
print('Edge Cases:')
print("Pass" if (None == sqrt(-5)) else "Fail")
print("Pass" if (10000 == sqrt(100000000)) else "Fail")
