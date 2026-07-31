sentence = input("Enter a sentence: ")
words = [word for word in sentence.split() if word]
if words:
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    print("Longest word =", longest)
else:
    print("No words found")