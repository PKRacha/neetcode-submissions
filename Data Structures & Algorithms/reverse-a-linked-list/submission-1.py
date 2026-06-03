"""
1. CLARITY QUESTIONS
- Is the list guaranteed to be singly linked? (Yes)
- Should we return the new head of the reversed list? (Yes)
- Are there constraints on the memory usage? (O(1) space is preferred)

2. CORNER CASES
- Empty list (head is None): Return None.
- Single node list: Return the node itself.
- List with two nodes: Reverse the pointers and return the second node.

3. BRUTE FORCE APPROACH
Create a new list by traversing the original list, storing all node values in an array/list,
reversing that array, and then creating a new set of nodes. This uses O(n) extra space.

4. BEST APPROACH
Use an iterative in-place reversal: maintain three pointers (`prev`, `curr`, `next_node`).
As you traverse, point `curr.next` to `prev` and slide the pointers forward.

5. LOGIC WALKTHROUGH (Whiteboarding)
head = [0, 1, 2, 3]
[Initial state: prev=None, curr=0]
[Action 1: next=1, curr.next=None, prev=0, curr=1]
[Action 2: next=2, curr.next=0, prev=1, curr=2]
[Final result/Update: Returns 3 as the new head, with pointers reversed]

6. TIME AND SPACE COMPLEXITY
- Time: O(n), where n is the number of nodes in the list.
- Space: O(1), as we only use a few pointers regardless of list size.

7. CODE
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead