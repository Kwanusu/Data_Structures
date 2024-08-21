import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0   
    
    for num in arr:
        # Check if the left sum equals the right sum
        if left_sum == (total_sum - num - left_sum):
            return "YES"
        
        # Update left sum
        left_sum += num
    
    # If no such index found, return "NO"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
