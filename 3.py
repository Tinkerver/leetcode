class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        a, b = 0, 0
        l = [0 for i in range(200)]
        l[ord(s[a])] = 1
        r = 1
        while b < len(s) - 1:
            b += 1
            if l[ord(s[b])] == 0:
                l[ord(s[b])] = 1
            else:
                while l[ord(s[b])] == 1:
                    l[ord(s[a])] = 0
                    a += 1
                l[ord(s[b])] = 1
            r = max(r, b - a + 1)
        return r
