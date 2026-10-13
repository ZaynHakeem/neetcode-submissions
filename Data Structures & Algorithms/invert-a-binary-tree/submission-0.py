"""
Understand:
Input: root of a binary tree
Output: the same tree with every node's left and right children swapped

Edge cases:
- Empty tree
- Single node
- Tree with only one child on some nodes

Match:
Use recursive DFS because we need to perform the same swap operation
on every node in the tree.

Plan:
- If root is None, return None
- Swap root.left and root.right
- Recursively invert the left subtree
- Recursively invert the right subtree
- Return root

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

"""
Time: O(n)
- Every node is visited once

Space: O(h)
- The recursion stack depends on the height of the tree

I'm using recursive DFS. For each node, I first swap its left and right
children. Then I recursively perform the same operation on both subtrees.
The base case handles a null node, and after the whole tree is processed,
I return the root.
"""
        