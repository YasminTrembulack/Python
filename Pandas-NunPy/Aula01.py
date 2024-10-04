import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
# print(my_array)

# shape retorna uma tupla que indica as dimenções do array.
# print(my_array.shape)

my_array = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
# print(my_array.shape)
# retorna que temos 2 dimenções com 5 elementos.

# np.arange, criar um array com valoes uniformemente distribuidos dentro do intervalo
# np.range(start, stop, step, dtype=None)
my_array = np.arange(1, 10)
# print(my_array)

#reshap para redimensionar o array
a = np.arange(10).reshape((2, 5))
# print(a)
b = np.array([[1, 2, 3],
          [1, 2, 3],
          [1, 2, 3],
          [1, 2, 3],
          [1, 2, 3],
          [1, 2, 3],]).reshape((3, 6))
# print(b)

lst = [1, 2, 3.8, 4, 5, 6.4, 7.1, 8, 9 ]
v = np.array(lst)
v = v * 2
# print(v)

my_array = np.full((3, 3), True)
# print(my_array)


a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a[[0, 1, 2], [0, 1, 0]])
# print(np.array([a[0, 0], a[1, 1], a[2, 0]]))

# print(a[[0, 0], [1, 1]])
# print(np.array([a[0, 1], a[0, 1]]))


#Cria um novo array
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
#Cria um array de index
b = np.array([0, 2, 0, 1])
#é selecionado um elemento de cada linha usando os indices b
# print(a[np.arange(4), b])
#Muda o valor dos elementos de cada linha usando os indeces de b
a[np.arange(4), b] += 10
# print(a)


#cria um novo array.E encontra os elementos que são maiores que 2, retornando um array bool
bool_idx = (a>2)
# print(bool_idx)
#Cria um array com os elementos correspondentes com valores True no array anterior
# print(a[bool_idx])
#Mesma cois que anteriormente mas de outra forma
# print(a[a>2])


#Retorna o tipo do array
# print(a.dtype) 
#force esse array a se tornar um int
x = np.array([1.4, 2], dtype= np.int64)
# print(x)

b = a[a % 2 != 0]
# print(b)

#substitui todos os elementos impares do array a por -1
a[a % 2 != 0] = -1
# print(a)



x = np.array([[1, 2], [3, 4]], dtype= np.float64)
y = np.array([[5, 6], [7, 8]], dtype= np.float64)

# print(x+y)
# print(np.add(x, y))

# print(x-y)
# print(np.subtract(x, y))

# print(x*y)
# print(np.multiply(x, y))

# print(x/y)
# print(np.divide(x, y))

# print(np.sqrt(x))



x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

# print(v.dot(w))
# print(np.dot(v, w))

# print(w.dot(v))
# print(np.dot(w, v))

# print(x.dot(y))
# print(np.dot(x, y))



x = np.array([[1, 2, 3], [2, 2, 2], [3, 3, 3]])
y = np.array([[3, 2, 1], [1, 2, 3], [-1, -2, -3]])
r = x * y
# print(r)

ma = np.mat(x)
mb = np.mat(y)
r = ma * mb
# print(r)



# print(np.sum(x)) # soma a matrix
# print(np.sum(x, axis=0)) #soma as colunas
# print(np.sum(x, axis=1)) #soma as linhas

# print(x.T) # transpor uma matriz, transformar as linhas em colunas