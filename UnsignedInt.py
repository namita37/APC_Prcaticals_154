from array import array

a = array('I', [1000, 2000, 3000, 4000, 2000])
print("1. Original array:", a)

a.append(5000)
print("2. After append:", a)

print("3. Buffer information:", a.buffer_info())

b = array('I', [1, 2, 3])
b.byteswap()
print("4. After byteswap:", b)

print("5. Count of 2000:", a.count(2000))

a.extend([6000, 7000])
print("6. After extend:", a)

byte_data = a.tobytes()
print("7. After tobytes:", byte_data)

c = array('I')
c.frombytes(byte_data)
print("8. After frombytes:", c)

with open("I_numbers.bin", "wb") as f:
    a.tofile(f)
print("9. Data written to file")

d = array('I')
with open("I_numbers.bin", "rb") as f:
    d.fromfile(f, len(a))
print("10. After fromfile:", d)

e = array('I')
e.fromlist([8000, 9000, 10000])
print("11. After fromlist:", e)

print("12. Index of 4000:", a.index(4000))

a.insert(1, 1500)
print("13. After insert:", a)

x = a.pop()
print("14. Popped element:", x)
print("15. After pop:", a)

a.remove(2000)
print("16. After remove:", a)

a.reverse()
print("17. After reverse:", a)

print("18. After tolist:", a.tolist())
