import random
import names

def generateRandomList():
  randomlist = []
  for i in range(0,100):
    n = random.randint(1,9999)
    randomlist.append(n)
  return randomlist

def generateNamesList():
  randomList = []
  for i in range(0,100):
    name = names.get_full_name()
    randomList.append(name)
  return randomList

def task1():
  list = generateRandomList()
  highLowList = []
  lim = int(input('Enter number of border.\r\n'))
  for num in list:
    if(num >= lim):
      highLowList.append('High')
    else:
      highLowList.append('Low')
  print('Limit is -', lim)
  print(list)
  print(highLowList)

def task2():
  lst = generateNamesList()
  chars = list(chr(chNum) for chNum in range(ord('A'),ord('M')+1))
  listAM = []
  listNZ = []
  for name in lst:
    letter = name[0]
    #print(name)
    #print(letter)
    if(letter in chars):
      listAM.append(name)
    else:
      listNZ.append(name)
  listAM.sort()
  listNZ.sort()
  print(listAM)
  print(listNZ)

def task3():
  akro = ''
  print('Enter your words:')
  while True:
    i = input()
    if(i == ''):
      return akro
    else:
      akro += i[0]

    
