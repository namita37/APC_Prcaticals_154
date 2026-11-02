# texttools/frequency.py - Word frequency analysis
def word_frequency(text):
    """Return a dictionary of word frequencies."""
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq

def top_n_words(text, n=5):
    """Return the top n most frequent words."""
    freq = word_frequency(text)
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]
