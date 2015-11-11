# Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            retrun 0
        i = 0
        for j in xrange(len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
        return i + 1