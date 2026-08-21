from array import array

a = array('L', [10000, 20000, 30000, 40000, 20000])
print("1. Original array:", a)

a.append(50000)
print("2. After append:", a)

print("3. Buffer information:", a.buffer_info())

b = array('L', [1, 2, 3])
b.byteswap()
print("4. After byteswap:", b)

print("5. Count of 20000:", a.count(20000))

a.extend([60000, 70000])
print("6. After extend:", a)

byte_data = a.tobytes()
print("7. After tobytes:", byte_data)

c = array('L')
c.frombytes(byte_data)
print("8. After frombytes:", c)

with open("L_numbers.bin", "wb") as f:
    a.tofile(f)
print("9. Data written to file")

d = array('L')
with open("L_numbers.bin", "rb") as f:
    d.fromfile(f, len(a))
print("10. After fromfile:", d)

e = array('L')
e.fromlist([80000, 90000, 100000])
print("11. After fromlist:", e)

print("12. Index of 40000:", a.index(40000))

a.insert(1, 15000)
print("13. After insert:", a)

x = a.pop()
print("14. Popped element:", x)
print("15. After pop:", a)

a.remove(20000)
print("16. After remove:", a)

a.reverse()
print("17. After reverse:", a)

print("18. After tolist:", a.tolist())
