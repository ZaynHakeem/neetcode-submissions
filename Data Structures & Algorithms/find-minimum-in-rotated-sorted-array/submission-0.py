"""
Understand:
Input: Rotated sorted array
Output: Minimum value

Match:
Use binary search because one side of the array is still sorted,
and the minimum is at the rotation point.

Plan:
- Set left and right to the ends of the array
- While left < right:
    - Find mid
    - Compare nums[mid] with nums[right]

    - If nums[mid] > nums[right]:
        minimum must be to the right
        move left to mid + 1

    - Otherwise:
        minimum is at mid or to the left
        move right to mid

- When left == right, return nums[left]

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid
        
        return nums[left]

        
        