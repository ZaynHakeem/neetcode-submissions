"""
Understand:
Input:
- n = number of nodes
- edges = undirected connections between nodes

Output:
- True if the graph forms a valid tree
- False otherwise

A valid tree must:
- Have exactly n - 1 edges
- Be fully connected

Edge cases:
- Too many edges
- Too few edges
- Disconnected nodes
- Single node

Match:
Use DFS with a stack.

We first use the tree rule:
A tree with n nodes must have exactly n - 1 edges.

Then we use DFS to check whether all nodes are connected.

Plan:
- If the number of edges is not n - 1, return False
- Build an adjacency list
- Because the graph is undirected:
    - add v to u's neighbors
    - add u to v's neighbors
- Create a seen set
- Start DFS from node 0
- Add node 0 to the stack and seen
- While the stack is not empty:
    - pop a node
    - loop through its neighbors
    - if a neighbor has not been seen:
        - add it to seen
        - add it to the stack
- After DFS finishes:
    - if len(seen) == n, all nodes are connected -> True
    - otherwise -> False
"""

from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        group = defaultdict(list)

        for u, v in edges:
            group[u].append(v)
            group[v].append(u)

        seen = {0}
        stack = [0]

        while stack:
            node = stack.pop()

            for neighbour in group[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append((neighbour))

        if len(seen) == n:
            return True

        return False
