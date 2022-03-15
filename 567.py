class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = [0 for i in range(200)]
        h2 = [0 for i in range(200)]
        l = len(s1)
        a, b = 0, l - 1
        for i in s1:
            h1[ord(i)] += 1
        for i in range(l):
            h2[ord(s2[i])] += 1

        if h1 == h2:
            return True

        while b < len(s2):
            h2[ord(s2[a])] -= 1
            a += 1
            b += 1
            h2[ord(s2[b])] += 1
            if h1 == h2:
                return True
        return False