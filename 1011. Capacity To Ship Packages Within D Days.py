class Solution(object):
    def shipWithinDays(self, weights, days):
        def solve(capacity):
            day = 1
            load = 0

            for w in weights:
                if w + load > capacity:
                    day += 1
                    load = w

                else: load += w
            
            return day <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left+right) // 2

            if solve(mid): right = mid

            else:
                left = mid + 1 

        return left
