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
        