"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]]
 such that 
 i != j, 
 i != k, and 
 j != k, 
 and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

"""
Thoughts:
two-pointers
"""




import timeit
from pip import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        zeroSumSet = []
        contents = set(nums)

        i = 0
        j = len(nums) - 1
        # print(nums)

        if len(nums) < 3:
            return []

        while True:
            if i+1 == j:
                break
            goal = (nums[i] + nums[j]) * -1
            # print(nums[i], nums[j], goal)
            if goal < nums[i]:
                i = 0
                j -= 1
            elif goal in contents:
                ans = [nums[i], nums[j], goal]
                ans.sort()
                if (goal == nums[i] or goal == nums[j]) and nums.count(goal) == 1:
                    pass
                elif ans not in zeroSumSet:
                    zeroSumSet.append(ans)
                i += 1
            else:
                i += 1

        return zeroSumSet


sol = Solution()

start = timeit.default_timer()
print(sol.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
# expected: [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
# missing: [-1,0,1]

stop = timeit.default_timer()
print('Time: ', stop - start)
