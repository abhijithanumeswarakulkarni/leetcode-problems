# from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach 1 (brute-force, but optimal helper): time = O(n^3), space = O(n) - Obv TLE
        # def isAnagram(s, t):
        #     counterS = Counter(s)
        #     counterT = Counter(t)
        #     for key in counterS:
        #         if key not in counterT or counterS[key] != counterT[key]:
        #             return False
        #     return True if len(counterS) ==len(counterT) else False
        
        # n = len(strs)
        # included = [False] * n
        # res = []
        # k = 0
        # for i in range(n):
        #     if included[i]:
        #         continue
        #     res.append([strs[i]])
        #     included[i] = True
        #     for j in range(i+1, n):
        #         if not included[j] and isAnagram(strs[i], strs[j]):
        #             res[k].append(strs[j])
        #             included[j] = True
        #     k += 1
        # return res
        
        # Approach 2 (sorting anagrams make them equal): time = O(n^2*log(n)), space = O(n)
        # n = len(strs)
        # sortedStrs = []
        # for x in strs: # O(n^2*log(n))
        #     sortedStrs.append(str(sorted(x)))
        # res = []
        # k = 0
        # included = [False] * n
        # res = []
        # k = 0
        # for i in range(n):
        #     if included[i]:
        #         continue
        #     res.append([strs[i]])
        #     included[i] = True
        #     for j in range(i+1, n):
        #         if not included[j] and sortedStrs[i] == sortedStrs[j]:
        #             res[k].append(strs[j])
        #             included[j] = True
        #     k += 1
        # return res   

        # Approach 3 (hashmaps + sorting): time = O(n*k*log(k)) k = avg len of word in strs, space = O(n)
        hmap = defaultdict()
        for s in strs:
            key = str(sorted(s))
            if key in hmap:
                hmap[key].append(s)
            else:
                hmap[key] = [s]
        return list(hmap.values())
