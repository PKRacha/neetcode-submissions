"""
1. Clarity questions
   - Are the digits in the linked list stored in reverse order? Yes.
   - Can the sum result in a new node being added (carry)? Yes.
   - Are the input linked lists guaranteed to be non-empty? Yes.

2. Corner cases to consider
   - Lists of different lengths.
   - Summing results in a carry at the final node (e.g., 5 + 5 = 10, needing an extra node).
   - Lists containing only one node.

3. Brute force Approach
   - Traverse both lists to extract the integers, add them, and create a new linked list from the digits of the sum. 
   - Note: This is limited by integer overflow in some languages, though Python handles large integers automatically.

4. Best Approach
   - Use a single pass traversal with a `carry` variable.
   - Iterate through both lists simultaneously, adding values and the carry at each step.
   - If one list is shorter, treat its missing nodes as 0.

5. Logic walk through
   l1 = [1, 2, 3], l2 = [4, 5, 6]
   [Initial: carry=0, head dummy, current=dummy]
   [Step 1: 1+4+0=5, carry=0, current.next=5]
   [Step 2: 2+5+0=7, carry=0, current.next=7]
   [Step 3: 3+6+0=9, carry=0, current.next=9]
   [Final result/Update: dummy.next = [5, 7, 9]]

6. Time and space complexity
   - Time: O(max(m, n)), where m and n are lengths of the lists.
   - Space: O(max(m, n)) to store the new list.

7. Code
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Compute sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            
            # Move pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next