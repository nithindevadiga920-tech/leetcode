class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        d = {i: chr(64 + i) for i in range(1, 27)}
        l1=[]
        x=columnNumber
        while x>0:
            x=x-1
            n=x%26
            x=x//26    
            l1.append(d[n+1])
        s="".join(l1)
        return s[::-1]
