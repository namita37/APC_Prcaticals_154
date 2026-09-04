def process_words(words):
    lengths = list(map(lambda word: len(word), words))
    long_words_list = list(filter(lambda word: len(word) > 5, words))
    sorted_words = sorted(words, key=lambda word: len(word))
    return lengths, long_words_list, sorted_words


print(process_words(['apple', 'banana', 'cat', 'elephant']))
