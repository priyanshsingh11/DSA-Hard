class Solution(object):
    def minEatingSpeed(self, piles, h):
        def solve(k):
            hours = 0

            for p in piles:
                # formula of efficient calculation
                hours += (p + k - 1) // k
            
            return hours <= h

    
        start = 1
        end = max(piles)

        while start < end:
            mid = (start + end) // 2

            if solve(mid):
                end = mid
            else:
                start = mid + 1

        return end
