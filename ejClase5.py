#Realizar un programa que me diga si un numero es par o impar

numero = int (input("Ingrese un número: "))

if(numero%2==0):
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")    


#Realizar un programa que genere la tabla de multiplicar de un numero ingresado por el
#usuario (del 1 al 10)

print("-------------")

numeroDeTabla = int(input("Ingrese el número que desea hacer la tabla de multiplicar:"))

for i in range(1,11):
    print(numeroDeTabla," * ",i, " = ", numeroDeTabla*i)

#Realizar un programa que le pida al usuario su nombre y edad y nos diga si es mayor de edad

print("-------------")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))    

if(edad>=18):
    print(f"{nombre} es mayor de edad..")
else:
    print(f"{nombre} no es mayor de edad")   

print("-------------")

#Realizar un programa donde el usuario ingrese una palabra y un numero e imprima por
#pantalla la palabra ingresa tantas veces como el numero ingresado

palabra = input("Ingrese una palabra: ")
numeroAInterar = int(input("Ingrese un número:"))

for i in range(1,numeroAInterar+1):
    print(f"Interacción {i}: {palabra}")

#Realizar un programa que sume los números ingresados por el usuario hasta que se
#ingrese un 0. Al finalizar nos debe mostrar la suma por pantalla   

print("-------------") 

Acumulador = 0

Numero = int(input("Ingrese un número: "))

while Numero!=0:
    Acumulador+=Numero
    Numero = int(input("Ingrese un número: "))
    

print(f"LA SUMA TOTAL DE LOS NÚMEROS INGRESADOS ES: {Acumulador}") 

#Realizar un programa que pide al usuario su nombre y apellido y en el caso de no
#estar la primera letra en mayúscula devolver el mismo nombre y apellido pero
#con la primer letra en mayúscula

print("-------------")
nombre2 = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

if not ( nombre2[0].isupper() and apellido[0].isupper()):
    nombre2=nombre2.capitalize()
    apellido= apellido.capitalize()

print(f"El nombre {nombre2} y apellido {apellido} están corregidos")


#Realizar un programa que pida al usuario su edad y nos diga si debe votar,
#y en caso de tener entre 16 y 18. preguntar al usuario si decide votar o no

print("-------------")

edadUsuario = int(input("Ingrese su edad:"))

if(edadUsuario<16):
    print("No debe votar")
elif(edadUsuario>=16 and edadUsuario<=18):
    respuesta=input("¿Usted esta decidido a votar? (Si/No): ")
    print(f"La respuesta del usuario fue: {respuesta}")   
else:
    print("Esta obligado a votar")    


#Realizar un programa que pida al usuario que ingrese varios
#números y que devuelva la suma del cuadrado de esos números
  
AcumuladorSuma = 0

for i in range(1, 5):
    numero = int(input("Ingrese un número: "))
    AcumuladorSuma += numero ** 2  # acumula el cuadrado

print(f"La suma de los cuadrados es: {AcumuladorSuma}")