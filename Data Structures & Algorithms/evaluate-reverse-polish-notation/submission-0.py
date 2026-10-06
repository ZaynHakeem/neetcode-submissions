"""
Understand:
Input: List of strings representing numbers and operators in RPN
Output: Integer result
Edge cases: Negative numbers, single number

Match:
Use a stack because operators use the two most recent numbers.

Plan:
- Create empty stack
- Loop through tokens
- If token is a number, convert to int and push it
- If token is an operator:
    a = pop()
    b = pop()
    calculate b operator a
    push result
- Return the final value in the stack

"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token in ["+", "-", "/", "*"]:
                a = stack.pop()
                b = stack.pop()

                if token == "+":
                    new_num = b + a
                elif token == "-":
                    new_num = b - a
                elif token == "*":
                    new_num = b * a
                else:
                    new_num = int(b / a)

                stack.append(new_num)

            else:
                stack.append(int(token))

        return stack[0]

"This solution is O(n) time becasue we access each token once, and it is O(n) space because at worst, the stack can be filled with numbers before they are operated on"

        