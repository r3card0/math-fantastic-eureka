# enumeracion exhaustiva
# el objetivo del programa es calcular
# todas las posibles respuestas hasta encontrar
# la respuesta que proporciona el usuario

objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta ** 2 < objetivo:
    #print(respuesta) # para entender que hace el programa
    respuesta += 1

if respuesta ** 2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')
