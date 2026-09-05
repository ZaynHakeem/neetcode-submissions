"""
U - UNDERSTAND
- Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
- Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
- Constraints: 1 <= strs.length <= 10^4, 0 <= strs[i].length <= 100
- Assumptions: All inputs consist of lowercase English letters.
- Edge Cases: strs = [""] -> [[""]], strs = ["a"] -> [["a"]]

M - MATCH
- Pattern: Hash Map (Dictionary)
- Key Insight: Anagrams contain the identical characters. Sorting any
  anagram produces the exact same signature string (e.g., "eat" -> "aet").

P - PLAN
1. Initialize an empty dictionary: `groups = {}`
2. Iterate through each string `word` in `strs`:
   a. Create the canonical key by sorting characters: "".join(sorted(word))
   b. If `key` exists in `groups`, append `word` to `groups[key]`
   c. If `key` does not exist, create a new entry: `groups[key] = [word]`
3. Return `list(groups.values())`
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())