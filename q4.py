# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Ajlal F. Paracha - Dec 13, 2022


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        total_nums = sorted(nums1 + nums2)
        
        if (((len(total_nums))% 2) == 0): 
            mid = ((len(total_nums)) / 2)
            return ((total_nums[mid] + total_nums[mid+1]) / 2)

        else: 
            mid = ((len(total_nums) + 1) / 2)
            return (total_nums[mid])






