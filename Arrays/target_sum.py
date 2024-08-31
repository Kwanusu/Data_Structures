import math
import os
import random
import re
import sys

#
# Complete the 'targetSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def targetSum(nums, target):
    memo = {}
    
    def backtrack(index, current_sum):
        if index == len(nums):
            return 1 if current_sum == target else 0
        
        key = (index, current_sum)
        if key in memo:
            return memo[key]
        
        # Choose plus
        add = backtrack(index + 1, current_sum + nums[index])
        # Choose minus
        subtract = backtrack(index + 1, current_sum - nums[index])
        
        memo[key] = add + subtract
        return memo[key]
    
    return backtrack(0, 0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    nums = list(map(int, input().rstrip().split()))

    target = int(input().strip())

    result = targetSum(nums, target)

    fptr.write(str(result) + '\n')

    fptr.close()
