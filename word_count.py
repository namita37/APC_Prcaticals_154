sentence = input("Enter a sentence: ")
words = [word for word in sentence.split() if word]
print("Word count =", len(words))