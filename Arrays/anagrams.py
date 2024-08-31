import math
import os
import random
import re
import sys

#
# Complete the 'groupAnagrams' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts STRING_ARRAY strs as parameter.
#

def groupAnagrams(strs):
    # Write your code here
    anagrams = {}
    
    for s in strs:
        
        sorted_str = ''.join(sorted(s))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        anagrams[sorted_str].append(s)
        
    return list(anagrams.values())    
            
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    strs = input().rstrip().split()

    result = groupAnagrams(strs)

    fptr.write('\n'.join([' '.join(x) for x in result]))
    fptr.write('\n')

    fptr.close()
