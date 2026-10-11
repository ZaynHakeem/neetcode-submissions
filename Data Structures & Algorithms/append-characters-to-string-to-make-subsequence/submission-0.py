"""
Understand: Input: string s and string t
            Output: Number of letters needed to be added from to to s to make t a subsequence of s
            edge cases: Already subsequence, empty string

Match: We can use a two pointer. With one pointer on the beginning of s and the other pointer at the beginning of t

Plan: Place pointer1 at the beginning of s
      Place pointer2 at the beginning of t
      if pointer1 == pointer2, increase pointer1 and pointer2 by 1
      if pointer1 != pointer2, just increase pointer2 by 1
      if pointer1 reaches the end of the str, return the length of the spliced t on where its pointer ended
"""
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer1 = 0
        pointer2 = 0

        while pointer1 < len(s) and pointer2 < len(t):
            if s[pointer1] == t[pointer2]:
                pointer2 += 1

            pointer1 += 1

        return len(t[pointer2:])
        