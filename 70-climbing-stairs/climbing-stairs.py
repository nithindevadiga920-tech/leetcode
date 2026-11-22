class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fact = lambda n: 1 if n <= 1 else n * fact(n - 1)
        way=0
        for i in range(n//2+1):
                way+=fact(n-i)//(fact(i)*fact(n-2*i))
        return way