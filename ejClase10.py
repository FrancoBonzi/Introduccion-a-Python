"""
Crea una tupla con los meses del año, pide números al usuario, si el numero
esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa
posición sino muestra un mensaje de error. El programa termina cuando el
usuario introduce un cero.
"""

print("EJERCICIO 1")

mesesDelAnio = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre',
                'Octubre','Noviembre','Diciembre')

numero = int(input("Ingrese un número: "))

while numero !=0:
    if numero>=1 and numero<len(mesesDelAnio):
        print(mesesDelAnio[numero-1])
    else:
        print("El número ingresado no es correcto. Intente de nuevo...")    

    numero = int(input("Ingrese un número: "))    


print("\n")    

print("---------")

"""
Pide números y mételos en una lista, cuando el usuario meta un 0 ya
dejaremos de insertar. Por último, muestra los números ordenados de menor
a mayor.
"""

print("EJERCICIO 2")

listaDeNumero = []

numero2 = int(input("Ingrese un número: "))

while numero2 !=0:
    listaDeNumero.append(numero2)
    numero2 = int(input("Ingrese un número: "))

print("MENOR A MAYOR: ")
listaDeNumero.sort()

print(listaDeNumero)

print("\n")    

print("---------")

"""
Crea una tupla con números, pide un numero por teclado e indica cuantas
veces se repite.
"""

print("EJERCICIO 3")

numeros = (1,2,4,22,34,22,5,6,10,1,1,5)
contador = 0

numero3 = int(input("Ingrese un número: "))

for i in range(len(numeros)):
    
    if numero3 == numeros[i]:
        contador = contador + 1


print(f"El número ingresado se repite {contador} veces")      

print("\n")    

print("---------")

"""
Vamos a crear un programa en python donde vamos a declarar un
diccionario para guardar los precios de las distintas frutas. El programa
pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará
el precio final de la fruta a partir de los datos guardados en el diccionario.
"""

print("EJERCICIO 4")

diccionario = {}

nombreFruta = input("Ingrese el nombre de la fruta: ").lower()
precio = float(input("Ingrese su precio: "))

diccionario[nombreFruta] = precio

print("\n")

frutaVendida = input("Ingrese la fruta vendida: ").lower()

if frutaVendida in diccionario:
    cantidad = float(input("Ingrese la cantidad vendida: "))

    total = diccionario[frutaVendida]*cantidad
    print(f"El precio total:$ {total}")
else:
    print("No existe la fruta. Intente de nuevo")    

