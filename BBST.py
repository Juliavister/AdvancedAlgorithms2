from sortedcontainers import SortedSet
import time

english_words = SortedSet()

# Load dictionary
start_time = time.time()
with open("C:\\Users\\lenovo\\Desktop\\english_words.txt") as f:
    for word in f:
        english_words.add(word.strip())
dictionary_build_time = time.time() - start_time

# Spell check text
start_time = time.time()
with open("C:\\Users\\lenovo\\Desktop\\lyrics.txt") as f:
    for line in f:
        for word in line.split():
            if not word.lower() in english_words:
                print(f"{word} is misspelled.")
spell_check_time = time.time() - start_time
print(f"Dictionary building time: {dictionary_build_time:.4f} seconds")
print(f"Spell checking time: {spell_check_time:.4f} seconds")
