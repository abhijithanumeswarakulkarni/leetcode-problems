# To create counter hashmaps, key = char, value = count
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 1 (brute force - convert to arr and manipulate) : time = O(n^2), space = O(n) - Passed
        # listS = list(s)
        # for x in t:
        #     if x in listS:
        #         listS.remove(x)
        #     else:
        #         return False
        # return True if len(listS) == 0 else False

        # Approach 2 (hashmaps again, compare the count) : time = O(n), space = O(n) - Passed (opt soln)
        sCount = Counter(s)
        tCount = Counter(t)
        if len(sCount) != len(tCount):
            return False
        for key in sCount:
            if sCount[key] != tCount[key]:
                return False
        return True
