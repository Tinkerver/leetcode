class Solution(object):
    def oneEditAway(self, first, second):
        """
        :type first: str
        :type second: str
        :rtype: bool
        """
        if abs(len(first) - len(second)) > 1:
            return False

        elif len(first) == len(second):
            count = 0
            for i in range(len(first)):
                if (first[i] != second[i]):
                    count = count + 1
                if count > 1:
                    return False
            return True
        if len(first) > len(second):
            tmp = first
            first = second
            second = tmp

        if len(first) == 0:
            return True

        j=0
        for i in range(len(first)):
            if first[i] == second[i+j]:
                continue
            elif j==0:
                j = 1
                if(first[i] != second[i+j]):
                    return False
            else:
                return False

        return True