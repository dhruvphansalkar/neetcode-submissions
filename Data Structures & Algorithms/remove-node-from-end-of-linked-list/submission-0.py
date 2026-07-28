# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def reverseLinkedList(curr: Optional[ListNide]):
            prev = None
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        reversed_list = reverseLinkedList(head)
        dummyHead = ListNode(0)
        dummyHead.next = reversed_list
        prev = None
        curr = dummyHead
        for i in range(n):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        return reverseLinkedList(dummyHead.next)
        