"""
Understand: Input: two strings called s and t
            Output: Boolean (True or False) of whether s is subsequence of t
            Edge cases: Imperfect sequence, empty strs

Match: We can use a two pointer. With one pointer on the beginning of s and the other pointer at the beginning of s

Plan: Place pointer1 at the beginning of s
      Place pointer2 at the beginning of t
      if pointer1 == pointer2, increase pointer1 and pointer2 by 1
      if pointer1 != pointer2, just increase pointer2 by 1
      if pointer1 reaches the end of the str, return True
      else if pointer2 reaches the end and pointer1 doesnt, return False
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer1 = 0
        pointer2 = 0

        while pointer1 < len(s) and pointer2 < len(t):
            if s[pointer1] == t[pointer2]:
                pointer1 += 1

            pointer2 += 1

        if pointer1 == len(s):
            return True
        else:
            return False

"""
Time is O(n) because we scan through t once. 
Space is O(1) because we only use two pointers and no extra data structure that grows with the input.
"""
    

            



        