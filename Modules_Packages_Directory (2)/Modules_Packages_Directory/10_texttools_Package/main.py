# main.py - texttools package demo
from texttools.cleaning import remove_punctuation, remove_extra_spaces
from texttools.tokenization import tokenize_words, tokenize_sentences
from texttools.frequency import word_frequency, top_n_words

text = input("Enter a paragraph of text:\n")

cleaned   = remove_punctuation(text)
no_spaces = remove_extra_spaces(cleaned)

print(f"\nCleaned text    : {no_spaces}")
print(f"Words           : {tokenize_words(no_spaces)}")
print(f"Sentences       : {tokenize_sentences(text)}")
print(f"Word Frequency  : {word_frequency(no_spaces)}")
print(f"Top 3 Words     : {top_n_words(no_spaces, 3)}")
