squares = {}

for number in range(1, 21):
    if number % 2 == 0:
        squares[number] = number * number

print(squares)
