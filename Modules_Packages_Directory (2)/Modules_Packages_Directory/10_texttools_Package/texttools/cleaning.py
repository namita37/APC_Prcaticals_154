# texttools/cleaning.py - Text cleaning utilities
import re

def remove_punctuation(text):
    """Remove all punctuation from text."""
    return re.sub(r"[^\w\s]", "", text)

def remove_extra_spaces(text):
    """Remove extra whitespace from text."""
    return " ".join(text.split())
