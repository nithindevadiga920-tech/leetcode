class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h=nums[0]
        n=len(set(nums))
        u=list(set(nums))
        i=0
        while i<n:
            c=nums.count(u[i])
            if c>nums.count(h):
                h=u[i]
            i+=1
        return h 
