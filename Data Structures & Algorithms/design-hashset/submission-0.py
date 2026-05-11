class ListNode:

    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.size = 10000
        # ex. [15] -> [10015] -> [20015]: remainder 15 with chaining
        self.buckets = [ListNode(0) for _ in range(self.size)]

    def hash(self, key: int) -> int:
        # remainder
        return key % self.size
        
    def add(self, key: int) -> None:
        current = self.buckets[self.hash(key)]

        while current.next:
            if current.next.key == key:
                return
            
            current = current.next
        
        current.next = ListNode(key)

    def remove(self, key: int) -> None:
        current = self.buckets[self.hash(key)]

        while current.next:
            if current.next.key == key:
                # from A -> B -> C to A -> C
                current.next = current.next.next
                return
            
            current = current.next
        
    def contains(self, key: int) -> bool:
        current = self.buckets[self.hash(key)]

        while current.next:
            if current.next.key == key:
                return True
            
            current = current.next
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)