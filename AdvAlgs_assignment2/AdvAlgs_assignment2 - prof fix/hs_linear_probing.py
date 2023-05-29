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

    def probe(self, index):
        return (index + 1) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        while self.table[index] is not None:
            index = self.probe(index)

        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            stored_key, value = self.table[index]

            if stored_key == key:
                return value

            index = self.probe(index)

        return None

    def display(self):
        for index, item in enumerate(self.table):
            print(f'Index {index}:', end=' ')
            if item is None:
                print('Empty')
            else:
                print(f'({item[0]}: {item[1]})')
