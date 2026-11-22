class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d1={"I":1,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        count=0
        n=len(s)
        for i in range(n):
            if i+1<n and d1[s[i]]<d1[s[i+1]]:
                count -=d1[s[i]]
            else:
                count += d1[s[i]]
        return count
