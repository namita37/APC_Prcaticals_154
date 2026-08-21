from array import array

a = array('f', [10.1, 20, 30.77, 40, 20, 50.8])

print("1. Original array:")
print(a)

a.append(60)

print("\n2. After append(60):")
print(a)

print("\n3. Buffer Information:")
print(a.buffer_info())

b = array('i', [1, 2, 3])

print("\n4. Original integer array:")
print(b)

b.byteswap()

print("After byteswap():")
print(b)

print("\n5. Count of 20:")
print(a.count(20))

a.extend([70, 80])

print("\n6. After extend([70, 80]):")
print(a)


byte_data = a.tobytes()

print("\n7. After tobytes():")
print(byte_data)

c = array('f')

c.frombytes(byte_data)

print("\n8. After frombytes():")
print(c)

with open("numbers.bin", "wb") as f:
    a.tofile(f)

print("\n9. tofile():")
print("Data written to numbers.bin")

d = array('f')

with open("numbers.bin", "rb") as f:
    d.fromfile(f, len(a))

print("\n10. After fromfile():")
print(d)

e = array('i')

e.fromlist([100, 200, 300])

print("\n11. After fromlist([100, 200, 300]):")
print(e)

print("\n12. Index of 40:")
print(a.index(40))


a.insert(1, 15)

print("\n13. After insert(1, 15):")
print(a)

x = a.pop()

print("\n14. Element removed by pop():")
print(x)

print("Array after pop():")
print(a)

a.remove(20)

print("\n15. After remove(20):")
print(a)

a.reverse()

print("\n16. After reverse():")
print(a)


list_data = a.tolist()

print("\n17. After tolist():")
print(list_data)


byte_data = a.tobytes()

print("\n18. After tobytes():")
print(byte_data)


