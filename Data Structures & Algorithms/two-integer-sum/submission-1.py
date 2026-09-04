'''
Understand - Input: list integers called nums and an integr called target
           - Output: List of indeces of two numbers in nums that add up to target
           - Edge cases: There are no values that add up to target
                         Empty list
Match - Use hashmap and the enumerate function
Plan - Create a hashmap called seen made up of the integers in nums
     - use the enumerate function to put nums in the form of i(index) and num(value)
     - we see if the result of target - num is in the hashmap
     - if yes, we return i and and the results index
     - we then add that new key and value into the hashmap
     - else if no pair is found, we return []
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        return []