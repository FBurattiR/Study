def primo(n):
    if n != 1:
        if gay(n):
            print("Es primo")
        else:
            print("No es primo")
        
        
def gay(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
        return True


def run():
    numero = int(input("Escribe un numero: "))
    primo(numero)


if __name__ == "__main__":
    run()