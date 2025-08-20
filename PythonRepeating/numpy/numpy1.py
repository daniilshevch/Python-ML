import numpy as np
def first_part():
    lst = [1,2,3,4,5]
    tp = type(lst)
    print(tp)
    arr = np.array(lst)
    print(arr)
    print(type(arr))
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    arr_matrix = np.array(matrix)
    print(arr_matrix)
    print(type(arr_matrix))
def second_part():
    rng = range(0,10,1)
    for i in rng:
        print(i, end = " ")
    print()
    print(np.arange(0,10,1))
    print(np.arange(0,10,2))

    print(np.zeros(6))
    print(np.zeros((6,4)))
    print(np.ones((3,4)))

    print(np.linspace(0, 10, 4))
    print(np.linspace(0,20,3))
    print(np.eye(4))
    print(np.random.rand(4,4))
    print(np.random.rand(1)[0])
    random_matrix = np.random.rand(2,2)
    print(random_matrix[0])
    print(random_matrix[1])
    print("$$$$$$$$$$$")
    print(np.random.randn(3,3))
    print(np.random.randint(1,14))
    print(np.random.randint(9,19,4))
    print(np.random.randint(1,10,(4,3)))
def third_part():
    np.random.seed(42)
    print(np.random.rand(3))

    arr = np.arange(0, 25)
    print(arr)
    print(arr.reshape(5,5))
    random_arr = np.random.randint(0, 11, 10)
    print(random_arr)
    print(random_arr.max())
    print(random_arr.argmax())
    print(random_arr.min())
    print(random_arr.argmin())
    print("###########")
    print(random_arr.dtype)
    print(random_arr.shape)
    matrix = np.zeros([4,3])
    print(matrix)
    print(matrix.shape)
    print(matrix.reshape(6,2))
def fourth_part():
    arr = np.arange(0,11)
    print(arr)
    for n in arr:
        print(n)
    print("$$$$$$$$$$$$")
    print(arr[8])
    print(arr[4:8])
    print(arr[:6])
    print(arr[2:])
    print(arr[3::2])
    lst = [0,1,2,3,4,5,6]
    arr = np.array(lst)
    print(arr)
    lst[0:4] = [100]
    print(lst)
    arr[0:4] = [100]
    print(arr)
    arr = np.arange(0,10)
    slice_of_arr = arr[0:5]
    print(slice_of_arr)
    print(slice_of_arr[2])
    slice_of_arr[:] = 500
    print(slice_of_arr)
    print(arr)

    matrix = np.array([[5,10,15], [20,25,30], [35,40,45]])
    print(matrix)
    for line in matrix:
        print(line, end = " %%%% ")
    print()
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = " ")
        print()
    print("********************")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i,j], end = " ")
        print()

    print(matrix[:2])
    print("------")
    print(matrix[:2,1:])
    matrix = np.array([[i] * 10 for i in range(0,10)])
    print(matrix)
    print("---")
    print(matrix[1::2])
    print(matrix[1::2, :7])
    arr = np.arange(1,11)
    print(arr > 4)
    print(arr[arr > 4])
    print(arr[arr % 2 == 0])
def fifth_part():
    arr = np.arange(0,10)
    arr += 5
    print(arr)
    arr -= 6
    print(arr)
    arr += 1
    print(arr)
    arr2 = np.arange(0,10) * 4
    print(arr2)
    print(arr + arr2)
    print((arr + arr2) / 5)
    print(arr * arr)
    ##print(arr / arr)
    arr += 1
    print(arr)
    print(10 / arr)

    arr = np.array([0,1,2,3,4])
    print(np.sqrt(arr))
    print(np.sin(arr))
    print(np.cos(arr))
    print(arr.sum())
    print(arr.min())
    print(arr.argmin())
    print(arr.argmax())

    arr = np.arange(0,25)
    arr = arr.reshape(5,5)
    print(arr)
    print(arr.sum())
    print(arr.sum(axis = 0))
    print(arr.sum(axis = 1))

arr = np.zeros(10)
print(arr)

arr = np.ones(10)
print(arr)

arr = np.ones(10) * 5
print(arr)

arr = np.arange(10,51)
print(arr)

arr = np.arange(10,51)[arr % 2 == 0]
print(arr)

arr = np.arange(9).reshape(3,3)
print(arr)

arr = np.eye(3)
print(arr)

print(np.random.rand())
print(np.random.randn(25))

arr = np.linspace(0.01, 1, 100).reshape(10,10)
print(arr)

arr = np.linspace(0,1,20)
print(arr)

matrix = np.arange(1,26).reshape(5,5)
print(matrix)
print("-----")
print(matrix[2:,1:])
print(matrix[3][4])
print(matrix[matrix > 14])
print(matrix[matrix == 20][0])
print("---------")
print(matrix[:3,1:2])
print(matrix[4])
print("----------")
print(matrix[3:])
print(matrix.sum())
print(matrix.sum(axis = 0))