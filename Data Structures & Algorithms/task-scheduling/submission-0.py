"""
1. CLARITY & REAL-WORLD SCENARIO
Clarity:
- Can idle cycles be placed anywhere? Yes, they are placeholders.
- Do tasks have to be performed in the input order? No, order is flexible.
Real-World:
- CPU scheduling of processes with dependency/cooldown constraints.
- Manufacturing line scheduling where specific tools need cool-down time after intense use.

2. CORNER CASES
- n = 0: No cooldown, result is simply len(tasks).
- All tasks are the same: Result is (count - 1) * (n + 1) + 1.
- No idle time needed: Result is len(tasks).

3. BRUTE-FORCE APPROACH
- Generate all possible permutations of tasks.
- Validate if each permutation satisfies the 'n' cooldown constraint.
- Keep track of the minimum length among all valid permutations.
- Complexity: O(m!), highly inefficient for m=1000.

4. BEST APPROACH
- Greedy approach using a Max-Heap to always pick the most frequent task available.
- Use a queue to track tasks currently in the cooldown period.
- Time Complexity: O(m), where m is the number of tasks.
- Space Complexity: O(1) (limited to 26 uppercase English characters).

5. LOGIC WALK-THROUGH
tasks = ["A", "A", "A", "B"], n = 2
[Initial State] Heap: [('A', 3), ('B', 1)], Queue: [], Time: 0
[Action 1] Pop 'A', Time: 1, Queue: [('A', 2, time_ready: 4)]
[Action 2] Pop 'B', Time: 2, Queue: [('A', 2, 4), ('B', 0, 5)]
[Action 3] Heap empty, Idle, Time: 3
[Action 4] Queue 'A' ready, push to Heap, Time: 4, Heap: [('A', 2)]
[Action 5] Pop 'A', Time: 5... and so on.
[Final Result] 7

6. COMPLEXITY
- Time: O(m) where m is the number of tasks.
- Space: O(1) as we store at most 26 tasks in the heap/queue.

7. TEST CASES
- Input: ["A","A","A","B","C"], n = 3, Output: 9
- Input: ["X","X","Y","Y"], n = 2, Output: 5
- Input: ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2, Output: 16

8. CODE
"""
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        
        time = 0
        q = deque()  # pairs of [-cnt, available_time]
        
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time