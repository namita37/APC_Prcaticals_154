s = input("Enter a string: ")
result = ''
for ch in s:
    result = ch + result
if s == result:
    print("Palindrome")
else:
    print("Not a palindrome")