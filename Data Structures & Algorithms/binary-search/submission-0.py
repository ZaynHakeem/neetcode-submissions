'''
Understand:
Input: sorted array and target
Output: index of target, or -1 if not found

Match:
Sorted array + searching for a value → Binary Search

Plan:
- Since the array is sorted, we can repeatedly cut the search area in half.

- Start by considering the entire array.

- Find the value in the middle of the current search area.

- If the middle value is the target, we are done.

- If the middle value is smaller than the target, then everything to the left of the middle can be ignored because those values are even smaller.
  We continue searching only the right half.

- If the middle value is larger than the target, then everything to the right of the middle can be ignored because those values are even larger.
  We continue searching only the left half.

- Keep repeating this until:
    - we find the target, or
    - there is no search area left.

- If the target is never found, return -1.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) //2 
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1

'''
Time: O(log n)
The reason it’s O(log n) is that every comparison removes half of the remaining array.
Space: O(1)
Space complexity is O(1) because no additional space that grows with the input size is needed.
'''
