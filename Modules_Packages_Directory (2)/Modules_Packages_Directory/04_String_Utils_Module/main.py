# main.py - Use string_utils module
import string_utils

s = input("Enter a string: ")
print(f"\nVowel count    : {string_utils.count_vowels(s)}")
print(f"Reversed       : {string_utils.reverse_string(s)}")
print(f"Is palindrome  : {string_utils.is_palindrome(s)}")
print(f"Word count     : {string_utils.count_words(s)}")
print(f"Without spaces : {string_utils.remove_spaces(s)}")
