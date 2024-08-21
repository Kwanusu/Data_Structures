# Implemented using a set of conditions and a function that keeps calling itself
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False #Base case
    else:
        midpoint = (len(list))//2
        
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)
            
def verify(result):
    print("Target found: ", result)
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(numbers, 12) 
verify(result)          
        
result = recursive_binary_search(numbers, 6) 
verify(result)          
 # The number of times a recursive function calls itself is called Recursive depth 
 # Space complexity is the measure of how working storage or extra storage is needed as a particular algorithm grows    