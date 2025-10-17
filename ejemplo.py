#Cantidad de dolares que posee el usuario (pesos a dolares)

valor_moneda = 1515
pesos = float(input("Ingrese cantidad de pesos: "))
total = pesos/valor_moneda
print("Usted posee dolares U$D:",round(total,2))
print(f"Usted posee dolares U$D {round(total,2)}")

