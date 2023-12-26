list1 = [11,16,28,97,2,44,7,39,27,19,32,1,12]
dir(list1)
help(list1.insert)
help(list1.append)
help(list1.sort)
help(list1.remove)
help(list1.reverse)
list1[2] = 111
list1[9] = 666
list1.append(777)
list1.insert(5, 312)
print(list1)
list1.pop(3)
list1.pop()
print(list1)

list1.sort(reverse = True)
print(list1)

list2 = [3,5,6,2,33,6,11]

list3 = sorted(list2)

print(list2)
print(list3)
