import csv

 
#OrderID,CustomerID,ManagerID,Quantity,Price,Freight,OrderDate,ShippedDate
csvFile = open('orderdata_sample.csv', newline='')
csvNewFile = open('orderdata_sample_finally.csv', 'w')
reader = csv.DictReader(csvFile)
headers = reader.fieldnames
#print(headers)
new_headers = headers
new_headers.append('Total')
writer = csv.DictWriter(csvNewFile,fieldnames=new_headers)
writer.writeheader()
print('Quantity * Price + Freight = Total')
for row in reader:
  total = float(row['Quantity']) * float(row['Price']) + float(row['Freight'])
  print(row['Quantity'],'*',row['Price'],'+',row['Freight'],'=',total)
  row['Total'] = total
  writer.writerow(row)
#print(new_headers)

