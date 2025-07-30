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
