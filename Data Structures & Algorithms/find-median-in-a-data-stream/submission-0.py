"""
1. CLARITY & REAL-WORLD SCENARIO
Clarity:
- Can we add numbers indefinitely? Yes, until memory limits.
- What if the number of elements is odd? Median is the middle element.
- What if the number of elements is even? Median is the average of the two middle elements.
Real-World:
- Real-time analytics (e.g., streaming stock prices, sensor data) where you need to track the median value as data arrives.

2. CORNER CASES
- Adding only one element: Median is that element.
- Adding two elements: Median is the average.
- Stream with identical values: Heap handles duplicates correctly.

3. BRUTE-FORCE APPROACH
- Maintain a list of all numbers.
- On findMedian(), sort the entire list and pick the middle.
- Complexity: O(N log N) per findMedian() call.

4. BEST APPROACH
- Use two heaps:
  - Max-Heap (left half) to store smaller numbers.
  - Min-Heap (right half) to store larger numbers.
- Keep the size difference between heaps at most 1.
- Time: O(log N) for addNum(), O(1) for findMedian().
- Space: O(N) to store all elements.

5. LOGIC WALK-THROUGH
num = [1, 3, 2]
[Initial State] MaxHeap: [], MinHeap: []
[addNum(1)] MaxHeap: [-1], MinHeap: []
[addNum(3)] MaxHeap: [-1], MinHeap: [3]
[addNum(2)] MaxHeap: [-2, -1], MinHeap: [3] -> Rebalance -> MaxHeap: [-1], MinHeap: [2, 3]
[Final Result] findMedian() = (1 + 2) / 2 = 1.5

6. COMPLEXITY
- Time: O(log N) for insertion, O(1) for retrieval.
- Space: O(N) to store the data stream.

7. TEST CASES
- Input: add(1), add(2), find(), add(3), find() -> Output: 1.5, 2.0
- Input: add(-1), add(-2), add(-3) -> Output: -2.0

8. CODE
"""
import heapq

class MedianFinder:
    def __init__(self):
        self.small = [] # Max-heap (invert values)
        self.large = [] # Min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large): return -self.small[0]
        if len(self.large) > len(self.small): return self.large[0]
        return (-self.small[0] + self.large[0]) / 2
