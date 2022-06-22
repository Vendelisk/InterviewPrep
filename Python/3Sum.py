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
fix 2 numbers
"""




import timeit
from pip import List
class Solution:
    more = True
    currI = 0
    currJ = 0

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        zeroSumCombos = []
        goals = set(nums)

        for i in goals:
            print(nums)
            Solution.currI = 0
            Solution.currJ = len(nums)-1
            Solution.more = True
            while Solution.more:
                val = Solution.findSum(Solution.currI, Solution.currJ, nums, i)
                Solution.currI += 1
                if val is not None:
                    val.sort()
                    if val not in zeroSumCombos:
                        zeroSumCombos.append(val)

        return zeroSumCombos

    def findSum(i: int, j: int, nums: List[int], goal: int):
        curr = nums[i] + nums[j]
        print(nums[i], "+", nums[j], "=", nums[i]+nums[j], "goal:", goal)
        if j <= i:
            Solution.more = False
            return
        elif nums.index(goal) == j:
            Solution.currI = i
            Solution.currJ = j
            return Solution.findSum(i, j-1, nums, goal)
        elif nums.index(goal) == i:
            Solution.currI = i
            Solution.currJ = j
            return Solution.findSum(i+1, j, nums, goal)
        elif curr == goal * -1:
            Solution.currI = i
            Solution.currJ = j
            return [nums[i], nums[j], goal]
        elif curr < goal * -1:
            Solution.currI = i
            Solution.currJ = j
            return Solution.findSum(i+1, j, nums, goal)
        elif curr > goal * -1:
            Solution.currI = i
            Solution.currJ = j
            return Solution.findSum(i, j-1, nums, goal)
        return


sol = Solution()

start = timeit.default_timer()
print(sol.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
# expected: [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
# missing: [-3,0,3], [-2,0,2], [-1,-1,2], [-1,0,1]

stop = timeit.default_timer()
print('Time: ', stop - start)
