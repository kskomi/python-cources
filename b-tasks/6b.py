import datetime
import csv
import os
example_dir = os.curdir  # '/Users/Admin/Example/'
content = os.listdir(example_dir)
csvs = []
for file in content:
    if os.path.isfile(os.path.join(example_dir, file)) and file.endswith('.csv'):
        csvs.append(file)
#print(csvs)
print("Enter files:")
listFiles = []
csvsNew = csvs
inpValue = 1
while(len(csvsNew) > 0 ):
  st = ""
  for i,x in enumerate(csvsNew):
    st =st + str(i) + ": " + x + ", "
  print(st)
  inpValue=input('Select file from list:')
  if(inpValue == ''):
    break
  elif(int(inpValue) >= len(csvsNew)):
    print("Your select is broken.")
  else:
    listFiles.append(csvsNew[int(inpValue)])
    csvsNew.pop(int(inpValue))

dt = str(datetime.datetime.now()).replace(' ', '_')

accessLog = os.curdir + '/access.log'
errorLog = os.curdir + '/error.log'
summaryFile = os.curdir + '/' + dt 
acWriter = open(accessLog,'w')
erWriter = open(errorLog,'w')

writer = open(summaryFile,"w")

for file in listFiles:
  try:
    rdFile=os.curdir + '/' + file 
    csvFile=open(rdFile,'r')
    acWriter.write("Open file: " + rdFile)
    acWriter.write('\n')
    reader = csv.DictReader(csvFile)

    headers = str(reader.fieldnames)
    writer.write(headers)
    writer.write('\n')
    for row in reader:
      writer.write(str(row))
      writer.write('\n')
    csvFile.close()
  except Exception as e:
    erWriter.write("Can't open file - " + os.curdir + "/" + file)
    erWriter.write('\n')
    erWriter.write(str(e))
    erWriter.write('\n')
    


print(list)




