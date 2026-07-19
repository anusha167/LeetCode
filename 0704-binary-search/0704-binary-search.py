class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Case 1
            if nums[mid] == target:
                return mid
            # Case 2
            elif nums[mid] < target:
                left = mid + 1                 
            # Case 3, discard the larger half.         
            else:
                right = mid - 1
        
        return -1