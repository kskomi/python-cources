rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
'job': ['dev', 'mgr'],
'age': 25}
fullName = str(rec['name']['firstname']) + " " + str(rec['name']['lastname'])
print('Name is:', fullName)
print('FirstName is:', rec['name']['firstname'])
print('Jobs are:', rec['job'])

rec['job'].append('janitor')

print('All information of person is:', rec)
