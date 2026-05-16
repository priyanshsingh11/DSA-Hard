class Solution(object):
    def partition(self, s):
        n = len(s)
        result = []

        def pallindrom (sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == n: 
                result.append(path[:]) 
                return

            for end in range(start+1, n+1):
                substring = s[start:end]
                if pallindrom(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
                

        backtrack(0, [])

        return result
