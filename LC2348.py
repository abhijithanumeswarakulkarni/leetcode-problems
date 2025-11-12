from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # Idea is that count of subsequent zeros in the list is equal
        # to (k*(k+1))//2 where k is number of subsequent zeroes till
        # that point
        # time = O(n), space = O(1)
        res = 0
        count = 0
        for x in nums:
            if x == 0:
                count += 1
            else:
                res += (count * (count+1)) // 2
                count = 0
        res += (count * (count+1)) // 2
        return res


s = Solution()
nums = [0,0,0,2,0,0]
print(s.zeroFilledSubarray(nums))