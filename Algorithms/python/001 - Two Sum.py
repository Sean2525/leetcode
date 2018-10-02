class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        temp = []
        for i,x in enumerate(nums):
            if x in hashmap:
                temp.append(hashmap[x])
                temp.append(i)
                break
            hashmap[target - x] = i
        
        return temp