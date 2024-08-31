import math
import os
import random
import re
import sys

#
# Complete the 'fractionalKnapsack' function below.
#
# The function is expected to return a FLOAT.
# The function accepts following parameters:
#  1. INTEGER W
#  2. INTEGER_ARRAY w
#  3. INTEGER_ARRAY p
#

def fractionalKnapsack(W, w, p):
    # Write your code here
    items = []
    for i in range(len(w)):
        items.append((p[i] / w[i], w[i], p[i]))

    # Sort items by their profit-to-weight ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0
    remaining_capacity = W

    for ratio, weight, profit in items:
        if weight <= remaining_capacity:
            # If the item can fully fit in the knapsack, take all of it
            total_value += profit
            remaining_capacity -= weight
        else:
            # Take the fraction of the item that fits
            fraction = remaining_capacity / weight
            total_value += profit * fraction
            break  # Knapsack is now full

    return total_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    W = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    p = list(map(int, input().rstrip().split()))

    result = fractionalKnapsack(W, w, p)

    fptr.write(str(result) + '\n')

    fptr.close()
