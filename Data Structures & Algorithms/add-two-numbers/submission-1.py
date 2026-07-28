# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def getNumberFromLinkedList(head):
            multiplier = 1
            total = 0
            curr = head
            while curr:
                total += (multiplier * curr.val)
                multiplier *= 10
                curr = curr.next
            return total
        
        def getLinkedListFromNumber(total):
            dummyNode = curr = ListNode(0)
            if not total:
                return dummyNode
            while total:
                newNode = ListNode(total % 10)
                curr.next = newNode
                curr = curr.next
                total //= 10
            return dummyNode.next

        total = getNumberFromLinkedList(l1) + getNumberFromLinkedList(l2)
        return getLinkedListFromNumber(total)


        
        