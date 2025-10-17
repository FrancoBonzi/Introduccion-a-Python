print("Ejercicio 1")

nombre = input("Ingrese su nombre: ")
print("Su nombre es: ",nombre.upper())

print("----------------")

print("Ejercicio 2")

numero = int(input("Ingrese un número: "))
print(f"El resultado de la suma es: {numero+5}")

print("----------------")
print("Ejercicio 3")

nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
print(f"Bienvenidos {nombre} {apellido}")

print("----------------")
print("Ejercicio 4")

nota1 = float(input("Ingrese la primera nota:"))
nota2 = float(input("Ingrese la segunda nota:"))
nota3 = float(input("Ingrese la tercera nota:"))
nota4 = float(input("Ingrese la cuarta nota:"))
nota5 = float(input("Ingrese la quinta nota:"))

promedio = (nota1+nota2+nota3+nota4+nota5)/5

print(f"El promedio es: {round(promedio,2)}")

print("----------------")
print("Ejercicio 5")

frase = input("Ingrese una frase:")
print(frase.lower())