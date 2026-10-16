"""
Understand: Input: an integer n, that represents the number of nodes
                   an array called edges that represents node and their neighbours

            Output: Number of components
            Edge cases: a source with no neighbours
                        a single component
                        too many components

Match: We can use a DFS algorithm to traverse through edges. We then add a source and its neighbours into a dictionary and a seen set. If theres still nodes that arent yet accounted for, that means it wasnt a part of the previous source and is a new component

Plan: from collections import defaultdict
      we then create a group dictionary
      for u,v in edges:
        group[u].append(v)
        group[v].append(u)
      we then create a seen set
      we then loop node in the range n
      if the node is not in seen, then it must be a new component
      component += 1
      stack = [node]
      seen.add(node)
      while stack
      current_node = stack.pop()
      for neighbour in group[current]:
        if neighbour not in seen
        seen.add(neighbour)
        stack.append(neighbour)
      we then return components


      
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict

        group = defaultdict(list)

        for u,v in edges:
            group[u].append(v)
            group[v].append(u)

        seen = set()
        components = 0

        for node in range(n):
            if node not in seen:
                components += 1

                stack = [node]
                seen.add(node)

                while stack:
                    current_node = stack.pop()
                    print(current_node)
                    for neighbour in group[current_node]:
                        if neighbour not in seen:
                            seen.add(neighbour)
                            stack.append(neighbour)

        return components

"""
Time is O(V + E) because we visit every node once, and we look through every edge when checking neighbors.
Space is O(V + E) because the adjacency list stores all nodes and edges, and seen + the stack can hold up to O(V) nodes.
"""
        