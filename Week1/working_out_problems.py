#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find_needle' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING haystack
#  2. STRING needle
#

def find_needle(haystack, needle):
    # Write your code here
    print(haystack)
    print(needle)
    
    # Edge cases
    if len(needle) > len(haystack):
        return -1
    if len(needle) == 0:
        return 0
    
    # Check each position in haystack
    for i in range(len(haystack)):
        # Use slicing to safely compare - Python won't throw an error if slice goes out of bounds
        if haystack[i:i+len(needle)] == needle:
            return i
    
    return -1
 

if __name__ == "__main__":
    # Read the entire input
    input_data = sys.stdin.read().strip().split("\n")
    
    results = []
    for i in range(0, len(input_data), 2):
        # Each test case contains two lines: haystack and needle
        haystack = input_data[i].strip()
        needle = input_data[i + 1].strip()
        
        # Redirect debugging output to stderr to suppress student print statements
        original_stdout = sys.stdout
        try:
            sys.stdout = sys.stderr  # Redirect stdout to stderr for debugging prints
            # Call the function here
            result = find_needle(haystack, needle)
        finally:
            sys.stdout = original_stdout  # Restore stdout
        
        # Collect the result for this test case
        results.append(result)
    
    # Print all results (one per line)
    for res in results:
        print(res)