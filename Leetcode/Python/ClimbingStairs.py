import timeit
from pip import List
"""
2 = 1 + 1
  = 2
=> 2

3 = 1 + 1 + 1
  = 1 + 2
  = 2 + 1
=> 3

4 = 1 + 1 + 1 + 1
    = 1 + 2 + 1
    = 1 + 1 + 2
    = 2 + 1 + 1
    = 2 + 2
=> 5

5 = 1 + 1 + 1 + 1 + 1
    = 1 + 1 + 1 + 2
    = 1 + 1 + 2 + 1
    = 1 + 2 + 1 + 1
    = 2 + 1 + 1 + 1
    = 1 + 2 + 2
    = 2 + 1 + 2
    = 2 + 2 + 1
=> 8
"""


class Solution:
    step_cache = {}

    def climbStairs(self, n: int) -> int:
        if n in Solution.step_cache:
            return Solution.step_cache[n]
        if n == 1:
            ret = 1
        elif n == 2:
            ret = 2
        else:
            ret = Solution.climbStairs(
                self, n-1) + Solution.climbStairs(self, n-2)
        Solution.step_cache[n] = ret
        return ret


start = timeit.default_timer()

sol = Solution()
print(sol.climbStairs(1001))

stop = timeit.default_timer()
print('Time: ', stop - start)
