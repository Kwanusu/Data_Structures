import math
import os
import random
import re
import sys

#
# Complete the 'climbingStairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER a as parameter.
#

def climbingStairs(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    
    # Start with the base cases
    first = 1
    second = 2
    
    # Calculate number of ways for each step from 3 to a
    for i in range(3, a + 1):
        current = first + second
        first = second
        second = current
    
    return second


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(input().strip())

    result = climbingStairs(a)

    fptr.write(str(result) + '\n')

    fptr.close()
