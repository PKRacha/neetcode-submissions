"""
1. CLARITY QUESTIONS
- Are the input linked lists guaranteed to be sorted? (Yes, per problem description)
- Should we create a new list or merge in-place? (Merging in-place is preferred for O(1) space)
- Is it acceptable to modify the original list nodes? (Yes, standard for this problem)

2. CORNER CASES
- One or both lists are empty: Return the non-empty list or None.
- Lists of different lengths: Continue appending the remaining nodes of the longer list.
- All nodes in one list are smaller than all nodes in the other: The logic should handle this naturally.

3. BRUTE FORCE APPROACH
Extract all values from both linked lists into a standard Python list, sort the list using a built-in sort function, 
and then iterate through the sorted values to create a new linked list. This takes O((N+M) log (N+M)) time 
and O(N+M) space.

4. BEST APPROACH
Use a dummy node to act as the head of the merged list. Use two pointers to iterate through both lists simultaneously, 
always attaching the smaller node to the current tail of the merged list. Once one list is exhausted, 
simply link the remainder of the other list.

5. LOGIC WALKTHROUGH (Whiteboarding)
list1 = [1, 2, 4], list2 = [1, 3, 5]
[Initial state: dummy = 0, tail = dummy, l1 = 1, l2 = 1]
[Action 1: Compare 1 vs 1, attach l1, tail=1, l1=2]
[Action 2: Compare 2 vs 1, attach l2, tail=1, l2=3]
[Action 3: Compare 2 vs 3, attach l1, tail=2, l1=4]
[Final result/Update: Continue until l1 is exhausted, attach remaining [5] from l2, return dummy.next]

6. TIME AND SPACE COMPLEXITY
- Time: O(n + m), where n and m are the lengths of the two lists.
- Space: O(1), as we are re-linking existing nodes without creating new ones.

7. CODE
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Attach the remainder
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next