'''
Time complexity O(n)
Space complexity O(1)
TODO: Space complexity O(n) (Larry https://www.youtube.com/watch?v=yp82286Nc3c)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseSubgroup(self, head: Optional[ListNode], tail: Optional[ListNode]):
        current = head
        nextNode = None
        prevNode = None

        while current != tail and current is not None:
            nextNode = current.next
            current.next = prevNode

            prevNode = current
            current = nextNode

        return (prevNode, head)


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        kLeft = k
        current = head
        lastHead = head
        lastTail = None
        firstHead = None
        while current is not None:
            current = current.next
            kLeft -= 1

            if kLeft == 0:
                n = self.reverseSubgroup(lastHead, current)
                # print(n[0], n[1])
                if firstHead is None:
                    firstHead = n[0]
                if lastTail is not None:
                    lastTail.next = n[0]
                lastTail = n[1]
                kLeft = k
                lastHead = current

        if kLeft > 0 and lastTail is not None:
            lastTail.next = lastHead
        if firstHead is None:
            firstHead = head

        return firstHead
        