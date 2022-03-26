def description():
    """Calcula el factorial de n

    n int > 0
    return n!
    """

description()

def factorial(n):
    print(n)
    if n == 1:
        return 1
    
    return n * factorial(n-1)

# # solicitar un numero entero al usuario
n = int(input("Escribe un entero: "))
print(factorial(n))