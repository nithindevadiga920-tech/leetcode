class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        x=0
        n=len(columnTitle)
        for i, a in enumerate(columnTitle):
            x+=(26**(len(columnTitle)-1-i)*(ord(a)-ord('A')+1))

        return x




