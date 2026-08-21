from array import array

a = array('q', [100000, 200000, 300000, 400000, 200000])
print("1. Original array:", a)

a.append(500000)
print("2. After append:", a)

print("3. Buffer information:", a.buffer_info())

b = array('q', [1, 2, 3])
b.byteswap()
print("4. After byteswap:", b)

print("5. Count of 200000:", a.count(200000))

a.extend([600000, 700000])
print("6. After extend:", a)

byte_data = a.tobytes()
print("7. After tobytes:", byte_data)

c = array('q')
c.frombytes(byte_data)
print("8. After frombytes:", c)

with open("q_numbers.bin", "wb") as f:
    a.tofile(f)
print("9. Data written to file")

d = array('q')
with open("q_numbers.bin", "rb") as f:
    d.fromfile(f, len(a))
print("10. After fromfile:", d)

e = array('q')
e.fromlist([800000, 900000, 1000000])
print("11. After fromlist:", e)

print("12. Index of 400000:", a.index(400000))

a.insert(1, 150000)
print("13. After insert:", a)

x = a.pop()
print("14. Popped element:", x)
print("15. After pop:", a)

a.remove(200000)
print("16. After remove:", a)

a.reverse()
print("17. After reverse:", a)

print("18. After tolist:", a.tolist())
