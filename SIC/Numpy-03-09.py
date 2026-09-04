"""
- Estructura de Datos:
 Elegir una buena estructura de datos es fundamental.
 -Primitivo: Integer-Float-Char-String
 -Linear: Sequencial List-Linked List-Stack-Colas-Pilas
 -No Lineales: Arboles-Grafo
 -Archivos: Archivos Secuenciales-Archivos Indexados-Archivos Directos
 Primitive: Integer-Float-String-Boolean
 No Primitive: Dictionary-List(Lineal: Stacks-Colas)(No Lineal: Grafos-Arboles)-Array-Tuple-Set-Fike

- Numpy: Diferencias entre Numpy Arrays y Secuencias Estandares de Python
 Numpy Array tiene el tamaño fijo.
 Un cambio en el tamaño del array crea un nuevo array y elimina el original.
 Los elementos del Numpy Array son homogeneos.
 Numpy Array realiza facilmente calculos matematicos avanzados.
 Las operaciones son mas eficinetes y con menos codigo.

 

"""
import numpy as np
"""
print(np.__version__)

arr1=np.array([1,2,3,4,5,9])

print(arr1)

arr2=np.array([1,2,3,4,5,9])

print(arr2)
print(id(arr1))

arr3 = arr1

print(arr3)

arr4 = np.copy(arr1) # Copia el contenido del array. Pero apuntan a zonas de memoria distintas.

print(arr4)

arr5 = np.array((1,3,5,7,9))

print(arr5)

dictarray = np.array({'one':1, 'two':2, 'three':3})

print(dictarray)

setarray= np.array({1,1,1,1,1,3,3,3,3,3,5,5,5,5,5})

print(setarray)

print([i for i in np.arange(10)])

print(np.arange(11)) # Recorre la iteracion sin utilizar bucles

len10 = np.arange(10)

print(len(len10))
print(len10.size)

print(np.array([111,2.3,True]))

print(type(arr5[0]))

arr6 = np.array(["HOLA"])

print(type(arr6[0]))

print(np.array(['apple','banana']))

arr = np.linspace(1, 11, 7) # Crea N valores distribuidos linealmente entre los 2 valores.

print(type(arr))

arrayvacio = np.zeros(5)

print(arrayvacio)

arrayvacio1 = np.ones(5)

print(arrayvacio1)

li1 = [[1,2,3],[4,5,6],[7,8,9]]

print(li1)
arr2d = np.array(li1)
print(np.array(li1))

print(arr2d.ndim)

arr3d = np.array([[(1,2),
                  (3,4)],
                  [(5,6),
                  (7,8)]])
print(arr3d.ndim)

print(arr3d[0][0][0])

print(np.zeros((2, 3)))

arra6 = np.zeros((2,3))

arra7 = np.zeros((2,3), dtype="int8")

print(type(arra7[0][0]))

arra8 = arra7.astype("float32")

print(arra8.dtype)

print(arra7.dtype)

print(arr6)

print(arr2d.size)

print(arr2d.shape)

print(arr3d.shape)

a2 = np.arange(15)
print(a2.shape)
print(a2.reshape((3,5)))

data = np.random.randn(100,100)

print(data)

print(np.mean(data))

rango = np.arange(1000000)

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.append(a,b))

aa = np.array([[[1,2],[3,4]]])
print(aa)

print(np.append(a,[9,9], axis=0)) # axis=0 significa añadir por filas.

print(np.delete(a,0))

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(arr1+arr2)


a = np.arange(15)

print(a)
print(a.shape)

b = a.reshape(5,3)
print(b)

print(a.strides)
print(a.dtype)
a.astype("int32")
print(b.strides) # Te explica cuantos baits tengo que saltar para ir al siguiente número


print(b[::2])
d = b[1::2]
print(d)
print(d.base)

copia_d = d.copy() # Crea una copia del dato.

print(copia_d.strides)
print(copia_d.strides)

print(d)
print(d.T)


print(a.dtype)
a = a.astype(np.int16)
print(a.dtype)

a = np.array(['Bob','Joe','Tom','Ana'])
b = np.array(['Bob','Joe','Ana','Tom'])

print(a=="Joe")
print(a==b)

if np.array_equal(a,b):
    print("Iguales")
else:
    print("Diferentes")

nombres = a

edades = np.array([20,12,5,21])

print(nombres[(edades >= 18) & (edades % 2 == 0)])

print("Hola" and 5)

a = np.zeros((3,5))

a[:,1:2+1] = 2

print(a)

a = np.arange(15).reshape(3,-1)

print(a)

print(a[:,[1,3,4]])

print(a[[1,2],[1,2]]) # El primer par toma el elemento de la fila 1, columna 1 → a[1, 1]
                      #  El segundo par toma el elemento de la fila 2, columna 2 → a[2, 2]       

print(a.T)
"""
import pandas as pd

# Vamos a dar las Series Pandas y los DataFrames. Pandas es una biblioteca basada en Numpy. 
# Ofrece:   Que los indices sean cosas más complejas.
#           Las Series pueden equipararse a un Array pero con datos heterogeneos.
#           Métodos de operaciones complejas.
#           Herramienta util para Data Science.

a = pd.Series(['Male','Female','Male','Male','Female','Female','Female'], name="nombres")
print(a)

b = pd.Series(a)

c = np.array([10,20,30])

d=pd.Series({"a":10,"b":20,"c":30})

print(d.index)

d["a"] = 12

print(d)

z = pd.Series(range(1,10+1))

serieA = pd.Series({'Juan':500,'Maria':300})
serieB = pd.Series([250,160], index=['Ana','Luis'])

print(serieA)
print(serieB)

datafra = pd.DataFrame({'Edad': [12,13,14],'Altura':[120,123,125]}, index = ["Ana","Luis","María"])

print(datafra)

print(pd.DataFrame([[1,2,"a"],
                    [3,4,"b"],
                    [4,5,"c"]],
                    columns=["edad","altura","nombre"],
                    index=["Juan","Maria","Ana"]))

a = pd.DataFrame({"edad":[1,3,4],
                  "altura":[2,4,5],
                  "nombre":["a","b","c"]},
                  index=["Juan","Maria","Ana"])
# Dos formas DISTINTAS de crear lo MISMO
print(a)

print(a.to_dict())

