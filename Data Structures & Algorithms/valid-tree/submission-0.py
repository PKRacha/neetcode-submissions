"""
1. Clarity Questions & Real-World Scenario
- Clarity: Is the graph undirected? (Yes, as per prompt). Does a valid tree require all nodes to be connected? (Yes, it must be a single component with no cycles).
- Scenario: Network topology design to ensure a set of servers is connected without redundant loops, or in project dependency management to ensure tasks form a clean hierarchy without circular references.

2. Corner Cases
- Empty graph: (n=1, edges=[]) is a valid tree.
- Disconnected graph: If nodes are 5 but only 3 are reachable, return false.
- Cycle: If edges count >= n, a cycle must exist.

3. Brute Force Approach
- Use Disjoint Set Union (DSU) to add edges one by one. If two nodes already belong to the same set, a cycle exists. Finally, check if the number of disjoint sets is 1.
- Time: O(E * alpha(V)). Space: O(V).

4. Best Approach
- DFS/BFS Traversal: Check two conditions:
    1. Edge count must be exactly `n - 1`.
    2. The graph must be fully connected (all nodes reachable from node 0).
- Time: O(V + E). Space: O(V + E).

5. Logic Walkthrough (Example: n=5, edges=[[0,1],[0,2],[0,3],[1,4]])
n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
[Initial: Adjacency list built. Set 'visited' = {}.]
[Action 1: Start DFS(0). Mark 0 visited. Visit neighbors 1, 2, 3.]
[Action 2: Continue DFS to 4. All nodes {0, 1, 2, 3, 4} now in 'visited'.]
[Final Result: len(visited) == 5, edges == 4. Return True.]

6. Time and Space Complexity
- Time: O(V + E)
- Space: O(V + E)

7. Test Cases
- Input: n=5, [[0,1],[0,2],[0,3],[1,4]] -> True
- Input: n=5, [[0,1],[1,2],[2,3],[1,3],[1,4]] -> False
- Input: n=1, [] -> True

8. Code
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
        
        dfs(0)
        return len(visited) == n