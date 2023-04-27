import time

class HashMapSpellChecker:
    def __init__(self, word_list_file):
        self.dictionary = {}
        self.build_dictionary(word_list_file)

    def build_dictionary(self, word_list_file):
        start_time = time.time()
        with open(word_list_file) as f:
            for line in f:
                word = line.strip().lower()
                self.dictionary[word] = True
        end_time = time.time()
        self.dictionary_build_time = end_time - start_time

    def spell_check(self, word):
        start_time = time.perf_counter()
        result = word.lower() in self.dictionary
        end_time = time.perf_counter()
        self.spell_check_time = end_time - start_time
        return result

spell_checker = HashMapSpellChecker("C:\\Users\\lenovo\\Desktop\\english_words.txt")
with open("C:\\Users\\lenovo\\Desktop\\lyrics.txt") as f:
    for line in f:
        for word in line.split():
            if not spell_checker.spell_check(word):
                print(f"{word} is misspelled.")
print(f"Dictionary building time: {spell_checker.dictionary_build_time:.4f} seconds")
print(f"Spell checking time: {spell_checker.spell_check_time:.10f} seconds")
