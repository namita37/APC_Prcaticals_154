# Module: string_utils.py - String utility functions

def count_vowels(s):
    """Count vowels in a string."""
    return sum(1 for ch in s.lower() if ch in "aeiou")

def reverse_string(s):
    """Return reversed string."""
    return s[::-1]

def is_palindrome(s):
    """Check if a string is a palindrome."""
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def count_words(s):
    """Count words in a string."""
    return len(s.split())

def remove_spaces(s):
    """Remove all spaces from a string."""
    return s.replace(" ", "")
