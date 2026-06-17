class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        pseudocode
        Time complexity: O(n^2) problem
        Data Structure: HashMap
        Keep numbers as keys and index numbers as values
        """

        pair_idx = {} # initialize dictionary

        for i, num in enumerate(nums): 
            #enumerate() iterates through nums list along with their indices
            if target - num in pair_idx:
                return [i, pair_idx[target-num]]
            pair_idx[num]=i