# Introducción al ejercicio en JavaScript

Para entender mucho mejor la función que desarrollaremos en JavaScript es importante tener en cuenta dos puntos: la lógica a implementar y el flujo de la ejecución.

El reto es escribir una función en JavaScript que muestre cuál es el segundo número más grande (en valor) dentro de un array de números.

Lo primero que debemos hacer ante un ejercicio de lógica es planear bien cómo lo vamos a ordenar, de esta forma nuestra solución en código será eficaz y no solo efectiva.

## Comprendamos el ejercicio
Empecemos graficando el problema:

Empecemos con un array de ejemplo:

````
[3, 7, 4, 8, 9]
````

Si lo organizamos en orden descendente, quedaría de la siguiente forma:

````
[9,8,7,4,3]
````

Aquí podemos ver que el número más grande, el de mayor valor, es el 9. Pero el enunciado nos pide el segundo número de mayor valor, así que en realidad estamos buscando, en este caso, el número 8.

Recuerda que estás creando la lógica de una función que puede recibir un array de cualquier longitud (que puede variar la cantidad de lugares que tendrá el array) y con el orden de números aleatorio, así que debemos implementarlo para que, sea cual sean sus características, lo podamos procesar.

## Paso a paso para resolver el ejercicio. 
Teniendo claro lo anterior, pasamos a ir paso a paso por la resolución del ejercicio:

Capturamos en una variable el valor de la posición 0 del array. No necesitamos conocer su valor, solo será nuestro punto de partida como referencia, no implica que tenga un valor fundamental.

Capturamos una segunda variable donde guardaremos el valor que estamos buscando, así que le llamaremos “second” y lo inicializamos en cero porque este valor va a cambiar mucho.

Creamos un ciclo for con el cual pasaremos por cada posición del array para encontrar el valor que estamos buscando.

Ahora tenemos un primer condicional que pregunta si nuestra posición actual del array es mayor al valor de nuestra variable first. Aquí hay un punto interesante porque en la primera iteración del ciclo estaremos evaluando en ambos casos la posición 0 del array, pero después de esa ya empezará a variar (porque va por cada posición), a pesar de esto siempre preguntaremos si es mayor a first.

Si la condición es verdadera, entonces nuestra variable resultado que hemos llamado “second” guardará este valor porque para este punto de la iteración el valor de la posición actual del array es mayor a la del número de referencia first.

Pero nuestra iteración no termina allí, tenemos una segunda condición que pregunta: si el valor de la posición actual del array es mayor al valor de second y además es menor que first entonces el segundo valor más grande del array es el que tenemos en nuestra posición actual del array.

## Ejercicio graficado
Si esta explicación aún no es totalmente clara para ti, hagamos este ejemplo gráficamente:

Al finalizar todas las iteraciones, la variable second quedó con el valor 4, justo el número que estábamos buscando en nuestro algoritmo.

## Otras soluciones
Hay una ruta aparentemente más fácil para solucionar nuestro ejercicio.

Podríamos ordenar nuestro array:
````
[5,4,3,1]
````

Y luego tomar su segundo valor de la siguiente manera:
````
numbers[1] = 4
````

En este caso, para este array en específico, la solución funciona correctamente. Sin embargo, debemos evaluar otros casos de uso, por ejemplo, si el array tiene números repetidos.

Si tomamos el siguiente array con números repetidos:
````
[1,3,2,1,4,4]
````

Lo ordenamos:
````
[4,4,3,2,1,1]
````

Y buscamos la segunda posición del array:
````
numbers[1]
````

El valor que obtendremos es un 4. ¡Eso es incorrecto! Recuerda que nuestro ejercicio consiste en encontrar el segundo valor más grande dentro de un array de números, por lo que el valor que buscábamos era un 3, no el 4. Este algoritmo no funciona correctamente si tenemos números repetidos en nuestro array.

No te preocupes si habías pensado en esta solución inicialmente. Haber pensado diferente (“fuera de la caja”) ayudará muchísimo a que tu cerebro encuentre las mejores soluciones ante cada nuevo problema que te encuentres. Solo recuerda tener en cuenta diferentes posibles casos de uso para probar tus algoritmos. 😉