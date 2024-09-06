# -*- coding: utf-8 -*-


# Consider the following examples:

# n = 5: There is one 5 and three 2s in prime factors of 5! (2 * 2 * 2 * 3 * 5). So a count of trailing 0s is min(1, 3) = 1.
# n = 11: There are two 5s and eight 2s in prime factors of 11! (2 8 * 34 * 52 * 7). So the count of trailing 0s is min(2, 8) = 2.

# We can observe that the number of 2s in prime factors is always more than or equal to the number of 5s. So, if we count 5s in prime factors, we are done.


def findTrailingZeros(n):
    # Negative Number Edge Case
    if(n < 0):
        return -1

    # Initialize result
    count = 0

    # Keep dividing n by
    # 5 & update Count
    while(n >= 5):
        n //= 5
        count += n

    return count


# Driver program
n = 100
print("Count of trailing 0s in 100! is", findTrailingZeros(n))