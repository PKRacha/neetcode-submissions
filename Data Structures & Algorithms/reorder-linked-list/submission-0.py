"""
1. Clarity questions
   - Can the list be empty or contain one node? Yes, constraints state length >= 1.
   - Do I need to modify node values? No, pointers must be adjusted in-place.

2. Corner cases to consider
   - Single node list: No action required.
   - Two-node list: No action required.

3. Brute force Approach
   - Copy all nodes into an array.
   - Use two pointers (left and right) on the array to reassign 'next' pointers.
   - Space: O(n).

4. Best Approach
   - Use three-step linked list manipulation:
     1. Find middle: Use slow/fast pointers.
     2. Reverse second half: Standard linked list reversal.
     3. Merge: Interleave nodes from first and second halves.
   - Space: O(1).

5. Logic walk through
   head = [1, 2, 3, 4]
   [Initial: slow=1, fast=1]
   [Find middle: slow moves to 2, fast moves to 4; split into [1, 2] and [3, 4]]
   [Reverse second half: [3, 4] becomes [4, 3]]
   [Merge: 1 -> 4 -> 2 -> 3]
   [Final result: [1, 4, 2, 3]]

6. Time and space complexity
   - Time: O(n)
   - Space: O(1)

7. Code
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return
        
        # 1. Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # 3. Merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
