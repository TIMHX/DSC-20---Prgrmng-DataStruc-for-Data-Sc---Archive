def unusual_sum(num1, num2):
    """Write a Python program to sum
    two given integers. However, if the sum is
    greater than 10, return the maximum of two numbers.
    If the sum is negative, then return the minimum of
    two numbers.
    >>> unusual_sum(1, 2)
    3
    >>> unusual_sum(11, 0)
    11
    >>> unusual_sum(0, -10)
    -10
    """
    # YOUR CODE IS HERE #
    if num1+num2>10:
        return max(num1,num2)
    elif num1+num2<0:
        return min(num1,num2)
    else:
        return num1+num2
