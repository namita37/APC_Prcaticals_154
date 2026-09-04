def recursive_palindrome(s):
    s = str(s)
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return recursive_palindrome(s[1:-1])


print(recursive_palindrome('level'))
