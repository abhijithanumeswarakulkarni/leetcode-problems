from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # # Approach 1: Brute force - Obv TLE
        # res = []
        # for spell in spells:
        #     count = 0
        #     for potion in potions:
        #         if spell * potion >= success:
        #             count += 1
        #     res.append(count)
        # return res

        # # Approach 2: Smarter (slightly) - TLE as wel
        # n = len(potions)
        # res = []
        # potions.sort()
        # for spell in spells:
        #     if spell * potions[-1] < success:
        #         res.append(0)
        #     else:
        #         for index, potion in enumerate(potions):
        #             if spell * potion >= success:
        #                 res.append(n-index)
        #                 break
        # return res

        # Approach 3: Bin Search
        n = len(potions)
        potions.sort()
        def binary_search(spell):
            l = 0
            h = n - 1
            idx = -1
            while l <= h:
                m = (l+h) // 2
                if spell * potions[m] >= success:
                    idx = m
                    h = m - 1
                else:
                    l = m + 1
            return idx

        res = []
        for spell in spells:
            idx = binary_search(spell)
            if idx != -1:
                res.append(n-idx)
            else:
                res.append(0)
        return res

s = Solution()
spells = [3,1,2]
potions = [8,5,8]
success = 16
print(s.successfulPairs(spells, potions, success))