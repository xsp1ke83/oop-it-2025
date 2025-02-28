myfloat = 7
print(myfloat)
myfloat = "text"
print(myfloat)

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781,
    True : False,
} 

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
    
    
for i in phonebook:
    print(i, sep= None)

john = phonebook.get("John")

john = None

number = None
print(number)

print("John: " , john)


mylist = []

mylist.append(1)
mylist.append(2)
mylist.append(3)

print(mylist, "Qqqq", "WWW", "EEE", sep="`")

print("Hello", end="TheEnd")
print("123")


#print(mylist, sep= None)