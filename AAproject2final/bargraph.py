import naive
import BBST
import hashmap
import trie
import matplotlib.pyplot as plt
import numpy as np
import timeit
from sortedcontainers import SortedSet


def dict_building_naive(dict_path):
    english_words = naive.load_word_list(dict_path)
    return english_words

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



start_time = timeit.default_timer()
naive_dictionary = dict_building_naive(dictionary_path)
end_time = timeit.default_timer()
naive_build = (end_time - start_time)

start_time = timeit.default_timer()
bbst_dictionary = dict_building_bbst(dictionary_path)
end_time = timeit.default_timer()
BBST_build = (end_time - start_time)

start_time = timeit.default_timer()
hash_dictionary = dict_building_hash(dictionary_path)
end_time = timeit.default_timer()
hash_build = (end_time - start_time)

start_time = timeit.default_timer()
trie_dictionary = dict_building_trie(dictionary_path)
end_time = timeit.default_timer()
trie_build = (end_time - start_time)

start_time = timeit.default_timer()
spell_check_naive(text,naive_dictionary)
end_time = timeit.default_timer()
naive_check = (end_time - start_time)

start_time = timeit.default_timer()
spell_check_bbst(text,bbst_dictionary)
end_time = timeit.default_timer()
BBST_check = (end_time - start_time)

start_time = timeit.default_timer()
spell_check_trie(text,trie_dictionary)
end_time = timeit.default_timer()
trie_check = (end_time - start_time)

start_time = timeit.default_timer()
spell_check_hash_map(text,hash_dictionary)
end_time = timeit.default_timer()
hash_check = (end_time - start_time)



labels = ['Naive', 'BBST', 'Trie', 'Hash']
x_pos = np.array([x / 2 for x in range(len(labels))])
width = 0.05
build_times = [naive_build, BBST_build, trie_build, hash_build]
check_times = [naive_check, BBST_check, trie_check, hash_check]

fig, ax = plt.subplots()
ax.bar(x_pos - width, build_times, width, align='center', label='Dictionary Building')
ax.bar(x_pos + width, check_times, width, align='center', label='Spell Checking')

# Set the plot labels and legend
ax.set_yscale('log')
ax.set_xlabel('Algorithms')
ax.set_ylabel('Time (seconds)')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.legend()

for i, v in enumerate(build_times):
    ax.text(i, v, f'{v:.4f}', ha='center', va='bottom')
for i, v in enumerate(check_times):
    ax.text(i, v, f'{v:.4f}', ha='center', va='bottom')

# Show the plot
plt.show()
