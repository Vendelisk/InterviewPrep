# [] array, () tuple, {} dictionary
# for index, val in enumerate(range(10)): do stuff


import string
from pip import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for i, strToAdd in enumerate(strs):  # things to group
            x = ''.join(sorted(strToAdd))
            if(x in grouped):
                grouped[x].append(strToAdd)
            else:
                grouped[x] = [strToAdd]

        x = list(grouped.values())
        return x


strs = ["", ""]
sol = Solution()
print(sol.groupAnagrams(strs))
