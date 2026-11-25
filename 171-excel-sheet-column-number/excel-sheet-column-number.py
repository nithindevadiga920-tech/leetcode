class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        d={chr(i+64): i for i in range(1,27)}
        x=0
        n=len(columnTitle)
        for i, a in enumerate(columnTitle):
            x+=(26**(len(columnTitle)-1-i)*d[a])

        return x




