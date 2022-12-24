#1 . Two Sum
# https://leetcode.com/problems/two-sum/

# Ajlal F. Paracha - Dec 13, 2022


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # We store the Number: Index
        nums_seen = {}

        for i in range(len(nums)):

            num_needed = target - nums[i]
            # If same number
            if nums[i] == num_needed: pass
            elif num_needed in nums_seen: 
                return [i, nums_seen[num_needed]]
            else: 
                nums_seen[nums[i]] = i
            
