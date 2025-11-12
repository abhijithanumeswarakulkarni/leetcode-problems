class Solution:
    MOD = 10 ** 9 + 7
    def numberOfWays(self, n: int, x: int) -> int:
        # Approach 1: Recursion
        # def solve(i, k):
        #     if k == n:
        #         return 1
        #     if k > n or i > n:
        #         return 0
        #     pick = solve(i+1, i**x+k)
        #     not_pick = solve(i+1, k)
        #     return pick + not_pick 
        # return solve(1, 0) % self.MOD

        # Approach 2: DP
        def solve(i, k, dp):
            if k == n:
                return 1
            if k > n or i > n:
                return 0
            if dp[i][k] == -1:
                pick = solve(i+1, i**x+k, dp)
                not_pick = solve(i+1, k, dp)
                dp[i][k] = pick + not_pick 
            return dp[i][k]
        dp = [[-1] * (n) for _ in range(n*2)]
        return solve(1, 0, dp) % self.MOD


s = Solution()
n = 4
x = 1
print(s.numberOfWays(n, x))