"""
1. CLARITY & REAL-WORLD SCENARIO
Clarity:
- Distance is Euclidean: sqrt((x1-x2)^2 + (y1-y2)^2).
- Origin is (0,0).
- Order of output does not matter.
Real-World:
- Location-based services: Finding the K nearest points of interest (restaurants, gas stations) relative to a user's current GPS coordinate.

2. CORNER CASES
- k = 1: Return the single closest point.
- k = points.length: Return all points.
- Points with identical distances: Any set of K points with the smallest distances is valid.

3. BRUTE-FORCE APPROACH
- Calculate the distance of all points from (0,0).
- Sort the entire list of points based on these distances.
- Return the first K elements.
- Time Complexity: O(n log n).

4. BEST APPROACH
- Use a Max-Heap to maintain the K closest points found so far.
- Iterate through the points:
  - Add point to heap (store as negative distance to simulate Max-Heap with Python's Min-Heap).
  - If heap size > k, remove the largest distance element.
- Time Complexity: O(n log k).
- Space Complexity: O(k).

5. LOGIC WALK-THROUGH
points = [[3,3],[5,-1],[-2,4]], k = 2
[Initial state] Heap: [], Distances squared: [18, 26, 20]
[Action 1] Process [3,3]: Heap = [[-18, 3, 3]]
[Action 2] Process [5,-1]: Heap = [[-26, 5, -1], [-18, 3, 3]]
[Action 3] Process [-2,4]: Heap = [[-26, 5, -1], [-18, 3, 3], [-20, -2, 4]] -> Pop max: [-26, 5, -1]
[Final result] [[3,3], [-2,4]]

6. TIME AND SPACE COMPLEXITY
- Time: O(n log k), where n is the number of points.
- Space: O(k) to store the heap elements.

7. TEST CASES
- Input: [[1,3],[-2,2]], k = 1 | Output: [[-2,1]]
- Input: [[3,3],[5,-1],[-2,4]], k = 2 | Output: [[3,3],[-2,4]]

8. CODE
"""
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        for x, y in points:
            dist = -(x**2 + y**2)
            if len(max_heap) == k:
                heapq.heappushpop(max_heap, (dist, x, y))
            else:
                heapq.heappush(max_heap, (dist, x, y))
        
        return [[x, y] for (dist, x, y) in max_heap]
