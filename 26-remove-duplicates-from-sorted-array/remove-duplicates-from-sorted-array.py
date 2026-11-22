class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        s1=set(nums)
        l=list(s1)
        l.sort()
        nums[:len(l)]=l
        return len(l)