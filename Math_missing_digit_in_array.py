# -*- coding: utf-8 -*-

# Input: arr[] = {1, 2, 4, 6, 3, 7, 8} , N = 8
# Output: 5
# Explanation: Here the size of the array is 8, so the range will be [1, 8]. The missing number between 1 to 8 is 5

# Input: arr[] = {1, 2, 3, 5}, N = 5
# Output: 4
# Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4



def missing_number(n, arr):
    sum_arr = sum(arr)
    # Calculate the expected sum
    expected_sum = (n * (n + 1)) // 2
    # Return the missing number
    return expected_sum - sum_arr


# Driver code
# arr = [1, 2, 3, 5]
# n = 5
arr = [1, 2, 4, 6, 3, 7, 8]
n = 8
print(missing_number(n, arr))
