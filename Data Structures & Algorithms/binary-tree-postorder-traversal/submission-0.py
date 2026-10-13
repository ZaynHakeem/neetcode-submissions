"""
Understand:
Input: root of a binary tree
Output: a list of node values in postorder traversal

Postorder means:
Left -> Right -> Node

Edge cases:
- Empty tree
- Single node
- Tree with only left children
- Tree with only right children

Match:
Use recursive DFS because postorder traversal requires us to fully traverse
the left subtree, then the right subtree, and visit the current node last.

Plan:
- If root is None, return an empty list
- Recursively get the postorder traversal of the left subtree
- Recursively get the postorder traversal of the right subtree
- Return the left subtree values first
- Then the right subtree values
- Then the current node value last
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        return left + right + [root.val]

"""
Time: O(n)
- Every node is visited once

Space: O(h)
- Recursive call stack depends on the height of the tree

I'm using recursive DFS. The base case returns an empty list for a null
node. Then I recursively get the postorder traversal of the left and right
subtrees. Since postorder is Left, Right, Node, I return the left result,
then the right result, and place the current node last.
"""