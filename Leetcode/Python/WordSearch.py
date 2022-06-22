import timeit
from pip import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        starts = []
        for i, v in enumerate(board):
            for j, w in enumerate(board[i]):
                if w not in word:
                    board[i][j] = "-"
                elif w == word[0]:
                    starts.append((i, j))
        for x in board:
            print(x)
        for i, j in starts:
            if Solution.wordSearch(board, word[1:len(word)], i, j):
                return True
        return False

    def wordSearch(board: List[List[str]], word: str, x: int, y: int):
        if len(word) == 0:
            return True
        if word[0] == board[x][y-1]:
            board[x][y-1] = "-"
            return Solution.wordSearch(board, word[1:len(word)], x, y-1)
        if word[0] == board[x+1][y]:
            board[x+1][y] = "-"
            return Solution.wordSearch(board, word[1:len(word)], x+1, y)
        if word[0] == board[x][y+1]:
            board[x][y+1] = "-"
            return Solution.wordSearch(board, word[1:len(word)], x, y+1)
        if word[0] == board[x-1][y]:
            board[x][y+1] = "-"
            return Solution.wordSearch(board, word[1:len(word)], x-1, y)
        return False

    def rangeCheck(board: List[List[str]], x: int, y: int):
        if x < 0 or x >=


start = timeit.default_timer()
sol = Solution()

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

print(sol.exist(board, "DB"))

stop = timeit.default_timer()
print('Time: ', stop - start)
