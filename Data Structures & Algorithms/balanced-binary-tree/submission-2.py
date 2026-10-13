"""
Understand:
Input: root of a binary tree
Output: True if the tree is height-balanced, otherwise False

A tree is balanced if:
- For every node, the height difference between the left and right subtrees
  is no more than 1

Edge cases:
- Empty tree
- Single node
- One side much deeper than the other
- Root looks balanced but a deeper subtree is not

Match:
Use recursive DFS.

We need:
- a helper function to calculate subtree height
- the main isBalanced function to return True or False

Plan:
- Create a helper function height(node)
- If node is None, return 0
- Recursively calculate the left subtree height
- Recursively calculate the right subtree height
- Return 1 + the larger of the two heights

Then in isBalanced:
- If root is None, return True
- Get the left subtree height
- Get the right subtree height
- If their absolute difference is greater than 1, return False
- Otherwise recursively check that the left subtree is balanced
- Recursively check that the right subtree is balanced
- Return True only if both are balanced
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)

            return 1 + max(leftHeight, rightHeight)

        if root is None:
            return True

        leftHeight = height(root.left)
        rightHeight = height(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

"""
Time: O(n^2) worst case
- height can be recalculated many times

Space: O(h)
- recursion stack depends on tree height

I use a helper to calculate subtree heights because isBalanced needs to return a boolean, not a height. At each node, I compare the left and right subtree heights. If the difference is greater than 1, I return false. Otherwise, I recursively check that both subtrees are also balanced.
"""
        