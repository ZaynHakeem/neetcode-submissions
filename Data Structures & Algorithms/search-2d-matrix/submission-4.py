"""
Understand:
Input: A 2D matrix and an integer target
Output: True if target exists in the matrix, otherwise False

Assumptions:
- Each row is sorted
- The first value of each row is greater than the last value of the previous row
- Therefore, the whole matrix can be treated like one sorted list

Edge Cases:
- Target is not in matrix
- Target is first or last value
- Matrix has one row or one column


Match:
Because the matrix is globally sorted and we need O(log(m * n)) time,
we can use Binary Search.

We do not actually flatten the matrix.
Instead, we pretend it is one long array and convert each middle index
back into a row and column.


Plan:
- Find the number of rows m and columns n
- m = len(nums) which will give us the number of rows (or lists within the list)
- n = len(nums[0]) which will give us the number of items in the first list
- m * n gives us the total number of elements in the list
- Treat the matrix as having indexes from 0 to (m * n) - 1
- Set left at the first imaginary index and right at the last

- While left <= right:
    - Find the middle index
    - Convert the middle index into:
        row = mid // n
        column = mid % n
    - Get the matrix value at that row and column

    - If the value equals target:
        return True

    - If the value is smaller than target:
        discard the left half and search the right half

    - If the value is larger than target:
        discard the right half and search the left half

- If the search finishes without finding target:
    return False

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = (m * n) - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False