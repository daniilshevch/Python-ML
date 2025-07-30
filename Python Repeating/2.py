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
def third_part():
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
        @property
        def person_name(self):
            return self.__name
        def print_person(self):
            print(f"Name: {self.__name}, Age: {self.__age}")
            print(f"Name: {self.person_name}")
            print(f"Age: {self.person_age}")
    karl = Person("Karl", 26)
    print(karl.person_age)
    karl.person_age = 88
    print(karl.person_age)
    karl.print_person()
    karl.person_age = 111
    karl.print_person()
    print("----------------")
    print(karl.person_age)
def fourth_part():
    class Person:
        def __init__(self, name, age):
            self.__name = name
            self.__age = age
        @property
        def Name(self):
            return self.__name
        @Name.setter
        def Name(self, new_name):
            self.Name = new_name
        def display_info(self):
            print(f"Name: {self.Name}, Age: {self.__age}")
    class Employee(Person):
        def __init__(self, name, age, company):
            super().__init__(name, age)
            self.__company = company
        def work(self):
            print(f"Employee {self.Name} works in {self.__company}")
    thomas = Employee("Thomas", 45, "Microsoft")
    thomas.work()
def fifth_part():
    class Person:
        def __init__(self, name):
            self.__name = name
        @property
        def name(self):
            return self.__name
        @name.setter
        def name(self, new_name):
            self.__name = new_name
        def display_info(self):
            print(f"Name: {self.__name}")
    class Employee(Person):
        def __init__(self, name, company):
            super().__init__(name)
            self.__company = company
        def display_info(self):
            super().display_info()
            print(f"Company: {self.__company}")
    jack = Employee("Jack", 25)
    jack.display_info()
def sixth_part():
    class Person:
        def __init__(self, name):
            self.__name = name
        @property
        def name(self):
            return self.__name

        def do_nothing(self):
            print(f"{self.name} does nothing")

    class Employee(Person):
        def work(self):
            print(f"{self.name } works")
    class Student(Person):
        def study(self):
            print(f"{self.name } studies")
    def act(person):
        print("---------------------------")
        if(isinstance(person, Person)):
            person.do_nothing()
        if(isinstance(person, Employee)):
            person.work()
        if(isinstance(person, Student)):
            person.study()

    tim = Employee("Tim")
    jack = Student("Jack")
    sam = Person("Sam")
    act(tim)
    act(jack)
    act(sam)
def seventh_part():
    class Test():
        __type = "Test"
        @staticmethod
        def print_type():
            print(Test.__type)
        value = 100
        def print(self):
            print(self.value)
    test = Test()
    test.print()
    test.value = 18
    test.print()
    test.print_type()
    class Trolleybus:
        def __init__(self, index, model, route):
            self.index = index
            self.model = model
            self.route = route
        def __str__(self):
            return f"Route {self.route}: {self.index} - {self.model}"
    trolleybus122 = Trolleybus(122, "ElectronT19102", 30)
    print(trolleybus122)
def eight_part():
    class Person:
        type = "Person"
        def __init__(self, name):
            self.__name = name
        @property
        def name(self):
            return self.__name
        @classmethod
        def from_dict(cls, data: dict):
            return cls(data["name"])
        @staticmethod
        def print_type():
            print(Person.type)
    person = Person.from_dict({"name": "John"})
    print(person.name)
    person.print_type()
def ninth_part():
    class MyClass:
        version = 1.0
        @classmethod
        def get_version_cls(cls):
            return cls.version
        @staticmethod
        def get_version_static():
            return MyClass.version


    class Base:
        name = "Base"
        @classmethod
        def print_name_cls(cls):
            print(f"Name: {cls.name}")
        @staticmethod
        def print_name_static():
            print(f"Name: {Base.name}")
    class Child(Base):
        name = "Child"
    # print(MyClass.get_version_cls())
    # print(MyClass.get_version_static())
    child = Child()
    child.print_name_cls()
    child.print_name_static()

