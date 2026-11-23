class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            count=nums.count(i)
            if count!=2:
                return i