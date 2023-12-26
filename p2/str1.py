string1 = "This is a string."
string2 = " This is another string."
print(string1+string2)
print(len(string1))
print(string2.title())
print(string1.lower())
print(string2.upper())
print(string1.rstrip())
print(string2.lstrip())
print(string1.strip())
print(string2.strip('.'))

d = "qwerty"
ch = d[3]
chm = d[1:3]

print('d is:', d)
print('ch is:', ch)
print('chm is:', chm)

print(d[1:], d[:3], d[:], d[1:5:2])

#d[2] = 'o' # error step
