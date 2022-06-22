"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s = "12:01:00PM"
Return '12:01:00'.

s = "12:01:00AM"
Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in 12 hour format
Returns

string: the time in 24 hour format
Input Format

A single string s that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).

Constraints

All input times are valid
Sample Input

07:05:45PM
Sample Output

19:05:45
"""

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    arr = s.split(":")
    twelve = arr[0] == "12"
    if arr[-1][2:] == "PM" and not twelve:
        arr[0] = str(int(arr[0])+12)
    elif arr[-1][2:] == "AM" and twelve:
        arr[0] = "00"
    arr[-1] = arr[-1][:2]
    return ":".join(arr)

s = "12:05:45AM"
print(timeConversion(s))
