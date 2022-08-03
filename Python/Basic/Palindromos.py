def palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    if palabra[::-1] == palabra:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True :
        print("Es palindromo")
    else :
        print("No es palindromo")
run()