"""
1. Clarity questions
   - Is n guaranteed to be valid (1 <= n <= length of list)? Yes.
   - Can the list be empty? No, constraints specify length >= 1.

2. Corner cases to consider
   - Removing the head (n = length of list).
   - Removing the only node in a single-node list.

3. Brute force Approach
   - Traverse the list once to count total length (L).
   - Traverse again to reach the (L - n)th node.
   - Update its next pointer to skip the next node.
   - Time: O(n), Space: O(1).

4. Best Approach
   - One-pass solution using two pointers.
   - Use a 'dummy' node pointing to head to handle edge cases like removing the head.
   - Move 'fast' pointer n steps ahead.
   - Move 'slow' and 'fast' together until 'fast' reaches the end.
   - 'slow.next' will be the node to remove.
   - Time: O(n), Space: O(1).

5. Logic walk through
   head = [1, 2, 3, 4], n = 2
   [Initial: dummy=0, slow=0, fast=0]
   [Step 1: fast moves 2 steps: fast=2]
   [Step 2: move slow, fast until fast.next is None: slow=2, fast=4]
   [Final result/Update: slow.next = slow.next.next (removes 3), return dummy.next]

6. Time and space complexity
   - Time: O(n)
   - Space: O(1)

7. Code
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        
        # Advance fast n steps ahead
        for _ in range(n):
            fast = fast.next
            
        # Move both until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        # Remove the target node
        slow.next = slow.next.next
        
        return dummy.next