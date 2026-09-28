"""
Understand: Input: A list of integers calleed nums
            Output: length of longest consecutive nums
            Edge case: Empty list, duplicates, neg nums, all values the same
Match: We can use a two pointer to compare the numbers
Plan: Initiate a left pointer and right pointer
      initiate longest = 1, current_longest = 1
      if right is one number greater than left
      current_longest += 1
      else current_longest = 1 
      we then set longest as the max between (longest, current_longest)
      we then move left = right and right += 1
      we then return longest
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        left = 0
        right = 1
        current_longest = 1
        longest = 1

        while right < len(nums):
            if nums[right] == nums[left]:
                right += 1
                continue

            if nums[right] == nums[left] + 1:
                current_longest += 1
            else:
                current_longest = 1

            longest = max(longest, current_longest)

            left = right
            right += 1

        return longest