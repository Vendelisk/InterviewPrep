from pip import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, temp = nums[0], nums[0]
        for i in range(1, len(nums)):
            if temp < 0:
                temp = nums[i]
            else:
                temp += nums[i]
            maxSum = max(maxSum, temp)
        return maxSum


nums = [5, 4, 1, -7, 8]
sol = Solution()
print(sol.maxSubArray(nums))
