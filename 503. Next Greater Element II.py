class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack = []
        ans = [-1]*n

        for i in range(2*n):
            curr = nums[i%n]
            while stack and curr > nums[stack[-1]]:
                element = stack.pop()
                ans[element] = curr

            if i < n:
                stack.append(i)

        return ans
