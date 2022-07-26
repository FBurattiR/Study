menu = """ Bienvenido al conversor de monedas. Elija una opcion para comenzar
1- Pesos Uruguayos a Dolares
2- Dolares a Pesos Uruguayos
3- Pesos Argentinos a Dolares Blue
4- Dolares Blue a Pesos Argentinos
Elija el numero de su opcion: """
opcion = input(menu)
if opcion == "1":
    pesos = float(input("Cantidad de pesos Uruguayos a convertir: "))
    valor_dolar = 42.09
    dolar = round(pesos / valor_dolar,2) 
    print("$" + str(dolar) + " dolares")
elif opcion == "2":
    dolar = float(input("Cantidad de dolares a convertir a pesos: "))
    valor_peso = 0.024
    pesos = round((dolar / valor_peso),4)
    print("$" + str(pesos) + " pesos")
elif opcion == "3":
    pesos = float(input("Cantidad de pesos a convertir a dolares blue: "))
    valor_dolar = 339
    dolar = round(pesos / valor_dolar,2)
    print("$" + str(dolar) + " dolares")
elif opcion == "4" :
    dolar = float(input("Cantidad de dolares blue a convertir a pesos: "))
    valor_peso = 0.0029
    pesos = round(dolar / valor_peso,4)
    print("$" + str(pesos)  + " pesos")
else :
    print("Por favor, elija una opcion correcta")