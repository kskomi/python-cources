def average(list):
  sum = 0
  lst = defineList(list)
  for i in lst:
    int(i)
    sum+=i
  print("Average value is:")
  print(sum/len(lst))

def defineList(lst):
  lst = list(filter(lambda a: a != None, lst))
# print(lst)
  return lst


def sortLists(*args):
  negative= []
  positive = []
  for x in args:
    if(x < 0):
      negative.append(x)
    else:
      positive.append(x)
  negative.sort(reverse=True)
  positive.sort()
  tuple = (negative,positive)
  return tuple


def powFirst(x, k):
  val = x
  while(k>1):
    val*=x
    k-=1
  return val
  

def powSecond(x, k):
  if (k == 1):
    return (x)
  if (k != 1):
    return (x * powSecond(x, k - 1))



print(powFirst(3,5))
print(powSecond(3,5))

print(sortLists(1,-2,5123413,-1231242345,-1231232,5345232,-6451,65,12,543,23,1,3,6,2))



lst = [0, 2 ,4, None]

average(lst)
    
