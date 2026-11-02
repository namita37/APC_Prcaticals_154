# texttools/tokenization.py - Tokenization utilities
def tokenize_words(text):
    """Split text into a list of words."""
    return text.split()

def tokenize_sentences(text):
    """Split text into sentences."""
    import re
    return [s.strip() for s in re.split(r"[.!?]", text) if s.strip()]
