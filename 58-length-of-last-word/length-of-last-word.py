class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=s.split()
        space=0
        if len(l)!=0:
            return len(l[-1])
        else:
            return 0