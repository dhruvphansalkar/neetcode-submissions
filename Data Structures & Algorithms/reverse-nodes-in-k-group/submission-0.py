# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(l):
            prev = None
            curr = l
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return (prev, l)
        
        dummy = ListNode(0)
        dummy.next = head
        h = dummy
        t = head
        while t:
            for _ in range(k - 1):
                if not t.next:
                    return dummy.next
                t = t.next
            previous_tail = h
            next_head = t.next
            t.next = None
            (start, end) = reverse(h.next)
            previous_tail.next = start
            end.next = next_head
            h = end
            t = end.next
        return dummy.next


            
        
        


        