class Solution(object):
    def nextsmall(self, heights, n):
            s = [-1]
            ans = [0]*n

            for i in range(n-1, -1, -1):
                curr = heights[i]

                while s[-1] != -1 and heights[s[-1]] >= curr:
                    s.pop()

                ans[i] = s[-1]
                s.append(i)
            
            return ans

    def prevsmall(self, heights, n):
            s = [-1]
            ans = [0]*n

            for i in range(n):
                curr = heights[i]

                while s[-1] != -1 and heights[s[-1]] >= curr:
                    s.pop()

                ans[i] = s[-1]
                s.append(i)
            
            return ans
            
    def largestRectangleArea(self, heights):
        n = len(heights)
        area = float('-inf')

        nextsmaller = self.nextsmall(heights, n)
        prevsmaller = self.prevsmall(heights, n)

        for i in range(n):
            if nextsmaller[i] == -1: nextsmaller [i] = n
            l = heights[i]
            b = nextsmaller[i] - prevsmaller[i] - 1

            newarea = l * b

            area = max(area, newarea)

        return area
