class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [3,0,1]
        n = len(nums) + 1
        range_nums = range(0,n)

        for i in range_nums:
            if i in nums:
                continue
            else:
                return i
        