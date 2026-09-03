"""
Understand - Input: two strings; s & t
           - Output: true or false(boolean)
           - Edge Cases: Empty String
Match - We can use two frequency counters and then compare if they are equal to each other
Plan - We set up the two frequency counters 
     - We then compare if the two frequency counters are equal to each other
     - If yes, then it'll return True
     - Otherwise, it'll return False
I
R
E
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts1 = {}
        counts2 = {}

        for char in s:
            counts1[char] = counts1.get(char, 0) + 1

        for char in t:
            counts2[char] = counts2.get(char, 0) + 1

        return counts1 == counts2
        