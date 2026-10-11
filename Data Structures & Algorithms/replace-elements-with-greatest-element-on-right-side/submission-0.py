"""
Understand:
Input: An integer array arr
Output: The same array where each element is replaced by the greatest
        element to its right, and the last element becomes -1

Edge cases:
- One element
- Already decreasing array
- Repeated values

Match:
We can traverse the array from right to left while keeping track of the
largest value seen so far.

Plan:
- Set max_num = -1
- Loop through arr from the last index to the first
- Save the current value before replacing it
- Replace arr[i] with max_num
- Update max_num to the larger of:
    - the old max_num
    - the saved current value
- Return arr

"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = -1

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_num
            max_num = max(max_num, current)

        return arr
        