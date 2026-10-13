"""
Understand:
Input: root of a binary tree
Output: the maximum depth of the tree

Depth means:
The number of nodes along the longest path from the root to a leaf

Edge cases:
- Empty tree
- Single node
- Tree with only one side

Match:
Use recursive DFS because we need to find the depth of the left and right
subtrees and use the deeper one.

Plan:
- If root is None, return 0
- Recursively find the depth of the left subtree
- Recursively find the depth of the right subtree
- Take the larger of the two depths
- Add 1 to count the current node
- Return the result

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)

"""
Time: O(n)
- Every node is visited once

Space: O(h)
- Recursion stack depends on the height of the tree

I'm using recursive DFS. If the current node is null, I return 0.
Otherwise, I get the maximum depth of the left and right subtrees,
take the larger one, and add 1 to count the current node.
"""
        