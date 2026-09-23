class Node: 
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val 
        self.next = None 
        self.prev = None  

class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {} 
        self.left = Node() 
        self.right = Node() 
        self.left.next = self.right 
        self.right.prev = self.left 
    
    def delete(self, node):
        prevnode =node.prev 
        nextnode = node.next 
        prevnode.next = nextnode 
        nextnode.prev = prevnode 
    
    def insert(self, node):
        prevnode = self.right.prev 
        prevnode.next = node 
        node.prev = prevnode 
        node.next = self.right 
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1 
        node = self.cache[key] #o(1) 
        self.delete(node)
        self.insert(node) 
        return node.val 
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            oldnode = self.cache[key]
            self.delete(oldnode)
        newnode = Node(key, value)
        self.cache[key] = newnode
        self.insert(newnode)
        if len(self.cache) > self.capacity: 
            lru = self.left.next 
            self.delete(lru)
            del self.cache[lru.key]
        



















        
