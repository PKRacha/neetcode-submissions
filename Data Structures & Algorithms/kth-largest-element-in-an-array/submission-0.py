"""
1. Clarity & Real-world Scenario:
   - Clarity: Find the k-th largest element in an array of integers. Duplicates count as distinct positions.
   - Scenario: Real-time leaderboard systems, finding the top-k trending products in a list, or selecting top-k performers from a large dataset.

2. Corner Cases:
   - k=1: Return the maximum.
   - k=n: Return the minimum.
   - Array with all identical elements.
   - Array with negative numbers.

3. Brute Force Approach:
   - Sort the entire array in descending order and return the element at index k-1.
   - Time Complexity: O(n log n), Space: O(1) or O(n) depending on the sort implementation.

4. Best Approach:
   - Use a Min-Heap of size k. Iterate through the array; if the current element is larger than the heap's root (the current k-th largest), replace the root and heapify.
   - The root of the Min-Heap will be the k-th largest element at the end.

5. Logic Walkthrough:
   nums = [2, 3, 1, 5, 4], k = 2
   [Initialize Min-Heap with first k elements: [2, 3]]
   [Process 1: 1 < root(2), ignore]
   [Process 5: 5 > root(2), pop 2, push 5 -> Heap: [3, 5]]
   [Process 4: 4 > root(3), pop 3, push 4 -> Heap: [4, 5]]
   [Final Result: The heap contains [4, 5], root is 4]

6. Time and Space Complexity:
   - Time Complexity: O(n log k), where n is the number of elements.
   - Space Complexity: O(k) to store the heap.

7. Test Cases:
   - nums = [3, 2, 1, 5, 6, 4], k = 2 -> 5
   - nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4 -> 4

8. Code:
"""

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Create a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Iterate through the remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
        
        # The root of the min-heap is the kth largest element
        return min_heap[0]