name = input("Enter your Firstname and Lastname: ")
name = name.title()
print(name)
firstname,lastname = name.split(' ')
login = lastname[:4] + firstname[0]
print(lastname + " " + firstname + ": " + login)
