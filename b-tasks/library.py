import random

def generateRandomList():
  randomlist = []
  for i in range(0,100):
    n = random.randint(1,9999)
    randomlist.append(n)
  return randomlist
def task1():
  list = generateRandomList()
  highLowList = []
  lim = int(input('Enter number of border.\r\n'))
  for num in list:
    if(num >= lim):
      highLowList.append('High')
    else:
      highLowList.append('Low')
  print('Limit is - ', lim)
  print(list)
  print(highLowList)
