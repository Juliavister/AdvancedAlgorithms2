import random
import string
import timeit
import matplotlib.pyplot as plt
import hs_double_hash
import hs_linear_probing
import hs_separate_chaining

def insert_elements(hash_table, keys, values, fill_percentage):
    length = int(len(keys) * fill_percentage)
    for i in range(length):
        hash_table.insert(keys[i], values[i])

def search_element(hash_table, key):
    return hash_table.search(key)

def generate_data(length):
    keys = [''.join(random.choices(string.ascii_letters, k=20)) for _ in range(length)]
    values = [random.randint(1, 9) for _ in range(length)]
    return keys, values

def measure_insertion_time(HashTable, keys, values, fill_percentages):
    insertion_times = []
    for fill_percentage in fill_percentages:
        hash_table = HashTable(1000000)  # Create a new hash table instance
        insert_func = lambda: insert_elements(hash_table, keys, values, fill_percentage)
        insertion_time = timeit.timeit(insert_func, number=1)
        insertion_times.append(insertion_time)
    return insertion_times

def measure_search_time(HashTable, keys, values, key_to_search):
    search_times = []
    for fill_percentage in fill_percentages:
        hash_table = HashTable(1000000)  # Create a new hash table instance
        insert_elements(hash_table, keys, values, fill_percentage)  # Insert elements before searching
        search_func = lambda: search_element(hash_table, key_to_search)
        search_time = timeit.timeit(search_func, number=1)
        search_times.append(search_time)
    return search_times

def plot_insertion_times(fill_percentages, DH_times, LP_times, SC_times):
    plt.plot(fill_percentages, DH_times, marker='o', label='Double Hashing')
    plt.plot(fill_percentages, LP_times, marker='o', label='Linear Probing')
    plt.plot(fill_percentages, SC_times, marker='o', label='Separate Chaining')
    plt.xlabel('Fill Percentage')
    plt.ylabel('Insertion Time (seconds)')
    plt.title('Insertion Time vs. Fill Percentage')
    plt.legend()
    plt.savefig('insertion_times.png')
    plt.show()

def plot_search_times(fill_percentages, DH_times, LP_times, SC_times):
    plt.plot(fill_percentages, DH_times, marker='o', label='Double Hashing')
    plt.plot(fill_percentages, LP_times, marker='o', label='Linear Probing')
    plt.plot(fill_percentages, SC_times, marker='o', label='Separate Chaining')
    plt.xlabel('Fill Percentage')
    plt.ylabel('Search Time (seconds)')
    plt.title('Search Time for Key "test"')
    plt.legend()
    plt.savefig('search_times.png')
    plt.show()

# Generate data
length = 1000000
keys, values = generate_data(length)

# Fill Percentage Values
fill_percentages = [0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# Measure insertion times
DH_insertion_times = measure_insertion_time(hs_double_hash.HashTable, keys, values, fill_percentages)
LP_insertion_times = measure_insertion_time(hs_linear_probing.HashTable, keys, values, fill_percentages)
SC_insertion_times = measure_insertion_time(hs_separate_chaining.HashTable, keys, values, fill_percentages)

# Plot insertion times
plot_insertion_times(fill_percentages, DH_insertion_times, LP_insertion_times, SC_insertion_times)

# Measure search times for key "test"
key_to_search = "test"
DH_search_times = measure_search_time(hs_double_hash.HashTable, keys, values, key_to_search)
LP_search_times = measure_search_time(hs_linear_probing.HashTable, keys, values, key_to_search)
SC_search_times = measure_search_time(hs_separate_chaining.HashTable, keys, values, key_to_search)

# Plot search times
plot_search_times(fill_percentages, DH_search_times, LP_search_times, SC_search_times)
