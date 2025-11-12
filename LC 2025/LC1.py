class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach 1 (bruteforce) - time = O(n^2), space = O(1) - Passed
        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [-1, -1] # Ideally this should never get triggered

        # Approach 2 (if I can get the index of an ele in O(1) -> hmap): time = O(n), space = O(n)
        hmap = {x: y for y, x in enumerate(nums)} # O(n)
        for index, val in enumerate(nums):
            complement = target - val
            if complement in hmap and hmap[complement] != index:
                return [index, hmap[complement]]
        return [-1, -1] # Ideally this should never get triggered

