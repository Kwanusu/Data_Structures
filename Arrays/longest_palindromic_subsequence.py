import math
import os
import random
import re
import sys

#
# Complete the 'longestPalindromicSubsequence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def longestPalindromicSubsequence(s):
    # Write your code here
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Base case: single character palindromes
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = longestPalindromicSubsequence(s)

    fptr.write(str(result) + '\n')

    fptr.close()
