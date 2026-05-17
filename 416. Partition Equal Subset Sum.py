class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        dp = [False] * (total + 1)

        half = total // 2
        if total%2 != 0: return False
        dp[0] = True

        for num in nums:
            for i in range(half, num-1, -1):
                dp[i] = dp[i] or dp[i-num]

        return dp[half]
