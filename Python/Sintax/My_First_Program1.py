def conversor_peso_dolar(tipo_peso, valor_dolar):
    pesos = float(input("Cantidad de pesos " + tipo_peso + " a convertir: "))
    dolar = str(round(pesos / valor_dolar,2)) 
    print("$" + dolar + " dolares")
def conversor_dolar_peso(tipo_dolar, valor_peso):
    dolar = float(input("Cantidad de " + tipo_dolar + " convertir a pesos: "))
    pesos = str(round((dolar / valor_peso),4))
    print("$" + pesos + " pesos")
menu = """ Bienvenido al conversor de monedas. Elija una opcion para comenzar
1- Pesos Uruguayos a Dolares
2- Dolares a Pesos Uruguayos
3- Pesos Argentinos a Dolares Blue
4- Dolares Blue a Pesos Argentinos
Elija el numero de su opcion: """
opcion = input(menu)
if opcion == "1":
    conversor_peso_dolar("uruguayos", 41.84)
elif opcion == "2":
    conversor_dolar_peso("dolares", 0.024)
elif opcion == "3":
    conversor_peso_dolar("argentinos", 339)
elif opcion == "4" :
    conversor_dolar_peso("dolar blue", 0.0029)
else :
    print("Por favor, elija una opcion correcta")