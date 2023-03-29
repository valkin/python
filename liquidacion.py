print("==========================================")
print("= Programa de Calculo de Liquidacion     =")
print("= Por favor ingrese los datos requeridos =")
print("==========================================")

import datetime
time = datetime.datetime.now()
print(time)

print("\n \n")

nom = str(input("Por favor ingrese su nombre: "))

pro = str(input("Por favor ingrese su profesión: "))

sal = int(input("Por favor ingrese su salario actual: "))
print("\n")

print(f'El sr. {nom} de profesion {pro} con un salario mensual de {sal}')



exit()
