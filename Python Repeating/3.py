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

tom = ("Tom", 23)
jack = ("Jack", 40)
print(tom)
print(jack)
data = ["Karl", 37, "Microsoft"]
karl = tuple(data)
print(data)
print(karl)




