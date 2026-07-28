class DoubleLinkedList:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val
        

class LRUCache:
    def __init__(self, capacity: int):
        self.head = DoubleLinkedList(0, 0)
        self.tail = DoubleLinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.m = {}

        

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        curr = self.m[key]
        self.moveNodeToTheTop(curr)
        return curr.val

    def moveNodeToTheTop(self, curr):
        if curr.prev and curr.next:
            prev = curr.prev
            next_node = curr.next
            prev.next = next_node
            next_node.prev = prev

        first_node = self.head.next
        self.head.next = curr
        curr.next = first_node
        first_node.prev = curr
        curr.prev = self.head

        

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            curr = self.m[key]
            curr.val = value
            self.moveNodeToTheTop(curr)
            return

        if len(self.m) == self.capacity:
            node_to_evict = self.tail.prev
            pre = node_to_evict.prev
            pre.next = self.tail
            self.tail.prev = pre

            node_to_evict.prev = None
            node_to_evict.next = None
            
            del self.m[node_to_evict.key]
            node_to_evict.key = key
            node_to_evict.val = value
            self.m[key] = node_to_evict
            self.moveNodeToTheTop(node_to_evict)
            return
        
        self.m[key] = DoubleLinkedList(key, value)
        self.moveNodeToTheTop(self.m[key])
