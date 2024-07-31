# Escribe un programa que le solicite al usuario
# un número entero y muestre todos los números
# correlativos entre el 1 y el número 
# ingresado por el usuario

entero = int(input("Escribe un número entero: "))
reverso = list(entero) 
reverso.reverse

for num in range(15, reverso + 1):
    print(dir(num))

