# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Approach: Create a new head and move through both lists and assign the next node to the smaller of
the two lists
Keep on moving till we reach the end of both the lists


Time complexity : O(n)
Space complexity : O(1) (since we are just manipulating the pointers and not creating newNode)
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(-1)
        current = newHead

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next
        
        while list1 is not None:
            current.next = list1
            current = current.next
            list1 = list1.next

        while list2 is not None:
            current.next = list2
            current = current.next
            list2 = list2.next

        return newHead.next