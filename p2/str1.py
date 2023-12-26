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


########

int1 = 103
int2 = 14
int3 = 2
print(int1/int2)
print(int1//int2)
print(int1%int2)
print(int2**int3)

#param = "string" + 15 #error

param = "string" + str(15)

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(n1) + float(n2)
print(str(n1) + " plus " + str(n2) + " = ", n3)
print("{:7.2f} plus {:7.2f} = {:8.2f}".format(n1, n2, n3))
