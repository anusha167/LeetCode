class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [3,0,1]
        n = len(nums) + 1
        range_nums = range(0,n)
        sum_range = sum(range_nums)
        req_num = sum_range - sum(nums)
        return req_num