from sortedcontainers import SortedSet


class BBSTSpellChecker:
    def __init__(self):
        self.dictionary = SortedSet()

    def spell_check(self, text):
        misspelled_words = []
        words = text.split()
        for word in words:
            if word not in self.dictionary:
                misspelled_words.append(word)
        return misspelled_words
