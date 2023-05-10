import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, value): #this is for separate chaining -> represents key-value pair in hash table
        self.key = key
        self.value = value
        self.next = None

class SeparateChainingHT:
   def __init__(self, capacity):
    self.capacity = capacity #determines hash table size
    self.size = 0 #keeps track of number of elements
    self.table = [None] * self.capacity #list -> this is the hash table

   def hash(self, key): #maps keys to indices in hash table
        return hash(key) % self.capacity #built in function ->

   def put(self, key, value): #inserting key-value pairs into hash
       index = self.hash(key)
       node = self.table[index]
       while node is not None: #traverses the list at the index to find if key exists.
           if node.key == key:
               node.value = value #value updates if it does
               return
           node = node.next #if not a new node is created at the start
       node = Node(key, value)
       node.next = self.table[index]
       self.table[index] = node
       self.size += 1 #increment size to keep track

   def get(self, key): #retrieve value connected to given key
       index = self.hash(key)
       node = self.table[index]
       while node is not None: #also traverses to find corresponing pair
           if node.key == key:
               return node.value
           node = node.next
       raise KeyError('Key not found')

   def delete(self, key): #deletes a key-value pair from the hash table
       index = self.hash(key)
       node = self.table[index]
       prev = None
       while node is not None: #traverses list to find key
           if node.key == key:
               if prev is None: #removes the node from the list
                   self.table[index] = node.next
               else:
                   prev.next = node.next
               self.size -= 1
               return
           prev = node
           node = node.next
       raise KeyError('Key not found')

class LinearProbingHT:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * self.capacity #lists that represent actual hash table
        self.values = [None] * self.capacity

    def hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value): #insert key-value pair
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.capacity #if calculated index is taken, it probes next index -> linear
        self.keys[index] = key
        self.values[index] = value
        self.size += 1

    def get(self, key): #retrieves value associated with key
        index = self.hash(key)
        while self.keys[index] is not None: #probes through the list until finds key or meets empty slot
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.capacity
        raise KeyError('Key not found')

    def delete(self, key): #
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.size -= 1
                return
            index = (index + 1) % self.capacity
        raise KeyError('Key not found')

class DoubleHashingHT:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def hash1(self, key): #maps keys to indices
        return hash(key) % self.capacity

    def hash2(self, key): #secondary hashsing  -> maps keys to step sizes -> step size always non zero & < capacity
        return 1 + (hash(key) % (self.capacity - 1))

    def put(self, key, value):
        index = self.hash1(key)
        step = self.hash2(key)
        while self.keys[index] is not None: #if calculated index is occupied -> increments index by step size using second hash until finds empty slot
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + step) % self.capacity
        self.keys[index] = key
        self.values[index] = value
        self.size += 1

    def get(self, key): #calculates intial index using first hash + the step size using second hash
        index = self.hash1(key)
        step = self.hash2(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + step) % self.capacity
        raise KeyError('Key not found')

    def delete(self, key):
        index = self.hash1(key)
        step = self.hash2(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.size -= 1
                return
            index = (index + step) % self.capacity
        raise KeyError('Key not found')


def measure_search_insert_time(hash_table, load_factor): #calculates time to insert and search elements in hash tables
    keys = list(range(int(load_factor * len(hash_table)))) #load factor is number of elements to insert into hash table -> creates list of keys
    values = keys #list identical to keys list
    start_time = time.time()
    for key, value in zip(keys, values): #calculate insertion time->iterates and assigns key-value pair to matching index in hash_table
        hash_table[key] = value
    elapsed_time_insert = time.time() - start_time

    start_time = time.time()
    for key in keys: #calclulates search time ->iterates over keys list and accesses each key in hash table
        hash_table[key]
    elapsed_time_search = time.time() - start_time

    return elapsed_time_insert, elapsed_time_search

load_factors = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
separate_chaining_insert_times = []
separate_chaining_search_times = []
linear_probing_insert_times = []
linear_probing_search_times = []
double_hashing_insert_times = []
double_hashing_search_times = []

hash_table_size = 1000

for load_factor in load_factors:
    separate_chaining_hash_table = {}
    linear_probing_hash_table = {}
    double_hashing_hash_table = {}

    insert_time, search_time = measure_search_insert_time(separate_chaining_hash_table, load_factor)
    separate_chaining_insert_times.append(insert_time)
    separate_chaining_search_times.append(search_time)

    insert_time, search_time = measure_search_insert_time(linear_probing_hash_table, load_factor)
    linear_probing_insert_times.append(insert_time)
    linear_probing_search_times.append(search_time)

    insert_time, search_time = measure_search_insert_time(double_hashing_hash_table, load_factor)
    double_hashing_insert_times.append(insert_time)
    double_hashing_search_times.append(search_time)

plt.plot(load_factors, separate_chaining_insert_times, label='Separate Chaining (Insert)')
plt.plot(load_factors, separate_chaining_search_times, label='Separate Chaining (Search)')
plt.plot(load_factors, linear_probing_insert_times, label='Linear Probing (Insert)')
plt.plot(load_factors, linear_probing_search_times, label='Linear Probing (Search)')
plt.plot(load_factors, double_hashing_insert_times, label='Double Hashing (Insert)')
plt.plot(load_factors, double_hashing_search_times, label='Double Hashing (Search)')

plt.xlabel('Load Factor')
plt.ylabel('Time')
plt.legend()
plt.show()

