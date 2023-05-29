class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        h = 0
        if isinstance(key, str):
            # Use a combination of polynomial rolling hash and XOR operations
            for char in key:
                h ^= (h << 5) + (h >> 2) + ord(char)
        else:
            # Use XOR and bit shifting for numeric keys
            for num in key:
                h ^= (h << 5) + (h >> 2) + num

        return h % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def display(self):
        for index in range(self.size):
            current = self.table[index]
            print(f'Index {index}:', end=' ')
            while current:
                print(f'({current.key}: {current.value})', end=' ')
                current = current.next
            print()
