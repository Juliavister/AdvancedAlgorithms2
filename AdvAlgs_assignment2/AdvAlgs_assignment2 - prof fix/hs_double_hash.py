class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        if isinstance(key, str):
            h = 0
            for char in key:
                h = (h * 31 + ord(char)) % self.size
            return h
        else:
            return key % self.size

    def second_hash_function(self, key):
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

    def double_hash(self, key, i):
        return (self.hash_function(key) + i * 3 + self.second_hash_function(key)) % self.size

    def insert(self, key, value):
        i = 0
        hash_value = self.hash_function(key)
        total_slots = 0

        while self.table[hash_value] is not None:
            i += 1
            hash_value = self.double_hash(key, i)
            total_slots += 1

            if total_slots == self.size:
                raise Exception("full")

        self.table[hash_value] = (key, value)

    def search(self, key):
        i = 0
        hash_value = self.hash_function(key)
        total_slots = 0

        while self.table[hash_value] is not None:
            stored_key, value = self.table[hash_value]
            if stored_key == key:
                return value

            i += 1
            hash_value = self.double_hash(key, i)
            total_slots += 1

            if total_slots == self.size:
                break

        return None

    def display(self):
        for index, item in enumerate(self.table):
            print(f'Index {index}:', end=' ')
            if item is None:
                print('Empty')
            else:
                print(f'({item[0]}: {item[1]})')
