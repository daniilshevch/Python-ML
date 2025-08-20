def first_part():
    print("Lviv", end = " and ")
    print("Odesa", end = " and ")
    print("Ternopil")
    name = input("Enter your name: ")
    print(f"Your name is {name}")
def second_part():
    # age = int(input("Enter your age: "))
    # print(f"{age} * {age} = {age ** 2}")
    result = (7 == 8)
    print(result)
    result = "b" and "w";
    print(result)
    result = 4 and "w"
    print(result)
    result = 0 and "k"
    print(result)
    print("---------------------")
    result = "b" or "w";
    print(result)
    result = 4 or "w"
    print(result)
    result = 0 or "k"
    print(result)
def third_part():
    language = "ukrainian"
    if(language == "english"):
        print("Hello")
    elif(language == "ukrainian"):
        print("Привіт")
    else:
        print("?")
    language = "english"
    time = "evening"
    if(language == "english"):
        print("Good", end = " ")
        if(time == "morning"):
            print("morning")
        else:
            print("evening")
    number = 1
    while(number <= 10):
        print(f"Number = {number}")
        number += 1
    else:
        print(f"Loop is done(Number = {number})")
def fourth_part():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end = " ")
        print(" ")
    message = "Message"
    for letter in message:
        print(letter, end = " ")
    print()
    for n in range(4, 10):
        print(n, end = " ")
    for i in range(10):
        print(f"Number = {i}")
    else:
        print(f"End(number = {i})")
    def sum(a, b):
        return a + b
    print(sum(1, 2))
    def print_sum(a, b):
        print(f"{a} + {b} = {a + b}")
    def print_minus(a, b):
        print(f"{a} - {b} = {a - b}")
    def perform_operation(a, b, operation):
        operation(a , b)
    perform_operation(4, 2, print_sum)
    perform_operation(4, 2, print_minus)
    ##Функції
def fifth_part():
    def print_person(name, age):
        print(f"Name: {name}, Age: {age}")
    print_person("Daniil", 20)
    print_person(age = 15, name = "Petro")
    def sum(*numbers):
        result = 0
        for n in numbers:
            result += n
        return result
    print(sum(1, 2, 3))
    print(sum())
    print(sum(1, 2, 3, 4, 5))
    def say_hello():
        print("Hello")
    def say_goodbye():
        print("Goodbye")
    message = say_hello
    message()
    message = say_goodbye
    message()
    def plus(a,b):
        return a + b
    op = plus
    print(op(4,2))
def sixth_part():
    def plus(a, b):
        print(f"{a} + {b} = {a + b}")
    def minus(a, b):
        print(f"{a} - {b} = {a - b}")
    def select_operation(choice):
        if(choice == 1):
            return plus
        else:
            return minus
    select_operation(1)(2,5)
    select_operation(2)(3,4)
    operation = select_operation(3)
    operation(2,5)
def seventh_part():
    message = lambda: print("Hello")
    message()
    sum = lambda a, b: print(f"{a} + {b} = {a+b}")
    sum(4,12)
    substraction = lambda a, b: a - b
    print(substraction(4,12))
    do_operation = lambda a, b, operation: operation(a, b)
    do_operation(1, 2, sum)
    do_operation(3, 4, lambda a, b: print(f"{a} - {b} = {a - b}"))
a = "2"
b = 3
c = int(a) + b
print(c)
d = a + str(b)
print(d)
age = 20
message = "My age is " + str(age)
print(message)
##Перетворення типів
name = "Tom"
def print_name():
    name = "Jack"
    print(name)
print_name()
print("-----------------")
def outer():
    n = 5
    def inner():
        nonlocal n
        n = 25
        print(f"Inner: {n}")
    inner()
    print(f"Outer: {n}")
outer()
