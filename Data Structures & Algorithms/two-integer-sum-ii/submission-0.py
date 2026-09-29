"""
Understand: Input: list of integers called nums, int called target
            Output: List of indexes that add up to target
            Edge Cases: Empty list. duplicates?, all the same number?
Match: Since the array is sorted, we can use a two pointer to compare elements
Plan: handle edge case if len(numbers) == 0, return []
      initiate a left pointer at 0 and a right pointer at len(nums) - 1
      we set current sum as left + right
      if current sum == target
      return [left + 1, right + 1] (Since its 1 indexed)
      if its less than target. left += 1
      if its greater. right -= 1
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            return []

        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        