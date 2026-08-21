from array import array

a = array('H', [100, 200, 300, 400, 200])
print("1. Original array:", a)

a.append(500)
print("2. After append:", a)

print("3. Buffer information:", a.buffer_info())

b = array('H', [1, 2, 3])
b.byteswap()
print("4. After byteswap:", b)

print("5. Count of 200:", a.count(200))

a.extend([600, 700])
print("6. After extend:", a)

byte_data = a.tobytes()
print("7. After tobytes:", byte_data)

c = array('H')
c.frombytes(byte_data)
print("8. After frombytes:", c)

with open("H_numbers.bin", "wb") as f:
    a.tofile(f)
print("9. Data written to file")

d = array('H')
with open("H_numbers.bin", "rb") as f:
    d.fromfile(f, len(a))
print("10. After fromfile:", d)

e = array('H')
e.fromlist([800, 900, 1000])
print("11. After fromlist:", e)

print("12. Index of 400:", a.index(400))

a.insert(1, 150)
print("13. After insert:", a)

x = a.pop()
print("14. Popped element:", x)
print("15. After pop:", a)

a.remove(200)
print("16. After remove:", a)

a.reverse()
print("17. After reverse:", a)

print("18. After tolist:", a.tolist())
