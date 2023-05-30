import time
import matplotlib.pyplot as plt
import naive
from sortedcontainers import SortedSet
import trie
import timeit
import hashmap


def dict_building_bbst(dict_path):
    english_words = SortedSet()
    with open(dict_path) as f:
        for word in f:
            english_words.add(word.strip().lower())
    return english_words


def dict_building_trie(dict_path):
    english_words = trie.Trie()
    with open(dict_path) as f:
        for word in f:
            english_words.insert(word.strip().lower())
    return english_words


def dict_building_hash(dict_path):
    hash_table = hashmap.HashTable(size=10000)
    with open(dict_path) as f:
        for word in f:
            hash_table.set_val(word.strip().lower(), True)
    return hash_table


def spell_check_naive(text, dictionary):
    misspelled_words = naive.spell_check(text, dictionary)
    return misspelled_words


def spell_check_bbst(text, dict):

    misspelled_words = []
    for line in text.split("\n"):
        for word in line.split():
            if not word.lower() in dict:
                misspelled_words.append(word)
    return misspelled_words


def spell_check_trie(text, dict):
    misspelled_words = []
    for line in text.split("\n"):
        for word in line.split():
            if not dict.search(word.lower()):
                misspelled_words.append(word)
    return misspelled_words


def spell_check_hash_map(text, dict):
    misspelled_words = []
    for line in text.split("\n"):
        for word in line.split():
            if not dict.get_val(word.lower()):
                misspelled_words.append(word)
    return misspelled_words


# Path to the text file
file_path = "C:\\Users\\lenovo\\Downloads\\karamazov.txt"
dictionary_path = "C:\\Users\\lenovo\\Desktop\\english_words.txt"

english_words = []

with open(dictionary_path, "r") as file:
    english_words = [word.strip().lower() for word in file.readlines()]

with open(file_path, encoding='utf8') as f:
    text = f.read().replace('\n', ' ')

# Initialize lists to store running times for each algorithm
naive_times = []
bbst_times = []
trie_times = []
hash_map_times = []

# the different dictionaries

hash_table = dict_building_hash(dictionary_path)
trie_dict = dict_building_trie(dictionary_path)
bbst_dictionary = dict_building_bbst(dictionary_path)

# Generate sample text of different lengths
text_lengths = [1000, 5000, 10000, 15000, 20000]  # Add more lengths as needed
# Perform spell checking for each text length
for length in text_lengths:
    substring = text[:length]
    # Spell checking with naive algorithm
    start_time = timeit.default_timer()
    spell_check_naive(substring, english_words)
    end_time = timeit.default_timer()
    naive_times.append(end_time - start_time)

    # Spell checking with string BBST algorithm
    start_time = timeit.default_timer()
    spell_check_bbst(substring, bbst_dictionary)
    end_time = timeit.default_timer()
    bbst_times.append(end_time - start_time)

    # Spell checking with trie algorithm
    start_time = timeit.default_timer()
    spell_check_trie(substring, trie_dict)
    end_time = timeit.default_timer()
    trie_times.append(end_time - start_time)

    # Spell checking with hash map algorithm
    start_time = timeit.default_timer()
    spell_check_hash_map(substring, hash_table)
    end_time = timeit.default_timer()
    hash_map_times.append(end_time - start_time)


# Plot the running time versus text length for each algorithm
# .plot(text_lengths, [time * 1e9 for time in naive_times], label='Naive')
plt.plot(text_lengths, [time * 1e9 for time in bbst_times], label='String BBST')
plt.plot(text_lengths, [time * 1e9 for time in trie_times], label='Trie')
plt.plot(text_lengths, [time * 1e9 for time in hash_map_times], label='Hash Map')

# Set labels and title for the plot
plt.xlabel('Text Length')
plt.ylabel('Running Time (seconds)')
plt.title('Running Time vs. Text Length')

# Add a legend
plt.legend()

# Display the plot
plt.show()
