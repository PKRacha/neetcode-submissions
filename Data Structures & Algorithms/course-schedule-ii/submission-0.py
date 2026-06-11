"""
1. Clarity questions and Real world scenario
   - Questions: Is it possible for prerequisites to have cycles? (Yes, if so, return empty list). 
     Are prerequisites always unique? (Assume yes).
   - Real World: Task scheduling systems, resolving software package dependencies, or 
     determining build orders in Makefiles/compilers.

2. Corner cases to consider
   - No prerequisites (any order is valid).
   - Impossible to complete (cycle exists).
   - Disconnected components (forest of graphs).

3. Brute force approach
   - Try all permutations of course sequences (O(V!)). Check each for validity 
     against prerequisites. Highly inefficient.

4. Best approach
   - Kahn's Algorithm (Topological Sort). Use indegree counts and a queue 
     to process courses as they become available.

5. Logic walk through
   numCourses = 3, prerequisites = [[1, 0]]
   [Initial State]
   indegree = [0, 1, 0]
   adj = {0: [1], 1: [], 2: []}
   queue = [0, 2]

   [Action 1: Pop 0]
   output = [0]
   adj[0] has 1, decrement indegree[1] -> 0
   queue = [2, 1]

   [Action 2: Pop 2, Pop 1]
   output = [0, 2, 1]
   [Final Result]
   [0, 2, 1]

6. Time and space complexity
   - Time: O(V + E) where V = courses, E = prerequisites.
   - Space: O(V + E) for adjacency list and indegree array.

7. Test cases
   - Input: numCourses = 2, prerequisites = [[1, 0]] -> Output: [0, 1]
   - Input: numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]] -> Output: [0, 1, 2, 3]
   - Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]] -> Output: []

8. Code
"""
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
            
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        output = []
        
        while queue:
            node = queue.popleft()
            output.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                    
        return output if len(output) == numCourses else []