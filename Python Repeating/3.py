def first_part():
    numbers = [1,2,3,4,5]
    for i in range(len(numbers)):
        print(numbers[i])
    for i in numbers:
        print(i)
    print("-----------------")

    for k in range(len(numbers)):
        numbers[k] *= 2
    print(numbers)
    for k in numbers:
        k *= 2
    print(numbers)

    names1 = ["Daniil", "Petro", "Victor"]
    names = list(names1)
    print(names)

    letters = list("Hello")

    for l in letters:
        print(l)


    numbers = [5] * 6
    print(numbers)
    people = ["Tom"] * 3
    print(people)

    students = ["Bob", "Sam"] * 4
    print(students)
    print(len(students))

    people = ["Jack", "Petro", "Thomas", "Mike"]
    print(people[0])
    print(people[1])
    print("---------")
    print(people[-1])
    print(people[-2])
    print("################")
    jack, petro, thomas, _ = people
    print(jack)
    print(petro)
    print(thomas)
    matrix = [
        [0,1,2,3,4,5],
        [6,7,8,9,10,11],
        [12,13,14,15,16,17]
    ]
    def print_matrix(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end = " ")
            print()
    print_matrix(matrix)
    matrix = [
        [0,1,2,3],
        [4,5],
        [6,7,8]
    ]
    print()
    print_matrix(matrix)
def second_part():
    arr = [0,1,2,3,4,5,6,7,8]
    arr1 = arr[:4]
    print(arr1)
    arr2 = arr[2:5]
    print(arr2)
    arr3 = arr[1:6:2]
    print(arr3)

    arr4 = arr[:3]
    arr5 = arr[3:]
    print(arr4)
    print(arr5)
    ##arr[a:b:c] -> a - from what index(including), b - to what index(excluding), c - step
    arr6 = arr[-3:]
    arr7 = arr[:-3]
    print(arr6)
    print(arr7)
    arr8 = arr[-6:-2]
    print(arr8)
    arr9 = arr[::-1]
    print(arr9)
    arr10 = arr[7:2:-1]
    print(arr10)
    arr11 = arr[3::-1]
    print(arr11)
    arr12 = arr[:4:-1]
    print(arr12)
    arr13 = arr[::-3]
    print(arr13)
def third_part():
    arr = [0,1,2,3,4,5,6,7]
    arr[0:3] = ["a", "b", "c", "d"]
    print(arr)
    arr[0:3] = [0,1]
    print(arr)
    del arr[0:5:2]
    print(arr)
    print(arr[1:16])
    names = ["Jack", "Mike"]
    print(len(names))
    names.append("Alice")
    print(names)
    names.insert(1, "Bill")
    print(names)

    names.extend(["Petro", "Poroshenko"])
    print(names)
    index_of_alice = names.index("Alice")
    print(index_of_alice)

    names.remove("Jack")
    print(names)
    print("Alice" in names)
    print("Hanna" in names)

    nums = [10,20,30,40,50]
    nums[1:4] = [11,22]
    print(nums)
    nums = [1,2,3,4,5,6,7,8,9]
    nums[::2] = [0,0,0,0,0]
    print(nums)

    print(nums.count(0))

    nums = [1,5,3,3,2,-1,5,8,-5, -6]
    nums.sort(key=lambda x: -x)
    print(nums)

    filtered_nums = filter(lambda x: x % 2 == 0, nums)
    for n in filtered_nums:
        print(n, end = " ")
    print()
    def condition(x):
        return x > 3
    filtered_nums = filter(condition, nums)
    for n in filtered_nums:
        print(n, end = " ")
    print()
    print("--------")


    numbers = [1,2,3,4,5]
    squares = map(lambda p: p * p, numbers)
    for k in squares:
        print(k)
def fourth_part():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __str__(self):
            return f"Person({self.name}, {self.age})"
        def __repr__(self):
            return self.__str__()

    people = [Person("Petro", 45), Person("Jack", 22), Person("Kate", 23)]

    view = map(lambda p: p.age, people)
    for age in view:
        print(age, end = " ")
    print()
    people2 = people.copy()
    people3 = people

    people2.append(Person("XXX", 80))
    print(people)

    people3.append(Person("YYY", 81))
    print(people)

    nums1 = [1,2,3,4]
    nums2 = [5,6,7]
    nums3 = nums1 + nums2
    print(nums3)

    objects = [
        ["Tom", 25],
        ["James", "Microsoft"],
        [True, False]
    ]
    for obj in objects:
        for item in obj:
            print(item, end = " ")
        print()
def fifth_part():
    tom = ("Tom", 23)
    jack = ("Jack", 40)
    print(tom)
    print(jack)
    data = ["Karl", 37, "Microsoft"]
    karl = tuple(data)
    print(data)
    print(karl)
    nums = (0,1,2,3,4,5,6,7,8)
    print(nums)
    nums2 = nums[4:0:-1]
    print(nums2)
    for n in nums:
        print(n, end = " ")
    print()
    for i in range(len(nums)):
        print(nums[i], end = " ")
        ##nums[i] = 2 * nums[i]
    print()
    for i in range(4):
        print([1,2,3,4][i])
    person = ("Jack", 45, "New York", "Microsoft")
    name, age, city, _ = person
    print(name)
    print(age)
    print(city)
    print(person[1:])
    print(person[:2])

    def get_user():
        name = "Tom"
        age = 33
        return name, age, "Microsoft"
    user = get_user()
    print(user)
    print("-----------")
    for prop in user:
        print(prop)
    print("----------")
    for i in range(len(user)):
        print(user[i])

    def print_person(name, age, company):
        print(f"Name: {name}, Age: {age}, Company: {company}")

    person = ("Karl", 55)
    print_person(*person, "MonoBank")
    full_person = ["Peter", 42, "PrivatBank"]
    print_person(*full_person)
def sixth_part():
    def print_range(input_range):
        for i in input_range:
            print(i, end = " ")
        print()

    print_range(range(5))
    print_range(range(2, 10))
    print_range(range(5, 16, 3))
    print_range(range(15, 3, -2))

    for i in range(1, 10):
        for j in range(1, 10):
            print(i * j, end = "\t")
        print()
    print(list(range(1, 15, 3)))
    print(range(2, 10)[0])
    print(range(2,10)[1])
    print(range(2,10, 3)[1])
    print("--------------")
    print(len(range(2,10,3)))
    print()
    for i in range(len(range(3, 18, 4))):
        print(range(3,18,4)[i])
def seventh_part():
    users = {1: "Tom", 2: "Bob", 3: "Sam"}
    objects = {1: True, 2: "text", 3: 3}
    users_list = dict([
        ["Tom", "1234"],
        ["Jack", "5678"],
        ["Peter", "9101"]
    ])
    print(users)
    print(objects)
    print(users_list)


    print(users_list["Tom"])
    print(objects[1])
    users_list["Miles"] = "8888"
    print(users_list["Miles"])
    try:
        print(users_list["M"])
    except Exception as ex:
        print("Exception")
        print(ex)
    users_list["Miles"] = "4444"
    print(users_list["Miles"])
    print("Miles" in users_list)
    print("Karl" in users_list)

    karl = users_list.get("Karl")
    print(karl)
    miles = users_list.get("Miles")
    print(miles)

    for key in users_list:
        print(f"{key} - {users_list[key]}")
    print("-------------------------------------")
    print(users_list.items())
    print(list(users_list.items()))
    for key, value in users_list.items():
        print(f"{key} - {value}")
    print("###############################")
    for key in users_list.keys():
        print(f"{key} - {users_list[key]}")
    print("###############################")
    for value in users_list.values():
        print(value)
def eighth_part():
    users = {"Tom", "Bob", "Jack", "Tom", "Karl"}
    print(users)

    numbers = [1,2,3,3,2,-9, 5,9,3, -3, -4, 2,5,6,-3, -5]
    numbers_set = set(numbers)
    print(numbers)
    print(numbers_set)
    numbers_set.add(100)
    print(numbers_set)
    for user in users:
        print(user, end = " ")
    print()
    n1 = [1,4,8,4,5,2,3,4,5]
    n2 = [1,5,9,11,4,8,5]
    nums1 = {*n1}
    nums2 = {*n2}
    nums = nums1.union(nums2)
    _nums = nums1 | nums2
    __nums = n1 + n2
    print(nums)
    print(_nums)
    print(__nums)
    inter = nums1.intersection(nums2)
    _inter = nums1 & nums2
    print(inter)
    print(_inter)
    diff12 = nums1.difference(nums2)
    diff21 = nums2.difference(nums1)
    print(diff12)
    print(diff21)
    sym_diff = nums1.symmetric_difference(nums2)
    print(sym_diff)
def ninth_part():
    numbers = [-3,-2,-1,0,1,2,3]
    positive_numbers = []
    for n in numbers:
        if(n > 0):
            positive_numbers.append(n)
    print(positive_numbers)
    positive_numbers2 = [n for n in numbers if n > 0]
    print(positive_numbers2)
    numbers10 = [n for n in range(10)]
    print(numbers10)
    squares = [n ** 2 for n in range(2,10,2)]
    print(squares)
    dictionary = {"red": "червоний", "blue":"блакитний", "green":"зелений"}
    keys = [word for word in dictionary.keys()]
    values = [word for word in dictionary.values()]
    print(keys)
    print(values)
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    people = (Person("Petro", 45), Person("Jack", 32), Person("Karl", 33))
    names = [person.name for person in people if person.age > 32]
    ages = [person.age for person in people]
    print(names)
    print(ages)

    numbers = [1,5,8,3,2,5,4,3,8,9,1,0]
    results = [n**2 if n % 2 == 0 else (-n**2) for n in numbers]
    print(results)

    first = [4,9,3,1,5,3,4,2,3]
    second = ["a", "b", "d", "k", "p", "j", "u", "m", "d"]
    pairs = zip(first, second)
    pairs_all = [(one, two) for one in first for two in second] ##all combinations
    for pair in pairs:
        print(f"{pair[0]} - {pair[1]}")

dictionary = {"a":1, "d":2, "k":5, "m":12}
pairs = [f"({key} - {value})" for key, value in dictionary.items()]
print(pairs)

some_numbers = [x for x in range(1, 10)][2:6]
print(some_numbers)
squared = {x ** 2 for x in range(-7,4)}
print(squared)

paired_squares = {x:x**2 for x in range(0, 7)}
print(paired_squares)

