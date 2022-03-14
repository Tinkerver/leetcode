
from functools import reduce
class Solution:
    def reverseWords(self, s: str) -> str:
        # r=s.split(' ')
        # r=[i[::-1] for i in r]
        # result=r[0]
        # for i in r[1:]:
        #     result += ' '
        #     result+=i
        # return result
        s=s[::-1]
        r=s.split(' ')
        r=r[::-1]
        return reduce(lambda x, y: x+' '+y, r)

