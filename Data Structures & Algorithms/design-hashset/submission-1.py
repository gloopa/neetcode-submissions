class MyHashSet:

    def __init__(self):
        self.hashmap = defaultdict(int)
        

    def add(self, key: int) -> None:
        self.hashmap[key]
        

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            del self.hashmap[key]
        

    def contains(self, key: int) -> bool:
        if key in self.hashmap:
            return True 
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)