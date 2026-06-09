"""
1. Clarity Questions & Real-World Scenario
- Clarity: Is the graph connected? (Yes). Can there be cycles? (Yes). Are node values unique? (Yes).
- Scenario: Used in networking to create a snapshot of a distributed system or in social media to replicate a user's connection network for a recommendation engine.

2. Corner Cases
- Empty graph (node is null): Return None.
- Single node graph: Return a new node with the same value and no neighbors.
- Graph with cycles: Must use a hash map to track visited/cloned nodes to avoid infinite recursion.

3. Brute Force Approach
- Traverse the graph to collect all nodes. Create new nodes for every unique value found. Then, iterate through the original nodes' adjacency lists to link the corresponding cloned nodes.
- Time: O(V + E). Space: O(V).

4. Best Approach
- DFS with Hash Map: Traverse the graph recursively. The hash map stores `{original_node: cloned_node}`. If a node is already in the map, return it immediately; otherwise, create a clone, add it to the map, and recursively clone its neighbors.
- Time: O(V + E). Space: O(V).

5. Logic Walkthrough (Example: Node 1 -> 2, Node 2 -> 1, 3)
node = 1
[Initial state: Map = {}, DFS(1)]
[Action 1: Clone 1. Map = {1: Clone1}. Neighbors of 1 is [2]. Call DFS(2)]
[Action 2: Clone 2. Map = {1: Clone1, 2: Clone2}. Neighbors of 2 is [1, 3]. DFS(1) returns Clone1. DFS(3) clones 3.]
[Final result/Update: Return Clone1, where Clone1.neighbors = [Clone2]]

6. Time and Space Complexity
- Time: O(V + E) where V is vertices and E is edges.
- Space: O(V) to store the hash map and recursion stack.

7. Test Cases
- Input: [[2,4],[1,3],[2,4],[1,3]] -> Output: [[2,4],[1,3],[2,4],[1,3]]
- Input: [[]] -> Output: [[]]
- Input: [] -> Output: []

8. Code
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        cloned = {}
        
        def dfs(curr):
            if curr in cloned:
                return cloned[curr]
            
            copy = Node(curr.val)
            cloned[curr] = copy
            
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)