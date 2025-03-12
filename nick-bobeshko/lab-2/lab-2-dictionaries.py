phonebook2 = {
    "John" : 5212312385,
    "Will" : 19239182,
    "Stive" : 465456121
}

for item in phonebook2.items():
    print(" - " + str(item) )

# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here

phonebook["Jake"] = "938273443"
del phonebook["Jill"]

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")