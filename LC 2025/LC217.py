from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Approach 1 (2 loops brute force) : time = O(n^2), space = O(n) - Obv TLE
        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Approach 2 (hashmaps) : time = O(n), space = O(n)
        hmap = {}
        for x in nums:
            if x in hmap:
                hmap[x] += 1
            else:
                hmap[x] = 1
        for key in hmap:
            if hmap[key] > 1:
                return True
        return False
