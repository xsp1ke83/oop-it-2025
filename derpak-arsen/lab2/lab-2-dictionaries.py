# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jake" : 938273443,
}  
# your code goes here

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")