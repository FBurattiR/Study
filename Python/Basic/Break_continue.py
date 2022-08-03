def run() :
    contador = 0
    for contador in range(7001) :
        while contador % 2 != 0:
            contador += 1
            print(contador)
            continue
        if contador == 6998:
            break

if __name__ == "__main__":
    run()