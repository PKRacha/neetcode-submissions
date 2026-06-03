"""
1. Clarity questions
   - Is it guaranteed that the input is a singly-linked list?
   - Can the list be empty?
   - Can the cycle begin at the head?

2. Corner cases to consider
   - Empty list (head is None).
   - Single node list without a cycle.
   - Single node list with a cycle (node points to itself).

3. Brute force Approach
   - Use a Hash Set to store references to nodes already visited. 
   - Traverse the list: if a node is already in the set, a cycle exists (return True). 
   - If we reach None, no cycle exists (return False). 
   - Space complexity: O(n).

4. Best Approach
   - Floyd’s Cycle-Finding Algorithm (Two Pointers).
   - Use a 'slow' pointer (moves 1 step) and a 'fast' pointer (moves 2 steps).
   - If they meet, a cycle exists. 
   - If 'fast' reaches the end, no cycle exists.
   - Space complexity: O(1).

5. Logic walk through
   Input: head = [1, 2, 3, 4], cycle connects tail to node index 1 (value 2)
   
   [Initial: slow=1, fast=1]
   [Step 1: slow=2, fast=3]
   [Step 2: slow=3, fast=1 (wrapped to 2)]
   [Step 3: slow=4, fast=4 (meet)]
   [Final result: True]

6. Time and space complexity
   - Time: O(n), where n is the number of nodes.
   - Space: O(1).

7. Code
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False