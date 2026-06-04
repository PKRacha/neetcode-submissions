"""
1. Clarity Questions:
   - Does "reverse" mean swapping values or changing next pointers? Must modify next pointers.
   - What happens if the final group has fewer than k nodes? Leave them as they are.

2. Corner Cases:
   - Empty list: Return None.
   - k = 1: List remains unchanged.
   - List length < k: List remains unchanged.
   - List length is a multiple of k: All nodes reversed.

3. Brute-force Approach:
   - Traverse and store node values in an array.
   - Process the array by reversing chunks of size k.
   - Reconstruct the linked list from the processed array.
   - Time: O(n), Space: O(n).

4. Best Approach:
   - In-place iterative reversal using a dummy node.
   - Use a pointer to identify group boundaries.
   - For each group of k, reverse pointers; connect the previous group's tail to the new head and the current group's tail to the next group.

5. Logic Walkthrough:
   head = [1, 2, 3, 4, 5], k = 2
   [Initial State] dummy -> 1 -> 2 -> 3 -> 4 -> 5, prev_group_tail = dummy
   [Action 1] Identify group [1, 2], reverse it to [2, 1]. Connect dummy->2, 1->3. prev_group_tail = 1
   [Action 2] Identify group [3, 4], reverse it to [4, 3]. Connect 1->4, 3->5. prev_group_tail = 3
   [Final Result] 2 -> 1 -> 4 -> 3 -> 5

6. Time and Space Complexity:
   - Time: O(n) as we traverse the list a constant number of times.
   - Space: O(1) as we only use a few pointers regardless of list size.

7. Code:
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            kth = self.getKth(group_prev, k)
            if not kth: break
            group_next = kth.next
            
            # Reverse group
            prev, curr = kth.next, group_prev.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # Connect
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
            
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr