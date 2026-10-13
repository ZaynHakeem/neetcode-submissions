"""
Understand:
Input: root of a binary tree
Output: a list of node values in preorder traversal

Preorder means:
Node -> Left -> Right

Edge cases:
- Empty tree
- Single node
- Tree with only left children
- Tree with only right children

Match:
Use recursive DFS because preorder traversal requires us to visit the
current node, then recursively traverse the left subtree, then the right subtree.

Plan:
- If root is None, return an empty list
- Recursively get the preorder traversal of the left subtree
- Recursively get the preorder traversal of the right subtree
- Return the current node first, followed by the left subtree values,
  then the right subtree values
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return [root.val] + left + right

"""
Time: O(n)
- Every node is visited once

Space: O(h)
- Recursive call stack depends on the height of the tree

I'm using recursive DFS. The base case handles a null node by returning
an empty list. Then I recursively get the preorder traversal of the left
and right subtrees. Since preorder is Node, Left, Right, I return the
current node first, followed by the left and right subtree results.
"""