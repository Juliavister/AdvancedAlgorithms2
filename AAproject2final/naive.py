import time


def load_word_list(file_path):
    with open(file_path, 'r') as file:
        word_list = set(word.strip().lower() for word in file)
    return word_list


def spell_check(text, word_list):
    misspelled_words = []
    words = text.split()
    for word in words:
        if word.lower() not in word_list:
            misspelled_words.append(word)
    return misspelled_words


