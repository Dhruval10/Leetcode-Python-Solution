from collections import defaultdict
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = defaultdict(int)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # if key not in hashmap:
        self.hashmap[key] = value
        return self.hashmap

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.hashmap:
            return self.hashmap[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hashmap:
            del self.hashmap[key]
        # return self.hashmap[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
