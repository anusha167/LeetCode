class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       
       # Using HashMap one pass method

        hashmap = {} # val : index

        for i, n in enumerate(nums): # enumerate() adds an automatic counter which allows you to track both the index and the value simultaneously
            complement = target - n
            if complement in hashmap:
                return [i, hashmap[complement]]
        
            # if the complement doesn't exist in the hashmap, we add that value to the hashmap
            hashmap[n] = i
    
        #return an empty list if no solution exists
        return[]