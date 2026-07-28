# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        prev = None
        while head2:
            next_node = head2.next
            head2.next = prev
            prev = head2
            head2 = next_node
        
        head2 = prev
        
        newHead = ListNode(0)
        curr = newHead
        while head and head2:
            curr.next = head
            head = head.next
            curr = curr.next
            curr.next = head2
            head2 = head2.next
            curr = curr.next
        if head:
            curr.next = head
        if head2:
            curr.next = head2