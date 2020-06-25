import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return None

    max_val = - float("inf")
    min_val = float("inf")

    for int in ints:
        if int > max_val:
            max_val = int
        if int < min_val:
            min_val = int

    return (min_val, max_val)

# Normal cases
print('Normal Cases:')
# Case 1
l = [i for i in range(0, 10)]
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Case 2
l = [i for i in range(-10, 10)]
random.shuffle(l)
print("Pass" if ((-10, 9) == get_min_max(l)) else "Fail")

# Edge cases
print('Edge Cases:')
# Case 3
l = [i for i in range(-1, 0)]
random.shuffle(l)
print("Pass" if ((-1, -1) == get_min_max(l)) else "Fail")

# Case 4
l = []
print("Pass" if (None == get_min_max(l)) else "Fail")
