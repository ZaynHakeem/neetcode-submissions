"""
UNDERSTAND - Input: A list of integers `nums` and an integer `k`
           - Output: A list containing the `k` most frequent elements in `nums`
           - Example:
             nums = [1,1,1,2,2,3], k = 2
             Output = [1,2]
           - Edge Cases: One unique element, Duplicate elements, k = 1, k equals the number of unique elements

M - MATCH
- Pattern: Hashmap / Frequency Map + Sorting
- Key Insight:
  First count how often each number appears.
  Then sort the unique numbers by their frequency from highest to lowest.

P - PLAN
1. Create an empty hashmap called `count`.
2. Loop through `nums`.
3. Store each number's frequency in `count`.
4. Sort the keys in `count` based on their frequency:
   `count[num]`
5. Use `reverse=True` so the most frequent numbers come first.
6. Return the first `k` elements using `[:k]`.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_nums = sorted(count, key = lambda num: count[num], reverse = True)
        return sorted_nums[:k]