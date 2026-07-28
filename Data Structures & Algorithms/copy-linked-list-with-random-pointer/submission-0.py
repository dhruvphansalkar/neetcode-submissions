"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {}
        curr = head
        while curr:
            if curr not in m:
                currCopy = Node(curr.val)
                m[curr] = currCopy
            currCopy = m.get(curr, None)
            if curr.next and curr.next not in m:
                nextCopy = Node(curr.next.val)
                m[curr.next] = nextCopy
            nextCopy = m.get(curr.next, None)
            currCopy.next = nextCopy
            if curr.random and curr.random not in m:
                randomCopy = Node(curr.random.val)
                m[curr.random] = randomCopy
            randomCopy = m.get(curr.random, None)
            currCopy.random = randomCopy
            curr = curr.next
        return m.get(head, None)
        