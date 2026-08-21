words = ["cat", "dog", "apple", "book", "sun", "orange", "pen", "table"]
result = {}

for word in words:
    length = len(word)
    if length not in result:
        result[length] = []
    result[length].append(word)

print(result)
