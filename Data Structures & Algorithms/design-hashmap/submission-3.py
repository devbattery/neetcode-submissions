class ListNode:
    
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.map = [ListNode() for _ in range(self.size)]

    def hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        current = self.map[self.hash(key)]

        while current.next:
            if current.next.key == key:
                current.next.value = value
                return
            
            current = current.next
            
        current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        current = self.map[self.hash(key)].next  # next: excluding dummy(ListNode)

        while current:
            if current.key == key:
                return current.value
            
            current = current.next
        
        return -1

    def remove(self, key: int) -> None:
        current = self.map[self.hash(key)]

        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            
            current = current.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)