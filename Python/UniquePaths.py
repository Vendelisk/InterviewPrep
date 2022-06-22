import timeit
from pip import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for i in range(n)] for j in range(m)]
        return Solution.pathFind(self, 0, 0, m, n, arr)

    def pathFind(self, x: int, y: int, m: int, n: int, arr: list):
        Solution.printArr(m, n, arr, x, y)
        # if you reach the end of a row or col, it's a straight shot to goal
        if x == m-1 or y == n-1:
            return 1

        # this will only happen if the number represents the possible paths from any node to the goal
        if arr[x][y] > 0:
            return arr[x][y]

        # at this point, the neighbors of any node will sum to the total paths from that node
        arr[x][y] = Solution.pathFind(
            self, x, y+1, m, n, arr) + Solution.pathFind(self, x+1, y, m, n, arr)
        return arr[x][y]

    def printArr(m: int, n: int, arr: list, x: int, y: int):
        print('----------------')
        for i in range(m):
            for j in range(n):
                if i == x and j == y:
                    print("*"+str(arr[i][j])+"*", end=' ')
                else:
                    print(" " + str(arr[i][j]) + " ", end=' ')
            print()
        print('----------------')


start = timeit.default_timer()

sol = Solution()
print(sol.uniquePaths(3, 4))

stop = timeit.default_timer()
print('Time: ', stop - start)
