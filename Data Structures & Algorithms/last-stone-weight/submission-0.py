"""
/*
1. CLARITY & REAL-WORLD SCENARIO
Clarity: Are stone weights always positive integers? Yes (1 to 100).
Real-world: This algorithm models resource depletion or competitive systems where the two largest items (or entities) interact until one or none remains, common in load-balancing tasks or game development mechanics.

2. CORNER CASES
- Single stone: The loop shouldn't execute; return the single weight.
- All stones equal: Final result should be 0.
- Empty input: Handled as 0.

3. BRUTE FORCE APPROACH
In each iteration, sort the array to find the two largest stones. Smash them, update the array, and repeat.
Time Complexity: O(n^2 log n) due to sorting in every iteration.

4. BEST APPROACH
Use a Max-Heap. Since Python's heapq is a Min-Heap, store negative weights to simulate a Max-Heap. This allows extracting the two largest elements in O(log n) time per step.

5. LOGIC WALKTHROUGH
stones = [2, 3, 6, 2, 4]
[Initial State: Max-Heap = [-6, -4, -3, -2, -2]]
[Action 1: Pop 6 and 4. Smash: 6 - 4 = 2. Push 2. Heap = [-3, -2, -2, -2]]
[Action 2: Pop 3 and 2. Smash: 3 - 2 = 1. Push 1. Heap = [-2, -2, -1]]
[Action 3: Pop 2 and 2. Smash: 2 - 2 = 0. Push nothing. Heap = [-1]]
[Final result: 1]

6. TIME AND SPACE COMPLEXITY
Time: O(n log n) - where n is number of stones.
Space: O(n) - to store stones in the heap.

7. TEST CASES
- [2, 7, 4, 1, 8, 1] -> Output: 1
- [1] -> Output: 1
- [2, 2] -> Output: 0

8. CODE
*/
"""
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate to simulate max-heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Pop max 2 
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            # Push the difference if not 0.
            if x != y:
                heapq.heappush(max_heap, -(y - x))
                
        return -max_heap[0] if max_heap else 0


"""
# stones[i] 
# 2 heaviest stones, smash
#     larger - smaller => will remain. 

# [2,3,6,2,4]
# i = 1 : 6-4 = 2 => [2,3,2,2] 
# i = 2 : 3 - 2 = 1 => [1,2,2] 
# i = 3 : 2 - 2 = 0 => [1] 

# Q's:
# 1. Can stones array empty? NO
# 2. we will return the interger and not list? yes
# 3. What is single number in the list? Just return

# Solution:
# 1. we can nested loop and outside loop will check for the len(stones)
#     in the loop, we can sort and find the 2 on top 
#         and then abs(x-y) will be in first number and remove 2nd number
#     TC: O(n * nlogn) and SC: O(1)

# 2. Heap approach: 
#     create the heap and then b/c Python is min Heap, 
#         Info: we will use negative numbers to make it max Heap
#         B/c is max heap, we will pick latest 2 numbers and subtrack them.
#     TC: O(n log n) and SC: O(n)

# Test cases:


"""
        