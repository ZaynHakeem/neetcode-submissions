"""
Understand - Input: a list of integers called nums
           - Output: Boolean(true/false)
           - Edge cases: Empty list, list of letters
Match - We can use a frequency hashmap and see if any counts are higher than 1
Plan - Set up the frequency map
     - After adding all items from nums in freqmaps
     - If any of the values are > 1, we return True
     - Else we return false
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for i in freq.values():
            if i > 1:
                return True

        return False

        