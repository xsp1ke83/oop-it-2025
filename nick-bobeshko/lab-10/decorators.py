class Person:
    def __init__(self, first, last):
        self._first_name = first
        self.__last = last

    @property
    def first(self):
        return self._first_name
    
    @first.setter
    def first(self, first):
        self._first_name = first
        print("Name was set")
    @first.deleter
    
    def first(self):
        self._first_name = None

person1 = Person("John", "Wine")


person1.first = "Carl"

print(person1.first)

print(person1._first_name)
