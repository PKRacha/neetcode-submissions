"""
Clarifying Questions:
1. Are the lists are always sorted?
2. What should we return if the input list is empty? Empty list
3. Can the number of lists (k) be zero? Yes

Corner Cases:
- Empty input array: lists = []
- Array containing empty lists = [[],[]]
- Array containing single list: = [[1,2,3]] -> Just return the list inside
- Lists with varying lengths and identical values. 

Brute-force approach:
- Collect all the nodes from all k lists into a single arrya
- sort the array
- create new linked list using the sorted array
- TC: O(n log n) SC: O(n)

Best Approach:
   - Min-Heap (Priority Queue).
   - Push the head of each of the k lists into the min-heap.
   - Pop the smallest node, add it to the result list, and push its next node into the heap.
   - Time: O(N log k). Space: O(k).

Logic Walkthrough (Using lists = [[1,4], [1,3]]):
   - Initial State: Heap = [(1, node1_1), (1, node2_1)]
   - Action 1: Pop (1, node1_1), result = 1, push node1_2 (val 4). Heap = [(1, node2_1), (4, node1_2)]
   - Action 2: Pop (1, node2_1), result = 1->1, push node2_2 (val 3). Heap = [(3, node2_2), (4, node1_2)]
   - Action 3: Pop (3, node2_2), result = 1->1->3. Heap = [(4, node1_2)]
   - Final Result: 1->1->3->4

Time and Space Complexity:
   - Time: O(N log k) where N is total nodes, k is number of lists.
   - Space: O(k) to store the heap elements.


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
        