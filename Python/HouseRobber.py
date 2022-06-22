"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,1,1,2]
Output: 4
Explanation: Rob house 1 (money = 2) and then rob house 4 (money = 2).
Total amount you can rob = 2 + 2 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

"""
technically dynamic programming - non-recursive though.
"bottom up" approach where array is used to calculate running total
"""




import timeit
from pip import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        total = []
        if size == 0:
            return 0
        if size == 1:
            return nums[0]

        total.append(nums[0])
        total.append(max(nums[0], nums[1]))

        for i in range(2, size):
            total.append(max(total[i-2] + nums[i], total[i-1]))
        # print(nums)
        # print(total)

        return total[-1]


sol = Solution()

start = timeit.default_timer()
print(sol.rob([2, 7, 9, 3, 1]))

stop = timeit.default_timer()
print('Time: ', stop - start)
