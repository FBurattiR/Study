numero = int(input("Hello, Mr. User, welcome to my first actual function. Input a number to see the variables! (1, 2, 3): "))
def imprimir_mensaje(mensaje):
    print("Look at that")
    print("It is all just one sentence")
    print("But the final word changes")
    print("This final word is:" + mensaje)
if numero == 1:
    imprimir_mensaje("Amogus")
elif numero == 2:
    imprimir_mensaje("Impostor")
elif numero == 3:
    imprimir_mensaje("SUS")
else:
    print("You SUCK")
    exit