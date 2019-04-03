
"""
check whether there are sum
@input:
    n: number of elements in the list
    ls: list of the elements concern (provided that it is sorted) ex : [1,3,4,8]
    k: expected sum to be counted
@returns:
    bool True/False: True if there exists a pair, False otherwise
"""
def check_pair(n, ls, k):
    left = 0
    right  = n-1  #       intialize left and right as the index pointer where
    while left != right:
        sum = ls[left] + ls[right]
        if sum == k:
            return True
        elif sum < k:
            left = left + 1
        elif sum > k:
            right = right - 1

    return False

# MAIN FUNCTION: For checking or whatever
print(check_pair(4, [1,2,6,7], 8))
