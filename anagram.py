s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
count1 = {}
count2 = {}
for ch in s1.replace(' ', '').lower():
    count1[ch] = count1.get(ch, 0) + 1
for ch in s2.replace(' ', '').lower():
    count2[ch] = count2.get(ch, 0) + 1
if count1 == count2:
    print("Anagrams")
else:
    print("Not anagrams")