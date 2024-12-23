class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                count += 1
                continue
            i += 1
        return len(nums)