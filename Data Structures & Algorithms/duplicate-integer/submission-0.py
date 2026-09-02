"""
Understand: Input - List of integers nums
            Output - true or false (boolean)
            Edge cases - empty string
Match: We can use a set to compare if its length is eqaul to the original array
Plan: i) Use the set function to create a set of unique characters
     ii) If the len of the set is equal to the len of the array, we print false
    iii) Else we print true
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       return len(set(nums)) != len(nums)
        