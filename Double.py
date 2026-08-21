from array import array

a = array('d', [10.1, 20.2, 30.3, 40.4, 20.2])
print("1. Original array:", a)

a.append(50.5)
print("2. After append:", a)

print("3. Buffer information:", a.buffer_info())

b = array('d', [1.1, 2.2, 3.3])
b.byteswap()
print("4. After byteswap:", b)

print("5. Count of 20.2:", a.count(20.2))

a.extend([60.6, 70.7])
print("6. After extend:", a)

byte_data = a.tobytes()
print("7. After tobytes:", byte_data)

c = array('d')
c.frombytes(byte_data)
print("8. After frombytes:", c)

with open("d_numbers.bin", "wb") as f:
    a.tofile(f)
print("9. Data written to file")

d = array('d')
with open("d_numbers.bin", "rb") as f:
    d.fromfile(f, len(a))
print("10. After fromfile:", d)

e = array('d')
e.fromlist([80.8, 90.9, 100.1])
print("11. After fromlist:", e)

print("12. Index of 40.4:", a.index(40.4))

a.insert(1, 15.5)
print("13. After insert:", a)

x = a.pop()
print("14. Popped element:", x)
print("15. After pop:", a)

a.remove(20.2)
print("16. After remove:", a)

a.reverse()
print("17. After reverse:", a)

print("18. After tolist:", a.tolist())
