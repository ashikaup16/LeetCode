class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = 0
        less_than = 0
        
        for num in nums:
            if num < target:
                less_than += 1
            elif num == target:
                count += 1
                
        return [less_than + i for i in range(count)]