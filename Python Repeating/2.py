def first_part():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            print(f"Person constructor worked for {self.name}")
        def print_info(self):
            print(f"Name: {self.name}, Age: {self.age}")
        def __del__(self):
            print(f"Person destructor worked for {self.name}")

    tom = Person("Tom", 24)
    tom.print_info()
    print(tom.name)
    print(tom.age)
    tom.company = "Microsoft"
    print(tom.company)
    jack = Person("Jack", 25)
    def create_person(name, age):
        return Person(name, age)
    thomas = create_person("Thomas", 35)
    thomas.print_info()
    def create():
        tim = Person("Tim", 25)
    create()
    print("End of program")
def second_part():
    class Person:
        def __init__(self, name, age):
            self.__name = name
            self.__age = age
        def print(self):
            print(f"Name: {self.__name}, Age: {self.__age}")
    tim = Person("Tim", 44)
    tim.print()
    tim.__name = "XXX"
    print(tim.__name)
    tim.__age = 100
    print(tim.__age)
    tim.print()
class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    @property
    def person_age(self):
        return self.__age
    @person_age.setter
    def person_age(self, new_age):
        if(0 < new_age < 100):
            self.__age = new_age
        else:
            print(f"Invalid age: {new_age}")
    