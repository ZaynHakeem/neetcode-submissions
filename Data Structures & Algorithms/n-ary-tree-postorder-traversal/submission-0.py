"""
If we reach a null node, we return an empty list. We create an empty list called result to store the postorder values for the current subtree. We then loop through each child of the current node from left to right. For each child, we recursively call postorder(child), which completely processes that child’s subtree before moving to the next child. We add the returned values to result. After all children have been processed, we add the current node’s value last. This gives us postorder because all children are visited before the parent.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = []

        for child in root.children:
            result += self.postorder(child)

        result.append(root.val)

        return result

"""
Time is O(n), because every node is visited once.
n = number of nodes in the tree.
Space is O(h) for the recursion stack.
h = height of the tree.
"""