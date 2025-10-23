class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]  # 初始化：组成0的组合为空集

        for c in candidates:
            for t in range(c, target + 1):
                for prev in dp[t - c]:
                    dp[t].append(prev + [c])
        return dp[target]