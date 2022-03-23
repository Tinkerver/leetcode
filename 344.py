class Solution:
    def reverseString(self, s):
        l = len(s)-1
        for i in range(l // 2+1):
            s[i], s[l - i] = s[l - i], s[i]
            return s
