"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

"""

"""




import timeit
from pip import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h = len(matrix)

        spiral = []
        while matrix:
            # add top row
            if not matrix:
                break
            spiral.extend(matrix.pop(0))
            h -= 1
            # add right col
            if not matrix or len(matrix[0]) == 0:
                break
            for i in range(h):
                spiral.append(matrix[i].pop())
            # add bot row
            if not matrix:
                break
            bot = matrix.pop()
            bot.reverse()
            spiral.extend(bot)
            h -= 1
            # add left col
            if not matrix or len(matrix[0]) == 0:
                break
            for i in range(h-1, 0, -1):
                spiral.append(matrix[i].pop(0))

        print(len(spiral))
        return spiral


sol = Solution()

start = timeit.default_timer()
print(sol.spiralOrder([[1, 2, 3, 4]]))

stop = timeit.default_timer()
print('Time: ', stop - start)
