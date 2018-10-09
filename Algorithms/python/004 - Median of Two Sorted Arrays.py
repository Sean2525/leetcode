class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        n = len(nums)
        i = int(n/2)
        if n%2:
            return nums[i]
        else:
            return (nums[i-1]+nums[i])/2