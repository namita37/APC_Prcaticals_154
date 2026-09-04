def sort_words_by_length(words):
    return sorted(words, key=lambda word: len(word))


print(sort_words_by_length(['apple', 'banana', 'cat', 'elephant']))
