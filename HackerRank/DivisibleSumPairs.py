"""
Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i < j and arr[i] + arr[j] is divisible by k.

Example
arr = [1,2,3,4,5,6]
k = 5

Three pairs meet the criteria: [1,4],[2,3] and [4,6].

Function Description
Complete the divisibleSumPairs function in the editor below.

divisibleSumPairs has the following parameter(s):
int n: the length of array arr
int ar[n]: an array of integers
int k: the integer divisor

Returns
- int: the number of pairs

Input Format
The first line contains 2 space-separated integers, n and k.
The second line contains n space-separated integers, each a value of arr[i].

Constraints
2 <= n <= 100
1 <= k <= 100
1 <= arr[i] <= 100

Sample Input
STDIN           Function
-----           --------
6 3             n = 6, k = 3
1 3 2 6 1 2     arr = [1, 3, 2, 6, 1, 2]

Sample Output

 5

Explanation

Here are the 5 valid pairs when k=3:
(0,2) -> arr[0] + arr[2] = 1 + 2 = 3
(0,5) -> arr[0] + arr[5] = 1 + 2 = 3
(1,3) -> arr[1] + arr[3] = 3 + 6 = 9
(2,4) -> arr[2] + arr[4] = 2 + 1 = 3
(4,5) -> arr[4] + arr[5] = 1 + 2 = 3

"""

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, arr):
    numPairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] + arr[j]) % k == 0: 
                numPairs += 1
    return numPairs

n = 6
k = 3
arr = [1, 3, 2, 6, 1, 2]
print(divisibleSumPairs(n, k, arr))