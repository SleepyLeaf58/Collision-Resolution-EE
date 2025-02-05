# Code is taken from https://www.geeksforgeeks.org/linear-probing-in-python/
class LinearProbeHashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)

        # Linear probing to find an empty slot
        while self.keys[index] is not None:
            if self.keys[index] == key: 
                # If key already exists, update its value
                self.values[index] = value
                return
            index = (index + 1) % self.size

        # Insert the key-value pair
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_function(key)
        cnt = 0

        # Linear probing to find the key
        while self.keys[index] is not None and cnt <= self.size:
            #print("Index:", index, "Count", cnt)
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
            cnt += 1

        # Key not found
        return None

