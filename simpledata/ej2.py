'''Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. '''

#por formula de sucesiones de gauss

n= round(float(input('Elige un numero cualqueira')))

suma=str( n* (n + 1)/2)

print(' La suma desde el 1 hasta ', n, 'es: '+ suma)