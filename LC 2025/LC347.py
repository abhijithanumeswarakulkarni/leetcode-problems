from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach (should know how to sort a dict by value)
        freq = Counter(nums)
        return list(dict(sorted(freq.items(), key=lambda it: it[1], reverse=True)).keys())[:k]