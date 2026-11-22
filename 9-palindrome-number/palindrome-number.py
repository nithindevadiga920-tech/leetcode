class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=str(x)
        if x>=0:
            z=y[::-1]
            if y==z:
                return True
            else:
                return False
        else:
            return False