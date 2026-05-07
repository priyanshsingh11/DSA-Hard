class Solution(object):
    from collections import Counter
    def findAnagrams(self, s, p):
        ns = len(s)
        np = len(p)
        ans = []

        if np > ns: return []

        p_count = Counter(p)
        window = Counter(s[:np])

        if p_count == window: ans.append(0)

        for i in range (np, ns):
            window[s[i]] += 1
            left_char = s[i-np]
            window[left_char] -= 1
            
            if window[left_char] == 0:
                del window[left_char]

            if window == p_count: ans.append(i-np + 1)

        return ans
