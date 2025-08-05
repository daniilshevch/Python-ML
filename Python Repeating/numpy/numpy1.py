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

