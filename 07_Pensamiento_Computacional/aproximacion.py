# aproximacion
# mas preciso, se toma mas tiempo
# menos preciso, se toma menor tiempo

objetivo = int(input('Escoge un número: '))
epsilon = 0.01
paso = epsilon ** 2
respuesta = 0.0

while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta ** 2 - objetivo), respuesta)# ver que está pasando y ver como se está moviendo la respuesa
    respuesta += paso

if abs(respuesta ** 2 - objetivo) >= epsilon:
    print(f'No se encontró la raíz cuadrada {objetivo}')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')