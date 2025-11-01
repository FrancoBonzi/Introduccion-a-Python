print("EJERCICIO 1")

# EJERCICIO 1
# Cree una función que calcule el promedio de N notas

def PromedioDeNotas():
    acumulador = 0
    contador = 0
    
    cantidad_notas = int(input("Ingrese la cantidad de notas: "))

    for i in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        acumulador += nota
        contador += 1

    promedio = acumulador / contador
    return promedio


print(f"El promedio es: {PromedioDeNotas():.2f}")
print("\n")



# EJERCICIO 2
# Cree una funcion que determine si un color es primario o no, se debe imprimir por
# pantalla la leyenda “el color X es primero “ o “el color X no es primario”

print("EJERCICIO 2")

def colorPrimario():
    color = input("Ingrese un color: ").lower()

    if color == "rojo" or color == "azul" or color == "amarillo":
        print(f"El color {color} es primario.")
    else:
        print(f"El color {color} no es primario.")


colorPrimario()
print("\n")



# EJERCICIO 3
# Cree una funcion que determine que numero de una serie de N numeros es mayor

print("EJERCICIO 3")

def numeroMayor():
    cantidad = int(input("¿Cuántos números quiere ingresar?: "))
    mayor = 0

    for i in range(cantidad):
        numero = int(input(f"Ingrese el número {i+1}: "))
        if numero>mayor:
            mayor = numero
        else:
            mayor    


    return mayor


print(f"El número mayor es: {numeroMayor()}")
print("\n")



# EJERCICIO 4
# Cree una funcion que dibuje un rectangulo de X filas y X columnas determinadas por el
# usuario

print("EJERCICIO 4")

def dibujarUnRectangulo():
    filas = int(input("Ingrese la cantidad de filas: "))
    columnas = int(input("Ingrese la cantidad de columnas: "))

    print()  
    for i in range(filas):
        for j in range(columnas):
            print("-", end="")
        print()
    print()  


dibujarUnRectangulo()


# EJERCICIO 5
# Crea una función que calcule el factorial de un número entero positivo

print("EJERCICIO 5")

def CalculoDelFactorial():
    numero = int(input("Ingrese un número entero positivo: "))
    factorial = 1

    for i in range(1, numero + 1):
        factorial *= i

    print(f"El factorial de {numero} es {factorial}")




CalculoDelFactorial()
