# Factorial

* El número factorial es el resultado de la multiplicación "contínua" de un número "n" por cada número anterior al número "n". 
* Es decir, si 5 es el número "n", entonces su factorial será el resultado de la multiplicación contínua del 5 por todos los números anteriores al 5
````
5! = 5 * 4 * 3 * 2 * 1 = 120
````
* Los números son positivos
* Calcular un factorial con Python
````
def factorial():
    n = int(input("Enter value: "))
    single = 1
    for i in range(1,n+1):
        single = single * i
    
    return single
 ````
 
