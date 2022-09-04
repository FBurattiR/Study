def run():
    diccionario = {
        "llave" : 1,
        "llaves" : 2,
        "lllave" : 3,
    } 
    for i, o in diccionario.items():
        print(i + " " + str(o))

if __name__ == "__main__":
    run()