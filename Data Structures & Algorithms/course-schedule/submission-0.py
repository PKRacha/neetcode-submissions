"""
1. Clarity & Real-world Scenario:
   - Clarity: Is the graph guaranteed to be directed? Yes (prerequisites). Is it possible for a cycle to exist? Yes, and that makes completion impossible.
   - Scenario: Dependency management in ETL workflow.

2. Corner Cases:
   - No prerequisites (numCourses = 1, prerequisites = []): Should return True.
   - Cycle exists (e.g., [[0, 1], [1, 0]]): Must return False.
   - Disconnected graph: Multiple components, must check all.
   - Single course with no dependency: Return True.

3. Brute Force Approach:
   - Try to perform a topological sort using Kahn's algorithm or DFS. If the number of sorted elements != numCourses, a cycle exists (return False).
   - Alternatively, check every possible ordering (O(N!)), which is inefficient.

4. Best Approach:
   - Use DFS with three states: 0 (unvisited), 1 (visiting/in current recursion stack), 2 (visited/safe).
   - If we encounter a node in state 1 during DFS, a cycle is detected.

5. Logic Walkthrough (Example: numCourses = 2, prerequisites = [[0, 1]]):
   Graph: 1 -> 0
   [Initial State]: adjacency_list = {0: [1], 1: []}, state = {0: 0, 1: 0}
   [Action 1]: Start DFS(0). Mark 0 as visiting (state 1).
   [Action 2]: Visit neighbor 1. Mark 1 as visiting (state 1). No neighbors for 1, mark 1 as visited (state 2).
   [Final Result]: Mark 0 as visited (state 2). No cycles found, return True.

6. Time and Space Complexity:
   - Time: O(V + E), where V is numCourses and E is number of prerequisites.
   - Space: O(V + E) to store the adjacency list and recursion stack/state array.

7. Test Cases:
   - Case 1: numCourses = 2, prerequisites = [[1, 0]] -> True
   - Case 2: numCourses = 2, prerequisites = [[1, 0], [0, 1]] -> False
   - Case 3: numCourses = 5, prerequisites = [[0, 1], [0, 2], [1, 3], [3, 4]] -> True

8. Code:
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        def has_cycle(node):
            if state[node] == 1: return True
            if state[node] == 2: return False
            
            state[node] = 1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            state[node] = 2
            return False
            
        for i in range(numCourses):
            if state[i] == 0:
                if has_cycle(i):
                    return False
        return True