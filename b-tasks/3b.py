import random

def generateRandomList():
  randomlist = []
  for i in range(0,100):
    n = random.randint(1,9999)
    randomlist.append(n)
  return randomlist

list = generateRandomList()
print(list)
