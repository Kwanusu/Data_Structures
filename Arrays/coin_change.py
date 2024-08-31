import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#
# Write your code here

def getWays(n, c):
    dp = [0] * (n + 1)
    
    # There is exactly one way to make change for 0, which is using no coins
    dp[0] = 1
    
    # For each coin in the list c
    for coin in c:
        # Update the dp array for all amounts from coin to n
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]
    
    # The result will be the number of ways to make change for n
    return dp[n]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()