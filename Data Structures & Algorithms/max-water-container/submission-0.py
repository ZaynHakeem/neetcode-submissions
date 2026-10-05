"""
Understand: Input: List of integers representing height
            Output: Area of largest amount of water that can be stored
            Edge cases: Same heights, Only one bar, No bars
Match: We can use a two pointer to calculate the width * height
Plan: We create a variable called biggest_area = 0
      We initialize a two pointer, left = 0 and right = len(height) - 1
      We then use a while loop to make sure left never overlaps with right
      we set height = min(height[left], height[right]))
      we see width = right - left
      we create a new varibale called current_area = height * width
      we then make biggest_area = max(biggest_area, current_area)
      if height[left] < height[right], we increase left by 1
      else we decrease right by 1
      return biggest area

"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left

            current_area = height * width
            biggest_area = max(biggest_area, current_area)

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

        return biggest_area