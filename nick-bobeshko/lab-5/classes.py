class NumberHolder:
   
    def __init__(my_self, a, b):       
       my_self.a = a
       my_self.b = b
    
    
    def get_sum(my_self):
       return my_self.a + my_self.b
    
    def get_prod(self):
       return self.a * self.b
      

# var = NumberHolder(7)
var = NumberHolder(1, 6)


print(var.__dict__)
# print(var.returnNumber()) #Prints '7'

print( var.get_sum())
print( var.get_prod())


# 
class MyClass:
    variable = "blah"

    def __init__(self13):
        self13.number = 15


    def my_function(afsd):
        print("The Funcitons was called.")
        


my_object_x = MyClass()

prop = my_object_x.variable

print(prop)

my_object_x.my_function()

