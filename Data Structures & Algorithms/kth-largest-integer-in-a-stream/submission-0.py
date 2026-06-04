"""
1. Clarity Questions:
   - Is k always valid? (Constraint: 1 <= k <= length of stream).
   - Can the stream contain duplicate values? Yes.
   - Do we need to return the k-th largest after every single add operation? Yes.

2. Corner Cases:
   - Stream size initially equal to k.
   - Stream size initially less than k.
   - All elements in the stream are identical.
   - Adding a value smaller than all existing values.

3. Brute-force Approach:
   - Store all elements in a list.
   - Every time `add()` is called, sort the list and return the element at index `len(list) - k`.
   - Time: O(m * n log n) where n is stream size and m is number of calls.

4. Best Approach:
   - Use a Min-Heap of size k.
   - The heap will store the k largest elements seen so far.
   - The root of the heap (the smallest in the heap) will always be the k-th largest element.
   - Time: O(log k) per `add()` call. Space: O(k).

5. Logic Walkthrough (k=3, initial=[4, 5, 8, 2], add(3)):
   - Initial state: Heap = [2, 4, 8, 5] -> heapify to size 3 -> [4, 5, 8]
   - Action 1 (add 3): Push 3. Heap = [3, 4, 8, 5]
   - Action 2: Pop smallest (3). Heap = [4, 5, 8]
   - Final result: Heap root is 4.

6. Time and Space Complexity:
   - Time: O(N log k) for constructor, O(log k) per `add` call.
   - Space: O(k) to store the heap.

7. Test Cases:
   - Input: k=3, nums=[4, 5, 8, 2], adds=[3, 5, 10, 9, 4]
   - Output: [4, 5, 5, 8, 8]

8. Code:
"""
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]