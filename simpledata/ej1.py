'''Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.'''

horas = float(input('Cuantas horas trabajaste? '))
precio = float(input('Cuanto cobras por hora? '))

sueldo= str(horas * precio)

print('Tu sueldo total hoy es de '+ sueldo)