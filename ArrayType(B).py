from array import array

a = array('B', [10, 20, 30, 40, 20])
print("1. Original array:", a)

a.append(50)
print("2. After append:", a)

print("3. Buffer information:", a.buffer_info())

b = array('B', [1, 2, 3])
print("4. byteswap(): Not applicable for 1-byte elements")

print("5. Count of 20:", a.count(20))

a.extend([60, 70])
print("6. After extend:", a)

byte_data = a.tobytes()
print("7. After tobytes:", byte_data)

c = array('B')
c.frombytes(byte_data)
print("8. After frombytes:", c)

with open("B_numbers.bin", "wb") as f:
    a.tofile(f)
print("9. Data written to file")

d = array('B')
with open("B_numbers.bin", "rb") as f:
    d.fromfile(f, len(a))
print("10. After fromfile:", d)

e = array('B')
e.fromlist([80, 90, 100])
print("11. After fromlist:", e)

print("12. Index of 40:", a.index(40))

a.insert(1, 15)
print("13. After insert:", a)

x = a.pop()
print("14. Popped element:", x)
print("15. After pop:", a)

a.remove(20)
print("16. After remove:", a)

a.reverse()
print("17. After reverse:", a)

print("18. After tolist:", a.tolist())
