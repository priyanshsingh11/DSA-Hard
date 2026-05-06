class Solution(object):
    def atMost(self, nums, k):
        left = 0
        count = 0
        right = 0
        ans = 0
        mapping = {}

        while right < len(nums):
            mapping[nums[right]] = mapping.get(nums[right], 0) + 1
            while len(mapping) > k:
                mapping[nums[left]] -= 1
                if mapping[nums[left]] == 0:
                    del mapping[nums[left]]
                left += 1
            
            count = right - left + 1
            ans += count      
            right += 1
        
        return ans

    def subarraysWithKDistinct(self, nums, k):

        return self.atMost(nums, k) - self.atMost(nums, k - 1)
        
