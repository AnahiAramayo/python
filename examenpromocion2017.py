# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Estimado alumno no modifique nada del codigo que le proveemos, 
# use los procedimientos o funciones que estan definidos y no 
# agregue mas a la solucion
#
# Realice un programa en Python con las siguientes caracteristicas:
#
# 1) La cantidad de filas y columnas de una matriz se ingresa por
# teclado.
#
# Validar que las filas y columnas son mayores a cero, sino emitir un
# mensaje en la consola "Las filas y columnas deben ser positivas"
# y terminar.
#
# 2) Debe ingresar los valores de la matriz desde el teclado (enteros).
# Una vez cargada se debe mostrar por consola, en la primera linea debe
# mostrar el texto "Matriz ingresada" y en las siguientes los datos de
# la matriz con formato de matriz. Usar la función "imprimirMatriz"
#
# 3) Con los datos de la matriz (2) se debera generar una NUEVA matriz, 
# de la misma cantidad de filas y columnas que la original,
# colocando en cada elemento la cantidad que veces que el correspondiente número 
# (situado en la misma fila y columna) en la matriz original
# aparece en esa misma matriz. Usar la función "generaMatriz" que
# a su vez llamará a la función "contarValor" que recibirá la matriz y un valor
# y devolverá las veces que ese valor ocurre en la matriz.
#
# 4) Mostrar la nueva matriz por consola, en la primera linea debe mostrar
# el texto "Nueva Matriz" y en las siguientes los datos de la matriz
# con formato de matriz. Usar la función "imprimirMatriz"

# 5) Calcular el mayor valor de la nueva matriz.
#
# 6) Mostrar el valor calculado en (5) y mostrar los valores
# de los elementos de la matriz original que coresponden al valor
# máximo de la nueva. 
#
# A) Cree una funcion "def GenerarMatriz(matriz)"
# esta funcion retornara la matriz solicitada en (3)
#
# B) Cree una función "def contarValor(matriz,valor)" que cuente 
# cuantas veces un valor aparece en una matriz.
#
# C) Cree una procedimiento "def imprimirMatriz(matriz, texto)"
# para mostrar por consola los valores de la matriz en los puntos (2) y (4)
# el parametro texto contendra el mensaje de la primera fila impresa
#
#
# Respetar el formato que se muestra en el ejemplo de salida. Si un punto pide 
# una operación de entrada salida y no se respeta el formato solcitado ese
# punto será evaluado con 0(cero)
#
# Usar obligatoriamente las funciones provistas con los parametros indicados
#
# NO se aceptara el uso de variables globales
#
# Ej. de las salidas de un caso particular.
#
# Matriz Ingresada
# 6  2  3  4
# 5  3  2  6 
# 4  5 14  7
# 3  4  8  6
#
# Nueva Matriz
# 3  2  3  3
# 2  3  2  3
# 3  2  1  1
# 3  3  1  3
#
# Valor mayor de la matriz nueva: 3
# Valores en la matriz original con 3 en la nueva:
# 6
# 3
# 4
# 3
# 6
# 4
# 3
# 4
# 6

# Programa Principal
# complete el codigo aqui
print "EXAMEN DE PROMOCIÓN - 2017" 
def imprimirMatriz(matriz,texto):
  print texto
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      print "%.f"%matriz[i][j],
    print 
  return 
def contarValor(matriz,valor):
  cont = 0
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
#Por cada posicion buscara e incrementara aquellos que se repiten
      if matriz[i][j] == valor: 
        cont +=1
  return cont
def GenerarMatriz(matriz):
#creamos e inicializamos una nueva matriz
  M = []
  for i in range(len(matriz)):
    M.append( [0] * len(matriz[i]) )
#Entramos a la matriz
  for i in range(len(M)):
    for j in range(len(M[i])):
      #en cada posicion asignamos la veces q se repite ese valor
      M[i][j]= contarValor(matriz,matriz[i][j])
  return M
#PROGRAMA PRINCIPAL
#INGRESAR NUMERO DE FILAS Y COLUMNAS DE MATRIZ
col=int(input("ingresar num de col:"))
fil=int(input("ingresar num de filas:"))
#La fila y columna debe ser positiva
if fil>0 and col>0:
  #declaramos las Matriz original
  A=[[0 for i in range(col)] for j in range(fil)]
  #Ingreso de valores de Matriz A[]
  for i in range(fil):
    for j in range(col):
        A[i][j]=int(input("ingresar valor de matriz Posicion(%d,%d): "%(i,j)))
  texto2= "Matriz Ingresada"
  texto4= "Nueva Matriz"
  imprimirMatriz(A,texto2)
#almacenamos en una variable auxiliar mas adelante la utilizaremos
  B=GenerarMatriz(A)
  imprimirMatriz(B,texto4)
  #Buscamos el MAXIMO de la matriz nueva generada
  max=B[0][0]
  for i in range(len(B)):
    for j in range(len(B[i])):
      if B[i][j] > max:
        max = B[i][j]
  print "Valor mayor de la matriz nueva: " '%d' %max
  #Mostramos la lista de valores que corresponden en la primera matriz
  print "Valores en la matriz original con "'%d' %max,
  print "en la nueva:"
  for i in range(len(B)):
    for j in range(len(B[i])):
      #Se recorre la matriz y por cada valor que seas igual maximo del punto anterior
      #vamos a mostrar por pantalla el valor que corresponde en A[]
      if B[i][j] == max:
        print A[i][j]
else:
   print "Las filas y columnas deben ser positivas"