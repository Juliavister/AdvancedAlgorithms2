import time

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

start_time=time.time()

english_words = Trie()
with open("C:\\Users\\lenovo\\Desktop\\english_words.txt") as f:
    for word in f:
        english_words.insert(word.strip())
dictionary_build_time = time.time() - start_time



misspelled_words = []
start_time = time.time()
with open("C:\\Users\\lenovo\\Desktop\\lyrics.txt") as f:
    for line in f:
        for word in line.split():
            if not english_words.search(word.lower()):
                misspelled_words.append(word)
spell_check_time = time.time() - start_time





print("Misspelled words:")
print(misspelled_words)
print(f"Dictionary building time: {dictionary_build_time:.4f} seconds")
print(f"Spell checking time: {spell_check_time:.4f} seconds")

