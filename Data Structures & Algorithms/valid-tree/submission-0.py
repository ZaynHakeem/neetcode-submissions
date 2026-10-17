"""
Understand: Input:number of nodes(n), an array of nodes and its neighbours(edges)
            Output: True or False(Boolean) of whther it is a valid tree
            Edge Cases: If it has cycles
                        If the starting node has no neighbours
                        Disconnected nodes
            Thinking process:
            We know that for an array to be a tree, it must have a root, all nodes in the array are connected as one component, there must be no cycles and there must be no outlier nodes that cant get access to the root.

Match: We can use a BFS to store the graph nodes and its neighbours. we also create a seen set and a stack, whose first value will be our "root". Then we run some checks, if we come accross a node and it is already in seen, that indicates that there is a cycle somewhere and we return False. 

Plan:   - Start traversal at node 0
        - Keep track of each node's parent
        - Add visited nodes to seen
        - For each neighbor:
            - skip it if it is the parent
            - if it has already been seen otherwise, we found a cycle
            - otherwise continue traversal
        - After traversal, check whether all n nodes were visited
"""

from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        group = defaultdict(list)

        for u, v in edges:
            group[u].append(v)
            group[v].append(u)

        seen = set()
        source = 0
        stack = [(source, -1)]
        seen.add(source)

        while stack:
            node, parent = stack.pop()

            for neighbour in group[node]:
                if neighbour == parent:
                    continue

                if neighbour in seen:
                    return False

                seen.add(neighbour)
                stack.append((neighbour, node))

        if len(seen) != n:
            return False

        return True