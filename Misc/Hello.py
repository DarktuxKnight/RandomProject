import string
import random

def generator(firstnamelen,lastnamelen):

    firstname = lastname = ''
    for i in range(0,firstnamelen):
        firstname = firstname + random.choice(string.ascii_lowercase)
    for i in range(0,lastnamelen):
        lastname = lastname + random.choice(string.ascii_lowercase)

    return(firstname,lastname)

firstnamelen = input("Enter Firstname Length: ")
lastnamelen = input("Enter Lastname Length: ")
firstnamelen = int(firstnamelen)
lastnamelen = int(lastnamelen)

firstname,lastname = generator(firstnamelen,lastnamelen)
firstname = firstname.title()
lastname = lastname.title()

print("Firstname : ",firstname)
print("Lastname  : ",lastname)


