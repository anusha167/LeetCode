class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        present = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in present:
                result.append(i)

        return result