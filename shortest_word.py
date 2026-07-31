sentence = input("Enter a sentence: ")
words = [word for word in sentence.split() if word]
if words:
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    print("Shortest word =", shortest)
else:
    print("No words found")