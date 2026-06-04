"""
1. Clarity questions
   - Does the list contain circular references? Yes, nodes can point to previous nodes.
   - Can we modify the original list? No, we must return a deep copy.

2. Corner cases to consider
   - Empty list (head is None).
   - List with a single node pointing to null.
   - List with a single node pointing to itself.

3. Brute force Approach
   - Use a Hash Map to store mappings from original nodes to their corresponding copy nodes.
   - First pass: Create all new nodes and store in map.
   - Second pass: Connect next and random pointers using the map.
   - Time: O(n), Space: O(n).

4. Best Approach
   - Interweaving: Create new nodes directly after the original nodes (A -> A' -> B -> B').
   - Assign random pointers for the new nodes: A'.random = A.random.next.
   - Unweave the list to restore original and extract the copy list.
   - Time: O(n), Space: O(1) (excluding output list).

5. Logic walk through
   Example: [1, 2] where 1.random -> 2, 2.random -> 1
   [Initial state: 1 -> 1' -> 2 -> 2']
   [Action 1: Set randoms: 1'.random = 1.random.next, 2'.random = 2.random.next]
   [Action 2: Separate: 1.next = 2, 1'.next = 2']
   [Final result/Update: Return head of copy list 1']

6. Time and space complexity
   - Time: O(n)
   - Space: O(1) (ignoring the O(n) space for the new list)

7. Code
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        # 1. Create copy nodes interweaved
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next
            
        # 2. Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # 3. Unweave list
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
            
        return copy_head