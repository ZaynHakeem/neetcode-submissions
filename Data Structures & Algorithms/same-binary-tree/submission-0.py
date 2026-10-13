"""
Understand:
Input: roots of two binary trees, p and q
Output: True if both trees are exactly the same, otherwise False

The trees are the same if:
- They have the same structure
- Corresponding nodes have the same values

Edge cases:
- Both trees are empty
- One tree is empty and the other is not
- Same values but different structure
- Same structure but different values

Match:
Use recursive DFS to compare both trees at the same time.

Plan:
- If p and q are both None, return True
- If only one of them is None, return False
- If p.val is not equal to q.val, return False
- Recursively compare p.left with q.left
- Recursively compare p.right with q.right
- If both left and right sides match, return True
- Otherwise return False
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        if left_same == True and right_same == True:
            return True
        else:
            return False

"""
Time: O(n)
- We compare each node once

Space: O(h)
- Recursion stack depends on tree height
"""
        