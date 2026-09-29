"""
Understand: Input: a string called s
            Output: Boolean of true or false
            Edge cases: Empty string, single element, numbers
Match: We can use a two pointer to compare letters from both ends
Plan: we first check get the list isalpha
      we then do list.join to get rid of the spaces
      we then initiate the two pointer
      one pointer at the beginning and the other at the end 
      if left == right, left +=1. right -=1
      if it finishes we return true
      else we return false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
      if len(s) == 0:
            return False
      
      letters = []

      for char in s:
            if char.isalnum():
                  letters.append(char.lower())

      s = "".join(letters)

      left = 0
      right = len(s) - 1

      while left < right:
            if s[left] != s[right]:
                  return False
            left += 1
            right -= 1

      return True
        