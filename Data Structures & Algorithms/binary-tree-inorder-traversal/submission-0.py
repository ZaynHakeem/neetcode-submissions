'''
Understand:
Input: root of a binary tree
Output: a list of node values in inorder traversal

Inorder means:
Left -> Node -> Right

Edge cases:
- Empty tree
- Single node
- Tree with only left children
- Tree with only right children

Match:
Use DFS recursion because we need to fully traverse the left subtree,
then visit the current node, then traverse the right subtree.

Plan:
- If root is None, return an empty list
- Recursively get the inorder traversal of the left subtree
- Recursively get the inorder traversal of the right subtree
- Return:
    left subtree values
    + current node value
    + right subtree values
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right

"""
Time: O(n)
It is O(n) because we access each element once
Space: O(h)
It is O(h) because the amount of space we use is determined by the height of the tree
n = number of nodes
h = height of the tree
"""