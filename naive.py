import time

start_time = time.time()


# Load the English word list
with open("C:\\Users\\lenovo\\Desktop\\english_words.txt") as f:
    english_words = [word.strip().lower() for word in f]
dictionary_build_time = time.time() - start_time


# Define the spell check function
def spell_check(word):
    return word.lower() in english_words

start_time = time.time()
with open("C:\\Users\\lenovo\\Desktop\\lyrics.txt") as f:
    for line in f:
        for word in line.split():
            if not spell_check(word):
                print(f"{word} is misspelled.")
spell_check_time = time.time() - start_time
print(f"Dictionary building time: {dictionary_build_time:.4f} seconds")
print(f"Spell checking time: {spell_check_time:.4f} seconds")

