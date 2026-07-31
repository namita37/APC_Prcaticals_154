sentence = input("Enter a sentence: ")
words = sentence.split()
result = ''
for word in words:
    if word:
        result += word[0].upper() + word[1:].lower() + ' '
print(result.rstrip())