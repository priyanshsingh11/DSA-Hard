from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        total = Counter(t)
        miss = len(t)

        i = 0
        I = J = 0

        for j, ch in enumerate(s):

            if total[ch] > 0:
                miss -= 1

            total[ch] -= 1

            if miss == 0:

                while total[s[i]] < 0:
                    total[s[i]] += 1
                    i += 1

                if J == 0 or (j - i + 1) < (J - I):
                    I, J = i, j + 1

                total[s[i]] += 1
                miss += 1
                i += 1

        return s[I:J]
