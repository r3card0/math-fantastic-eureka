# Sistema Binario

Sistema de numeración representado por el 0 y el 1. El número 1 representa cuando hay carga eléctrica, el 0 indica que no hay carga eléctrica.

Ademas pueden representar:
* 1 = True
* 0 = False

## Conversión de números decimales a números binarios

Convertir el número 34 en binario

| Dividendo | Divisor | Cociente | Residuo |
|-----------|---------|----------|---------|
| 34        | 2       | 17       | 0       |
| 17        | 2       | 8        | 1       |
| 8         | 2       | 4        | 0       |
| 4         | 2       | 2        | 0       |
| 2         | 2       | 1        | 0       |
| 1         | 2       | 0        | 1       |

El conjunto de residuos, tomados del último residuo al último, será el valor binario de 34 = 100010

La forma adecuada de leer los número binarios es solo nombrar la suceción de unos y ceros. En el ejemplo del 34, su valor binario se lee: *uno cero cero cero uno cero*

Por lo tanto, para calcular el valor binario de un número es la división del número entre dos, asi sucesivamente con todos sus cocientes hasta llegar al número más pequeño y el conjunto de sus residuos será el valor binario.

## Operaciones Artiméticas con el Sistema Binario

### Suma
Para realizar una suma entre números binarios, se debe considerar las siguientes reglas:

1. 0 + 0 = 0
2. 0 + 1 = 1
3. 1 + 0 = 1
4. 1 + 1 = 10
````

    1
  10011000
+ 00010101
-----------
  10101101
````
* Se empieza de izquierda a derecha
* Cuando se suman 1 + 1, se deja el 0 abajo y el 1 se sube en la línea siguiente derecha

### Multiplicación y División de números binarios

Para ambos casos se siguen las reglas de multiplicación de cualquier número con el cero "0"
1. 0 * 0 = 0
2. 0 * 1 = 0
3. 1 * 0 = 0
4. 1 * 1 = 1

Reto: Calcular en binario (año actual - edad) para encontrar el año que naciste

año actual:2022

![Sistem-binario](/images/SistemaBinario.webp)

[Resta Binaria](https://www.youtube.com/watch?v=d1TwfFDfrmg)

