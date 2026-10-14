'''
Understand:
Input: root of a binary tree
Output: a list of lists where each inner list contains the values at one level

Edge cases:
- Empty tree
- Single node
- Tree with only one side

Match:
Use BFS because the problem wants us to process the tree level by level.

BFS uses a queue:
First In, First Out

Plan:
- If root is None, return []
- Put the root into a queue
- Create an empty result list
- While the queue is not empty:
    - Create an empty list for the current level
    - Use len(queue) to know how many nodes are currently in this level
    - Process exactly that many nodes
    - Remove each node from the front of the queue
    - Add its value to the current level
    - If it has a left child, add it to the queue
    - If it has a right child, add it to the queue
    - After finishing the level, add the level list to result
- Return result
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:

            level = []

            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

"""
Time: O(n)
- Every node is processed once

Space: O(n)
- The queue can hold many nodes at once
"""
            