"""
Understand:
Input: A string of parentheses/brackets
Output: True if every bracket is correctly matched and ordered, otherwise False

Edge cases:
- Empty string
- Closing bracket before an opening bracket
- Only one bracket
- Extra opening brackets
- Wrong nesting, e.g. "([)]"

Match:
Use a stack because each closing bracket must match the most recent unmatched opening bracket.
Use a hashmap to map each closing bracket to the opening bracket it expects.

Plan:
- Create an empty stack
- Create a hashmap:
      ")" -> "("
      "]" -> "["
      "}" -> "{"

- Loop through each character in s

- If the character is an opening bracket:
      push it onto the stack

- Otherwise, it is a closing bracket:
      if the stack is empty:
          return False

      if the top of the stack is not the opening bracket
      required by this closing bracket:
          return False

      otherwise:
          pop the matching opening bracket

- At the end, return True only if the stack is empty
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        group = {"}":"{",
                 ")":"(",
                 "]":"["
        }
        
        for char in s:
            if char in "{[(":
                stack.append(char)

            else:
                if not stack:
                    return False

                if stack[-1] != group[char]:
                    return False

                stack.pop()

        return len(stack) == 0